# AUDIT-002 — Large-Stock Long-Only Gate

**Status:** exploratory / adversarial, not confirmatory

Common analysis end: **2026-08**

## Source provenance

| Input | Vintage header | ZIP SHA-256 | CSV SHA-256 |
|---|---|---|---|
| op | This file was created using the 202608 CRSP database. | `5974ba70b4e23e46e58bdc821fb0c93caea86f46ca50523d0622e86d7f2eba5b` | `7a58a3eece5e69eca8c23f06cb393e52b41c9fe17ee27a9cf9f5a572bd5d7c7c` |
| mom | This file was created by using the 202608 CRSP database. | `68d90a218235b2c14e67eb1b7b1acd2d9fcc6b626bc4c64e854e2788bcf44bf3` | `0a53513f2e1eb803607619fb1efefa64fe87897fe826d91917041b489f1da898` |
| ff5 | This file was created using the 202608 CRSP database. | `36756c5c2559648519ac4b22913d860c6afd865cfebce920e3e8927f8e2d10b7` | `c4915afc1e2a1fce6fbba415f574d825a3e1b800c8d1aa31c72351789851eb22` |

## FUND_QUALITY_PROFITABILITY

Frozen classification: **clear_survivor**

| Window | Portfolio CAGR | Market CAGR | Ann. vol | Max DD | Monthly win rate | Active ann. mean | Relative compounded | Tracking error | Info ratio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 201601–202608 | 17.06% | 15.03% | 15.51% | -24.85% | 54.69% (70/128) | 1.74% | 20.51% | 3.68% | 0.47 |
| 202001–202608 | 17.10% | 15.32% | 17.34% | -24.85% | 50.00% (40/80) | 1.51% | 10.74% | 4.23% | 0.36 |

## PRICE_CROSS_SECTIONAL_MOMENTUM

Frozen classification: **not_supported**

| Window | Portfolio CAGR | Market CAGR | Ann. vol | Max DD | Monthly win rate | Active ann. mean | Relative compounded | Tracking error | Info ratio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 201601–202608 | 14.30% | 15.03% | 16.78% | -24.14% | 48.44% (62/128) | -0.49% | -6.60% | 6.55% | -0.07 |
| 202001–202608 | 14.89% | 15.32% | 19.00% | -24.14% | 51.25% (41/80) | -0.14% | -2.48% | 7.26% | -0.02 |

## Interpretation boundary

These Fama/French portfolios are research portfolios, not investable products. The audit does not deduct fund fees, taxes, spreads, or investor-specific implementation costs, and it does not authorize capital deployment.

## Execution record

GitHub Actions run: `37074371866`  
Workflow head: `7a7388de4bcaa955ce82c2b1ebb07cf24b3907fb`  
Artifact: `audit-002-results`  
Artifact SHA-256: `adc480b2dc7dd7fc6daa795baddbcb39cdbaf3bb0f7b096d9a57079e12ce94d3`
