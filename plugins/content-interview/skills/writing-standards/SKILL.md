---
name: writing-standards
description: Draft LinkedIn posts from an inventory idea using the three-phase protocol (Hooks, Takeaways, Draft). Use when the user picks an idea from an idea-inventory and says "let's work on this one", "draft this idea", "give me hooks for this", "write this post", or wants the pillar-by-funnel framework, the 6 Hook Levers, or the 10 Takeaway Types applied to a draft. Every phase stops for the user's lock before the next begins.
---

# Writing standards

## Section 1 — Reference

Read once at the start of a session. Don't repeat this information in outputs.

### The two-dimensional content framework

Every post has two dimensions decided before any drafting begins:

- **Dimension 1 — Content Pillar:** what the post is about
- **Dimension 2 — Funnel Stage:** who the hook targets and what LinkedIn universe the post enters

These work together. A post is never just "tactical" — it's "tactical, TOFU" or "tactical, MOFU". The pillar determines the substance; the funnel stage determines how the hook is written.

### Content pillars

- **Tactical** — actionable how-tos the ICP can implement immediately. Steps, tools, specific numbers, concrete outputs.
- **Aspirational** — success stories and wins with real outcomes. Proof of what's possible. Before/after with the mechanism that produced the result.
- **Insightful** — industry takes, trend analysis, strong opinions. A clear POV stated early, supported by evidence or experience, never just an assertion.
- **Personal** — behind-the-scenes, building in public, human moments. Grounded in a real moment first; the lesson comes after, never before.

### Funnel stages

- **TOFU — Top of Funnel (industry-oriented).** The hook speaks to a broad industry space, not a specific role. Goal: build authority and reach new audiences. The hook makes a claim, shares a take, or surfaces data relevant to the industry. Someone scrolling who works in this space should feel: "this is about my world." Not TOFU: a post about the client's own product or company — that's promotion.
- **MOFU — Middle of Funnel (ICP-oriented).** The hook calls out a precise job title — not "leaders" or "executives" but "VP of E-commerce", "early-stage founder", "CFO at a Series A". The post then delivers content genuinely useful to that exact person. If the title is named and the post is generic, it fails.
- **BOFU — Bottom of Funnel / ABM (person- or company-oriented).** The post names a specific person or company, makes them the hero, and highlights something genuinely impressive about them. Goal: get on their radar to open a door. Not BOFU: mentioning the client's own company, generic praise, or tagging many unrelated people.

### The 6 Hook Levers

Every hook must hit at least 3. Label every hook option with its levers before presenting.

1. **Social Proof** — establishes authority before the reader has a reason to keep scrolling
2. **Story** — creates tension by hinting at a narrative; makes the reader want to see how it ends
3. **Specific Numbers** — vague claims get ignored. "16 weeks" not "a few months". "$10M ARR" not "significant revenue"
4. **Bold Stance** — takes a confident position that forces the reader to pick a side
5. **Framework** — promises a list, system, or tangible takeaway; makes the post feel save-worthy
6. **Open Loop** — creates a question the reader can only answer by clicking "see more"

Weak hook (1 lever): "Here are 3 tips for sales."
Dense hook (3+ levers): "I scaled to $1M in 16 weeks using this exact outbound framework." (Social Proof + Numbers + Framework)

### Hook templates (ICP-grounded)

Use these when a hook feels too abstract or too founder-to-founder. Fill the brackets with the client's specific material.

- "How I [action] and [desired ICP result]."
- "In [year], I didn't know how to [ICP desire]. Here's what changed."
- "My #1 feedback for [ICP description]."
- "90% of my clients can't [desired ICP result] — here's why."
- "Last week, I spoke to a [ICP role] who [ICP pain point]."
- "How my client got [desired ICP result] in [timeframe]."

### The 10 Takeaway Types

Every post body delivers substance through one or more of these forms. When generating takeaway options in Phase 2, tag each one with its type.

Tips / Steps / Lessons / Stats / Benefits / Reasons / Mistakes / Examples / Questions / Personal stories / Myths

## Section 2 — The three-phase drafting protocol

This is the operating procedure. Follow it sequentially. Don't skip phases or combine them.

### Before starting any phase

State out loud:

- **Pillar:** Tactical / Aspirational / Insightful / Personal
- **Funnel stage:** TOFU / MOFU / BOFU
- **ICP target:** exact job title for MOFU, industry for TOFU, named person/company for BOFU
- **Source material:** the transcript moment, story, or data point that anchors this post

Don't proceed if source material is vague or missing. Flag `[NEED: specific story / number / result]` and stop. Then go straight into Phase 1 — don't wait for a prompt.

### Phase 1 — Hook brainstorming

Trigger: an idea is fed. State the pillar, funnel stage, ICP target, and source material, then immediately present 5 hooks. No extra prompt needed.

Output — present exactly this, nothing else:

```
PHASE 1 — HOOKS
Hook 1: [hook text]  [lever 1] + [lever 2] + [lever 3] ([N] levers)
Hook 2: ...
Hook 3: ...
Hook 4: ...
Hook 5: ...
```

Then: invite the user to select a hook, ask for variations, or request a different angle. Always give your recommendation of the best hook and why. Phase 2 begins when a hook is locked.

Rules:

- Every hook must hit at least 3 levers. Don't present a hook that hits fewer — rewrite it first.
- Vary the approach across the 5 options; never 5 versions of the same angle.
- Use the hook templates when the material risks being too abstract or too founder-to-founder.
- If the user requests variations, stay in Phase 1 and regenerate. Don't move to Phase 2 until a hook is explicitly locked.
- No body copy in Phase 1.

### Phase 2 — Takeaway brainstorming

Trigger: the user locks a hook.

Output — present exactly this, nothing else:

```
PHASE 2 — TAKEAWAYS
Locked hook: [the selected hook]
Option A — [Takeaway type: e.g. Steps] [1–2 sentence description of what this set of takeaways would cover]
Option B — [Takeaway type: e.g. Mistakes] [brief description]
Option C — [Takeaway type: e.g. Personal story + Lesson] [brief description]
Option D — [Takeaway type: e.g. Stats + POV] [brief description]
Option E — [Takeaway type: e.g. Examples] [brief description]
```

Then: invite the user to select a direction, request alternatives, or mix options. Always recommend the best takeaway format and why. Phase 3 begins when takeaways are locked.

Rules:

- Present 5 distinct takeaway directions using different types from the 10 Takeaway Types.
- Each option is a direction, not a full draft — describe the structure and contents, not the finished content.
- Vary the types across options; never 5 versions of the same format.
- If the user requests alternatives, stay in Phase 2. Don't move to Phase 3 until takeaways are locked.
- No full post body in Phase 2.

### Phase 3 — Draft

Trigger: the user locks takeaways.

Output:

```
PHASE 3 — DRAFT
Locked hook: [hook]
Locked takeaways: [type + brief description]

[Full post draft]

[NEED:] flags: [any missing specifics that need client input before publishing — omit if none]
```

Rules:

- Don't begin the draft until both hook and takeaways are locked.
- Flag every gap with `[NEED: ...]` rather than inventing specifics.
- No CTA unless the user asks for one or the post is a lead-magnet format.

Drafting standards — apply every one actively while writing:

- **One Main Idea:** the entire post orbits one clear point. A skimming reader gets the OMI without reading every word.
- **Substance:** the post teaches, proves, or reveals something the reader didn't know. It creates either a "save this" moment (specific and reference-worthy enough to return to) or a "who is this person?" moment (a perspective sharp enough to earn a profile visit). Generic posts do neither.
- **ICP language, not product language:** use the vocabulary the ICP uses to describe their own problems, not the vocabulary the client uses to describe their solution. The algorithm matches posts to readers by conceptual territory — ICP language reaches ICP feeds, product language does not.
  - Fail: "Our platform delivers seamless, compliant FSA payment experiences."
  - Pass: "Every year HR managers find out in December that half their team never used their FSA. The money's gone."
- **Stays in the client's conceptual territory:** every post should feel like it belongs to the same professional world as every other post on this account. If it would be read by a completely different audience than the client's ICP, it doesn't belong.
- **Transformation, not features:** the post helps the ICP become something or understand something; it does not describe what the client's product does. Test: could this post exist if the client's product didn't? If yes, it's content. If no, it's a pitch.
- **Sounds like the client's world, not the founder's peer group:** the post makes the ICP feel seen, not the founder look impressive to peers. If the hook addresses a problem only practitioners care about, or the takeaway is more useful to a fellow founder than to a buyer, rewrite it from the ICP's perspective.
- **Client voice intact:** sounds like this specific human — their vocabulary, cadence, industry framing. Not a template. Not AI. If it could have been written by anyone, revise it.
- **No AI tells:** de-slop every draft against `references/ai-tells.md`.
- **Sentence-level standards:**
  - Every sentence ends on its most important word.
  - Rate of revelation is high — new information introduced as quickly as possible, no stretched points.
  - Rhythm alternates between short declarative sentences and longer explanatory passages throughout the entire post.
  - No tiny word chunks (clusters of small filler words).
  - No adverbs — if the sentence weakens without one, replace the verb.
  - No opening "I think" / "I believe" / "I conclude" phrases.
