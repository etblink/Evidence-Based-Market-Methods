#!/usr/bin/env python3
"""AUDIT-003 frozen live ETF implementation gate.

Uses the predeclared cohort QUAL, SPHQ, JQUA, FQAL vs VTI and the frozen
2020-01 through 2026-09 monthly window. Data source: Yahoo Finance chart API
adjusted-close series. No parameter search, ticker substitution, or selective
end-date choice.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import math
import statistics
import urllib.parse
import urllib.request
from pathlib import Path

TICKERS = ["QUAL", "SPHQ", "JQUA", "FQAL", "VTI"]
CANDIDATES = ["QUAL", "SPHQ", "JQUA", "FQAL"]
BENCHMARK = "VTI"
START_MONTH = "2020-01"
END_MONTH = "2026-09"
OUT = Path("audit-output")
RAW = OUT / "raw"
OUT.mkdir(exist_ok=True)
RAW.mkdir(exist_ok=True)

def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def ts(date: dt.date) -> int:
    return int(dt.datetime(date.year, date.month, date.day, tzinfo=dt.timezone.utc).timestamp())

def fetch_chart(ticker: str) -> tuple[dict, bytes]:
    # Pull a little before the frozen window to calculate January 2020 return.
    p1 = ts(dt.date(2019, 12, 1))
    p2 = ts(dt.date(2026, 10, 2))
    params = {
        "period1": str(p1),
        "period2": str(p2),
        "interval": "1d",
        "events": "div,splits",
        "includeAdjustedClose": "true",
    }
    url = "https://query1.finance.yahoo.com/v8/finance/chart/" + urllib.parse.quote(ticker) + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 Evidence-Based-Market-Methods/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        raw = resp.read()
    obj = json.loads(raw.decode("utf-8"))
    if obj.get("chart", {}).get("error"):
        raise RuntimeError(f"{ticker}: Yahoo error {obj['chart']['error']}")
    if not obj.get("chart", {}).get("result"):
        raise RuntimeError(f"{ticker}: no chart result")
    return obj, raw

def month_key(unix_ts: int) -> str:
    d = dt.datetime.fromtimestamp(unix_ts, tz=dt.timezone.utc).date()
    return f"{d.year:04d}-{d.month:02d}"

def month_end_adjusted(obj: dict, ticker: str) -> dict[str, float]:
    result = obj["chart"]["result"][0]
    stamps = result.get("timestamp") or []
    adjs = (((result.get("indicators") or {}).get("adjclose") or [{}])[0].get("adjclose") or [])
    if len(stamps) != len(adjs):
        raise RuntimeError(f"{ticker}: timestamp/adjclose length mismatch")
    out: dict[str, tuple[int, float]] = {}
    for stamp, val in zip(stamps, adjs):
        if val is None:
            continue
        k = month_key(stamp)
        cur = out.get(k)
        if cur is None or stamp > cur[0]:
            out[k] = (stamp, float(val))
    return {k: v[1] for k, v in out.items()}

def max_drawdown(rets: list[float]) -> float:
    wealth = 1.0
    peak = 1.0
    worst = 0.0
    for r in rets:
        wealth *= 1.0 + r
        peak = max(peak, wealth)
        worst = min(worst, wealth / peak - 1.0)
    return worst

def metrics(rets: list[float]) -> dict:
    n = len(rets)
    mean = statistics.mean(rets)
    vol = statistics.stdev(rets) * math.sqrt(12.0)
    ann_mean = mean * 12.0
    wealth = 1.0
    for r in rets:
        wealth *= 1.0 + r
    years = n / 12.0
    cagr = wealth ** (1.0 / years) - 1.0
    return {
        "months": n,
        "annualized_arithmetic_mean": ann_mean,
        "cagr": cagr,
        "annualized_volatility": vol,
        "max_drawdown": max_drawdown(rets),
        "cumulative_return": wealth - 1.0,
    }

def active_metrics(port: list[float], bench: list[float]) -> dict:
    active = [a-b for a,b in zip(port, bench)]
    te = statistics.stdev(active) * math.sqrt(12.0)
    ann = statistics.mean(active) * 12.0
    ir = ann / te if te else float("nan")
    wp = 1.0
    wb = 1.0
    wins = 0
    for a,b in zip(port, bench):
        wp *= 1.0+a
        wb *= 1.0+b
        if a > b:
            wins += 1
    return {
        "benchmark_relative_arithmetic_mean": ann,
        "benchmark_relative_compounded_return": wp / wb - 1.0,
        "tracking_error": te,
        "information_ratio": ir,
        "monthly_benchmark_win_rate": wins / len(port),
        "monthly_benchmark_wins": wins,
    }

def main() -> None:
    charts = {}
    month_ends = {}
    source_meta = {}

    for ticker in TICKERS:
        obj, raw = fetch_chart(ticker)
        charts[ticker] = obj
        RAW.joinpath(f"{ticker}.json").write_bytes(raw)
        me = month_end_adjusted(obj, ticker)
        month_ends[ticker] = me
        result = obj["chart"]["result"][0]
        stamps = result.get("timestamp") or []
        source_meta[ticker] = {
            "raw_sha256": sha256(raw),
            "first_observation_date": dt.datetime.fromtimestamp(stamps[0], tz=dt.timezone.utc).date().isoformat() if stamps else None,
            "last_observation_date": dt.datetime.fromtimestamp(stamps[-1], tz=dt.timezone.utc).date().isoformat() if stamps else None,
            "currency": (result.get("meta") or {}).get("currency"),
            "exchange_name": (result.get("meta") or {}).get("exchangeName"),
        }

    # Require the prior month and every frozen month across all tickers.
    months = []
    y, m = 2020, 1
    while (y, m) <= (2026, 9):
        months.append(f"{y:04d}-{m:02d}")
        m += 1
        if m == 13:
            y += 1
            m = 1

    required = ["2019-12"] + months
    for ticker in TICKERS:
        missing = [x for x in required if x not in month_ends[ticker]]
        if missing:
            raise RuntimeError(f"{ticker}: missing required month-end observations: {missing}")

    monthly_returns: dict[str, list[float]] = {}
    for ticker in TICKERS:
        vals = []
        prev = month_ends[ticker]["2019-12"]
        for mon in months:
            cur = month_ends[ticker][mon]
            vals.append(cur / prev - 1.0)
            prev = cur
        monthly_returns[ticker] = vals

    benchmark = monthly_returns[BENCHMARK]
    results = {}
    for ticker in CANDIDATES:
        base = metrics(monthly_returns[ticker])
        active = active_metrics(monthly_returns[ticker], benchmark)
        results[ticker] = {**base, **active}

    benchmark_result = metrics(benchmark)

    # Predeclared survivor classification.
    for ticker in CANDIDATES:
        x = results[ticker]
        x["classification"] = (
            "implementation_survivor"
            if x["benchmark_relative_arithmetic_mean"] > 0
            and x["benchmark_relative_compounded_return"] > 0
            else "implementation_not_supported"
        )

    payload = {
        "audit": "AUDIT-003",
        "status": "exploratory_not_confirmatory",
        "data_source": "Yahoo Finance chart API adjusted close",
        "window": {"start_month": START_MONTH, "end_month": END_MONTH, "months": len(months)},
        "cohort": CANDIDATES,
        "benchmark": BENCHMARK,
        "source_meta": source_meta,
        "benchmark_result": benchmark_result,
        "results": results,
    }
    OUT.joinpath("AUDIT-003-results.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    def pct(x: float) -> str:
        return f"{100*x:.2f}%"
    def num(x: float) -> str:
        return f"{x:.2f}"

    lines = [
        "# AUDIT-003 — Live ETF Implementation Gate",
        "",
        "**Status:** exploratory / adversarial, not confirmatory",
        "",
        f"Frozen window: **{START_MONTH} through {END_MONTH}** ({len(months)} monthly returns)",
        "",
        "Benchmark: **VTI**",
        "",
        "## Results",
        "",
        "| ETF | Classification | Ann. mean | CAGR | Ann. vol | Max DD | Active ann. mean | Relative compounded | Tracking error | Info ratio | Monthly win rate |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for ticker in CANDIDATES:
        x = results[ticker]
        lines.append(
            f"| {ticker} | {x['classification']} | {pct(x['annualized_arithmetic_mean'])} | {pct(x['cagr'])} | "
            f"{pct(x['annualized_volatility'])} | {pct(x['max_drawdown'])} | {pct(x['benchmark_relative_arithmetic_mean'])} | "
            f"{pct(x['benchmark_relative_compounded_return'])} | {pct(x['tracking_error'])} | {num(x['information_ratio'])} | "
            f"{pct(x['monthly_benchmark_win_rate'])} ({x['monthly_benchmark_wins']}/{x['months']}) |"
        )
    lines += [
        "",
        "## Benchmark",
        "",
        f"VTI annualized arithmetic mean: {pct(benchmark_result['annualized_arithmetic_mean'])}",
        f"VTI CAGR: {pct(benchmark_result['cagr'])}",
        f"VTI annualized volatility: {pct(benchmark_result['annualized_volatility'])}",
        f"VTI max drawdown: {pct(benchmark_result['max_drawdown'])}",
        "",
        "## Data integrity",
        "",
    ]
    for ticker in TICKERS:
        m = source_meta[ticker]
        lines.append(f"- {ticker}: raw SHA-256 `{m['raw_sha256']}`; observations {m['first_observation_date']} to {m['last_observation_date']}.")
    lines += [
        "",
        "## Boundary",
        "",
        "Adjusted close is used as a practical total-return proxy. These results are not an investable recommendation, do not include investor-specific taxes or trading frictions, and do not authorize capital deployment.",
        "",
    ]
    OUT.joinpath("AUDIT-003-results.md").write_text("\n".join(lines), encoding="utf-8")

if __name__ == "__main__":
    main()
