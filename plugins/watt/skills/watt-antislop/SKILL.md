---
name: watt-antislop
description: Strip AI tells out of prose — em-dashes, "not X, it's Y" contrasts, false agency, business jargon, adverbs, throat-clearing, vague declaratives. Use to de-slop a draft, kill AI giveaways, or clean copy before it ships. Watt-aware — preserves Jared Parker's intentional staccato rhythm and forward-beat closers. Modeled on hardikpandya/stop-slop.
argument-hint: "<the draft to de-slop>"
---

# Watt Antislop — remove AI tells from prose

AI writing has patterns: predictable phrases, structures, rhythms. This skill catches and removes them. Run it on any draft to make it sound like a person wrote it, not a model.

**Watt-aware:** Some things generic anti-slop tools ban are Jared Parker's deliberate voice. This skill keeps those and cuts the rest. See "Watt exceptions" before stripping anything in a Jared post.

The two the client hates most — kill on sight, no exceptions:

1. **Em-dashes.** Every one. Replace with a comma, a period, parentheses, or restructure the sentence. No `—`, no ` - ` standing in for one, no `--`.
2. **"Not X, it's Y" contrasts** (and every cousin: "isn't X, it's Y," "not because X, but Y," "the answer isn't X, it's Y," "it's not about X, it's about Y," "not just X but Y"). State Y directly and drop the negation.

---

## Inputs

The draft (pasted, file path, or URL). Optionally a flag for whether it's a Jared post (apply Watt exceptions) or generic copy (apply the full ruleset). Default: detect from content; if it reads like a Jared post, keep the Watt exceptions on.

---

## Core rules

1. **Cut em-dashes entirely.** No em-dash anywhere. Comma, period, or restructure. (See references/structures.md → Em-dashes.)

2. **Kill the binary contrast.** Delete every "not X, it's Y" / "isn't X, it's Y" / "not because X, but Y" / "stops being X and starts being Y." State Y. (See references/structures.md → Binary contrasts.)

3. **Cut filler phrases.** Throat-clearing openers ("Here's the thing," "Here's what," "The truth is"), emphasis crutches ("Let that sink in," "Make no mistake"), and adverbs (really, just, genuinely, honestly, simply, actually, literally, deeply). (See references/phrases.md.)

4. **Use active voice.** Every sentence needs a human subject doing something. No passive. No inanimate object doing a human verb ("the data tells us," "the complaint becomes a fix"). Name the actor, or use "you."

5. **Be specific.** No vague declaratives ("the implications are significant," "the reasons are structural"). Name the specific thing. No lazy extremes (every, always, never) doing vague work.

6. **Break formulaic structures.** No negative listing ("Not a X. Not a Y. A Z."), no rhetorical setups ("What if I told you," "Think about it," "And that's okay"), no meta-commentary ("Let me walk you through," "as we'll see").

7. **Replace business jargon** with plain words: leverage → use, navigate → handle, unpack → explain, deep dive → analysis, lean into → accept, double down → commit, circle back → revisit, moving forward → next.

8. **Trust the reader.** State facts directly. Cut softening, justification, and hand-holding. If a line sounds like a pull-quote, rewrite it.

---

## Watt exceptions (keep these in a Jared post)

Jared's brief calls for these on purpose. Do NOT flatten them when de-slopping his copy:

- **Staccato rhythm / fragments for cadence** — "You ship. You hit PMF. Revenue compounds." This is his signature beat (three short hits, line break, longer landing). Generic stop-slop bans fragmentation; here it stays.
- **Forward-beat closers** — "Let's go." / "We're going." / "Now go build a real moat." These are intentional, not slop.
- **Casual dropped numbers as voice** — "$18 to $96 CAC," "30 competitors in 30 days." Keep.
- **Naming incumbents as a category** — ZoomInfo, Apollo, Meta, Google. Keep.
- **Arrows (→)** for emphasis. Keep (Jared's formatting convention).
- **One earned "fucking"** as an intensifier in punchy/reflective copy. Keep if it lands.

The line: cut **AI tells** (em-dashes, mechanical contrasts, jargon, adverbs, false agency, vague declaratives, throat-clearing). Keep **Jared's deliberate craft** (rhythm, closers, specificity, directness). When a fragment is doing rhythmic work in Jared's voice, it stays. When fragmentation is manufactured profundity ("This unlocks something. Power."), it goes.

For generic (non-Jared) copy, drop the exceptions and apply the full ruleset.

---

## Quick checks (run before delivering)

- Em-dash anywhere? Remove it. (Highest priority.)
- Any "not X, it's Y" / "isn't X, it's Y" / "not just X but Y"? State Y, drop the negation. (Highest priority.)
- Any adverbs (-ly, really, just, genuinely, honestly, simply, actually)? Kill them.
- Passive voice? Find the actor, put them first.
- Inanimate thing doing a human verb ("the market rewards," "the decision emerges")? Name the person, or use "you."
- "Here's what/this/the thing" throat-clearing? Cut to the point.
- Sentence starts with What/When/Why/How as a setup? Restructure, lead with the subject.
- Vague declarative ("the stakes are high," "this is the deepest problem")? Name the specific thing.
- Negative listing ("Not a memo. Not a plan. A bet.")? State the thing.
- Rhetorical setup ("What if I told you," "Think about it," "And that's okay")? Cut.
- Business jargon (leverage, navigate, deep dive, lean into)? Plain words.
- Three-item list where two would do? Trim to two.
- **Jared post?** Confirm you did NOT strip his staccato beat, forward-beat closer, arrows, or earned intensifier.

---

## Scoring

Rate the draft 1–10 on each. Below 35/50, revise.

| Dimension | Question |
|-----------|----------|
| Directness | Statements, or announcements about what's coming? |
| Rhythm | Varied, or metronomic? (For Jared: is his beat intact?) |
| Trust | Respects the reader's intelligence? |
| Authenticity | Sounds like a person? |
| Density | Anything cuttable? |

Add a sixth, pass/fail gate: **AI-tell scan** — zero em-dashes, zero "not X, it's Y" contrasts, zero false agency. Any hit = automatic revise regardless of score.

---

## Output format

1. **The de-slopped draft**, ready to paste.
2. **AI-tell scan** — a one-line count: em-dashes removed, contrasts rewritten, adverbs cut, false-agency fixes, jargon swaps.
3. **Score** — the 1–10 table plus the pass/fail AI-tell gate.
4. If it's a Jared post: a one-line confirmation that his rhythm, closer, and formatting survived.

Keep commentary short. The point is clean prose, not a lecture about it.

---

## References

- [references/phrases.md](references/phrases.md) — words and phrases to remove (throat-clearing, emphasis crutches, jargon, adverbs, vague declaratives, meta-commentary).
- [references/structures.md](references/structures.md) — structural patterns to break (em-dashes, binary contrasts, negative listing, false agency, passive voice, rhythm).
- [references/examples.md](references/examples.md) — before/after transformations, including Watt/Jared-flavored ones.

## Source

Modeled on hardikpandya/stop-slop (MIT). Adapted to be Watt-aware and to prioritize the two tells the client flagged: em-dashes and "not X, it's Y" contrasts. Pairs with `watt-voice-match` (write) and `watt-voice-review` (QA).
