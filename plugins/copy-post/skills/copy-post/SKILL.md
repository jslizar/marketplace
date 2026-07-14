---
name: copy-post
description: >
  This skill should be used when the user wants to draft a LinkedIn post that matches an
  example's style for a client or their own account — "draft a LinkedIn post for a
  client", "write a post like this example", "reverse engineer this post and write one
  like it", "turn this into a LinkedIn post", "make an ABM post for my ICP", "match this
  post's style". It is the front door of the LinkedIn
  Post Engine: it loads the client context, reverse-engineers the example, classifies the
  funnel stage, optionally researches the ICP, drafts candidates in the matched style,
  de-slops each draft to strip AI tells, and runs the QA gate before presenting them. Defaults to 3 candidates.
metadata:
  version: "0.1.0"
---

# copy-post

Front door and drafter. Run the full loop, or pick up wherever the user already is (they may have a style spec or context loaded). Produce posts that match an example's *style* while carrying the *client's* substance.

## Inputs to gather

- **Example post** to match — screenshot, paste, or URL → handed to `post-deconstruct`. A screenshot is ideal; it preserves the visual formatting.
- **Client** (slug, e.g. `aicro`, or `self`) → handed to `context-loader`.
- **Topic / intent** for the new post.
- **Funnel stage** if the user knows it; otherwise `funnel-classify` infers it.
- **ABM?** If the goal is "this style, aimed at my ICP" or a named account → run `icp-research`.

Ask only for what's missing. If the user gives an example and a client, proceed.

## The loop

1. **Context** — run `context-loader` for the client. Note the **Author** (the only voice), Pillars, Conversion ask, Proof status, and Canon **Hard constraints**.
2. **Style** — get the fill-in **template**. If the user names a saved style (or one fits), load it with `style-library`. Otherwise run `post-deconstruct` (which calls `post-structure`) on the example to build the Style Spec + template, and offer to save it to the library.
3. **Classify** — run `funnel-classify` to get the stage directive (job, structure, CTA strength, proof level).
4. **Research (if ABM)** — run `icp-research` to get the target company set + per-account angle. Decide with the user: one segment-level post, or a batch (one per account).
5. **Draft** — produce **3 candidates** by filling the template (`references/drafting-framework.md`, `references/hook-framework.md`, and the structure blueprint from `post-structure`). Speak as the Author; stay on a Pillar; obey the stage directive.
6. **De-slop** — rewrite every candidate with `references/deslop-pass.md` before anything else sees it. An active rewrite, not a flag pass: kill every em-dash, every "not X, it's Y" contrast, throat-clearing, hollow adverbs, jargon, false agency, and vague declaratives. Preserve any move the Style Spec marks as an intentional signature (deliberate staccato, fragments doing rhythmic work).
7. **Match** — run `style-match` on each candidate. Below the threshold, apply its fixes and re-draft — at most **2 re-draft cycles per candidate**; if it still scores below threshold, present the best version anyway with its score and remaining misses labeled, never a silent drop.
8. **QA** — run `post-qa` on each surviving candidate (brand voice, Canon, Proof, AI-tells). Fix flags in place. If a candidate fails a hard block that can't be fixed with what you have, drop it and say so; if ALL candidates fail, present what failed and what's missing (usually Proof or Canon gaps) and ask — never silently return fewer candidates than promised.

## Output

Present **3 labeled candidates**. For each: the post text, its **style-match score**, hook character count, the stage, and one line on what makes it different from the others. Then a **recommended pick** and why. If a candidate needs a link, put the link in a **first comment** (links in the body suppress reach) and show that comment.

For an ABM batch, output one post per target account, each tagged with the company and the angle used.

## Hard guardrails

- **Voice:** write only as the Author named in context. Never introduce a second voice.
- **Proof:** if Proof is "None on record", do not invent results — pivot to credibility/process (see funnel map). 
- **Canon:** never break a Hard constraint (e.g. "no generic GTM advice without a proptech angle").
- **Hook:** keep the first line under the mobile fold (~140 chars) so it lands before "…see more".
- **Style, not topic:** match the example's mechanics; never reuse the example's claims, names, or story as if they were the client's.

These are enforced again by `post-qa` — but build them in from the first draft.
