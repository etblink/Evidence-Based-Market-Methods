#!/usr/bin/env python3
"""AUDIT-004 Stage A: post-publication AQR TSMOM survivability.

Downloads the official AQR updated monthly TSMOM workbook, hashes the exact
bytes, uses only the aggregate published TSMOM factor, and applies the
predeclared 2013+ and 2020+ gates. No parameter or asset-class selection.
"""

from __future__ import annotations

import hashlib
import io
import json
import math
import statistics
import urllib.request
from pathlib import Path

import pandas as pd

URL = (
    "https://www.aqr.com/-/media/AQR/Documents/Insights/Data-Sets/"
    "Time-Series-Momentum-Factors-Monthly.xlsx"
)
OUT = Path("audit-output")
OUT.mkdir(exist_ok=True)
WORKBOOK = OUT / "Time-Series-Momentum-Factors-Monthly.xlsx"

def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def download() -> bytes:
    req = urllib.request.Request(
        URL,
        headers={"User-Agent": "Mozilla/5.0 Evidence-Based-Market-Methods/1.0"},
    )
    with urllib.request.urlopen(req, timeout=90) as response:
        payload = response.read()
    if len(payload) < 20_000:
        raise RuntimeError(f"AQR workbook unexpectedly small: {len(payload)} bytes")
    if not payload.startswith(b"PK"):
        raise RuntimeError("AQR download is not an XLSX/ZIP payload")
    WORKBOOK.write_bytes(payload)
    return payload

def load_factor(path: Path) -> pd.Series:
    preview = pd.read_excel(path, sheet_name=0, header=None, nrows=50)
    header_row = None
    for idx, row in preview.iterrows():
        if any(str(v).strip() == "TSMOM" for v in row.dropna()):
            header_row = int(idx)
            break
    if header_row is None:
        raise RuntimeError("Could not find TSMOM header row")

    df = pd.read_excel(path, sheet_name=0, header=header_row)
    df = df.iloc[:, :6].copy()
    df.columns = ["date", *[str(c).strip() for c in df.columns[1:]]]
    if "TSMOM" not in df.columns:
        raise RuntimeError(f"TSMOM column missing; columns={list(df.columns)!r}")
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["TSMOM"] = pd.to_numeric(df["TSMOM"], errors="coerce")
    df = df.dropna(subset=["date", "TSMOM"]).sort_values("date")
    s = pd.Series(df["TSMOM"].to_numpy(), index=df["date"], name="TSMOM")
    s.index = s.index.to_period("M").to_timestamp("M")
    if s.index.duplicated().any():
        raise RuntimeError("Duplicate factor months found")
    if s.abs().quantile(0.99) > 1.0:
        raise RuntimeError(
            "TSMOM values appear not to be decimal returns; refusing implicit rescaling"
        )
    return s

def metrics(s: pd.Series) -> dict:
    vals = [float(x) for x in s]
    n = len(vals)
    if n < 12:
        raise RuntimeError("Window has fewer than 12 months")
    mean = statistics.mean(vals)
    sd = statistics.stdev(vals)
    wealth = 1.0
    peak = 1.0
    max_dd = 0.0
    for r in vals:
        wealth *= 1.0 + r
        peak = max(peak, wealth)
        max_dd = min(max_dd, wealth / peak - 1.0)
    return {
        "start": s.index[0].strftime("%Y-%m"),
        "end": s.index[-1].strftime("%Y-%m"),
        "months": n,
        "annualized_arithmetic_mean": mean * 12.0,
        "annualized_volatility": sd * math.sqrt(12.0),
        "sharpe": (mean / sd * math.sqrt(12.0)) if sd else None,
        "cumulative_return": wealth - 1.0,
        "max_drawdown": max_dd,
        "positive_month_rate": sum(r > 0 for r in vals) / n,
    }

def calendar_years(s: pd.Series) -> dict[str, float]:
    out = {}
    for year, group in s.groupby(s.index.year):
        wealth = 1.0
        for r in group:
            wealth *= 1.0 + float(r)
        out[str(int(year))] = wealth - 1.0
    return out

def classify(a: dict, b: dict) -> str:
    pa = a["annualized_arithmetic_mean"] > 0 and a["cumulative_return"] > 0
    pb = b["annualized_arithmetic_mean"] > 0 and b["cumulative_return"] > 0
    na = a["annualized_arithmetic_mean"] <= 0 and a["cumulative_return"] <= 0
    nb = b["annualized_arithmetic_mean"] <= 0 and b["cumulative_return"] <= 0
    if pa and pb:
        return "clear_survivor"
    if na and nb:
        return "not_supported"
    return "mixed"

def main() -> None:
    payload = download()
    series = load_factor(WORKBOOK)
    post = series.loc[series.index >= pd.Timestamp("2013-01-31")]
    recent = series.loc[series.index >= pd.Timestamp("2020-01-31")]
    if post.empty or recent.empty:
        raise RuntimeError("Frozen windows unavailable in workbook")

    post_m = metrics(post)
    recent_m = metrics(recent)
    disposition = classify(post_m, recent_m)

    result = {
        "audit": "AUDIT-004",
        "stage": "A",
        "status": "exploratory_not_confirmatory",
        "source": {
            "url": URL,
            "sha256": sha256(payload),
            "bytes": len(payload),
            "first_factor_month": series.index[0].strftime("%Y-%m"),
            "last_factor_month": series.index[-1].strftime("%Y-%m"),
        },
        "representation": "AQR aggregate published TSMOM factor",
        "post_publication_2013_plus": post_m,
        "recent_2020_plus": recent_m,
        "calendar_year_returns": calendar_years(post),
        "classification": disposition,
    }
    (OUT / "AUDIT-004-stage-a.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    def pct(x):
        return f"{100*x:.2f}%"
    def num(x):
        return "n/a" if x is None else f"{x:.2f}"

    lines = [
        "# AUDIT-004 Stage A — TSMOM Post-Publication Survivability",
        "",
        "**Status:** exploratory / adversarial, not confirmatory",
        "",
        f"Frozen classification: **{disposition}**",
        "",
        f"Official AQR workbook SHA-256: `{sha256(payload)}`",
        f"Published factor coverage in downloaded workbook: {series.index[0].strftime('%Y-%m')} through {series.index[-1].strftime('%Y-%m')}",
        "",
        "| Window | Months | Ann. mean | Ann. vol | Sharpe | Cumulative | Max DD | Positive months |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for label, m in [("2013+ post-publication", post_m), ("2020+ recent", recent_m)]:
        lines.append(
            f"| {label} ({m['start']}–{m['end']}) | {m['months']} | "
            f"{pct(m['annualized_arithmetic_mean'])} | {pct(m['annualized_volatility'])} | "
            f"{num(m['sharpe'])} | {pct(m['cumulative_return'])} | "
            f"{pct(m['max_drawdown'])} | {pct(m['positive_month_rate'])} |"
        )
    lines += ["", "## Calendar-year compounded returns", ""]
    for year, value in result["calendar_year_returns"].items():
        lines.append(f"- {year}: {pct(value)}")
    lines += [
        "",
        "## Boundary",
        "",
        "The AQR series is a research factor, not an investable product. This stage tests persistence of the published factor only. It does not include ETF fees, futures execution, investor taxes, or direct capital deployment.",
        "",
    ]
    (OUT / "AUDIT-004-stage-a.md").write_text("\n".join(lines), encoding="utf-8")

if __name__ == "__main__":
    main()
