---
name: funnel-classify
description: >
  This skill should be used when the user wants to set or check the funnel stage of a
  LinkedIn post — "what funnel stage is this", "classify this post", "is this TOFU /
  MOFU / BOFU", "make this a top-of-funnel post", "should this have a CTA". It maps a
  post's intent to TOFU / MOFU / BOFU and returns a stage directive (the post's job,
  required structure, CTA strength, and proof level) that shapes the draft. Runs inside
  copy-post before drafting and inside the funnel engine's Step 0 stage resolution.
metadata:
  version: "0.1.0"
---

# funnel-classify

Decide what job a post is doing in the funnel, then translate that into concrete drafting constraints. Stages are TOFU (top), MOFU (middle), BOFU (bottom).

## Two modes

- **Set** (most common): the user is about to draft. Given the topic + intent (and the client's Conversion ask from context), pick the stage and return a directive for the drafter.
- **Check**: the user has a draft or example and asks "what stage is this?" Classify it and explain the tells.

If the stage is ambiguous, ask one question: "Is the goal reach, trust, or conversion?" — that maps cleanly to TOFU / MOFU / BOFU.

## The three stages

Full mapping (job, structure, CTA, proof, pillar fit, failure mode) is in `references/funnel-map.md`. In short:

- **TOFU — reach.** Relatable or contrarian take, broad appeal, a story or observation. **No hard ask**; CTA is at most a soft "what's your take?". Proof optional. Risk: being so broad it says nothing.
- **MOFU — trust.** Educate, show how you think, soft proof (a method, a framework, an anonymized example). CTA is soft (follow, comment, "DM me"). Risk: sounding like a brochure.
- **BOFU — convert.** A specific result, a named offer, the client's **Conversion ask** as the CTA. Proof required (or, if Proof is "None on record", pivot to a process/credibility angle and flag that no results can be cited). Risk: pitching to a cold audience.

## Output: the stage directive

Return a compact directive the drafter consumes:

```
stage: TOFU | MOFU | BOFU
job: <one line>
structure: <skeleton bias for this stage>
cta: { strength: none|soft|hard, ask: <text or "engagement"> }
proof: required | soft | optional   (+ note if Proof is empty)
pillar_fit: <which context pillar this serves>
```

## Guardrails

- Respect the client's Canon. A BOFU post still cannot break a Hard constraint or invent Proof — if Proof is "None on record", say so and steer to a credibility/process angle instead of fabricating results.
- One stage per post. If the user wants a series, classify each post separately.
