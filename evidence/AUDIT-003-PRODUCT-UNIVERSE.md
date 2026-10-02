# AUDIT-003 — Product Universe and Methodology Screen

Captured: 2026-10-02

Purpose: identify individually accessible U.S. equity ETFs that satisfy the product rules frozen in `STATE.yaml` at commit `3c4ff1fc3acc2817400e3eb785c253895359e2c6`, before comparative returns are inspected.

Authority boundary: this file records source evidence and classification inputs. Canonical project state remains `STATE.yaml`.

## Frozen inclusion rules

The product gate requires a U.S.-listed, long-only, unlevered, diversified U.S. equity ETF with a current methodology that uses profitability, financial quality, earnings quality, or closely related financial-strength measures as a primary selection or weighting input. Net expense ratio must be no more than 0.30%.

For the frozen 2020+ live-return comparison, the ETF must have live inception on or before 2019-12-31 and must not have undergone a material methodology change after that date.

Methodology proximity:

- **A** — profitability or operating/gross profitability is itself a principal selection/weighting signal and the portfolio is predominantly large U.S. equities.
- **B** — profitability is one principal component of a transparent broader quality composite.
- **C** — quality is materially different from the Fama/French profitability concept or dominated by unrelated factors; Tier C cannot alone justify a deeper profitability implementation test.

## Eligible live-comparison cohort

### QUAL — iShares MSCI USA Quality Factor ETF

- Inception: 2013-07-16.
- Expense ratio: 0.15%.
- Universe: U.S. large- and mid-cap stocks.
- Method: quality score based on high return on equity, low earnings variability, and low leverage; sector-neutralized.
- Recent turnover: 21% in the 2025 prospectus.
- Methodology proximity: **B**.
- Live-comparison status: **eligible**.
- Post-2019 review: a 2026 prospectus supplement changed diversification-policy wording, not the three-variable quality signal. No material post-2019 signal-construction change was identified in the reviewed documents.

Sources:
- iShares product page: https://www.ishares.com/us/products/256101/QUAL
- SEC 2025 summary prospectus: https://www.sec.gov/Archives/edgar/data/1100663/000119312525302174/d947225d497k.htm
- SEC 2026 diversification supplement: https://www.sec.gov/Archives/edgar/data/1100663/000119312526114010/d864601d497.htm

### SPHQ — Invesco S&P 500 Quality ETF

- Inception: 2005-12-06.
- Net expense ratio: 0.15%.
- Universe: S&P 500.
- Method: quality score based on return on equity, accruals ratio, and financial leverage.
- Methodology proximity: **B**.
- Live-comparison status: **eligible**, subject to the caveat that the audit found no evidence of a material post-2019 change in the current quality methodology but did not establish an exhaustive index-history proof.

Source:
- Invesco product page: https://www.invesco.com/us/en/financial-products/etfs/invesco-sp-500-quality-etf.html

### JQUA — JPMorgan U.S. Quality Factor ETF

- Inception: 2017-11-08.
- Net expense ratio: 0.12%.
- Universe: primarily Russell 1000 constituents.
- Method: rules-based quality factor using profitability, earnings quality, and solvency/financial risk; sector weights are aligned with the market.
- Recent portfolio turnover: 19%.
- Methodology proximity: **B**.
- Live-comparison status: **eligible**.
- No material post-2019 methodology change was identified in the reviewed current prospectus/fact-sheet material.

Sources:
- JPMorgan 2026 fact sheet: https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/literature/fact-sheet/etfs/FS-JQUA.PDF
- SEC 2026 summary prospectus: https://www.sec.gov/Archives/edgar/data/1485894/000119312526071872/d49733d497k.htm

### FQAL — Fidelity Quality Factor ETF

- Inception: 2016-09-12.
- Expense ratio: 0.15%.
- Universe: U.S. large- and mid-cap companies.
- Method: free-cash-flow margin, return on invested capital, and free-cash-flow stability, ranked within sectors.
- Recent portfolio turnover: 39% for the fiscal year ended 2026-07-31.
- Methodology proximity: **B**.
- Live-comparison status: **eligible**.
- A December 2025 policy update allowed qualifying derivative exposures within the 80% policy but did not replace the underlying three-variable quality index construction; this is not treated as a material signal-methodology change.

Sources:
- SEC 2025 prospectus: https://www.sec.gov/Archives/edgar/data/945908/000094590825000707/filing10090.htm
- Fidelity 2026 fact sheet: https://institutional.fidelity.com/app/proxy/content?literatureURL=%2F9880844.PDF
- SEC 2026 annual shareholder report: https://www.sec.gov/Archives/edgar/data/945908/000094590826000328/filing13079.htm

## Eligible methodology-only cohort

### VFQY — Vanguard U.S. Quality Factor ETF

- Inception: 2018-02-13.
- Expense ratio: 0.13%.
- Current methodology includes operating profitability, gross profitability, change in net operating assets, intangibles intensity, and financial-sector profitability/equity issuance.
- Current turnover: 41%.
- Current portfolio has a substantial small-cap allocation, so it is not a close large-stock analogue even though the underlying profitability measures are unusually close to the research signal.
- Methodology proximity: **A on signal definition, weaker on size/universe match**.
- Live-comparison status: **excluded from the frozen 2020+ gate** because Vanguard filed a material investment-strategy update effective June 2026. The current methodology is useful for implementation mapping but the pre/post-change return history is not treated as one unchanged live implementation.

Sources:
- Vanguard product page: https://advisors.vanguard.com/investments/products/vfqy/vanguard-us-quality-factor-etf
- SEC 2026 strategy supplement: https://www.sec.gov/Archives/edgar/data/105563/000010556326000200/f45558d1.htm

### DUHP — Dimensional US High Profitability ETF

- ETF trading launch: 2022-02-23 in Dimensional's ETF listing history; current Dimensional materials may display earlier predecessor/share-class history after later reorganizations, so the audit does not backfill ETF live history before the ETF existed.
- Current expense ratio: approximately 0.20%-0.22% depending on the current share-class disclosure.
- Current turnover: 3% in the 2026 summary prospectus.
- Universe: broad and diversified group of readily marketable large U.S. companies.
- Method: explicitly targets companies with high profitability, defined as high earnings or profits from operations relative to book value or assets.
- Methodology proximity: **A** and the closest identified accessible product to the Fama/French operating-profitability concept.
- Live-comparison status: **not eligible for the frozen 2020+ gate** because the ETF itself did not have live trading history at 2019-12-31.
- Implementation relevance: **high**; if the older live cohort passes the gate, DUHP is a natural candidate for later implementation comparison.

Sources:
- SEC 2026 summary prospectus: https://www.sec.gov/Archives/edgar/data/1816125/000181612526000075/c497k.htm
- SEC 2026 full prospectus: https://www.sec.gov/Archives/edgar/data/1816125/000181612526000046/c485bpos.htm
- Dimensional fund listing: https://www.dimensional.com/us-en/funds/

## Considered but excluded by frozen rules

- **QDF — FlexShares Quality Dividend Index Fund:** dividend strategy with quality as one component; excluded because dividend exposure is a primary strategy dimension.
- **DGRW — WisdomTree U.S. Quality Dividend Growth Fund:** dividend-growth strategy; excluded because dividend/growth construction is not a clean profitability implementation.
- **FLQL — Franklin U.S. Large Cap Multifactor Index ETF:** combines value, momentum, quality, and other factors; excluded because quality is not the primary standalone signal.
- Broad multifactor products such as GSLC/QUS-type strategies: excluded because quality is combined with unrelated factors and cannot isolate the surviving profitability signal.
- Sector-specific or small-cap-only quality ETFs: excluded by the diversified U.S. equity / research-representation matching rules.

## Frozen cohort for return inspection

The comparative live-return gate is therefore frozen to:

- QUAL
- SPHQ
- JQUA
- FQAL

Benchmark:

- VTI — Vanguard Total Stock Market ETF

No comparative return series for these five tickers was inspected in constructing this universe.
