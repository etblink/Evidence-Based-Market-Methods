# RECON-003 — FUND and PRICE Deepening Evidence

Captured: 2026-10-02

Purpose: deepen the two strongest immediately actionable families from RECON-002 without yet authorizing an experiment.

Authority boundary: this file preserves source findings and limitations. It does **not** define current project state or dispositions; those belong only in `STATE.yaml`.

## FUND — Fundamental corporate information

### FUND-VALUE

#### EV-FUND-VALUE-001 — International value evidence
Source: Fama and French, "Size, value, and momentum in international stock returns," Journal of Financial Economics (2012).
URL: https://www.sciencedirect.com/science/article/pii/S0304405X12000931

Finding: value premiums appeared across North America, Europe, Japan, and Asia Pacific; outside Japan, value spreads generally decreased with firm size.
Limit: an average return premium does not determine whether the cause is mispricing or risk, and implementation can become more difficult where the effect is strongest.

#### EV-FUND-VALUE-002 — Fundamental valuation residuals
Source: Köstlmeier, "Pricing and mispricing of accounting fundamentals: Global evidence," Quarterly Review of Economics and Finance (2024).
URL: https://www.sciencedirect.com/science/article/abs/pii/S1062976923001485

Finding: a fundamentals-based valuation model explained substantial cross-sectional price variation in a global developed-market sample; firms classified as undervalued outperformed overvalued firms after several controls.
Limit: the easily exploitable long leg showed post-publication return decline, directly warning against assuming historical magnitude remains available.

#### EV-FUND-VALUE-003 — International five-factor evidence
Source: Fama and French, "International tests of a five-factor asset pricing model," Journal of Financial Economics (2017).
URL: https://www.sciencedirect.com/science/article/pii/S0304405X1630215X

Finding: average returns increased with book-to-market in all four tested regions, while profitability and investment relations were strong in North America, Europe, and Asia Pacific but weaker in Japan.
Limit: asset-pricing-factor success describes return structure; it does not prove a retail-tradable alpha.

### FUND-QUALITY-PROFITABILITY

#### EV-FUND-QP-001 — Gross profitability
Source: Novy-Marx, "The Other Side of Value: The Gross Profitability Premium," Journal of Financial Economics (2013).
URL: https://www.sciencedirect.com/science/article/pii/S0304405X13000044

Finding: gross profitability had roughly comparable cross-sectional predictive power to book-to-market and improved historical value strategies, including among larger and more liquid stocks.
Limit: the finding does not by itself distinguish mispricing from risk compensation or establish present-day net alpha.

#### EV-FUND-QP-002 — Quality Minus Junk
Source: Asness, Frazzini, and Pedersen, "Quality minus junk," Review of Accounting Studies (2019).
URL: https://link.springer.com/article/10.1007/s11142-018-9470-2

Finding: a composite quality factor based on profitability, growth, and safety earned significant historical risk-adjusted returns in the United States and 24 other countries.
Limit: the authors are affiliated with an asset manager that uses related ideas; the result is a long-short factor study, not a direct demonstration of an individual's attainable long-only excess return.

#### EV-FUND-QP-003 — International profitability and investment
Source: Fama and French, "International tests of a five-factor asset pricing model," Journal of Financial Economics (2017).
URL: https://www.sciencedirect.com/science/article/pii/S0304405X1630215X

Finding: profitability and conservative investment were associated with average returns in several developed-market regions.
Limit: geographic heterogeneity, including weak Japanese profitability/investment relations, argues against treating the signal as universal.

### FUND-FINANCIAL-STATEMENT-SCREENS

#### EV-FUND-FS-001 — Piotroski F-score
Source: Piotroski, "Value Investing: The Use of Historical Financial Statement Information to Separate Winners from Losers," Journal of Accounting Research (2000).
URL: https://www.jstor.org/stable/2672906

Finding: within high book-to-market stocks, a simple accounting-strength score historically separated stronger from weaker performers.
Limit: the result is conditional on a specific value-stock universe and historical sample; it is not evidence that arbitrary accounting screens remain exploitable.

#### EV-FUND-FS-002 — Large-scale anomaly replication
Source: Hou, Xue, and Zhang, "Replicating Anomalies," Review of Financial Studies (2020).
URL: https://www.nber.org/papers/w23394

Finding: 64% of 447 finance/accounting anomaly variables were insignificant at the conventional 5% threshold under standardized replication choices, rising to 85% under a t-value threshold of three.
Limit: replication outcomes depend on portfolio construction, breakpoints, weighting, and factor models; failure of many signals does not imply all accounting information is useless.

### FUND-EARNINGS-REVISION

#### EV-FUND-ER-001 — PEAD review
Source: Fink, "A review of the Post-Earnings-Announcement Drift," Journal of Behavioral and Experimental Finance (2021).
URL: https://www.sciencedirect.com/science/article/pii/S2214635020303750

Finding: a review spanning more than fifty years of literature found extensive evidence that prices can continue drifting in the direction of earnings surprises.
Limit: the literature offers multiple explanations—including risk, frictions, and underreaction—and anomaly existence does not establish current net profitability.

#### EV-FUND-ER-002 — Analyst forecast-revision underreaction
Source: "Analysts’ cash flow forecasts and the underreaction to earnings forecast revisions" (2025).
URL: https://www.tandfonline.com/doi/full/10.1080/00014788.2025.2545847

Finding: the paper reports that markets underreact to analyst earnings-forecast revisions and that richer cash-flow information mitigates the subsequent drift.
Limit: the result concerns a specific information environment and may require timely analyst data; it does not establish an inexpensive retail implementation.

### FUND-DISCRETIONARY-STOCK-PICKING

#### EV-FUND-DISC-001 — Active-manager persistence
Source: S&P Dow Jones Indices, "U.S. Persistence Scorecard Year-End 2025" (2026).
URL: https://www.spglobal.com/spdji/en/spiva/article/us-persistence-scorecard/

Finding: persistence among previously strong active U.S. equity funds was generally weak over multi-year horizons; none of the top-quartile large-cap funds from 2021 remained top quartile through 2025.
Limit: fund outcomes include fees, capacity, mandates, and organizational constraints and therefore cannot prove that no individual investor possesses skill.

#### EV-FUND-DISC-002 — Event-based evidence of stock-picking skill
Source: Baker, Litov, Wachter, and Wurgler, "Can Mutual Fund Managers Pick Stocks? Evidence from the Trades Prior to Earnings Announcements," JFQA (2010; NBER 2004).
URL: https://www.nber.org/papers/w10685

Finding: stocks bought by mutual funds before earnings announcements subsequently outperformed stocks they sold at the announcement, and the event-based skill metric showed some persistence.
Limit: evidence that some professional managers display skill does not supply a simple identification rule for finding skilled managers ex ante or prove that discretionary stock picking is the best use of an individual's time.

## PRICE — Price and volume dynamics

### PRICE-CROSS-SECTIONAL-MOMENTUM

#### EV-PRICE-XMOM-001 — U.S. momentum
Source: Jegadeesh and Titman, "Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency," Journal of Finance (1993).
URL: https://onlinelibrary.wiley.com/doi/full/10.1111/j.1540-6261.1993.tb04702.x

Finding: past winners outperformed past losers over subsequent three-to-twelve-month holding periods in the historical U.S. sample.
Limit: the original result predates decades of publication, market adaptation, and modern trading costs.

#### EV-PRICE-XMOM-002 — International momentum
Source: Rouwenhorst, "International Momentum Strategies," Journal of Finance (1998).
URL: https://onlinelibrary.wiley.com/doi/10.1111/0022-1082.95722

Finding: medium-term return continuation appeared in all twelve sampled international equity markets and was not confined to small firms.
Limit: the sample ended in 1995 and does not establish current after-cost profitability.

#### EV-PRICE-XMOM-003 — International value and momentum
Source: Fama and French, "Size, value, and momentum in international stock returns," Journal of Financial Economics (2012).
URL: https://www.sciencedirect.com/science/article/pii/S0304405X12000931

Finding: momentum appeared in North America, Europe, and Asia Pacific but not Japan and was generally stronger among smaller stocks.
Limit: smaller-stock concentration can increase trading frictions and reduce capacity.

#### EV-PRICE-XMOM-004 — Momentum crash risk
Source: Daniel and Moskowitz, "Momentum crashes," Journal of Financial Economics (2016).
URL: https://www.sciencedirect.com/science/article/pii/S0304405X16301490

Finding: momentum has strong positive average returns across multiple asset classes but can suffer infrequent, persistent crashes, particularly after market declines, in high-volatility panic states, and during rebounds.
Limit: regime management proposed in the paper introduces additional estimation and implementation choices that themselves require validation.

### PRICE-TIME-SERIES-MOMENTUM-TREND

#### EV-PRICE-TSMOM-001 — Time-series momentum
Source: Moskowitz, Ooi, and Pedersen, "Time series momentum," Journal of Financial Economics (2012).
URL: https://www.sciencedirect.com/science/article/pii/S0304405X11002613

Finding: one-to-twelve-month return persistence appeared across 58 liquid equity-index, currency, commodity, and bond futures.
Limit: implementation relies heavily on diversified futures exposure, shorting, leverage, and volatility management.

#### EV-PRICE-TSMOM-002 — Long-history trend following
Source: Hurst, Ooi, and Pedersen, "A Century of Evidence on Trend-Following Investing" (2017).
URL: https://www.aqr.com/insights/research/journal-article/a-century-of-evidence-on-trend-following-investing

Finding: reconstructed diversified trend-following strategies showed positive average returns over a historical sample extending to 1880.
Limit: reconstructed historical trading is not equivalent to live execution, and the authors are affiliated with a manager that uses trend-following strategies.

#### EV-PRICE-TSMOM-003 — Volatility-scaling critique
Source: Kim, Tse, and Wald, "Time series momentum and volatility scaling," Journal of Financial Markets (2016).
URL: https://www.sciencedirect.com/science/article/abs/pii/S1386418116301379

Finding: the study argues that much of previously reported time-series-momentum alpha can be attributed to volatility scaling rather than the directional signal alone.
Limit: this changes the interpretation and possibly the implementation value of the evidence; it does not establish that trends are nonexistent.

### PRICE-SHORT-TERM-REVERSAL

#### EV-PRICE-SREV-001 — Cost-aware reversal
Source: de Groot, Huij, and Zhou, "Another look at trading costs and short-term reversal profits," Journal of Banking & Finance (2012).
URL: https://www.sciencedirect.com/science/article/pii/S0378426611002263

Finding: restricting the universe to large-cap stocks and reducing turnover substantially lowered trading costs; the studied strategies retained reported net reversal profits.
Limit: the result is historical and strategy economics remain highly cost- and implementation-sensitive.

#### EV-PRICE-SREV-002 — Global industry-adjusted reversal
Source: Stosik and Zaremba, "Short-term reversal persists globally—If properly measured," Economics Letters (2026).
URL: https://doi.org/10.1016/j.econlet.2026.113113

Finding: industry-adjusted short-term reversal was reported across 64 markets through 2023 and remained positive after modeled trading costs, though weaker later in the sample.
Limit: this is a recent short communication and the effect remains turnover intensive; independent replication and implementability deserve scrutiny before elevation.

### PRICE-LONG-TERM-REVERSAL

#### EV-PRICE-LREV-001 — International cross-sectional reversal
Source: Blackburn and Cakici, "Overreaction and the cross-section of returns: International evidence," Journal of Empirical Finance (2017).
URL: https://www.sciencedirect.com/science/article/pii/S0927539817300075

Finding: long-term reversals appeared in several developed regions after controls for value and momentum but were strongest in small stocks and insignificant among large stocks.
Limit: small-stock concentration raises liquidity and implementation concerns.

#### EV-PRICE-LREV-002 — Two centuries of national-index evidence
Source: Zaremba, Kizys, and Raza, "The long-run reversal in the long run," Journal of Empirical Finance (2020).
URL: https://ideas.repec.org/a/eee/empfin/v55y2020icp177-199.html

Finding: long-horizon reversal appeared across 71 country indices over 1830–2019 but was highly unstable through time.
Limit: national-index evidence is not equivalent to a directly implementable security-selection edge, and temporal instability is a major practical weakness.

### PRICE-CLASSICAL-TECHNICAL-RULES

#### EV-PRICE-RULE-001 — Automated chart-pattern evidence
Source: Lo, Mamaysky, and Wang, "Foundations of Technical Analysis: Computational Algorithms, Statistical Inference, and Empirical Implementation," Journal of Finance (2000; NBER 2000).
URL: https://www.nber.org/papers/w7613

Finding: objectively defined chart patterns altered conditional return distributions for some U.S. stocks in the 1962–1996 sample.
Limit: incremental information is not equivalent to a durable after-cost trading strategy, and the sample provides no post-publication confirmation.

#### EV-PRICE-RULE-002 — Large technical-rule test
Source: Rink, "The predictive ability of technical trading rules: an empirical analysis of developed and emerging equity markets," Financial Markets and Portfolio Management (2023).
URL: https://link.springer.com/article/10.1007/s11408-023-00433-2

Finding: across 6,406 technical rules and 41 equity markets, apparent historical profitability degraded strongly, was sensitive to costs, and the rules selected as recent winners generally failed to persist out of sample.
Limit: this is strong evidence against broad rule mining and rule-selection schemes, not a proof that no particular price-based rule can work.

## Cross-family observations supported by the evidence

1. The strongest surviving evidence does not align neatly with a fundamental-versus-technical dichotomy.
2. Value, profitability/quality, earnings underreaction, cross-sectional momentum, and diversified trend each have materially stronger empirical foundations than generic discretionary stock picking or broad technical-rule mining.
3. Several strongest effects can be represented systematically, reducing subjective reinterpretation and making them more amenable to honest testing.
4. The apparent strongest effects also carry distinct implementation problems: momentum crash risk, trend leverage/futures requirements, value drawdowns and post-publication decay, earnings-data speed, and small-stock/trading-cost sensitivity.
5. A candidate's existence remains insufficient for experiment authorization; the project still needs a direct comparison of expected informational value, practical accessibility, and the opportunity cost of building and maintaining a strategy.
