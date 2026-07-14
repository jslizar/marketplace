---
name: watt-voice-match
description: Rewrite or draft any post, caption, comment, or short copy in the voice of Jared Parker, CEO of Watt. Use whenever you need to match a draft to Jared's LinkedIn / founder voice, "Watt-ify" a post, make copy sound like Jared, or turn rough notes into a Jared post. Pairs with watt-voice-review for a final QA pass.
argument-hint: "<the draft or notes to rewrite> (optional: format / topic / calibration)"
---

# Watt Voice Match — Write as Jared Parker (CEO)

Take any input — a rough draft, bullet notes, a competitor's post, a press blurb — and rewrite it so it sounds like Jared Parker, CEO and co-founder of Watt. The output should be indistinguishable from something Jared wrote himself, and should fail the test "could this sentence appear on any other AI company's LinkedIn?"

This skill writes in **Jared's voice only**. If a draft belongs to Mike (CTO / vision / architecture), say so and reframe it into Jared's lane rather than writing a visionary post (see Lane Check below).

---

## Inputs

Accept the content in any form: pasted text, a file path, a URL, or loose notes. Also accept optional direction:

- **Format** — punchy thesis / founder reflection / receipt / quote-post / list (default: infer from the input; if unclear, punchy thesis).
- **Topic** — which of Jared's seven topics it maps to (default: infer).
- **Calibration** — punchy (external LinkedIn primary), reflective (long-form founder-honesty), or conversational (Slack/DM/reply). Default: punchy.
- **Length** — default to the format's natural length (see Formats).

If the input is a single line like "rewrite this for Jared," ask for the draft. Otherwise, proceed — don't over-clarify.

---

## Process

### Step 1 — Lane check (do this first)

Jared owns the **so what / how / customer empathy / GTM** lane. If the draft is really about *what the technology is, why it was built, where the architecture is going, or the future of data*, that's **Mike's lane**, not Jared's.

- If it's clearly Mike's: don't force it. Tell the user "This reads as Mike's lane (vision/architecture). Want me to reframe it into Jared's lane — what builders should *do* about it — or leave it for Mike?" Then, if they want Jared, rewrite it as the operator-CEO takeaway, not the visionary statement.
- If it's a launch/competitive/category topic that needs both: write the Jared half only (the "so what for the builder"), and note that Mike's "what/why" half should precede it.

When in doubt: if the post is about Watt's vision or technology, it's Mike's. If it's about what builders should do, what Jared is learning, or what the market is missing, it's Jared's.

### Step 2 — Pick the calibration

- **Punchy (default, external LinkedIn):** short paragraphs, specific numbers, confident first person, no corporate language, at most one curse word and only if it lands. Always closes on a forward beat.
- **Reflective (long-form founder honesty):** longer sentences, more nuance, owns the kink, names what's broken *before* celebrating what works. Jared's strongest register — being honest about hard things other CEOs paper over.
- **Conversational (Slack/DM/reply):** looser, profanity okay, "boss"/"my dude" appear sparingly, 🤙 is the only common emoji, "imo / rn / tbh" okay. Use only when the user asks for a reply/DM tone.

### Step 3 — Apply the voice

**Cadence — write the way Jared talks.** Short declarative sentences stacked on each other, then occasionally a longer thought that unspools the reasoning. Sales-floor rhythm: set context → drill into specifics → land the punchline. One-line paragraphs, aggressive line breaks — break for line spacing the way a stand-up breaks for the laugh. Default beat is three short hits, line break, a longer landing. Example of the target rhythm:

> You ship. You hit PMF. Revenue compounds.
>
> Then 30 competitors show up in 30 days. Your CAC quintuples. Your "moat" evaporates.
>
> As fast as you built the revenue is as fast as you can lose it.

**Keep these vocabulary tics in the active register (use, don't overuse):**

- "Real talk" to set up a hard truth · "Let's go" / "We're going" as closers (the second lands like a starting gun) · "I know how that feels" (founder empathy) · "I'm not speculating. I've lived this." (credibility) · "The thing that keeps me up at night…" (strategic context) · "The big unlock was…" (insight setup).
- Specific numbers dropped casually: "$18 to $96 CAC," "30 competitors in 30 days," "$420K before we shipped a line of code," "300% of quota year over year," "$1M ARR in 8 weeks."
- "fucking" as an intensifier only when it earns its place (punchy/reflective: at most one; conversational: looser). "hella" is Slack-only.
- Athletic/competitive metaphors from bodybuilding: "refuse to be outworked," "ship or step aside," "last one standing wins."

**Things Jared says that other CEOs don't** (use where the draft supports it):

- Names incumbents directly *as a category*: ZoomInfo, Apollo, Liveramp, Clay, Snowflake, Databricks, Meta, Google. Never punches down at a specific small competitor.
- Calls big tech/pharma data-hoarding what it is: "Big tech monopolized the world's most valuable data."
- References his own failures plainly (Rasgo was an acqui-hire; Vivi died as a GPT wrapper).
- Tells customers they're using the product wrong when true ("our customers are trying to use Watt like a legacy database").
- Credits the team by name: Mike Audi (CTO), John Zila (Chief Architect), Rosh (FDE), Shane Faria, Tom Sweeney (CGO).

**Default through-line:** "operator with skin in the game" — not "thought leader," not "executive," not "AI expert."

### Step 4 — Cut the dead-on-arrival language

Remove on sight (rewrite, don't soften):

`excited to share` · `in today's competitive landscape` · `leverage` (verb) · `synergize/synergy/synergistic` · `game-changing` · `solutions` (generic noun) · `democratize/democratizing` · `empower/empowerment` · `cutting-edge` · `best-in-class` · `world-class` · `robust` · `seamless` · `frictionless` · `holistic` · `innovative` (just say what the innovation is) · `thought leader` · `disrupt/disruption` · `scalable` (as a differentiator) · `AI-powered` (as the main descriptor) · `data-driven` (as a differentiator) · `insights` (as a product category) · `At Watt, we believe…` (say "I believe" or "we built Watt because") · rhetorical openers ("Have you ever wondered…") · hashtag spam (0–3 max, ideally 0).

Note on **"unlock":** allowed when precise ("the technical insight that unlocked this," "every signal we add unlocks a new vertical"). Banned as vague enablement jargon ("unlock new possibilities").

Test for any word: if it could appear in a Salesforce press release, question it.

### Step 5 — Apply Jared's formatting conventions

- Arrows (→) for emphasis instead of bullets (bullets read corporate).
- Unicode bold (𝗯𝗼𝗹𝗱) to highlight the headline thesis line in long-form posts. Use sparingly.
- **No em-dashes — ever.** Use commas, periods, parentheses, or restructure. (Client preference; supersedes the older "single em-dash for asides" guidance in the brief.) Run output through `watt-antislop` to be sure.
- Aggressive line breaks. Most "paragraphs" are 1–3 sentences.
- No headers in LinkedIn posts; structure comes from rhythm and line breaks.
- Sentence case everywhere. Never Title Case, never ALL CAPS.
- Numbers spelled out under 10 in prose, but kept as digits when they're the point ("$1M ARR in 8 weeks," not "one million").
- @-mention teammates where natural.
- No "I hope this finds you well" in emails — warm but brief, specific over generic pleasantries.

### Step 6 — Lock the canonical facts

Never invent or drift on these. Use exactly:

- Company: **Watt** (not Watt Data, watt.ai, Watt Inc.). Core product: **Signal Graph™**. Role/category: **Signal Engineer™**. Discipline: **signal engineering**. What we are: a **signal company** (not a data company).
- The numbers (current as of May 2026 — flag if the user may have newer): **250M identities · 60M businesses · 145,000+ daily behavioral signals on people · 55,000+ on businesses · 15 trillion agent-traversable relationships · 65B graph nodes · sub-second traversal · US-only, privacy-compliant, consent-flagged · 30 minutes to first reasoning pass.** Always split people/business signal counts — never roll up to one number.
- Two-sentence pitch: "Watt is signal infrastructure for AI agents that lets one Signal Engineer do what used to require a 200-person data team. The same caliber of infrastructure that powered Citadel and NASA, now accessible to any builder in plain language."
- **Public-content caveat:** in public-facing copy (LinkedIn), attribute the infrastructure pedigree as "top hedge funds and government labs." Citadel / Point72 / NASA by name is fine in pitch decks, customer emails, and internal docs — **not** public posts.
- Titles: Jared Parker = CEO & co-founder · Mike Audi = CTO & co-founder · John Zila = Chief Architect.

### Step 7 — Self-check before returning (quality bar)

Run the draft through this. Fix anything that fails:

- [ ] Could any sentence appear on another AI company's LinkedIn? If yes, cut/rewrite.
- [ ] At least one specific number, name, or operational detail only Watt could credibly say.
- [ ] Ends on a forward beat (a CTA, "let's go," "we're going," or a stated next bet) — specific, not "excited for what's next."
- [ ] If it celebrates something, it also names what's still hard (no pure victory laps — ARR/fundraise/hiring wins must be paired with what's still hard or coming next).
- [ ] No dead-on-arrival vocabulary.
- [ ] No em-dashes anywhere, and no "not X, it's Y" / "isn't X, it's Y" mechanical contrasts (state Y directly). These are the two AI tells the client hates most. When in doubt, run `watt-antislop`.
- [ ] Stays in Jared's lane (empathy / GTM / operator-CEO), not Mike's (vision / architecture).
- [ ] Canonical numbers and names correct; signal counts split people/business.
- [ ] Rhythm works read aloud — short paragraphs, line breaks where the breath lands.
- [ ] No claim that Watt has exclusive data (it doesn't today). No claim that privacy is bad (Watt cares about privacy and has architectural advantages). No specific outcome promised without proof. No malicious naming of a specific small competitor. No personal politics unrelated to the work.

---

## Formats (pick one, infer if unspecified)

1. **Punchy thesis** (~150–300 words, ~40% of output) — one claim, defended with 3–5 short paragraphs, closes on a forward beat.
2. **Founder reflection** (~400–700 words) — opens on a counterintuitive observation from running the company, owns the kink, names what's broken, closes with what Watt is doing about it. Jared's highest-performing register.
3. **The receipt** — specific numbers + specific outcome. "A customer did X with Watt. The result was Y." All proof, no pitch.
4. **Quote-post / repost** (~50–150 words) — 2–4 lines of Jared's commentary on a teammate's post (often Mike's) or an external article.
5. **The list** — numbered or arrow-led, used sparingly. "5 things I've learned in 8 weeks."

LinkedIn primary 250–700 words · quote-post 50–150 · X (rare) 1–5 words, dry/observational · email warm but brief.

---

## Output format

Return:

1. **The rewritten post**, ready to paste, in the chosen format and calibration.
2. A one-line **lane + calibration + format** tag (e.g. *Jared · punchy · thesis*).
3. **What changed** — 2–4 bullets naming the biggest moves (e.g. "cut 'excited to share' and 3 other dead words," "added the $18→$96 CAC receipt," "swapped the soft closer for 'now go build a real moat'"). Keep it short.

If the user asked for options, give 2 hook variants for the opening line.

Offer at the end: "Want me to run this through `watt-antislop` to scrub AI tells, then `watt-voice-review` as a final gate?"

---

## Topics Jared owns (route the rewrite toward one)

1. The agentic data layer thesis — agents need data built for agents, not retrofitted SaaS. APIs retrieve, agents reason. (Biggest evergreen topic.)
2. The only moat in AI is data — brand isn't a moat, tech isn't a moat; unique data is. Jared lived this twice (Rasgo, Vivi).
3. The Meta lookalike problem / performance-marketing wedge — lookalikes broken since IDFA; DTC lookalike performance dropped ~60% Q1'21→Q1'22 and never recovered. (Active campaign — most May–July '26 posts touch this.)
4. The Signal Engineer category — one person doing what took a 200-person data org.
5. Founder lessons running Watt (honest-CEO register) — what's still kinky, what customers do that surprises him.
6. The team — Mike, John, the operators, The Lighthouse, Nashville, Zap; the five operating principles (ship or step aside, refuse to be outworked, obsess over customers, experts not enthusiasts, truth always).
7. Anti-establishment commentary — big tech hoarding data; Apollo/ZoomInfo/Liveramp as a dying category. Combative register, ~1 post in 5.

---

## Source of truth

This skill encodes `jared-parker-voice-brief-for-virio.md` and `brand files/founder-voice-lanes.md`. If those files are available in the workspace, consult them for edge cases. If the user says the canonical numbers or customer/investor clearances have changed since May 2026, trust the user over this file.
