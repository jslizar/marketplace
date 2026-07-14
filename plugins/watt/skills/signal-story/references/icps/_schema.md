# ICP profile — schema

An ICP profile is the **lens** the signal story is drafted through. It does not
change a single number — it decides *which* findings lead, *how* they're worded,
and *what action* the report drives, for one specific reader. One file per ICP,
named for its `id` (e.g. `dtc-agency.md`). The skill reads the chosen profile and
authors the editorial blocks through it.

## Fields

| Field | What it is | Drives which block |
|---|---|---|
| `id` | slug, matches the filename (`dtc-agency`) | output naming, the `icp` spec field |
| `label` | human name ("DTC marketing agency") | masthead eyebrow, footer |
| `reader` | one line: who is actually reading this | the whole voice |
| `jtbd` | the job the report does for them | masthead title + dek |
| `kpis` | what this reader is judged on | which stat leads; the recs |
| `vocabulary` | words/frames to use — and a few to avoid | all editorial copy |
| `objection` | the skepticism to preempt | the callout |
| `cta` | the action the report should drive | the closing recommendation |
| `lead_with` | which existing finding to foreground for this reader | beat order / emphasis |
| `serves` *(optional)* | a downstream reader this can be white-labelled to | a second variant |
| `evidence_hook` *(optional)* | the cross-read to run **only if** you want a hard ICP-specific number | the additive re-search |
| `example_headline` | a sample reframed masthead title — anchors the lens | — |

## The two modes

1. **Framing (default).** Everything above is draft-layer. Same reach, same map,
   same composition — re-narrated for the reader. No new data.
2. **Evidence (optional).** `evidence_hook` names a single additive Watt cross-read
   (the audience × something the ICP's world cares about) that puts a hard,
   ICP-specific number in the report. It is **additive and labelled** — layered on
   the honest core finding, never a reweighting of it. The core search stays
   ICP-blind.

## Guardrails

- The lens reorders and rewords. It **never** changes, drops, or invents a number.
- The core audience is whatever the data says — built before any ICP is chosen.
- An `evidence_hook` read is marked as an ICP read in its label so a reader can
  see it sits on top of the base finding.
