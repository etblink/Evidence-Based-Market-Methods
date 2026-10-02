# AUDIT-001 — U.S. Factor Survivability Audit

Captured: 2026-10-02

Status: **exploratory / adversarial, not confirmatory**

Purpose: execute the frozen `AUDIT-001` gate from `STATE.yaml` without parameter search or strategy optimization.

Authority boundary: this file records the audit evidence and calculations. It does **not** define current project state or authorize capital deployment; those belong only in `STATE.yaml`.

## Frozen protocol

The protocol was frozen before full factor-history inspection:

- public monthly research data only;
- common analysis window beginning 2016-01;
- no parameter search;
- no strategy optimization;
- report full-period and 2020+ results;
- measure annualized arithmetic mean, annualized volatility, annualized Sharpe, maximum drawdown, cumulative return, and sign consistency;
- treat HML, RMW, and Mom as research-factor evidence rather than live portfolios;
- exploratory label required;
- no capital deployment.

## Inputs and provenance

To keep the factor series on one matched reconstruction vintage, the audit uses files whose own headers both state that they were created from the **202606 CRSP database**.

### HML and RMW

Repository: `BuyRisk/buyrisk.github.io`  
Path: `data/sources/french/F-F_Research_Data_5_Factors_2x3.csv`  
Git blob SHA: `fdd1ed5af3a03910cf96334d6ad6937ed80f17e7`  
Header: `This file was created using the 202606 CRSP database.`  
Monthly coverage in the file: 1963-07 through 2026-06.

### Mom

Repository: `robinmak/thematic-investing`  
Path: `backtest/factor_data/F-F_Momentum_Factor.csv`  
Git blob SHA: `c49c65accaa1d47d75cb899b524e661fe9b7abc8`  
Header: `This file was created using the 202606 CRSP database.`  
Monthly coverage in the file: 1927-01 through 2026-06.

The live Kenneth French Data Library had subsequently advanced beyond this frozen mirror vintage. The matched June 2026 vintage was used intentionally rather than mixing reconstruction vintages.

The official French library also documents a material CRSP input-format transition beginning with the January 2025 data release: U.S. research returns moved from the legacy FIZ files to CIZ files, including a change in the timing of dividend reinvestment. This reinforces why the exact input vintage and blob identity are preserved here.

## Definitions

All source factor returns are percentage monthly returns and were divided by 100 before calculation.

For monthly returns \(r_t\):

- annualized arithmetic mean = \(12\bar r\);
- annualized volatility = \(s_r\sqrt{12}\), using sample standard deviation;
- annualized Sharpe = \(\bar r / s_r \times \sqrt{12}\);
- cumulative return = \(\prod_t(1+r_t)-1\);
- maximum drawdown = largest peak-to-trough decline in the compounded factor wealth series;
- sign consistency = fraction of months with factor return strictly greater than zero.

No risk-free rate is subtracted from the long-short factor returns.

## Results

### Full frozen window: 2016-01 through 2026-06

| Factor | Months | Ann. mean | Ann. vol. | Sharpe | Cumulative | Max drawdown | Positive months |
|---|---:|---:|---:|---:|---:|---:|---:|
| HML | 126 | 0.53% | 13.18% | 0.04 | -3.39% | -51.32% | 43.65% (55/126) |
| RMW | 126 | 1.84% | 8.26% | 0.22 | 17.10% | -26.15% | 57.14% (72/126) |
| Mom | 126 | 2.59% | 13.48% | 0.19 | 19.14% | -25.42% | 54.76% (69/126) |

### Recent subperiod: 2020-01 through 2026-06

| Factor | Months | Ann. mean | Ann. vol. | Sharpe | Cumulative | Max drawdown | Positive months |
|---|---:|---:|---:|---:|---:|---:|---:|
| HML | 78 | 2.45% | 15.04% | 0.16 | 9.00% | -33.73% | 46.15% (36/78) |
| RMW | 78 | 1.68% | 9.82% | 0.17 | 8.17% | -26.15% | 56.41% (44/78) |
| Mom | 78 | 5.59% | 14.38% | 0.39 | 34.22% | -25.42% | 60.26% (47/78) |

## Frozen-question answers

### Did HML remain directionally positive?

**Mixed / weak.** Its arithmetic monthly mean was slightly positive over 2016-06/2026-06, but compounding the factor produced a **-3.39%** cumulative return and a **-51.32%** maximum drawdown. It was positive over the 2020+ subperiod. This does not look like a strong survivability result for HML over the full frozen window.

### Did RMW remain directionally positive?

**Yes, modestly.** RMW had positive arithmetic and compounded returns in both windows, with lower volatility than HML or Mom. The magnitude is not large and the maximum drawdown still reached about 26%.

### Did Mom remain directionally positive?

**Yes.** Mom had positive arithmetic and compounded returns in both windows. Its recent 2020+ record was the strongest of the three in this audit, although the full-window Sharpe remained modest and the maximum drawdown was about 25%.

## What the audit does and does not establish

The result supports continued investigation of profitability/quality and cross-sectional momentum more strongly than a standalone HML implementation.

It does **not** establish that RMW or Mom is a profitable strategy available to an individual because:

1. HML, RMW, and Mom are long-short research factors, not directly investable long-only portfolios.
2. Factor returns do not deduct an individual's commissions, spreads, slippage, taxes, financing, shorting constraints, or fund fees.
3. The audit uses a reconstructed research-data vintage rather than raw point-in-time CRSP security histories.
4. The project had already reviewed literature about these factors, so the 2016 start is an exploratory post-publication stress window, not an untouched holdout.
5. French factor histories can change as CRSP data and construction inputs are revised; this audit therefore pins exact blob identities.
6. The official U.S. series changed CRSP source-file methodology beginning with the January 2025 release, which is another reason not to overinterpret small differences.
7. The favorable long-short result can come partly from the short leg; an individual may only want or be able to hold the long side.

## Decision value

A more expensive raw-security replication is **not yet justified**.

The cheapest next discriminator is to test whether the two better-surviving signals translate into simple, large-stock, long-only portfolio behavior:

- robust/profitable large stocks versus the broad market;
- high-prior-return large stocks versus the broad market.

That next gate can still use public French portfolio-sort data and can therefore answer an implementation-relevant question before the project incurs point-in-time CRSP/Compustat engineering or commercial-data costs.

HML/value remains retained as a scientifically credible family, but this audit does not justify prioritizing it for the next implementation gate.
