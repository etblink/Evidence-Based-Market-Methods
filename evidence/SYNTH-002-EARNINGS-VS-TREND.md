# SYNTH-002 — Earnings Underreaction vs. Diversified Trend

Captured: 2026-10-02

Purpose: compare the two remaining serious provisional candidates by evidence quality, test cost, implementation burden, and decision value after the quality/profitability implementation path was deferred.

Authority boundary: this file records synthesis evidence. `STATE.yaml` remains the sole canonical current state.

## Candidate 1 — FUND_EARNINGS_REVISION

### Evidence status

Post-earnings-announcement drift (PEAD) remains a substantial research literature. Recent work continues to find drift or mechanisms associated with underreaction, attention, order flow, and retail behavior.

Recent supportive/qualified evidence includes:
- NBER 2025: retail investors' contrarian trading around large earnings surprises is associated with PEAD and momentum.
  https://www.nber.org/papers/w34086
- 2025 Journal of Contemporary Accounting & Economics: firm-specific news before earnings announcements reduces subsequent drift, consistent with information-processing effects.
  https://www.sciencedirect.com/science/article/pii/S1815566925000256
- 2026 working paper on the SEC T+1 settlement reform: the shortest-horizon PEAD compressed after settlement-cycle shortening, while longer horizons remained.
  https://papers.ssrn.com/sol3/Delivery.cfm/7490899.pdf

But the interpretation is not settled:
- A 2026 U.S. analyst-SUE study covering 2000–2024 reports that, after decomposing expected returns, the 60-day post-announcement residual Q5-Q1 spread falls to an insignificant level, arguing that longer drift may reflect expected-return compensation rather than continued underreaction.
  https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6440878

Trading frictions also matter:
- 2024 experimental evidence finds transaction fees and short/margin constraints reduce the profitability of PEAD exploitation.
  https://www.sciencedirect.com/science/article/pii/S0148619524000584

### Data and test burden

The clean classic test usually needs point-in-time analyst expectations, actual reported earnings, announcement timing, security identifiers, and return data.

LSEG I/B/E/S is the market-standard source:
- U.S. estimates history from 1976;
- more than 18,000 analysts and 950+ contributing firms;
- estimate values, source/announcement dates, fiscal periods, and related metadata.
  https://www.lseg.com/en/data-catalogue/company-data/ibes-estimates/broker-estimates

WRDS lists the global historical I/B/E/S estimates product at hundreds of gigabytes and institutional access scale.

Public substitutes are possible, such as announcement-window returns or SEC filing/event proxies, but they test a materially different hypothesis or require substantial point-in-time engineering.

### Individual implementation

No comparably clean, low-cost retail vehicle was identified that isolates classic PEAD or analyst-revision drift. An individual implementation is therefore likely to require direct security selection, event timing, and meaningful turnover.

### Disposition from this synthesis

**Defer, not reject.**

The phenomenon remains scientifically interesting, but the next honest test has high data and engineering cost and the underlying interpretation is currently contested. It fails the project's finite-time test for the next experiment.

---

## Candidate 2 — PRICE_TIME_SERIES_TREND

### Evidence status

The classic TSMOM evidence remains unusually broad and long-lived, and AQR continues to publish an updated monthly version of the original 58-market factor through 2026:
https://www.aqr.com/Insights/Datasets/Time-Series-Momentum-Factors-Monthly

The public series uses the classic 12-month own-return signal with one-month holding period across equity-index, currency, commodity, and developed-government-bond futures.

However, the effect is not beyond dispute:
- prior work shows volatility scaling explains part of reported TSMOM alpha;
- a 2024 replication study reports no statistically reliable TSMOM effect across roughly 55 developed commodity futures under bootstrap inference.
  https://www.sciencedirect.com/science/article/abs/pii/S0927538X24002245

This disagreement is a reason to test the effect rather than assume it.

### Data and test burden

Independent raw replication with official futures data remains nontrivial. CME now offers official continuous futures series, but historical access is licensed:
https://www.cmegroup.com/market-data/cme-group-continuous-price-series.html

Crucially, the project does **not** need to buy that data to run the next screen:
1. AQR provides the updated classic research factor publicly.
2. A direct retail implementation exists with a transparent mechanical rule.

### Individual implementation

KMLM — KraneShares Mount Lucas Managed Futures Index Strategy ETF:
- inception: 2020-12-01;
- expense ratio: 0.90%;
- 22 futures markets: 11 commodities, 6 currencies, 5 global bond markets;
- each market receives a daily long/short trend signal based on price relative to a long-term moving average;
- target average annualized volatility: approximately 15%;
- monthly rebalancing.

Official sources:
https://kraneshares.com/etf/kmlm/
https://kraneshares.com/kmlm-managed-futures-faq/
https://kraneshares.com/resources/compliance/2024_08_01_kraneshares_statutory.prospectus.pdf

This is not the same signal as AQR's 12-month TSMOM factor, but it is close enough in economic mechanism to provide an inexpensive product-level implementation check without constructing a futures system.

Other managed-futures ETFs exist, but many mix trend with carry, mean reversion, replication, or discretionary components. KMLM is preferred for the first implementation gate because the trend rule is unusually transparent and comparatively pure.

### Disposition from this synthesis

**Select for the next bounded experiment.**

Trend has:
- a serious but contested empirical claim;
- a free continuously updated research-factor series;
- an individually accessible transparent implementation;
- no requirement for paid data at the screening stage;
- a clean failure path before any futures infrastructure is built.

---

## Comparative decision

| Criterion | Earnings underreaction | Diversified trend |
|---|---|---|
| Strong historical literature | Yes | Yes |
| Recent controversy | Yes | Yes |
| Free canonical research series | No clean equivalent identified | Yes |
| Clean test without paid institutional data | Difficult | Yes |
| Transparent retail implementation | No close pure vehicle identified | Yes — KMLM |
| Engineering burden for first screen | High | Low-to-moderate |
| Turnover/timing sensitivity | High | Moderate |
| Appropriate next use of scarce research time | Defer | **Proceed** |

The choice of trend is based on **information gain per unit of time**, not a presumption that trend is true.

No capital deployment is authorized.
