---
name: post-deconstruct
description: >
  This skill should be used when the user wants to reverse-engineer the style of an
  example LinkedIn post — "reverse-engineer this post", "deconstruct this post", "what
  makes this post work", "break down this LinkedIn post", "extract the style", "extract
  the style from this screenshot", or when they upload or screenshot a swipe post to match
  later. It turns one or more example posts into a
  reusable Style Spec (hook, skeleton, rhythm, voice, formatting, CTA, length, and the
  AI-tells to avoid) that the copy-post drafter consumes.
metadata:
  version: "0.1.0"
---

# post-deconstruct

Convert an example post into a **Style Spec** — a structured description of *how* the post is built, so a new post can be drafted in the same style with different content. Capture mechanics, not topic.

## Input

Accept the example as a **screenshot/image, pasted text, or a URL** — use whatever the user gives:

- **Screenshot (best for style work).** Read both the text and the *visual formatting* straight from the image — line breaks, whitespace, emoji, bold, and bullet glyphs (→ vs • vs —) — which pasted text often loses. Have the user expand the post's "…more" before capturing so the body isn't truncated; for a long post, ask for multiple screenshots or a scrolling capture. Ignore UI chrome and engagement counts.
- **URL.** Fetch the post text first; if it can't be fetched, ask for a screenshot or a paste.
- **Pasted text.** Fine, but formatting may be flattened — ask for a screenshot if the visual rhythm matters.

The user may supply several examples from the same author — use all of them.

## Extract the Style Spec

Read the example closely and capture each dimension below. Infer from what's on the page; don't impose generic "best practice."

- **Hook** — the first 1–3 lines. Type (contrarian, curiosity-gap, bold claim/stat, story-open, question, confession/mistake, list-tease, callout), character count, and the pattern as a fill-in template with the specifics blanked out.
- **Skeleton** — the bones in order, e.g. `hook → turn → story → takeaway → CTA`. Name the actual moves this post makes. For the deep structural read (transitions, whitespace map, close pattern), run `post-structure` and fold its blueprint in here.
- **Rhythm** — average sentence length, one-line vs. multi-line paragraphs, how heavily line breaks and white space are used.
- **POV & person** — first-person / third-person; singular "I" vs. "we".
- **Tone** — register (e.g. plain-spoken operator, hype, academic) and **signature moves** (recurring devices: short declaratives, rhetorical questions, numbered lists, em-dash asides).
- **Formatting** — emoji (none/sparse/heavy), list style (arrows, dashes, numbers, none), bold/caps usage, link placement (body vs. first comment).
- **CTA** — style and strength (none / soft engagement / hard ask) and placement.
- **Length** — total character band.
- **Avoid** — the AI-tells and off-brand moves this author clearly does *not* do (feeds `post-qa`).

## Build the fill-in template

The spec above *describes* the style; the template makes it **executable**. Convert the example into a block-by-block skeleton with quantified constraints the drafter fills in — so "match the format" becomes mechanical, not a vibe.

For each block in order, capture: its **intent**, and a **constraint** with real numbers (character ceiling, sentence length, glyph, line breaks). Add a `formatting_map` (line-break rhythm, glyphs, emoji policy) and `rhythm_targets` (avg sentence words, % one-line paragraphs, total length band). Example:

```
template:
  - block: hook        | intent: contrarian claim   | constraint: ≤120 chars, one line, before mobile fold
  - block: whitespace  |                             | constraint: blank line
  - block: reframe     | intent: 1–2 sentence turn   | constraint: short sentences, ~8–12 words
  - block: list        | intent: 3 parallel points   | constraint: "→" glyph, each ≤90 chars
  - block: takeaway    | intent: personal one-liner  | constraint: 1 line
  - block: cta         | intent: stage-dependent     | constraint: soft question OR hard ask
formatting_map: { line_breaks: double-between-blocks, glyphs: ["→"], emoji: none }
rhythm_targets:  { avg_sentence_words: 8–12, pct_one_line_paragraphs: ~60%, total_chars: 700–1100 }
```

The full field list is in `references/style-spec-schema.md`. This template is what `copy-post` fills and what `style-match` scores a draft against.

## Multiple examples

When given several posts, produce one **averaged** spec plus short **variance notes** ("hook length ranges 80–140 chars; sometimes opens on a question, sometimes a stat"). The averaged spec is the default; variance notes tell the drafter where there's room to move.

## Output

Emit the Style Spec **and its fill-in template** in the format in `references/style-spec-schema.md`. Show the user a compact summary, not a wall of YAML.

Offer to save it to the **style library** (`style-library`) so it's reusable across clients — name it after the example's author or theme. If no library is in use, save to `clients/<name>/style-specs/`. Mention the save in one line.

## Hand off

The Style Spec feeds `copy-post` (the drafter matches skeleton + rhythm + voice) and `post-qa` (which checks the draft against `avoid` and the skeleton). It does **not** carry the example's topic or claims forward — only its style.
