---
name: sales-motion-modeler
description: >
  This skill should be used when designing the sales motion, sales-team
  structure, or channel mix in a GTM strategy — "what sales motion", "PLG vs
  sales-led", "how many reps do we need", "sales capacity model", "quota and
  comp", "OTE", "headcount plan", "which channels should we use", "channel
  mix", "rank our channels". It picks the motion from deal economics and runs
  capacity, comp, and channel-fit math deterministically.
metadata:
  version: "0.1.0"
---

# Sales Motion Modeler

Match the selling motion to the economics, then size and resource it with math
rather than vibes. Powers template §11 (Sales Motion) and §12 (Channel Strategy).

## Why this skill exists

A language model knows the motion concepts but **defaults to "run every channel"
and botches the capacity/comp arithmetic** (reps, ratios, quota:OTE). It also
forgets the cardinal constraint: an expensive motion bolted onto a cheap product
loses money. This skill enforces the ACV→motion decision and computes the team
deterministically. Pair benchmark inputs (win rates, ratios) with the
gtm-benchmarks skill.

## What to run

```bash
python ${CLAUDE_PLUGIN_ROOT}/skills/sales-motion-modeler/scripts/capacity_calc.py <subcommand> ...
```

### 1. Pick the motion from the economics

```bash
capacity_calc.py motion --acv 40000 --rep-cost 160000
```

Returns the archetype (self-serve/PLG → inside → mid-market → enterprise/field)
and a feasibility check: how many deals a rep would have to close at that ACV. If
that count is implausible, the human motion can't pay for itself — move to
self-serve or partner-led, or change the packaging/ACV. **The motion must be
consistent with the segment (§6), price (§8), and channel mix (§12).**

After picking, document deal economics (ACV, cycle, win rate, CAC, payback) and
the **buying committee** (economic buyer, champion, technical/user buyer,
blockers) — the multi-thread map a model otherwise omits.

### 2. Size the team from the target (work backward)

```bash
capacity_calc.py capacity --target 6000000 --quota 800000 --ramp 0.6 \
  --sdr-per-ae 1 --se-per-ae 0.33 --book 6000000 --csm-book 2000000
```

Returns AEs (target ÷ ramp-adjusted quota), then SDR/SE/CSM counts from ratios,
and the pipeline coverage required (default 3.5×). Never hand-derive headcount —
the model rounds and ratios inconsistently.

### 3. Set comp that aligns behavior

```bash
capacity_calc.py comp --ote 240000 --base-pct 0.5 --quota 800000
```

Returns the quota:variable ratio with a healthy-band check (~4–6×) and flags rich
or unreachable comp. Reminder: align each role's variable pay to the metric it
controls — SDRs on meetings/pipeline, AEs on closed revenue, CSMs on retention.

### 4. Choose the channel mix (don't run everything)

Build a `criterion,weight,ChannelA,ChannelB,...` CSV scored 1–5, then:

```bash
capacity_calc.py channel-fit --matrix channels.csv
```

Suggested criteria: ICP reachability, ACV economics, buyer-behavior fit, motion
fit, speed to results, scalability, cost to start, competitive saturation (less
crowded = higher), team capability. The script ranks channels; make the top
scorer(s) **primary**, the mid band **secondary/experiments**, and **cut the
rest**. State explicitly what you are *not* doing. Concentration beats sprawl:
prove one channel to repeatable pipeline before layering the next.

## Stage discipline (for the process, §11.2)

Define pipeline stages with **objective exit criteria** — a stage advance must be
earned by a buyer action, not rep optimism. Track no-decision losses separately
from competitive losses (different problem, different fix). Pick one qualification
methodology (BANT for simple, MEDDPICC for enterprise) and align it to the buyer
journey.

## Output back into the strategy

Produce: the motion archetype + rationale, deal economics, the buying committee,
the staged pipeline, the capacity/comp tables, and the ranked channel mix with a
"not doing" line. Fill the one-page Sales Motion snapshot. Keep capacity/comp
models in the appendix.

## Guardrails

- Use current benchmark ranges (gtm-benchmarks), not memorized numbers, for win
  rates, cycle lengths, ratios, and quota:OTE.
- Flag every economic input (CAC, win rate, ACV) as sourced or assumption.
