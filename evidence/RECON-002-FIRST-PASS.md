# RECON-002 — First-Pass Evidence Snapshot

Captured: 2026-10-02

Purpose: preserve the evidence inspected during the first comparative reconnaissance across the frozen method families.

Authority boundary: this file records source findings and limitations. It does **not** define the project's current dispositions or next action; those belong only in `STATE.yaml`.

## General and benchmark evidence

### EV-BENCH-001 — SPIVA U.S. Year-End 2025
Source: S&P Dow Jones Indices, "SPIVA U.S. Year-End 2025" (2026).
URL: https://www.spglobal.com/spdji/en/spiva/article/spiva-us

Finding: 79% of active U.S. large-cap equity funds underperformed the S&P 500 in 2025; other categories also showed substantial underperformance rates.
Limit: one-year results are not evidence that all active methods are impossible; the value is primarily as a benchmark reminder.

### EV-BENCH-002 — SPIVA Institutional Scorecard Year-End 2025
Source: S&P Dow Jones Indices, "SPIVA Institutional Scorecard Year-End 2025" (2026).
URL: https://www.spglobal.com/spdji/en/spiva/article/institutional-spiva-scorecard/

Finding: over the ten years ending 2025, at least 80% of equity funds in the reported institutional/mutual-fund formats underperformed their benchmarks after fees.
Limit: manager/fund outcomes do not isolate the causal validity of any one investment method.

### EV-GEN-001 — Replicating Anomalies
Source: Hou, Xue, and Zhang, "Replicating Anomalies," Review of Financial Studies (2020; NBER working paper 2017).
URL: https://www.nber.org/papers/w23394

Finding: in a standardized replication library of 447 anomaly variables, 64% were insignificant at the conventional 5% threshold and 85% were insignificant under a stricter t-value threshold of three; surviving magnitudes were often smaller than originally reported.
Limit: replication choices such as breakpoints, weighting, and factor models affect which anomalies survive.

### EV-GEN-002 — Post-publication anomaly decay
Source: Jacobs and Müller, "Anomalies across the globe: Once public, no longer existent?" Journal of Financial Economics (2020).
URL: https://www.sciencedirect.com/science/article/pii/S0304405X19301618

Finding: U.S. anomaly returns declined materially out of sample and after publication, while the international post-publication pattern differed.
Limit: decay is not uniform across countries or anomaly definitions and does not imply every published effect disappears.

## FUND — Fundamental corporate information

### EV-FUND-001 — Piotroski F-score
Source: Joseph D. Piotroski, "Value Investing: The Use of Historical Financial Statement Information to Separate Winners from Losers," Journal of Accounting Research (2000).
URL: https://www.jstor.org/stable/2672906

Finding: within high book-to-market firms, a simple accounting-strength score materially shifted historical portfolio returns toward financially stronger firms.
Limit: original-sample success does not establish current net exploitability, and small/distressed firms can create implementation frictions.

### EV-FUND-002 — Gross profitability
Source: Robert Novy-Marx, "The Other Side of Value: The Gross Profitability Premium," Journal of Financial Economics (2013; NBER working paper 2010).
URL: https://www.nber.org/papers/w15940

Finding: gross profitability had substantial cross-sectional relation to average stock returns and complemented value in the historical sample.
Limit: a return characteristic may represent risk compensation, mispricing, or both; existence does not establish a standalone live strategy.

### EV-FUND-003 — Profitability and investment factors
Source: Eugene F. Fama and Kenneth R. French, "A five-factor asset pricing model," Journal of Financial Economics (2015).
URL: https://www.sciencedirect.com/science/article/pii/S0304405X14002323

Finding: adding profitability and investment factors improved the model's description of average stock returns relative to the earlier three-factor model.
Limit: factor-model explanatory power is not equivalent to a tradable alpha and the model still leaves important return patterns unexplained.

## PRICE — Price and volume dynamics

### EV-PRICE-001 — Time-series momentum
Source: Moskowitz, Ooi, and Pedersen, "Time series momentum," Journal of Financial Economics (2012).
URL: https://www.sciencedirect.com/science/article/pii/S0304405X11002613

Finding: the study documented one-to-twelve-month return persistence across 58 liquid equity-index, currency, commodity, and bond futures.
Limit: later work disputes how much reported alpha is due to the momentum signal itself versus volatility scaling and portfolio construction.

### EV-PRICE-002 — Long-history trend following
Source: Hurst, Ooi, and Pedersen, "A Century of Evidence on Trend-Following Investing" (2017).
URL: https://www.aqr.com/insights/research/journal-article/a-century-of-evidence-on-trend-following-investing

Finding: reconstructed trend-following strategies showed positive long-run historical results across a sample extending back to 1880.
Limit: the authors are affiliated with a firm that uses related strategies, and reconstructed historical implementation is not identical to live individual execution.

### EV-PRICE-003 — Volatility-scaling critique
Source: Kim, Tse, and Wald, "Time series momentum and volatility scaling," Journal of Financial Markets (2016).
URL: https://www.sciencedirect.com/science/article/abs/pii/S1386418116301379

Finding: the paper argues that much of the previously reported time-series-momentum alpha is attributable to volatility scaling rather than the directional signal alone.
Limit: this challenges the interpretation and implementation of the effect rather than establishing that all trend information is absent.

### EV-PRICE-004 — Large technical-rule test
Source: Kevin Rink, "The predictive ability of technical trading rules: an empirical analysis of developed and emerging equity markets," Financial Markets and Portfolio Management (2023).
URL: https://link.springer.com/article/10.1007/s11408-023-00433-2

Finding: 6,406 technical rules across 41 equity markets showed severe degradation, sensitivity to costs, and weak out-of-sample persistence among rules that looked best historically.
Limit: the result is strongest against broad rule-mining and strategy selection; it does not by itself negate every price-based phenomenon.

## EVENT — Event-driven and special situations

### EV-EVENT-001 — Post-earnings-announcement drift review
Source: Josef Fink, "A review of the Post-Earnings-Announcement Drift," Journal of Behavioral and Experimental Finance (2021).
URL: https://www.sciencedirect.com/science/article/pii/S2214635020303750

Finding: the review documents a long literature in which prices continue to drift in the direction of earnings surprises; explanations include risk, trading frictions, and behavioral underreaction.
Limit: persistence of the anomaly does not guarantee implementable profit after trading frictions and modern information processing.

### EV-EVENT-002 — Risk arbitrage
Source: Mitchell and Pulvino, "Characteristics of Risk and Return in Risk Arbitrage," Journal of Finance (2001).
URL: https://onlinelibrary.wiley.com/doi/10.1111/0022-1082.00401

Finding: a large merger sample produced estimated excess returns after transaction costs, but risk-arbitrage returns behaved nonlinearly and were especially exposed in severe market declines.
Limit: the premium can be compensation for concentrated deal/tail risk rather than a free mispricing.

### EV-EVENT-003 — Limited arbitrage in mergers
Source: Baker and Savaşoglu, "Limited arbitrage in mergers and acquisitions," Journal of Financial Economics (2002).
URL: https://www.sciencedirect.com/science/article/pii/S0304405X02000727

Finding: diversified merger-arbitrage positions earned historical abnormal returns that increased with completion risk and constraints on arbitrage capital.
Limit: the sample is historical, and current spreads are competed over by specialized participants with superior deal infrastructure.

### EV-EVENT-004 — Long-run corporate-event anomalies under controls
Source: Bessembinder and Zhang, "Firm characteristics and long-run stock returns after corporate events," Journal of Financial Economics (2013).
URL: https://www.sciencedirect.com/science/article/pii/S0304405X13000524

Finding: several apparent long-run abnormal-return patterns after corporate events became insignificant after improved controls for firm characteristics.
Limit: the result targets broad long-horizon event-study claims and does not invalidate all event-driven strategies.

## MACRO — Macro and cross-asset premia

### EV-MACRO-001 — Value and momentum across markets
Source: Asness, Moskowitz, and Pedersen, "Value and Momentum Everywhere," Journal of Finance (2013).
URL: https://onlinelibrary.wiley.com/doi/10.1111/jofi.12021

Finding: value and momentum premia appeared across multiple markets and asset classes with a common global structure.
Limit: the findings do not establish that an individual can reproduce institutional long-short implementations cheaply.

### EV-MACRO-002 — Carry across asset classes
Source: Koijen, Moskowitz, Pedersen, and Vrugt, "Carry," Journal of Financial Economics (2018).
URL: https://www.sciencedirect.com/science/article/pii/S0304405X17302908

Finding: carry predicted returns across equities, bonds, commodities, Treasuries, credit, currencies, and options and was associated with recession, liquidity, and volatility risks.
Limit: part of the return may be compensation for adverse states rather than mispricing.

### EV-MACRO-003 — Aggregate market timing
Source: Welch, Goyal, and Zafirov, "A Comprehensive 2022 Look at the Empirical Performance of Equity Premium Prediction," Review of Financial Studies (2024).
URL: https://academic.oup.com/rfs/article/37/11/3490/7749383

Finding: many published equity-premium predictors weakened in extended samples or out of sample, though a small subset retained useful performance.
Limit: this addresses aggregate equity-premium forecasting, not all systematic cross-asset risk-premium strategies.

## STAT — Statistical and relative-value relationships

### EV-STAT-001 — Pairs-trading costs
Source: "Costly arbitrage through pairs trading," Journal of Economic Dynamics and Control (2015).
URL: https://www.sciencedirect.com/science/article/pii/S016518891500072X

Finding: the literature summarized in the paper shows pairs-trading returns can fall sharply after realistic transaction costs, with some optimized continuous-trading approaches becoming impractical.
Limit: costs and opportunity sets vary by market, horizon, instrument, and implementation.

### EV-STAT-002 — Statistical limit of arbitrage
Source: Da, Nagel, and Xiu, "The Statistical Limit of Arbitrage," NBER Working Paper 33070 (2024).
URL: https://www.nber.org/papers/w33070

Finding: when alphas are weak and rare, estimation error prevents even sophisticated statistical learners from fully identifying and exploiting true pricing errors.
Limit: this is a theoretical/high-dimensional result and does not show that every statistical strategy is unprofitable.

## DERIV — Derivatives and volatility

### EV-DERIV-001 — Variance risk premium
Source: Bollerslev, Tauchen, and Zhou, "Expected Stock Returns and Variance Risk Premia," Review of Financial Studies (2009).
URL: https://academic.oup.com/rfs/article-abstract/22/11/4463/1565787

Finding: the gap between option-implied and realized variation contained substantial information about subsequent aggregate returns in the studied sample.
Limit: implementation depends on option data, volatility measurement, and exposure to risks not captured by a simple directional forecast.

### EV-DERIV-002 — Compensation for variance risk
Source: Bekaert, Engstrom, and Ermolov, "The Variance Risk Premium in Equilibrium Models," Review of Finance (2023; NBER working paper 2020).
URL: https://www.nber.org/papers/w27108

Finding: the equity variance risk premium is positive on average and is explicitly interpreted as compensation for selling variance risk, with high premia associated with adverse consumption-tail states.
Limit: a positive premium is not a free arbitrage; harvesting it can entail severe adverse-state exposure.

### EV-DERIV-003 — Option microstructure and inference
Source: Jefferson Duarte, "Very Noisy Option Prices and Inference Regarding the Volatility Risk Premium," Journal of Finance (2024).
URL: https://onlinelibrary.wiley.com/doi/10.1111/jofi.13365

Finding: option-return inference is highly sensitive to microstructure biases; after addressing them, the paper finds substantial negative average returns for several option categories and evidence of volatility risk pricing.
Limit: the result reinforces the reality of option risk premia while also showing that backtests in options are especially easy to mismeasure.

## MICRO — Microstructure and liquidity

### EV-MICRO-001 — Market microstructure survey
Source: Biais, Glosten, and Spatt, "Market microstructure: A survey of microfoundations, empirical results, and policy implications," Journal of Financial Markets (2005).
URL: https://www.sciencedirect.com/science/article/pii/S1386418104000382

Finding: spreads and short-horizon pricing reflect real order-handling, inventory, adverse-selection, market-power, and information frictions.
Limit: existence of microstructure frictions does not imply they are exploitable by a participant without competitive execution infrastructure.

### EV-MICRO-002 — Latency arbitrage
Source: "A note on the relationship between high-frequency trading and latency arbitrage" (2016).
URL: https://www.sciencedirect.com/science/article/pii/S1057521916301090

Finding: the study reports profitable latency-arbitrage behavior and measurable effects on other market participants and market quality.
Limit: the mechanism is inherently speed- and infrastructure-dependent, making direct replication unlike ordinary retail investing.

## INFO — Specialized information and alternative data

### EV-INFO-001 — Analyst coverage as information
Source: "Uncovering expected returns: Information in analyst coverage proxies," Journal of Financial Economics (2017).
URL: https://www.sciencedirect.com/science/article/pii/S0304405X1730020X

Finding: abnormal analyst coverage predicted subsequent returns and future fundamental improvements in the historical sample.
Limit: the signal may be difficult to reproduce in real time and could overlap with other known characteristics.

### EV-INFO-002 — News-sentiment persistence
Source: "The persistence of news sentiment: Implications for return predictability," Economics Letters (2026).
URL: https://www.sciencedirect.com/science/article/pii/S0165176525006408

Finding: firm-level news sentiment from 2000–2023 showed short-horizon continuation and longer-horizon reversal patterns after standard factor adjustment.
Limit: the study uses a commercial RavenPack dataset and does not by itself establish an accessible after-cost individual strategy.

### EV-INFO-003 — News trading and spreads
Source: "When machines read the news: Using automated text analytics to quantify high frequency news-implied market reactions" (2011).
URL: https://www.sciencedirect.com/science/article/pii/S0927539810000873

Finding: machine-classified news contained predictive information, but bid-ask spreads materially degraded the profitability of news-implied trading.
Limit: modern competition and faster information processing may further change the economics of this class of signal.
