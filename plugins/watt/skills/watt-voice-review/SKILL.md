---
name: watt-voice-review
description: Audit a draft against Jared Parker's Watt voice and flag issues by severity with specific before/after fixes — without rewriting the whole thing. Use as a final gate before a Jared post ships, to catch dead-on-arrival words, lane drift, wrong canonical facts, weak closers, victory laps, and publishability risks. Pairs with watt-voice-match.
argument-hint: "<the draft to review>"
---

# Watt Voice Review — QA a draft against Jared's voice

Audit a draft meant to go out under Jared Parker's name. **Flag and explain — do not rewrite the whole post.** Output is a scored checklist plus a findings table with targeted before/after fixes, ending in a clear ship / fix / hold verdict.

If the user wants a full rewrite instead, hand off to `watt-voice-match`.

---

## Inputs

The draft (pasted, file path, or URL). Optionally the intended format and calibration. If none given, infer.

---

## Review dimensions

Score each pass/warn/fail and cite the exact offending text.

### 1. Lane discipline
Jared owns **so what / how / customer empathy / GTM**. Flag if the draft drifts into **Mike's lane** — vision, "the future of data," architecture deep dives, Signal Graph internals, category-creation theory, fundraising narrative. A Jared post is about what builders should *do*, what Jared is *learning*, or what the market is *missing*. Test: if it reads as a visionary statement on the future of data, it's drifting → **High**.

### 2. Voice & cadence
- Short declarative sentences stacked, then a longer unspooling thought. Sales-floor rhythm: context → specifics → punchline. Aggressive one-line paragraphs and line breaks.
- Flag corporate cadence: long even paragraphs, no line breaks, hedged passive voice, "executive" tone.
- Flag missing register: no first-person operator voice, no specificity, sounds like a brand account not a person.
- Confirm at least one Jared tic is *available* where natural ("real talk," "I'm not speculating. I've lived this.," a casually dropped number) — don't force them, but a post with zero specificity and zero voice → **Medium/High**.

### 3. Dead-on-arrival vocabulary (always checked)
Flag any of: `excited to share` · `in today's competitive landscape` · `leverage` (verb) · `synergize/synergy/synergistic` · `game-changing` · `solutions` (generic) · `democratize` · `empower/empowerment` · `cutting-edge` · `best-in-class` · `world-class` · `robust` · `seamless` · `frictionless` · `holistic` · `innovative` (as self-descriptor) · `thought leader` · `disrupt/disruption` · `scalable` (as differentiator) · `AI-powered` (as main descriptor) · `data-driven` (as differentiator) · `insights` (as a product category) · `At Watt, we believe…` · rhetorical question openers ("Have you ever wondered…") · 4+ hashtags.
Each instance → **High** (these are cut-on-sight). Note: "unlock" is fine when precise ("unlocked this," "unlocks a new vertical"), **flag only** when it's vague enablement ("unlock new possibilities").
Test offered for borderline words: would this appear in a Salesforce press release?

### 4. Canonical facts & naming
Flag drift from:
- **Watt** (not Watt Data / watt.ai / Watt Inc.) · **Signal Graph™** · **Signal Engineer™** · **signal engineering** · "**signal company**" not "data company."
- Numbers: **250M identities · 60M businesses · 145,000+ daily signals on people · 55,000+ on businesses · 15 trillion relationships · 65B nodes**. Signal counts must be **split people/business — never one rolled-up number** → wrong/rolled-up number = **High**.
- Titles: Jared = CEO & co-founder · Mike Audi = CTO & co-founder · John Zila = Chief Architect.
- **Public-content pedigree rule:** in a public post (LinkedIn), naming **Citadel / Point72 / NASA** directly is a flag — public copy says "top hedge funds and government labs." (By name is fine only in decks / customer emails / internal docs.) → **High** if the draft is public-facing.

### 5. Formatting conventions
Flag: bullets where arrows (→) belong · Title Case or ALL CAPS (should be sentence case) · headers inside a LinkedIn post · numbers-as-words where the number is the point ("one million ARR" → "$1M") · hashtag spam. Mostly **Low/Medium**.

### 5a. AI tells (always checked — client's top peeves)
- **Em-dashes** — any `—`, `–`, `--`, or spaced ` - ` used as one → **High**. Jared copy uses none; replace with comma, period, parentheses, or restructure.
- **"Not X, it's Y" contrasts** — "isn't X, it's Y," "not because X but Y," "the answer isn't X, it's Y," "it's not about X, it's about Y," "not just X but Y" → **High**. State Y directly.
- Other tells (Medium unless stacked): false agency ("the data tells us," "the market rewards"), throat-clearing ("here's the thing," "the truth is"), vague declaratives ("the implications are significant"), adverb crutches (really, just, genuinely, simply, actually), negative listing, rhetorical setups ("what if I told you," "and that's okay").
- For deeper coverage or to fix these in place, hand off to `watt-antislop`.

### 6. Closer & victory-lap rule
- Flag a generic/soft closer ("excited for what's next," "stay tuned") — Jared closes on a specific forward beat ("now go build a real moat," "let's go," "we're going," or a stated next bet) → **Medium**.
- Flag a **pure victory lap**: any ARR milestone, fundraise, or hiring win that is *not* paired with what's still hard or coming next → **High**. Jared never papers over the hard part.

### 7. Publishability / risk (always checked)
Flag → **High**:
- Claims Watt has **exclusive data** (it doesn't today — every signal is on the open market; the moat is the substrate).
- Says or implies **privacy is bad** or that Watt doesn't care (Watt cares and has architectural advantages — no SDKs, cookies, tracking; US-only).
- **Specific outcome promised without proof.**
- **Malicious naming of a specific small competitor** (naming ZoomInfo/Apollo/Liveramp/Meta/Google *as a category* is fine; viciously trashing a named small player is not).
- **Unnamed customer or investor referenced as if cleared** — named customer/investor references need clearance; anonymized is the default for external content. Flag any specific customer name and note it needs Tom Sweeney sign-off.
- Personal politics unrelated to the work.

---

## Severity definitions

- **High** — would not ship under Jared's name as-is: dead-on-arrival language, lane drift, wrong canonical fact, a victory lap with no hard truth, or a publishability/clearance risk.
- **Medium** — off-voice but not damaging: weak closer, flat cadence, soft specificity.
- **Low** — minor style/formatting (em-dash, casing, arrows vs. bullets).

---

## Output format

### Verdict
One line: **Ship** (no High issues) · **Fix first** (High issues present, listed) · **Hold** (clearance/publishability risk needs a human). Then one sentence on the single most important thing to change.

### Scorecard
A compact pass / warn / fail line per dimension (Lane · Voice & cadence · Dead words · Facts & naming · Formatting · AI tells · Closer & victory-lap · Publishability). Any em-dash or "not X, it's Y" contrast is an automatic fail on AI tells.

### Findings
A table — every issue, located and fixable:

| Issue | Offending text | Severity | Fix (before → after) |
|-------|----------------|----------|----------------------|

Give a concrete before→after for each High and Medium. For Low items a short note is fine.

### Clearance flags
List separately any named customer/investor, public-facing Citadel/NASA mention, or outcome claim that needs sign-off (Tom Sweeney for customer/investor/competitive/anti-big-tech framing; Jared directly for sensitive topics).

### After review
Offer: "Want me to apply the High-severity fixes, hand this to `watt-voice-match` for a full rewrite, or re-review a new version?"

---

## Source of truth

Encodes `jared-parker-voice-brief-for-virio.md` (esp. §2 voice, §8 naming, §9 will/won't publish, §12 quality bar, §13 approvals) and `brand files/founder-voice-lanes.md`. Consult those files for edge cases if available. If the user says canonical numbers or clearances have changed since May 2026, trust the user over this file.
