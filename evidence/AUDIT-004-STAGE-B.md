# AUDIT-004 Stage B — Accessible Trend Implementation

Captured: 2026-10-02

Status: **implementation_survivor**

Authority boundary: this file records the Stage B evidence. `STATE.yaml` is the sole canonical current state. No capital deployment is authorized.

## Authorization

Stage B was entered only because AUDIT-004 Stage A classified the directly downloaded AQR aggregate TSMOM factor as a `clear_survivor` under the rule frozen before data inspection.

The Stage B interpretation rule was then frozen before reading the current KMLM standardized performance table:

- **implementation_survivor:** official KMLM NAV annualized return is strictly positive for every available 3-year, 5-year, and since-inception standardized period.
- **implementation_not_supported:** one or more of those available official NAV annualized returns is nonpositive.
- Index-to-NAV gaps are reported descriptively; no after-the-fact threshold is imposed.

Freeze commit: `30d69fac433202c9da1dac7db49ec9f369cc1130`.

## Current implementation

KMLM — KraneShares Mount Lucas Managed Futures Index Strategy ETF

Official fund information as of 2026-10-01:

- inception: 2020-12-01;
- total annual fund operating expense: 0.90%;
- underlying index: KFA MLM Index;
- 22 liquid futures contracts;
- 11 commodities, 6 currencies, and 5 global bond markets;
- baskets are weighted by relative historical volatility; constituent markets inside each basket are equal-dollar weighted.

KraneShares' official FAQ describes the index as rule-based:
- a daily trend signal is generated from each market's price relative to its long-term moving average;
- signals can be long or short;
- the portfolio rebalances monthly and futures are rolled market by market.

Official sources:
- https://kraneshares.com/etf/kmlm/
- https://kraneshares.com/kmlm-managed-futures-faq/

KMLM is economically related to time-series momentum/trend following but is **not identical** to the AQR 12-month TSMOM research factor.

## Frozen performance gate

Official standardized performance as of quarter-end 2026-09-30:

| Period | KMLM NAV | KFA MLM Index | Index minus NAV |
|---|---:|---:|---:|
| 3 Year annualized | 0.41% | 1.51% | 1.10 pp |
| 5 Year annualized | 5.94% | 7.98% | 2.04 pp |
| Since inception annualized | 8.23% | 10.17% | 1.94 pp |

Additional official figures:
- 1-year NAV: 20.67%;
- YTD through 2026-09-30: 19.23%;
- cumulative NAV since inception: 58.62%;
- cumulative index since inception: 75.94%.

Source:
https://kraneshares.com/etf/kmlm/

## Disposition

All three predeclared standardized NAV periods are strictly positive.

Frozen classification: **implementation_survivor**.

The classification establishes only that a transparent, individually accessible trend-following ETF has delivered positive net-of-fund-expense returns over every predeclared standardized horizon currently available.

It does **not** establish:
- that KMLM will outperform passive equities or cash;
- that managed futures should be a portfolio allocation;
- that KMLM replicates the AQR TSMOM factor;
- that the 0.90% expense ratio or approximately 1–2 percentage-point historical index-to-NAV gap is attractive for a particular investor;
- that future trend environments will resemble the observed period.

The 3-year annualized NAV return of only 0.41% is especially important negative context: implementation survived the literal gate, but the return stream can be weak for multi-year stretches.

No capital deployment is authorized.
