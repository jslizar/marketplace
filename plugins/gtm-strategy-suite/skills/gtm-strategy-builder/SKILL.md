---
name: gtm-strategy-builder
description: >
  This skill should be used to produce a full go-to-market strategy document
  for a company or product — "build a GTM strategy", "go-to-market plan",
  "GTM strategy for [client]", "marketing strategy report", "market entry
  plan", "launch strategy", "write a GTM deck/doc". It is the orchestrator: it
  drives the master template end-to-end and pulls in the specialist GTM skills
  (segmentation, pricing, sales-motion, channels, conjoint, research, benchmarks)
  at the right section, then runs a consistency audit.
metadata:
  version: "0.1.0"
---

# GTM Strategy Builder (orchestrator)

Produce a complete, rigorous, client-ready GTM document by working a proven
template in the right order and delegating the hard parts to specialist skills.
This skill owns the *process*; the specialists own the *rigor*.

## Start here

1. **Load the scaffold:** read
   `references/gtm-template.md` — a 16-section master GTM template with fill-in
   placeholders (`[[ ]]`), author-guidance callouts (delete before delivery), and
   a pre-delivery checklist. Build the document from this structure.
2. **Confirm scope** with the user: the company/product, the business model
   (B2B SaaS / services / physical), and the deliverable format.
3. **Research before writing** (see order below). Do not draft numbers from
   memory.

## Build order (do NOT go top-to-bottom)

Research-heavy sections first; the Executive Summary last. At each step, invoke
the specialist skill that powers it:

| Order | Section(s) | Specialist skill to use |
|---|---|---|
| 1 | §3 External Environment, §4 Market Assessment | **research-grounding** (every figure sourced or tagged) |
| 2 | §5 Segmentation | **segmentation-architect** (enumerate → validate → score) |
| 3 | §6 Targeting & Positioning | (carry top segments; write value props) |
| 4 | §7 Product / Offering | **conjoint-analysis** (attribute/price trade-offs) |
| 5 | §8 Pricing | **pricing-economics** (EVC, breakeven, unit economics) |
| 6 | §9 Game Theory, §10 Distribution | (qualitative; model handles directly) |
| 7 | §11 Sales Motion | **sales-motion-modeler** + **gtm-benchmarks** |
| 8 | §12 Channel Strategy | **sales-motion-modeler** (channel-fit) + **gtm-benchmarks** |
| 9 | §13 Promotion | (qualitative; model handles directly) |
| 10 | §14 Recommendations | (synthesis — no new analysis) |
| 11 | §1 Executive Summary | write last, reflecting the finished plan |

## What to do yourself vs. delegate

- **Delegate** anything involving enumeration, scoring, pricing math, capacity
  math, conjoint, benchmark numbers, or sourced facts — those are the specialist
  skills' jobs and the model's weak spots.
- **Write directly** the prose-heavy, qualitative parts the model already does
  well: executive summary, mission/vision, narrative SWOT/PESTEL, game-theory
  scenarios, distribution/promotion narrative, recommendations.

## Cross-section consistency audit (run before delivery)

A long strategy doc fails when sections drift apart. Verify:

- Targets in §6 trace to the §5.4 attractiveness scores.
- Value props (§6.2), offering (§7), and price (§8) are mutually consistent.
- The sales motion (§11) fits the ACV (§8), segment (§6), and channel mix (§12) —
  no expensive motion on a cheap product.
- The channel mix (§12) is focused (1–2 primary), resourced, and names what it
  is *not* doing.
- The promotion funnel (§13) feeds the sales motion; budget reconciles with
  breakeven (§8.7).
- Every quantitative claim appears in the research claims ledger (sourced or
  `[ASSUMPTION]`).
- Recommendations (§14) mirror the body and add no new analysis.

For a high-stakes deliverable, run this audit as a separate verification pass
(or subagent) rather than inline.

## Finish

- Strip every guidance callout and fill every `[[ placeholder ]]` (or mark the
  section "Not applicable — reason").
- Deliver in the requested format. Keep the enumerate/validate/score tables,
  pricing scenarios, capacity/comp models, conjoint output, and claims ledger in
  the appendix.

## Guardrails

- Adapt vocabulary to the business model (the template's 🔀 model notes show the
  swaps).
- US-adults framing for any audience/segmentation work unless told otherwise.
- A section without a sourced number or an explicit assumption is not done.
