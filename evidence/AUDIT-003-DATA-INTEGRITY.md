# AUDIT-003 — Data Integrity Failure and Official-Return Reconciliation

Captured: 2026-10-02

Status: **original live-return gate invalidated for cohort classification**

Authority boundary: this file records evidence and the reason the original computational result is not promoted to canonical truth. `STATE.yaml` remains the sole canonical mutable project state.

## Frozen run

GitHub Actions run: `37079076596`  
Workflow head: `55177538b144b234561f106543cccaa95673b6db`  
Artifact: `audit-003-results`  
Artifact digest: `sha256:f9f5cf1197943d88acf0edcf91d6d049ae8c2a3b7dadd64cc46e0be63a29ba12`

The run executed the frozen cohort QUAL, SPHQ, JQUA, and FQAL versus VTI over 2020-01 through 2026-09 using Yahoo Finance adjusted-close data.

Literal output:
- QUAL: implementation_not_supported
- SPHQ: implementation_not_supported
- JQUA: implementation_survivor
- FQAL: implementation_not_supported

The literal JQUA pass is **not accepted as a canonical project conclusion** because the required official-return cross-check found a material source-integrity failure within the common data source.

## Cross-check finding

### SPHQ failed the source-integrity check

The Yahoo-derived calendar returns were approximately:
- 2020: 16.93%
- 2021: 27.59%

Invesco's official fund-reported NAV returns are:
- 2020: 17.42%
- 2021: 27.96%

The official Invesco Q4 2025 fact sheet reports the same current quality methodology and the full calendar series.

Source:
https://www.invesco.com/us-rest/contentdetail?contentId=115407c649400410VgnVCM10000046f1bf0aRCRD

The preserved Yahoo event stream contains March, June, and December SPHQ distributions in both 2020 and 2021 but no September distribution. Independent historical distribution records show SPHQ paid approximately $0.1432 in September 2020 and $0.1730 in September 2021. This is consistent with the adjusted-return shortfall and demonstrates that the common Yahoo series cannot be assumed complete for this audit.

Corroborating distribution history:
https://companiesmarketcap.com/invesco-sp-500-quality-etf/distributions/

### JQUA cross-check was internally consistent

JPMorgan's official market-price calendar returns:
- 2020: 16.52%
- 2021: 28.67%
- 2022: -13.46%
- 2023: 25.13%
- 2024: 21.21%
- 2025: 11.69%

These closely match the Yahoo-derived annual returns used by the frozen run.

Source:
https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/literature/fact-sheet/etfs/FS-JQUA.PDF

### VTI cross-check was internally consistent

Vanguard's official annual fund returns:
- 2020: 21.00%
- 2021: 25.73%
- 2022: -19.51%
- 2023: 26.02%
- 2024: 23.75%
- 2025: 17.13%

These are close to the Yahoo-derived values and do not reveal a comparable integrity problem.

Source:
https://personal1.vanguard.com/pub/Pdf/spi855.pdf

### QUAL and FQAL checks

QUAL's official reported market-price returns for the available calendar years closely match the Yahoo-derived series. FQAL's official five-year annualized NAV return through 2025-07-31 was 14.74%; the corresponding Yahoo adjusted-close calculation was approximately 14.55%, close enough to support the conclusion that the large source-integrity defect detected here is concentrated in SPHQ rather than obviously universal.

QUAL:
https://www.ishares.com/us/literature/fact-sheet/qual-ishares-msci-usa-quality-factor-etf-fund-fact-sheet-en-us.pdf

FQAL:
https://www.actionsxchangerepository.fidelity.com/ShowDocument/documentPDF.htm

## Official-return reconciliation

Because the original common source failed, official calendar-year NAV returns were used only as a **reconciliation**, not as a retroactive replacement confirmatory test.

For the six complete calendar years 2020–2025:

- VTI compounded return: approximately **+123.68%**
- JQUA NAV compounded return: approximately **+119.52%**
- JQUA relative compounded return versus VTI: approximately **-1.86%**
- SPHQ NAV compounded return: approximately **+124.43%**
- SPHQ relative compounded return versus VTI: approximately **+0.34%**

Thus the two products closest to the decision boundary land on opposite sides of zero under official complete-calendar returns, and both differences are small.

This reconciliation does not reproduce the frozen monthly tracking-error and information-ratio metrics. It is therefore evidence about robustness and magnitude, not a replacement execution of the original gate.

## Decision implication

The product-level evidence is **weak and source/period sensitive**.

A quality/profitability implementation remains plausible and scientifically interesting, but the accessible ETF evidence does not currently justify the opportunity cost of a more expensive point-in-time raw-security build.

The project should therefore:
1. preserve profitability/quality as a retained method;
2. withdraw the provisional claim that AUDIT-003 identified a robust implementation survivor;
3. defer a raw-security profitability replication unless stronger evidence or a cheaper clean test appears;
4. redirect scarce research time to the remaining untested serious candidates.

No capital deployment is authorized.
