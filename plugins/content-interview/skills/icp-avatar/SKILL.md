---
name: icp-avatar
description: Build a deep emotional ICP avatar for a client. Use when the user says "build the ICP avatar", "create the avatar for [client]", "who is [client]'s ideal customer really", "build the persona", or when interview-kit or idea-inventory needs the psychological profile of a client's ideal customer. Produces a full psychological profile (pains, fears, desires, limiting beliefs, trigger moments, painful questions, failed solutions, identity transformation) saved to clients/<slug>/icp-avatar.md.
---

# ICP avatar builder

Build the avatar: a deep psychological profile of the client's ideal customer. Not just demographics and pain points — the emotional texture of their daily life, their failed attempts at solving the problem, how their identity would transform with the solution, and the language they use internally but would never say out loud.

The avatar is built once per client, saved to `clients/<slug>/icp-avatar.md`, and feeds every downstream task: idea extraction, hook writing, and post drafting. It is the emotional foundation that makes content feel like it's reading the ICP's mind.

## Inputs

Read the client's brief or `context.md` before starting. You need three things:

- The client's product / service — what they do and how it works
- The ICP description — job title, company type, and any details about who they are
- The Transformation Statement — what the ICP wants to become and what adjacent topics they care about

Don't ask for additional input; everything needed is in the client material. Where it's sparse, use your knowledge of the industry and ICP type to synthesise — but flag any section that is primarily inference rather than directly stated by the client, so the user can review and correct it.

## The five-step synthesis

Work through these five steps in sequence. Don't skip steps — the output of each informs the next.

### Step 1 — Build the Core Avatar

Using the ICP description and transformation statement, build a detailed psychological profile. Give the avatar a real first name to use throughout.

Include:

- **Demographics** — job title, company size/type, years of experience, where they are in their career
- **Psychographics** — how they think about their work, what they read, what they follow, how they make decisions
- **Values** — what they care about most professionally and personally
- **Pains (at least 5)** — current manifestations of their problem. Specific and emotionally resonant: what is actually happening in their day right now because this problem exists.
- **Fears (at least 5)** — future manifestations of their problem. What they are afraid will happen if nothing changes.
- **Desires (at least 5)** — what they genuinely want, stated in their own internal language
- **Limiting Beliefs (at least 5)** — beliefs keeping them stuck. Things they tell themselves that prevent them from solving the problem.
- **Trigger Moments (at least 5)** — specific daily or weekly events that make the pain feel acute. The moment they open Slack and see that message. The moment that question gets asked in a meeting.
- **Painful Questions (at least 5)** — questions they ask themselves privately but would never admit to others. The 2am thoughts.
- **Core Problem** — the single root cause underneath all the symptoms. Not a feature request. The fundamental thing that is wrong.
- **Ultimate Desire** — the deepest version of what they want. Not the surface goal — the identity-level transformation they're reaching for.

### Step 2 — Map the Failed Solutions

What solutions has [NAME] already tried for their core problem? For each, capture:

- What the solution was
- Why they tried it
- Why it failed or disappointed them
- Their frustration with it, written as a direct internal quote from [NAME]

Include at least 4–5 failed solutions. These are critical for content: they tell you exactly what the ICP is tired of hearing, and what makes the client's approach feel different.

### Step 3 — Identity Transformation

If the client's solution completely solved [NAME]'s problem, how would their identity transform? List at least 10 changes per category:

- **How [NAME] would see themselves differently** — internal identity shifts: confidence, self-perception, relationship with their work
- **How others would perceive [NAME] differently** — external signals: how their team sees them, how peers see them, what their reputation becomes

These are not feature benefits. They are identity-level outcomes — what makes content feel aspirational rather than just informational.

### Step 4 — Before and After Daily Life

Compare [NAME]'s day-to-day life before and after the solution:

- **10 unpleasant things [NAME] no longer has to do** — with how each one makes them feel now. Be specific: not "spend time on manual tasks" but "manually reconcile the spreadsheet every Friday afternoon while everyone else has already left."
- **10 new, pleasant things [NAME] gets to do** — with how each one makes them feel. The positive version of their day, in specific detail.

### Step 5 — Comprehensive Avatar Summary

Synthesise Steps 1–4 into a single summary — the thing to read before writing any post for this client. It provides the emotional context that makes hooks and bodies feel written for a specific human, not a job title.

The summary must:

- Capture all the deep emotional drivers that motivate people like [NAME] to take action
- Include the most resonant quotes, trigger moments, and painful questions
- Be written so anyone reading it could immediately write content that makes [NAME] feel seen
- Be detailed enough to be genuinely useful, but scannable — headers and short sections

## Output format

Save the full avatar to `clients/<slug>/icp-avatar.md`, structured exactly as:

```
ICP AVATAR — [CLIENT NAME]
Built from: [source file]
Flagged as inference (not directly stated by client): [list any sections]

Avatar: [NAME]
[One-paragraph introduction — who [NAME] is, what they do, what their life looks like right now]

Demographics & Psychographics
[Concise profile]

Core Problem
[One clear statement of the root cause]
Ultimate Desire
[One clear statement of the identity-level transformation they want]

Pains
[Numbered list — specific and emotionally resonant]
Fears
[Numbered list]
Desires
[Numbered list]
Limiting Beliefs
[Numbered list]
Trigger Moments
[Numbered list — specific daily/weekly events]
Painful Questions
[Numbered list — internal questions they'd never admit to]

Failed Solutions & Frustrations
[For each solution: what it was, why it failed, direct quote from [NAME]]

Identity Transformation
How [NAME] sees themselves after
[Numbered list — 10 items]
How others see [NAME] after
[Numbered list — 10 items]

Before and After Daily Life
Things [NAME] no longer has to do
[Numbered list — 10 items with emotional note for each]
Things [NAME] gets to do now
[Numbered list — 10 items with emotional note for each]

Comprehensive Summary
[Full synthesis — everything needed to write resonant content for this ICP: emotional drivers, key language, the specific texture of this person's world. Scannable, short sections, as long as it needs to be.]

Content Language Bank
[The most useful phrases, questions, and emotional triggers, pulled out as a quick-reference list for hook writing and post drafting:
- 5–8 phrases in [NAME]'s own words that could anchor a hook
- 3–5 trigger moments specific enough to open a post with
- 3–5 painful questions specific enough to use as a hook or post opener]
```
