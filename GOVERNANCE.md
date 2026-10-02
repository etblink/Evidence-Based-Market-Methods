# Governance

## 1. Authority model

This repository uses a single-source-of-truth architecture.

- `STATE.yaml` is the sole canonical representation of current mutable project state.
- This file defines stable operating rules only; it must not contain current research conclusions, current phase, or current next action.
- Git history is the authoritative archive of prior states.
- Evidence, experiment outputs, issues, discussions, and generated summaries are non-authoritative with respect to current state.
- A mutable fact must not be canonically represented in more than one place.

If two artifacts appear to disagree about current project state, `STATE.yaml` governs unless and until it is deliberately changed.

## 2. State discipline

`STATE.yaml` must be sufficient for a successor to recover the project's current objective, phase, active research state, and exactly one authoritative next action.

State changes should be:

1. evidence-linked when they concern empirical claims;
2. explicit rather than implied by prose elsewhere;
3. narrow enough that Git history reveals what changed and why;
4. free of manually duplicated historical summaries.

Historical conclusions are not copied into a separate changelog. Git preserves them.

Issues request or coordinate work; they do not define state.

## 3. Evidence discipline

The project distinguishes among:

- **evidence** — what a source, dataset, or experiment shows;
- **synthesis** — what the project currently concludes from the evidence;
- **decision** — what action, if any, the project authorizes.

These layers must not be silently collapsed.

For empirical market claims, analysis should consider, where applicable:

- out-of-sample performance;
- multiple testing and data-snooping risk;
- look-ahead, survivorship, and selection bias;
- transaction costs, spreads, slippage, financing, taxes, and market impact;
- risk adjustment and an appropriate benchmark;
- stability across instruments, periods, and regimes;
- post-publication or forward evidence;
- plausible mechanisms and limits to arbitrage;
- whether an effect is accessible to an individual rather than only to specialized institutions.

Statistical significance, predictability, economic profitability, and practical usefulness are distinct claims.

Evidence of an effect does not by itself establish that a specific implementation is profitable.

Institutional exploitability does not by itself establish individual accessibility.

## 4. Experiments

A confirmatory experiment must freeze its material rules before holdout inspection.

Where relevant, the protocol should specify:

- hypothesis;
- universe and sampling rule;
- signal and parameter definitions;
- entry, exit, sizing, and risk rules;
- benchmark;
- cost model;
- evaluation metrics;
- treatment of all strategies and parameters tried;
- holdout or forward-test boundary;
- failure conditions.

Exploratory work must be labeled exploratory and must not be retrospectively presented as confirmatory evidence.

Negative results and failed replications are first-class evidence.

## 5. Research economy

The project exists to improve decisions, not to maximize research volume.

Research should be bounded by decision relevance. Additional work requires a plausible path by which its result could change a real allocation of time, attention, or capital.

A method may be scientifically interesting yet still be rejected as a practical use of scarce time.

Deep experimentation should follow comparative reconnaissance rather than precede it, unless new evidence creates a clear reason to deviate.

## 6. Capital and execution boundary

Research findings do not authorize deployment of money.

Any transition from research to live trading, investment, or other capital deployment requires a separate explicit decision by the human project owner, with the relevant risks and assumptions visible at that time.

## 7. Continuity

A successor should begin with `STATE.yaml`, then read this file, then inspect only the evidence or history needed for the active task.

The repository should not grow infrastructure preemptively. New folders, schemas, automation, CI, or generated views should be introduced only when actual project work demonstrates a need.

When convenience views are introduced, they must be derived mechanically from canonical state and must not be hand-maintained.

## 8. Governance changes

This document may evolve, but governance changes must not silently rewrite current research state. A governance change and a state change should be separable in Git whenever practical.
