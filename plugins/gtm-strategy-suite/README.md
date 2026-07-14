# GTM Strategy Suite

A plugin that helps build rigorous, client-ready go-to-market strategy documents. It exists to close the specific gaps a general language model is *weakest* on when writing a GTM plan — not the prose (the model already writes that well), but the parts that require **structured enumeration, deterministic math, current domain benchmarks, executable methods, and grounded facts.**

## What's inside

| Skill | Closes this gap | Carries |
|---|---|---|
| **gtm-strategy-builder** | Losing the thread across a 16-section doc; running steps out of order | The master GTM template + the end-to-end build order + a cross-section consistency audit. The orchestrator. |
| **segmentation-architect** | Shallow, overlapping (non-MECE) segments; no systematic enumeration; skipped validation | A script that crosses segmentation axes into the full leaf set, dedupes, and runs weighted attractiveness scoring with calibration anchors |
| **pricing-economics** | Arithmetic slips in breakeven / margins; weak value-to-customer math | A calculator for contribution margin, multi-scenario breakeven, EVC, elasticity, LTV:CAC, CAC payback |
| **sales-motion-modeler** | Botched capacity/comp math; "run every channel" sprawl | A calculator for rep capacity, team ratios, comp/OTE, and weighted channel-fit scoring + the ACV→motion decision rule |
| **conjoint-analysis** | Can describe conjoint but can't design or run it | A script that generates a fractional-factorial design and estimates part-worth utilities + willingness-to-pay |
| **research-grounding** | Confidently inventing market sizes, competitor facts, benchmarks | A research-before-write workflow, connector routing, and a "claims ledger" forcing every number to be sourced or tagged `[ASSUMPTION]` |
| **gtm-benchmarks** | Guessing or remembering stale sales/channel benchmarks | A curated, sourced reference library (win rates & cycles by ACV band, quota:OTE, CAC payback, channel CAC & conversion, ramp times) |

## How it's meant to be used

Say something like *"build a GTM strategy for [client]"* and **gtm-strategy-builder** runs the show — it works the template in order and pulls in the other skills at the right section (segmentation-architect at §5, pricing-economics at §8, sales-motion-modeler at §11–12, and so on). The individual skills also trigger on their own (e.g., *"score these segments,"* *"run a breakeven,"* *"what's a good win rate for a $40k ACV?"*).

## Setup

- The scripts are pure Python 3 (standard library only) — no install required.
- **research-grounding** and **gtm-benchmarks** are most powerful when data connectors are wired in (e.g., an enrichment tool for firmographics, a web/competitive-intel source, and the client's own CRM). They degrade gracefully to web research + the bundled benchmark library when connectors aren't available.
- Benchmarks in **gtm-benchmarks** are date-stamped. Treat them as ranges to anchor on, and refresh against live sources for anything time-sensitive.

## A note on scope

These skills make the *hard, error-prone* parts reliable. They deliberately do **not** wrap the parts the model already does well — executive summaries, narrative, mission/vision, qualitative SWOT/PESTEL. That's by design: a skill earns its place only where it removes a real failure mode.
