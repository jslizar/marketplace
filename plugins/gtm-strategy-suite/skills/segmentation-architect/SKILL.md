---
name: segmentation-architect
description: >
  This skill should be used when building or reviewing market segmentation
  for a GTM/marketing strategy — "segment the market", "build a segmentation
  tree", "what segments should we target", "score these segments", "validate
  our segments", "segment attractiveness", "ICP segments", "TAM segmentation".
  It enforces MECE structure, enumerates the full segment space with a script,
  collapses duplicate segments, and scores attractiveness deterministically.
metadata:
  version: "0.1.0"
---

# Segmentation Architect

Produce a rigorous, defensible segmentation instead of a handful of plausible-
sounding groups. Use this whenever a strategy needs segments chosen, validated,
and ranked (template §5 Segmentation → §6 Targeting).

## Why this skill exists (the failure modes to beat)

Left unaided, a language model tends to: invent 5–6 overlapping segments;
**mix segmentation bases** (jamming demographics, behavior, and needs onto one
axis); skip the enumeration that surfaces non-obvious segments; never **collapse
duplicate** segments; and score attractiveness with compressed, all-7s judgment.
This skill replaces each of those with a discipline plus a deterministic script.

## The procedure — do it in this order

### 1. Choose segmentation bases (axes), kept clean

Pick 3–6 **axes**, each a single base. Do not blend bases on one axis.

- **Consumer:** demographic (age, income), behavioral (frequency, occasion),
  needs-based (job-to-be-done), psychographic.
- **B2B:** firmographic (industry, employee count, revenue, geography),
  technographic (their stack / maturity), buying-situation (trigger, use case,
  urgency). **Do not segment B2B on job title as a primary axis** — segment on
  firmographics/needs and treat titles as the buying-committee map later.

State each axis and its mutually-exclusive levels. Confirm the levels on an axis
are **collectively exhaustive** (add an "other/none" level if needed) and
**mutually exclusive** (no overlap).

### 2. Enumerate the full leaf set with the script

Write the axes to a JSON file and run the enumerator — never hand-enumerate a
cross-product, the model miscounts and drops combinations:

```bash
python ${CLAUDE_PLUGIN_ROOT}/skills/segmentation-architect/scripts/segment_tree.py \
  enumerate --axes axes.json --out segments.csv
```

`axes.json` example:

```json
{"Type": ["Personal", "Commercial"],
 "Use":  ["Professional", "Recreational"],
 "Income": ["Low/Mid", "High"],
 "Frequency": ["Low", "High"]}
```

This produces every combination (this is how a real segmentation reaches 50+
candidates). Then **narrow on purpose**: drop whole branches with a one-line
rationale each (e.g., "skip Commercial-Retail — out of scope this launch"), the
way a disciplined analyst prunes.

### 3. Validate — prove segments are real and distinct

Build a segment × attribute matrix (score each candidate 1–10 on the attributes
that drive choice in this category — price sensitivity, durability, the
performance dimensions, tech-savviness, premium preference, etc.). Run:

```bash
python ${CLAUDE_PLUGIN_ROOT}/skills/segmentation-architect/scripts/segment_tree.py \
  validate --matrix validation.csv
```

It flags identical/near-identical segments (**collapse them into their parent**)
and attributes that don't discriminate (drop them). A segmentation where nothing
collapses and every attribute varies is a healthy one.

### 4. Score attractiveness — weighted, calibrated, ranked

Build a criterion × segment matrix with a weight per criterion, then run:

```bash
python ${CLAUDE_PLUGIN_ROOT}/skills/segmentation-architect/scripts/segment_tree.py \
  score --matrix evaluation.csv
```

Suggested criteria: Market Size, Growth Potential, Sustainability/Repeatability,
Profitability/Margin, Volume/Scale, Desire for the Offering, Competitive
Intensity (low intensity = high score), Influence/Market Penetration, Fit.

The script returns weighted totals, a 0–100 normalization, and ranking, and
**warns if the spread is too low** (a sign scores are compressed). Let the
script do the arithmetic — never sum weighted scores by hand.

## Calibration anchors (use these so scores aren't all 7s and 8s)

Score the full 1–10 range. Anchor explicitly:

- **1–2** = essentially absent / strongly negative for this segment.
- **5** = average / neutral / "could go either way".
- **9–10** = best-in-class / decisive strength.

If you cannot name a concrete segment that deserves a 9 *and* one that deserves
a 2 on a criterion, your scale is too compressed — re-anchor before scoring.

## Output back into the strategy

Carry the top-ranked segments into Targeting (§6) as Primary / Secondary /
Alternative, and keep the full enumerate/validate/score tables for the appendix.
Each target segment then needs its own value proposition and, downstream, its
own offering, price, channel mix, and motion.

## Guardrails

- US-adults framing unless told otherwise; no segmentation of minors.
- Every segment must be reachable in the real world — if you can't name how you'd
  find or target it, it isn't a usable segment.
- Keep bases unmixed; keep levels MECE; let the script enumerate and compute.
