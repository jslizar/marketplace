---
name: pricing-economics
description: >
  This skill should be used for any pricing or unit-economics math in a GTM
  strategy — "set the price", "value-based pricing", "breakeven analysis",
  "contribution margin", "what should we charge", "willingness to pay", "EVC",
  "LTV:CAC", "CAC payback", "price elasticity", "demand curve". It runs the
  numbers with a deterministic calculator instead of mental math.
metadata:
  version: "0.1.0"
---

# Pricing Economics

Get pricing math right by computing it, not estimating it. Use for template §8
(Pricing) and the deal-economics parts of §11 (Sales Motion).

## Why this skill exists

A language model reasons about pricing correctly but **slips on the arithmetic
and loses internal consistency** across scenarios: breakeven units that don't
match the margin, an EVC story with no numbers, LTV:CAC quoted without the
inputs. The bundled calculator makes every figure deterministic and reproducible.
Always run the script; never present pricing math you did in your head.

## What to run, and when

All commands:

```bash
python ${CLAUDE_PLUGIN_ROOT}/skills/pricing-economics/scripts/pricing_calc.py <subcommand> ...
```

### Value-based price — start here, not with cost

Price to the **value the customer gets**, anchored on their next-best
alternative. Build the EVC (Economic Value to the Customer):

```bash
pricing_calc.py evc --reference 49.99 --gains 20 --losses 2
```

- `--reference` = the all-in cost of the buyer's next-best alternative.
- `--gains` = quantified value your offering adds (savings, time, risk reduced).
- `--losses` = quantified negatives (switching cost, missing capability).

It returns the EVC ceiling and a price band that captures a share of the surplus
while leaving the buyer an obvious reason to switch. Do the EVC arithmetic in
real units — the strongest pricing narratives show the dollar math (e.g.,
"saves the buyer $10.85 per use, so the premium pays back in two uses").

### Breakeven — run three scenarios

```bash
pricing_calc.py breakeven --price 69.99 --vc 6.00 --fixed 2900000
# or multi-scenario:
pricing_calc.py breakeven --scenarios scenarios.csv
```

`scenarios.csv` columns: `scenario,price,variable_cost,fixed_costs`. Always run
**low / target / high** price scenarios and compare breakeven volume against a
realistic projected volume — the gap is the margin of safety. Formulas the
script uses: contribution margin = price − variable cost; breakeven units =
fixed ÷ contribution margin; breakeven $ = breakeven units × price.

### Unit economics (subscription / recurring)

```bash
pricing_calc.py unit-econ --arpa 12000 --gm 0.80 --cac 9000 --churn 0.15
```

Returns LTV, LTV:CAC, and CAC payback with health flags. Use `--lifetime <years>`
if you know it directly, otherwise `--churn <annual rate>` (lifetime = 1/churn).
This ties pricing to the motion: a price that can't support the cost to sell it
is the wrong price (or the wrong motion — see sales-motion-modeler).

### Elasticity (if you have two price/volume points)

```bash
pricing_calc.py elasticity --p1 50 --q1 1000 --p2 60 --q2 820
```

Returns arc elasticity and which way revenue moves: |e| > 1 elastic (cut price to
grow revenue), |e| < 1 inelastic (raise price to grow revenue).

## Setting the pricing objective first

Before any number, state what price optimizes for — penetration (price low for
share), profit maximization (price to value), portfolio consistency, or
premium/skim. The objective decides which output above matters most.

## Output back into the strategy

Record the chosen price(s) per segment/variant with the EVC justification, the
breakeven verdict (projected volume vs. breakeven), and — for recurring models —
LTV:CAC and payback. Keep the full scenario tables for the appendix. Reconcile
these numbers with any promotion budget (§13) and capacity plan (§11) so the
document is internally consistent.

## Guardrails

- Never quote a breakeven, LTV:CAC, or payback without showing the inputs.
- Flag every market-derived input (competitor price, churn, CAC) as sourced or
  an explicit assumption — pair with the research-grounding skill.
