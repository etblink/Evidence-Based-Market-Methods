#!/usr/bin/env python3
"""AUDIT-002: frozen long-only profitability/momentum gate.

Downloads current official Kenneth R. French Data Library ZIPs, pins their hashes,
extracts the value-weighted monthly sections, and evaluates the predeclared
Big Robust and Big High portfolios against the broad U.S. market.

Standard-library only. No parameter search or optimization.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import math
import re
import statistics
import urllib.request
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


BASE = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/"
SOURCES = {
    "op": BASE + "6_Portfolios_ME_OP_2x3_CSV.zip",
    "mom": BASE + "6_Portfolios_ME_Prior_12_2_CSV.zip",
    "ff5": BASE + "F-F_Research_Data_5_Factors_2x3_CSV.zip",
}

OUT = Path("audit-output")
OUT.mkdir(exist_ok=True)

START_FULL = "201601"
START_RECENT = "202001"


@dataclass(frozen=True)
class Downloaded:
    key: str
    url: str
    zip_bytes: bytes
    zip_sha256: str
    member_name: str
    csv_text: str
    csv_sha256: str
    vintage_line: str


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def download(key: str, url: str) -> Downloaded:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Evidence-Based-Market-Methods/1.0 (research audit)"},
    )
    with urllib.request.urlopen(req, timeout=60) as response:
        payload = response.read()

    with zipfile.ZipFile(io.BytesIO(payload)) as zf:
        members = [n for n in zf.namelist() if not n.endswith("/")]
        csv_members = [n for n in members if n.lower().endswith(".csv")]
        if len(csv_members) != 1:
            raise RuntimeError(f"{key}: expected exactly one CSV member, got {members!r}")
        member = csv_members[0]
        csv_bytes = zf.read(member)

    text = csv_bytes.decode("cp1252")
    first_nonempty = next((line.strip() for line in text.splitlines() if line.strip()), "")
    return Downloaded(
        key=key,
        url=url,
        zip_bytes=payload,
        zip_sha256=sha256(payload),
        member_name=member,
        csv_text=text,
        csv_sha256=sha256(csv_bytes),
        vintage_line=first_nonempty,
    )


def normalize(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def first_monthly_table(text: str) -> tuple[list[str], list[list[str]]]:
    rows = list(csv.reader(io.StringIO(text)))
    date_re = re.compile(r"^\s*\d{6}\s*$")
    first_idx = None
    for i, row in enumerate(rows):
        if row and date_re.match(row[0] if row else ""):
            first_idx = i
            break
    if first_idx is None or first_idx == 0:
        raise RuntimeError("No monthly table found")

    header = [cell.strip() for cell in rows[first_idx - 1]]
    data: list[list[str]] = []
    for row in rows[first_idx:]:
        if not row or not date_re.match(row[0] if row else ""):
            break
        data.append([cell.strip() for cell in row])

    if len(data) < 12:
        raise RuntimeError(f"Monthly table unexpectedly short: {len(data)} rows")
    return header, data


def pick_column(header: list[str], candidates: Iterable[str]) -> int:
    norms = [normalize(h) for h in header]
    wanted = [normalize(x) for x in candidates]
    for w in wanted:
        if w in norms:
            return norms.index(w)
    for w in wanted:
        matches = [i for i, n in enumerate(norms) if w and (w in n or n in w)]
        if len(matches) == 1:
            return matches[0]
    raise RuntimeError(f"Could not find any of {list(candidates)!r} in header {header!r}")


def parse_portfolio(text: str, candidates: Iterable[str]) -> dict[str, float]:
    header, rows = first_monthly_table(text)
    idx = pick_column(header, candidates)
    out: dict[str, float] = {}
    for row in rows:
        if idx >= len(row):
            raise RuntimeError(f"Short row for {row[0]}")
        value = float(row[idx])
        if value <= -99:
            continue
        out[row[0].strip()] = value / 100.0
    return out


def parse_market(text: str) -> dict[str, float]:
    header, rows = first_monthly_table(text)
    mkt_idx = pick_column(header, ["Mkt-RF", "Mkt RF", "MktRF"])
    rf_idx = pick_column(header, ["RF"])
    out: dict[str, float] = {}
    for row in rows:
        mkt_excess = float(row[mkt_idx])
        rf = float(row[rf_idx])
        if mkt_excess <= -99 or rf <= -99:
            continue
        out[row[0].strip()] = (mkt_excess + rf) / 100.0
    return out


def compounded(xs: list[float]) -> float:
    wealth = 1.0
    for x in xs:
        wealth *= 1.0 + x
    return wealth


def max_drawdown(xs: list[float]) -> float:
    wealth = 1.0
    peak = 1.0
    worst = 0.0
    for x in xs:
        wealth *= 1.0 + x
        peak = max(peak, wealth)
        worst = min(worst, wealth / peak - 1.0)
    return worst


def window_metrics(
    portfolio: dict[str, float],
    market: dict[str, float],
    start: str,
    end: str,
) -> dict[str, float | int | str]:
    dates = sorted(d for d in portfolio if d in market and start <= d <= end)
    if not dates:
        raise RuntimeError(f"No overlapping dates for {start} through {end}")
    p = [portfolio[d] for d in dates]
    m = [market[d] for d in dates]
    active = [a - b for a, b in zip(p, m)]
    n = len(dates)

    wp = compounded(p)
    wm = compounded(m)
    years = n / 12.0
    p_cagr = wp ** (1.0 / years) - 1.0
    m_cagr = wm ** (1.0 / years) - 1.0
    p_vol = statistics.stdev(p) * math.sqrt(12.0)
    tracking_error = statistics.stdev(active) * math.sqrt(12.0)
    active_ann_mean = statistics.mean(active) * 12.0
    info_ratio = active_ann_mean / tracking_error if tracking_error else float("nan")
    relative_compounded = wp / wm - 1.0
    wins = sum(1 for a, b in zip(p, m) if a > b)

    return {
        "start": dates[0],
        "end": dates[-1],
        "months": n,
        "portfolio_cagr": p_cagr,
        "market_cagr": m_cagr,
        "portfolio_annualized_volatility": p_vol,
        "portfolio_max_drawdown": max_drawdown(p),
        "monthly_benchmark_win_rate": wins / n,
        "monthly_benchmark_wins": wins,
        "tracking_error": tracking_error,
        "information_ratio": info_ratio,
        "active_annualized_arithmetic_mean": active_ann_mean,
        "relative_compounded_return": relative_compounded,
        "portfolio_cumulative_return": wp - 1.0,
        "market_cumulative_return": wm - 1.0,
    }


def classification(full: dict, recent: dict) -> str:
    pairs = [
        (full["active_annualized_arithmetic_mean"], full["relative_compounded_return"]),
        (recent["active_annualized_arithmetic_mean"], recent["relative_compounded_return"]),
    ]
    if all(a > 0 and c > 0 for a, c in pairs):
        return "clear_survivor"
    if all(a <= 0 and c <= 0 for a, c in pairs):
        return "not_supported"
    return "mixed"


def pct(x: float) -> str:
    return f"{100*x:.2f}%"


def num(x: float) -> str:
    return f"{x:.2f}"


def main() -> None:
    downloads = {k: download(k, u) for k, u in SOURCES.items()}

    robust = parse_portfolio(
        downloads["op"].csv_text,
        ["BIG HiOP", "BIG Robust", "Big Robust", "BIG Hi OP"],
    )
    high_mom = parse_portfolio(
        downloads["mom"].csv_text,
        ["BIG HiPRIOR", "BIG Hi PRIOR", "Big High", "BIG High"],
    )
    market = parse_market(downloads["ff5"].csv_text)

    common = sorted(set(robust) & set(high_mom) & set(market))
    common = [d for d in common if d >= START_FULL]
    if not common:
        raise RuntimeError("No common dates at or after 2016-01")
    end = common[-1]

    candidates = {
        "FUND_QUALITY_PROFITABILITY": robust,
        "PRICE_CROSS_SECTIONAL_MOMENTUM": high_mom,
    }

    results: dict[str, dict] = {}
    for name, series in candidates.items():
        full = window_metrics(series, market, START_FULL, end)
        recent = window_metrics(series, market, START_RECENT, end)
        results[name] = {
            "full_2016_plus": full,
            "recent_2020_plus": recent,
            "classification": classification(full, recent),
        }

    payload = {
        "audit": "AUDIT-002",
        "status": "exploratory_not_confirmatory",
        "protocol": {
            "full_start": START_FULL,
            "recent_start": START_RECENT,
            "common_end": end,
            "parameter_search": False,
            "strategy_optimization": False,
            "benchmark": "Fama/French broad U.S. market total return = Mkt-RF + RF",
            "class_rule": {
                "clear_survivor": (
                    "benchmark-relative arithmetic mean and compounded relative "
                    "return both > 0 in both windows"
                ),
                "not_supported": (
                    "benchmark-relative arithmetic mean and compounded relative "
                    "return both <= 0 in both windows"
                ),
                "mixed": "any other pattern",
            },
        },
        "sources": {
            k: {
                "url": d.url,
                "zip_sha256": d.zip_sha256,
                "zip_bytes": len(d.zip_bytes),
                "member_name": d.member_name,
                "csv_sha256": d.csv_sha256,
                "vintage_line": d.vintage_line,
            }
            for k, d in downloads.items()
        },
        "results": results,
    }

    (OUT / "AUDIT-002-results.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    lines = [
        "# AUDIT-002 — Large-Stock Long-Only Gate",
        "",
        "**Status:** exploratory / adversarial, not confirmatory",
        "",
        f"Common analysis end: **{end[:4]}-{end[4:]}**",
        "",
        "## Source provenance",
        "",
        "| Input | Vintage header | ZIP SHA-256 | CSV SHA-256 |",
        "|---|---|---|---|",
    ]
    for key in ("op", "mom", "ff5"):
        d = downloads[key]
        lines.append(
            f"| {key} | {d.vintage_line} | `{d.zip_sha256}` | `{d.csv_sha256}` |"
        )

    for label, result in results.items():
        lines += [
            "",
            f"## {label}",
            "",
            f"Frozen classification: **{result['classification']}**",
            "",
            "| Window | Portfolio CAGR | Market CAGR | Ann. vol | Max DD | "
            "Monthly win rate | Active ann. mean | Relative compounded | "
            "Tracking error | Info ratio |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
        for key in ("full_2016_plus", "recent_2020_plus"):
            x = result[key]
            lines.append(
                f"| {x['start']}–{x['end']} | {pct(x['portfolio_cagr'])} | "
                f"{pct(x['market_cagr'])} | {pct(x['portfolio_annualized_volatility'])} | "
                f"{pct(x['portfolio_max_drawdown'])} | "
                f"{pct(x['monthly_benchmark_win_rate'])} "
                f"({x['monthly_benchmark_wins']}/{x['months']}) | "
                f"{pct(x['active_annualized_arithmetic_mean'])} | "
                f"{pct(x['relative_compounded_return'])} | "
                f"{pct(x['tracking_error'])} | {num(x['information_ratio'])} |"
            )

    lines += [
        "",
        "## Interpretation boundary",
        "",
        "These Fama/French portfolios are research portfolios, not investable products. "
        "The audit does not deduct fund fees, taxes, spreads, or investor-specific "
        "implementation costs, and it does not authorize capital deployment.",
        "",
    ]
    (OUT / "AUDIT-002-results.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
