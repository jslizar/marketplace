---
name: draft
description: Draft posts from a chosen angle and format spec. Use when the user says "draft it", "write the post", picks an angle from angles, or names a lane, format, and subject directly ("write a MOFU gated-playbook post about [topic] for [client]", "write a credit-roll post about [campaign]"). Produces 2–3 de-slopped candidates that follow the format skeleton, the client's voice rules, and the lane directive.
---

# Draft

Turn angle + format spec + client context + lane directive into ship-ready candidates.

## Before drafting

- Load the format spec, the client context, and the lane directive (`content-library/<library>/<lane>/config.md`). If any is missing, run the upstream skill first.
- Research the subject until every skeleton block can be filled with REAL specifics (names, numbers, dates, insider details). The seed formats work because of verifiable detail density — a rise story with vague plays is dead. If research can't fill a block, tell the user instead of inventing.

## Drafting rules

- Follow the spec's skeleton block-for-block and its rhythm/formatting notes (arrow bullets, numbered sections, line-break density, length).
- Voice comes from the client context, not the source post's author. Hard constraints: banned phrases, tone rules, and Canon facts from context.md. A draft citing proof not in the Canon/Proof sections is invalid.
- The lane directive governs the CTA and proof level: TOFU — no CTA or follow-level only, light proof; MOFU — soft CTA (resource, comment prompt), medium proof; BOFU — hard CTA (demo, call, trial), heavy proof from the Proof section; ABM — the post itself is the CTA, heavy named-specificity, and the target must come out glad it exists.
- Fill-in hooks: adapt the hook pattern to the subject; never copy a source post's sentences.
- 2–3 candidates by default, varying the hook and the subject's entry point, not the skeleton.

## De-slop pass (every candidate, before showing)

Strip: em-dashes, "not X, it's Y" contrasts, rule-of-three padding, "dive in", throat-clearing openers, rhetorical-question hooks (unless the format spec's hook pattern IS a question), aphoristic closers, exclamation marks, adverb stacks. Keep intentional staccato.

## QA gate (every candidate)

- [ ] Skeleton matches the spec block sequence
- [ ] Every claim traceable to context Canon/Proof or to the subject research (with source)
- [ ] No banned phrases; voice rules honored
- [ ] Hook lands inside the first ~200 characters (before the fold)
- [ ] Lane check: CTA strength and proof level match the lane directive — a BOFU draft with no CTA fails; a TOFU draft with a demo ask fails; an ABM draft whose target wouldn't be glad it exists fails
- [ ] Named people/accounts are correct and current — titles verified this run
- [ ] Lane deconfliction: if a funnel-lane draft's engine turns out to be glorifying a named account, flag it — that post belongs to the abm lane (and vice versa: an "ABM" draft that never really features the target isn't one)

## Output

Present candidates with a one-line note each (hook variant + any tradeoff). Save chosen drafts to `clients/<slug>/drafts/<lane>/YYYY-MM-DD-<slug>.md` with frontmatter recording `format: <format-name>` and `library: <virio|millies>` — the pipeline's rotation check reads these.
