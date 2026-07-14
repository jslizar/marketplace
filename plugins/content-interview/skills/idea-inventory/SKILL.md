---
name: idea-inventory
description: Mine a content-interview transcript into a structured inventory of 20+ tagged post concepts. Use when the user says "generate an idea inventory", "extract ideas from this transcript", "mine this interview", "what posts are in this session", or after interview-kit produces a transcript. Every idea carries six required tags (pillar, funnel, ICP, source material, angle, intent signal) and is draftable via the writing-standards skill without further context. Not for generating interview questions — that's interview-kit.
---

# Idea inventory

Extract post ideas from session material and format them as a structured idea inventory. The inventory is the bridge between a content interview and the drafting workflow — every idea must be specific enough to enter Phase 1 of the writing-standards skill immediately, with no additional context needed.

## What a good idea looks like

A good idea is not a topic. It is a specific post concept with enough material attached to generate 5 grounded hooks immediately.

Weak idea (a topic):
> Pillar: Insightful | Topic: "Why most AI implementations fail"

Strong idea (a draftable concept):
> Pillar: Insightful | Funnel: TOFU | ICP: Head of Engineering at mid-market SaaS
> Source: Client said "we've done 12 AI pilots in the last 18 months and 11 of them never made it past the first quarter because the team that requested it was never the team that had to maintain it"
> Angle: Objection challenger — challenges the assumption that AI failure is a technology problem

The difference is the source material. A specific quote, moment, or result from the session is what makes hooks dense and grounded. Without it, Phase 1 produces generic hooks.

## Extraction protocol

Given a transcript or session notes:

- **Read the full material before extracting anything** — don't pull the first ideas you see. Read the whole session to find the richest material.
- **Extract ideas, not topics** — anchor every idea to a specific moment: a quote, a story, a number, a result, a strong opinion. If you can't point to the specific line in the transcript that anchors the idea, it is not ready to be an inventory item.
- **Check against previous sessions** — if earlier session transcripts exist, scan them first. Don't surface ideas that closely overlap with material already extracted. Flag topic areas running thin.
- **Tag every idea with all six fields** — pillar, funnel stage, ICP target, source material, content angle, intent signal. All six are required; an idea missing any field is incomplete.
- **Aim for 20+ ideas per session** — extract every viable angle, not just the obvious ones. Mine for secondary ideas inside stories the client told, opinions expressed in passing, numbers mentioned casually. If the session only yielded 12 strong ideas, output 12 — but push hard before settling. Thin inventory is almost always under-extraction, not a thin session.
- **Surface multiple angles from the same source** when they produce genuinely different posts — different audiences, pillars, or arguments. Don't split one idea into two to inflate the count. The test: would a reader who saw both posts feel they got something different each time? If they'd feel repetitive to the same audience, they're one idea.
- **Vary across pillars and funnel stages** — don't produce an inventory dominated by one pillar. Distribute across all four; flag if the session material was skewed and note what's missing.

## The six required fields

1. **Pillar** — Tactical / Aspirational / Insightful / Personal
2. **Funnel stage** — TOFU / MOFU / BOFU
   - TOFU: hook speaks to a broad industry audience
   - MOFU: hook calls out a specific job title
   - BOFU: hook names a specific person or company
3. **ICP target** — the exact person this post is for
   - TOFU: name the industry or space (e.g. "HR tech space", "enterprise SaaS")
   - MOFU: name the precise job title (e.g. "Head of Benefits at companies 200–1000 employees")
   - BOFU: name the specific person or company
4. **Source material** — the exact quote, story, number, or moment from the session that anchors this idea. This is what hooks are generated from; it must be specific enough that someone reading it could picture the moment.
   - Strong: "Client said 'we had 94% FSA forfeiture last December and my CEO asked me why in front of the whole exec team'"
   - Weak: "Client talked about FSA forfeiture being a problem"
5. **Content angle** — one type from the list below; it tells the drafter what kind of post body to propose in Phase 2.
6. **Intent signal** — the primary way this post earns algorithmic distribution. LinkedIn rewards two types:
   - **Save-worthy** — specific, tactical, or reference-worthy enough that a reader wants to return to it. Frameworks, step-by-steps, data breakdowns, decision tools.
   - **Profile-visit-worthy** — a perspective sharp or specific enough that a reader wants to know who wrote it. Strong hot takes, objection challengers, personal stories with a surprising angle.
   - **Both** — when the post is likely to do both.

   Prioritise save-worthy and profile-visit-worthy ideas when picking what to draft first. A post that earns neither is unlikely to reach the right audience.

## Content angle types

Tag each idea with one primary angle:

- **Real client conversation** — a story from a sales call, DM, onboarding, or support interaction
- **Real client result** — a specific before/after with numbers, timeline, and mechanism
- **Objection challenger** — directly addresses a belief the ICP holds that is wrong or incomplete
- **Zero-to-hero** — a failure, the turning point, and the win
- **Past-self callout** — the client addressing an earlier version of themselves or their ICP
- **ICP self-diagnosis** — a framework or question that helps the ICP identify their own problem
- **ICP pain/desire** — something that makes the ICP feel seen in their current situation
- **Hot take** — a confident stance on something in the industry most people won't say
- **Trend-jack** — a reaction to a specific news story, report, or market moment
- **Framework/process** — a step-by-step the ICP can implement immediately
- **Monthly update** — wins and learnings from the past month
- **New hire highlight** — a recent hire worth celebrating publicly
- **Customer conversation narrative** — a story from a recent customer interaction with a surprising insight

## Output format

Output the inventory in four sections — one per content pillar. Within each section, number ideas sequentially. Each idea gets its own block with all six fields.

```
IDEA INVENTORY — [CLIENT NAME] — Session [#] — [DATE]
Source: [transcript filename or session type]
Previous sessions checked: [yes/no — if yes, note what was avoided]

INSIGHTFUL
Idea I-1
Funnel: [X]
ICP target: [X]
Source material: "[exact quote or specific moment]"
Content angle: [angle type]
Intent signal: [Save-worthy / Profile-visit-worthy / Both]
[continue for all Insightful ideas]

TACTICAL
Idea T-1
[same block — continue for all Tactical ideas]

ASPIRATIONAL
Idea A-1
[same block — continue for all Aspirational ideas]

PERSONAL
Idea P-1
[same block — continue for all Personal ideas]

Session summary:
- Total ideas: [N]
- Insightful: [N] | Tactical: [N] | Aspirational: [N] | Personal: [N]
Gaps flagged: [pillars with thin material, topic areas running dry, angle types unavailable this session]
Conceptual territory flags: [ideas that stretch outside the client's established content pillars — judgment calls, not automatic cuts; flag them so the user can decide consciously]
```

## How the inventory feeds drafting

When the user selects an idea and says "let's work on this one", read the six fields and immediately enter Phase 1 of the writing-standards skill — state the pillar, funnel stage, and ICP target out loud, then generate 5 hooks grounded in the source material.

The source material is what makes hooks specific: use the exact language, numbers, and details from that field when writing hooks, never a generalised version of the idea. Don't ask the user to re-explain the idea — everything needed to start Phase 1 is in the inventory entry.
