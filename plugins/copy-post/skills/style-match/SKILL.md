---
name: style-match
description: >
  This skill should be used when the user wants to verify how closely a draft copies an
  example's format — "does this match the example", "score the style match", "how close is
  this to the example", "check the format fidelity", "is this on-style". It compares a
  draft against the Style Spec / profile (and the raw example if available) across hook
  type, block sequence, length, rhythm, formatting, and open/close, and returns a 0–100
  fidelity score with per-dimension misses and concrete fixes. Runs inside copy-post
  before post-qa.
metadata:
  version: "0.1.0"
---

# style-match

Measure whether a draft actually copied the format, instead of trusting that it did. This is the enforcement layer for the plugin's core promise: return a fidelity score, name the misses, and hand back fixes so the drafter can iterate.

## Inputs

- The **draft** (one or several candidates).
- The **Style Spec / template** from `post-deconstruct`, or a **profile** from `style-library`.
- The **raw example** if available (lets you compare rhythm and glyphs directly).

## Score it

Grade each dimension in `references/match-rubric.md`, then combine into a weighted **0–100**:

- **Hook type** — same type as the target (contrarian, question, stat…)?
- **Block sequence** — does the draft follow the template's modal skeleton (or a documented variance alternate)?
- **Length band** — total chars inside the target band?
- **Rhythm** — avg sentence words and % one-line paragraphs within tolerance?
- **Formatting** — same glyphs, emoji policy, line-break rhythm?
- **Open/close** — hook lands before the fold; close matches the example's close pattern?

Respect the profile's **variance**: don't penalize a choice the profile lists as legitimate.

## Output

```
match_score: 84 / 100   → SHIP  (threshold 80)
by_dimension:
  hook_type: pass
  block_sequence: pass
  length_band: pass (940 / 700–1100)
  rhythm: miss — avg 15 words vs target 8–12; one-line paras 35% vs ~60%
  formatting: miss — used "•" bullets; example uses "→"
  open_close: pass
fixes:
  - split the long sentences in the reframe + list; aim 8–12 words
  - swap "•" for "→" in the list block
```

Show a compact version to the user (score + the misses). Below **threshold (default 80)**, return the fixes to `copy-post` and re-score after the revision. Cap the loop at **2 revision cycles per candidate** — if it still scores below threshold, hand back the best version with its score and remaining misses labeled rather than looping or silently dropping it.

## Boundary with post-qa

`style-match` owns **structural fidelity** (does it look/move like the example). `post-qa` owns **brand safety** (Author voice, Canon constraints, invented Proof, AI-tells). Run `style-match` first, then `post-qa`. Don't duplicate each other's checks.
