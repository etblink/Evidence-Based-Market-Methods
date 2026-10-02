# SYNTH-001 — Finalist Implementability Synthesis

Captured: 2026-10-02

Purpose: compare provisional experiment candidates by the cost and cleanliness of learning something decision-relevant.

Authority boundary: this file records implementation facts and synthesis inputs. Current finalist status and next action belong only in `STATE.yaml`.

## Public research infrastructure

### EV-IMPL-001 — Kenneth French Data Library
Source: Kenneth R. French Data Library, Dartmouth.
URL: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html

Finding: the library publicly provides monthly and daily U.S. factor returns and portfolio sorts for book-to-market, operating profitability, momentum, and related signals, including historical archives for several factor constructions. Momentum portfolios are reconstituted monthly; many fundamental portfolios are reconstituted annually.
Important limitation: the library reconstructs full histories as underlying CRSP data and construction methods are updated, so a current download is not a pristine time-stamped historical dataset. Historical archives should be used where needed to study revision sensitivity.

### EV-IMPL-002 — AQR public research datasets
Source: AQR Data Sets.
URL: https://www.aqr.com/Insights/Datasets

Finding: AQR publicly maintains updated monthly datasets for Quality Minus Junk, momentum, Value and Momentum Everywhere, time-series momentum, and other published factor research. Long-only quality-sorted portfolios are also available.
Important limitation: these are author/practitioner-maintained research series and should not be mistaken for an independent raw-data replication.

### EV-IMPL-003 — SEC EDGAR APIs
Source: U.S. Securities and Exchange Commission, EDGAR APIs.
URL: https://www.sec.gov/search-filings/edgar-application-programming-interfaces

Finding: public, unauthenticated APIs expose submissions history and standardized XBRL financial-statement facts and are updated throughout the day; bulk data are also available.
Important limitation: standardized XBRL coverage begins in the modern filing era and a clean historical equity backtest still needs point-in-time security identifiers, prices, delistings, corporate actions, and careful taxonomy handling.

### EV-IMPL-004 — I/B/E/S estimates
Source: LSEG I/B/E/S Broker Estimates.
URL: https://www.lseg.com/en/data-catalogue/company-data/ibes-estimates/broker-estimates

Finding: I/B/E/S provides deep historical point-in-time analyst estimates, revisions, recommendations, and consensus data extending to 1976 in the United States and 1987 internationally.
Important limitation: this is a commercial institutional dataset rather than a simple free public source, materially raising the cost of a clean earnings-revision replication.

### EV-IMPL-005 — CME continuous futures data
Source: CME Group Continuous Price Series.
URL: https://www.cmegroup.com/market-data/cme-group-continuous-price-series.html

Finding: CME provides official settlement-based continuous futures series intended for strategy design and backtesting, with roll information and optional mapped volume/open-interest data.
Important limitation: historical access is a licensed data product, and a faithful diversified trend implementation adds futures-roll, leverage, collateral, and execution assumptions beyond an equity-factor audit.

## Candidate comparison

### FUND_VALUE
- Empirical case: strong enough to retain.
- Public audit data: high accessibility.
- Raw independent replication burden: moderate to high.
- Turnover burden: low.
- Live implementation can be long-only: yes.
- Main unresolved question: whether the premium remains useful after publication and in accessible large/liquid stocks.
- Cheapest next test: common-universe public factor/portfolio persistence audit.

### FUND_QUALITY_PROFITABILITY
- Empirical case: strong enough to retain.
- Public audit data: high accessibility through operating-profitability and QMJ research portfolios.
- Raw independent replication burden: moderate to high.
- Turnover burden: low.
- Live implementation can be long-only: yes.
- Main unresolved question: how much of the published long-short premium survives in simple long-only exposure.
- Cheapest next test: common-universe public profitability-factor/portfolio persistence audit.

### FUND_EARNINGS_REVISION
- Empirical case: strong enough to retain.
- Public audit data: incomplete for the cleanest version because historical analyst expectations/revisions are usually commercial.
- Raw independent replication burden: high.
- Turnover burden: moderate to high.
- Live implementation can be long-only: yes, but signal timing matters.
- Main unresolved question: contemporary net profitability after data timing, spreads, and attention competition.
- Decision for first test: preserve as a later candidate; do not pay the data/engineering cost before cheaper candidates are screened.

### PRICE_CROSS_SECTIONAL_MOMENTUM
- Empirical case: strong enough to retain.
- Public audit data: high accessibility.
- Raw independent replication burden: moderate because point-in-time universes and delistings matter.
- Turnover burden: moderate.
- Live implementation can be long-only: yes, though classic evidence is often long-short.
- Main unresolved question: post-publication persistence, crash behavior, and long-only implementation economics.
- Cheapest next test: common-universe public momentum-factor/portfolio persistence audit.

### PRICE_TIME_SERIES_TREND
- Empirical case: strong enough to retain.
- Public audit data: available as author-maintained factor series.
- Independent raw replication burden: high relative to the equity finalists.
- Turnover burden: moderate.
- Live implementation usually requires multi-asset futures or imperfect proxies: yes.
- Main unresolved question: how much directional trend value survives after separating volatility scaling and realistic futures implementation.
- Decision for first test: preserve as a later candidate; do not incur futures-data and implementation complexity before the simpler equity candidates are screened.

## Minimal informative next gate

The lowest-cost common comparison is a U.S. equity factor survivability audit using the same public research-data ecosystem for:

1. value, represented initially by HML;
2. profitability, represented initially by RMW;
3. cross-sectional momentum, represented initially by Mom.

This is an evidence gate, not yet a proposed live trading strategy. HML, RMW, and Mom are long-short research factors and therefore do not by themselves establish an individually implementable long-only portfolio.

The audit should emphasize a common post-publication period, recent-period stability, drawdowns, and sensitivity to data revisions. It should use no parameter search and no strategy optimization.

Because the current research process has already viewed some recent factor summaries and the literature itself reports historical performance, this retrospective audit must be labeled exploratory/adversarial rather than a pristine confirmatory holdout. A genuinely confirmatory test would require a frozen prospective period or an independently sequestered dataset.
