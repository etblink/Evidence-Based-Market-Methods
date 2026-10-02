# RECON-004 — EVENT, MACRO, and INFO Deepening Evidence

Captured: 2026-10-02

Purpose: deepen the remaining retained families enough to determine whether any should join or displace the provisional FUND and PRICE experiment candidates.

Authority boundary: this file preserves source findings and limitations. It does **not** define current project state or dispositions; those belong only in `STATE.yaml`.

## EVENT — Event-driven and special situations

### EVENT-MERGER-ARBITRAGE

#### EV-EVENT-MA-001 — Risk-arbitrage returns and nonlinear risk
Source: Mitchell and Pulvino, "Characteristics of Risk and Return in Risk Arbitrage," Journal of Finance (2001).
URL: https://onlinelibrary.wiley.com/doi/10.1111/0022-1082.00401

Finding: a large historical merger sample produced positive estimated excess returns after transaction costs, but the payoff was nonlinear and especially exposed during severe market declines.
Limit: the return can represent compensation for deal-break and crash risk rather than free mispricing; implementation also requires diversified deal monitoring and event-specific judgment.

#### EV-EVENT-MA-002 — Limited arbitrage in mergers
Source: Baker and Savaşoglu, "Limited arbitrage in mergers and acquisitions," Journal of Financial Economics (2002).
URL: https://www.sciencedirect.com/science/article/pii/S0304405X02000727

Finding: merger-arbitrage spreads increased with completion risk and constraints on arbitrage capital, supporting a coherent source of returns.
Limit: the mechanism itself implies that easy capital can compress the opportunity and that the remaining premium may be concentrated in difficult states and transactions.

### EVENT-SPINOFFS

#### EV-EVENT-SPIN-001 — Historical spinoff evidence
Source: Cusatis, Miles, and Woolridge, "Restructuring through spinoffs: The stock market evidence," Journal of Financial Economics (1993).
URL: https://www.sciencedirect.com/science/article/pii/0304405X9390009Z

Finding: spinoffs and parents showed positive long-horizon abnormal returns in the 1965–1988 sample, but the abnormal performance was concentrated in firms later involved in takeover activity.
Limit: the result is old, conditional, and belongs to the methodologically fragile long-horizon event-study literature; it does not establish a generic modern spinoff premium.

### EVENT-REPURCHASES

#### EV-EVENT-REP-001 — Long-run repurchase anomaly debate
Source: "Long-run stock performance following stock repurchases" (2010), Quarterly Review of Economics and Finance.
URL: https://www.sciencedirect.com/science/article/abs/pii/S1062976910000268

Finding: some studies report post-repurchase drift consistent with underreaction to undervaluation signals.
Limit: the same literature notes that long-run abnormal returns often weaken or disappear under calendar-time methods that better handle cross-correlation; the anomaly is method-sensitive.

## MACRO — Macro and cross-asset premia

### MACRO-CARRY-TERM

#### EV-MACRO-CT-001 — Carry across asset classes
Source: Koijen, Moskowitz, Pedersen, and Vrugt, "Carry," Journal of Financial Economics (2018).
URL: https://www.sciencedirect.com/science/article/pii/S0304405X17302908

Finding: carry predicted returns across multiple asset classes and had common variation associated with recession, liquidity, and volatility risks.
Limit: the shared adverse-state exposures support a risk-premium interpretation and make historical average return an incomplete measure of attractiveness.

#### EV-MACRO-CT-002 — Carry post-publication performance
Source: Hsu, Taylor, Wang, and Li, "On the profitability of influential carry-trade strategies: Data-snooping bias and post-publication performance," Journal of Empirical Finance (2025).
URL: https://www.sciencedirect.com/science/article/pii/S0927539825000623

Finding: most of thirteen influential FX carry strategies remained profitable before publication after multiple-testing corrections, but profits declined materially after academic publication.
Limit: the paper addresses influential currency carry rules rather than every possible carry implementation, but it directly weakens the assumption that published historical magnitudes remain available.

### MACRO-DIRECTIONAL-FORECASTING

#### EV-MACRO-DF-001 — Extended equity-premium prediction review
Source: Goyal, Welch, and Zafirov, "A Comprehensive 2022 Look at the Empirical Performance of Equity Premium Prediction," Review of Financial Studies (2024).
URL: https://academic.oup.com/rfs/article/37/11/3490/7749383

Finding: among 29 newer variables from 26 papers plus 17 older variables, more than one-third of the newer predictors lost even in-sample significance in the extended data; among those retaining significance, about half had poor out-of-sample performance, while only a small subset remained useful.
Limit: a few predictors survive and improved methods can extract additional information; the evidence argues against generic confidence in macro market timing, not against all predictability.

#### EV-MACRO-DF-002 — Machine-learning equity-premium forecasting
Source: "Forecasting the equity premium: can machine learning beat the historical average?" Quantitative Finance (2024).
URL: https://www.tandfonline.com/doi/abs/10.1080/14697688.2024.2409278

Finding: multiple machine-learning models showed strong in-sample ability, but the out-of-sample results generally failed to beat the historical-average forecast.
Limit: model classes and predictors are finite; failure of tested ML methods is not a theorem that aggregate returns cannot be forecast.

## INFO — Specialized information and alternative data

### INFO-ANALYST-ACTIONS

#### EV-INFO-AA-001 — Abnormal analyst coverage
Source: Lee and So, "Uncovering expected returns: Information in analyst coverage proxies," Journal of Financial Economics (2017).
URL: https://www.sciencedirect.com/science/article/pii/S0304405X1730020X

Finding: abnormal analyst coverage predicted subsequent returns and future improvements in fundamentals, consistent with analysts allocating attention toward underpriced firms.
Limit: reconstructing expected versus abnormal coverage requires data and modeling choices, and the historical relation may overlap with other firm characteristics.

### INFO-NEWS-SENTIMENT

#### EV-INFO-NS-001 — Text-identified fundamental news
Source: Boudoukh, Feldman, Kogan, and Richardson, "Which News Moves Stock Prices? A Textual Analysis," Journal of Finance (2013; NBER working paper).
URL: https://www.nber.org/papers/w18725

Finding: better classification of economically relevant news produced much stronger relationships between news, tone, and stock-price behavior; identified news days showed continuation rather than the reversal common on no-news days.
Limit: information content does not establish that an investor observing public news can trade fast enough or cheaply enough to earn abnormal returns.

#### EV-INFO-NS-002 — High-frequency sentiment predictability
Source: Sun, Najand, and Shen, "Stock return predictability and investor sentiment: A high-frequency perspective," Journal of Banking & Finance (2016).
URL: https://www.sciencedirect.com/science/article/abs/pii/S0378426616301595

Finding: lagged half-hour sentiment from a proprietary textual dataset predicted intraday S&P 500 returns in the study.
Limit: the horizon is extremely short and the dataset proprietary, making speed, data access, and transaction costs central to actual exploitability.

#### EV-INFO-NS-003 — News trading and bid-ask costs
Source: "When machines read the news: Using automated text analytics to quantify high frequency news-implied market reactions" (2011).
URL: https://www.sciencedirect.com/science/article/pii/S0927539810000873

Finding: machine-classified news contained predictive information, but bid-ask spreads materially degraded trading profitability.
Limit: modern automated competition is faster than in the historical sample, so accessibility to a non-specialized individual is unlikely to have improved.

## Cross-family observations supported by the evidence

1. Event-driven returns can be real, but merger arbitrage in particular carries explicit deal-break and market-stress risk, while other event anomalies are often method-sensitive.
2. Carry has unusually coherent evidence as a cross-asset premium, yet adverse-state exposure and recent post-publication decay materially reduce its appeal as a first individual experiment.
3. Generic directional macro forecasting remains fragile out of sample even when richer predictor sets and machine learning are used; a small surviving subset prevents a blanket claim of impossibility.
4. Analyst behavior and textual/news information demonstrably contain market-relevant information, but the most directly exploitable versions tend to require timely proprietary data, fast execution, or specialized modeling.
5. None of these three families currently supplies a clearly cheaper, cleaner, and more individually accessible first experiment than the strongest FUND and PRICE subfamilies already retained.
