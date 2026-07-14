---
name: post-structure
description: >
  This skill should be used when the user wants to copy or analyze the structural shape of
  a LinkedIn post — "map the structure of this post", "what's the skeleton", "copy the
  format / structure", "match the paragraph structure", "break down how this post is
  built", or when post-deconstruct or the drafter needs the structural layer. It extracts a
  structural blueprint from an example (skeleton archetype, block sequence, transitions,
  line-break map, close pattern, rhythm) and serves as the structural reference for
  drafting — the counterpart to the hook framework.
metadata:
  version: "0.1.0"
---

# post-structure

Own the **structure** — everything that makes a post *look and move* like the example, apart from the hook's wording: the block sequence, the transitions between them, the line-break/whitespace shape, the sentence rhythm, and the close. This is half of "copy the format" and gets equal weight with the hook.

## When it runs

- Inside `post-deconstruct` — supplies the structural layer of the Style Spec + template.
- Standalone — "map the structure of this post" / "copy this format."
- Referenced by the drafter (`copy-post`) when building the body.

## Extract a structural blueprint

Map the example **line by line** to structural roles, then abstract:

1. **Archetype** — which skeleton pattern is this? (see `references/structure-framework.md`: PAS, story-arc, listicle, contrarian-reframe, before/after, how-to, observation→insight, myth-bust.)
2. **Block sequence** — the ordered blocks (`hook → reframe → list(3) → takeaway → cta`), each tagged with its role.
3. **Transitions** — how it moves between blocks (one-line pivot, question pivot, "But…" turn, numbered progression).
4. **Whitespace map** — line-break rhythm: one-idea-per-line? double breaks between blocks? the scannable single-column shape LinkedIn rewards?
5. **Rhythm** — average sentence length (words), sentence-length variance, and the % of one-line paragraphs.
6. **Close** — the ending move (question-to-comments, restate-the-stakes, hard CTA, mic-drop one-liner, loop-back to the hook).

## Reproduce it

To copy the structure with new content: keep the **block sequence, transitions, whitespace map, and close pattern**; refill each block with the client's substance; hold the rhythm targets (sentence length, one-line ratio, total length band). Copy the *shape*, never the example's words or claims.

## Output

Emit a compact structural blueprint that folds into the `post-deconstruct` template (the `skeleton`, `formatting_map`, and `rhythm_targets` fields) and that `style-match` scores against:

```
archetype: <name>
blocks: [hook, reframe, list-3, takeaway, cta]
transitions: [one-line-pivot, "but"-turn]
whitespace: one-idea-per-line, double-break-between-blocks
rhythm: { avg_sentence_words: 8-12, pct_one_line_paragraphs: ~60% }
close: question-to-comments
```

Keep it structural — no topic, no claims.
