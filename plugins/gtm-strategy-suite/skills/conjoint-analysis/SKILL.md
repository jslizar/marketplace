---
name: conjoint-analysis
description: >
  This skill should be used for conjoint analysis or feature/price trade-off
  studies in product and pricing work — "run a conjoint", "conjoint analysis",
  "part-worth utilities", "feature trade-offs", "which attributes matter most",
  "willingness to pay by feature", "design a conjoint survey", "attribute
  importance". It generates a balanced profile design and estimates part-worths
  and WTP with a real regression.
metadata:
  version: "0.1.0"
---

# Conjoint Analysis

Actually run conjoint instead of describing it. Use when a strategy needs to know
which attributes drive choice and what each is worth (template §7 Product
Offering and §8 Pricing).

## Why this skill exists

Conjoint is a true capability gap: a language model can explain the method but
**cannot build a balanced fractional-factorial design or run the part-worth
regression** — the source GTM report this suite is modeled on even punted to
"estimated" results. The bundled script does both deterministically.

## Step 1 — Design the study

List attributes and their levels (include price as an attribute with 2–4 points),
then generate the profiles to show respondents:

```bash
python ${CLAUDE_PLUGIN_ROOT}/skills/conjoint-analysis/scripts/conjoint.py \
  design --attributes attrs.json --out design.csv
```

`attrs.json`:

```json
{"Performance": ["Low", "High"],
 "GPS": ["No", "Yes"],
 "Durability": ["Standard", "Extra"],
 "Price": ["39.99", "54.99", "69.99"]}
```

The script reports the full factorial size and the minimum profiles needed for
estimability, then either shows the full factorial (if small) or searches for a
**balanced, near-orthogonal fractional design** so respondents rate a manageable
set. Don't hand-pick profiles — unbalanced designs make part-worths
uninterpretable.

## Step 2 — Collect ratings

Field the design (panel, customer survey, or sales-assisted). Put the average
rating or share-of-preference for each profile in the `rating` column of the CSV.
If you genuinely cannot field a study, you may seed estimated ratings from prior
research — but **label the output "estimated, pending fielding,"** exactly as a
rigorous report would.

## Step 3 — Estimate part-worths and WTP

```bash
python ${CLAUDE_PLUGIN_ROOT}/skills/conjoint-analysis/scripts/conjoint.py \
  estimate --responses responses.csv --price-attr Price
```

Returns:

- **Part-worth utilities** per level (reference level = 0).
- **Attribute importance** — each attribute's share of the total utility range
  (what buyers actually weight).
- **Willingness-to-pay** — when `--price-attr` is numeric, the dollar value of
  each level, derived from the price coefficient. (If the price coefficient comes
  out non-negative, the script warns — the data is suspect.)

## Choosing other methods (know when conjoint is overkill)

- **MaxDiff** when you only need to rank many items by importance (no price).
- **Van Westendorp / Gabor-Granger** when you only need a price range, not
  feature trade-offs. (These are simpler and don't need this script.)
- Full **conjoint** when feature *and* price trade-offs both matter — that's
  this skill.

## Output back into the strategy

Use the winning attribute configuration to define the offering (§7) and the WTP
to anchor price (§8). If two target segments value attributes very differently,
that's the signal to split into segment-specific variants. Keep the design and
regression output in the appendix.
