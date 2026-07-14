---
description: Strip AI tells from a post — kills em-dashes and "not X, it's Y" contrasts, plus jargon, adverbs, false agency, and throat-clearing. Paste the post after the command. Watt-aware, so Jared's staccato and closers survive.
argument-hint: "<paste the post to de-slop>"
---

The text to de-slop is in $ARGUMENTS. If $ARGUMENTS is empty, ask the user to paste the post and stop.

Apply the **watt-antislop** skill to that text. Load its full ruleset, including the reference files:

- `${CLAUDE_PLUGIN_ROOT}/skills/watt-antislop/SKILL.md`
- `${CLAUDE_PLUGIN_ROOT}/skills/watt-antislop/references/phrases.md`
- `${CLAUDE_PLUGIN_ROOT}/skills/watt-antislop/references/structures.md`
- `${CLAUDE_PLUGIN_ROOT}/skills/watt-antislop/references/examples.md`

Non-negotiable, no exceptions:

1. Remove every em-dash (`—`, `–`, `--`, or a spaced ` - ` used as one). Replace with a comma, period, parentheses, or restructure.
2. Rewrite every "not X, it's Y" / "isn't X, it's Y" / "not because X but Y" / "not just X but Y" contrast. State Y directly, drop the negation. (Keep real positioning shifts like "data company → signal company"; only the rhetorical sentence shape dies.)

Then clear the rest: business jargon, adverbs (really, just, genuinely, simply, actually), false agency ("the data tells us"), throat-clearing ("here's the thing," "the truth is"), vague declaratives, negative listing, rhetorical setups.

Detect whether this is a Jared post. If it is, preserve his deliberate craft: the staccato beat ("You ship. You hit PMF. Revenue compounds."), forward-beat closers ("Let's go."), arrows (→), casually dropped numbers, and one earned intensifier. Strip the tells, keep the voice.

Output, in this order:

1. **The edited post**, ready to paste.
2. **AI-tell scan** — one line: em-dashes removed, contrasts rewritten, adverbs cut, false-agency fixes, jargon swaps.
3. If it was a Jared post: one line confirming his rhythm, closer, and formatting survived.

Keep commentary short. Do not explain the rules back to the user; just return clean prose.
