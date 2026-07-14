---
description: Run a post through the full Watt voice pipeline — rewrite in Jared Parker's voice, strip AI tells, then QA against the brand. Paste a draft or rough notes after the command; get back a clean, ship-ready post plus a verdict.
argument-hint: "<paste the draft or notes>"
---

The draft or notes are in $ARGUMENTS. If $ARGUMENTS is empty, ask the user to paste a draft and stop.

Run the three voice skills in sequence on that text. Load each skill (and its references) from `${CLAUDE_PLUGIN_ROOT}/skills/`:

**Step 1 — Rewrite (watt-voice-match).** Recast the text in Jared Parker's CEO voice. First confirm it belongs in Jared's lane (so what / GTM / customer empathy / operator-CEO). If it is really Mike's lane (vision / architecture / the future of data), say so and reframe it into Jared's "what should a builder do about this" angle rather than forcing a visionary post. Pick the calibration (punchy default, or reflective for founder-honesty) and format. Apply the cadence, lock the canonical facts and naming, and avoid the dead-on-arrival vocabulary.

**Step 2 — De-slop (watt-antislop).** Scrub the rewrite. Remove every em-dash. Rewrite every "not X, it's Y" contrast to state Y. Clear jargon, adverbs, false agency, throat-clearing, vague declaratives. Preserve Jared's staccato beat, forward-beat closer, arrows, and any earned intensifier.

**Step 3 — Review (watt-voice-review).** Audit the de-slopped post. Score the dimensions, run the AI-tell scan (any em-dash or "not X, it's Y" is an automatic fail), and check lane, canonical facts, closer, the no-victory-lap rule, and publishability. Surface any clearance flags (named customers/investors, public Citadel/NASA mention, unproven outcome claims).

Output, in this order:

1. **Final post**, ready to paste.
2. **One-line tags** — lane · calibration · format.
3. **What changed** — 2 to 4 bullets covering the biggest voice moves and the AI-tell scan counts.
4. **Verdict** — Ship / Fix first / Hold, with any clearance flags listed.

If the verdict is Fix first or Hold, apply the high-severity fixes and show the corrected version. Keep commentary tight.
