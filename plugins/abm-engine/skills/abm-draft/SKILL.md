---
name: abm-draft
description: Draft ABM posts from a chosen angle and format spec. Use when the user says "draft it", "write the post", picks an angle from abm-angles, or names a format and subject directly ("write a credit-roll post about [campaign] for [client]"). Produces 2–3 de-slopped candidates that follow the format skeleton and the client's voice rules.
---

# ABM draft

Turn angle + format spec + client context into ship-ready candidates.

## Before drafting

- Load the format spec and the client context. If either is missing, run the upstream skill first.
- Research the subject until every skeleton block can be filled with REAL specifics (names, numbers, dates, insider details). The seed formats work because of verifiable detail density — a rise story with vague plays is dead. If research can't fill a block, tell the user instead of inventing.

## Drafting rules

- Follow the spec's skeleton block-for-block and its rhythm/formatting notes (arrow bullets, numbered plays, line-break density, length).
- Voice comes from the client context, not the source post's author. Hard constraints: banned phrases, tone rules, and Canon facts from context.md. A draft citing proof not in the Canon/Proof sections is invalid.
- Fill-in hooks: adapt the hook pattern to the subject; never copy a source post's sentences.
- 2–3 candidates by default, varying the hook and the subject's entry point, not the skeleton.

## De-slop pass (every candidate, before showing)

Strip: em-dashes, "not X, it's Y" contrasts, rule-of-three padding, "dive in", throat-clearing openers, rhetorical-question hooks (unless the format spec's hook pattern IS a question), aphoristic closers, exclamation marks, adverb stacks. Keep intentional staccato.

## QA gate (every candidate)

- [ ] Skeleton matches the spec block sequence
- [ ] Every claim traceable to context Canon/Proof or to the subject research (with source)
- [ ] No banned phrases; voice rules honored
- [ ] Hook lands inside the first ~200 characters (before the fold)
- [ ] Named people/accounts are correct and current — titles verified this run
- [ ] ABM payoff intact: the target would be glad this exists

## Output

Present candidates with a one-line note each (hook variant + any tradeoff). Save chosen drafts to `abm-clients/<slug>/drafts/YYYY-MM-DD-<slug>.md`.
