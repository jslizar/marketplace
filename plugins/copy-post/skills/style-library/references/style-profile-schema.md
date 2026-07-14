# Style Profile schema

`styles/<slug>/profile.md` — a Style Spec + template compiled from all examples in the style, plus metadata and variance. This is what the drafter loads and `style-match` scores against.

```markdown
# Style Profile — <name>

meta:
  slug: <style-slug>
  author: <who, or "house">
  n_examples: <int>
  sources: [<links or filenames>]
  tags: [contrarian, story-led, b2b, ...]
  confidence: high | medium | low   # low if n_examples == 1

# --- averaged Style Spec (see post-deconstruct/style-spec-schema.md) ---
hook: { types_seen: [...], patterns_seen: [...], length_chars: <band> }
skeleton_modal: [hook, reframe, list, takeaway, cta]
skeleton_alternates: [[hook, story, takeaway, cta], ...]
rhythm_targets: { avg_sentence_words: <band>, pct_one_line_paragraphs: <~%>, total_chars: <band> }
formatting_map: { line_breaks: ..., glyphs: [...], emoji: ... }
cta: { styles_seen: [...], strength: ... }
avoid: [ <union of all examples' avoid lists> ]

# --- executable template (the modal skeleton, quantified) ---
template:
  - {block: hook, intent: ..., constraint: ...}
  - ...

variance:
  - "hook opens on a question OR a stat"
  - "list length 3–5"
  - "sometimes drops the takeaway block"
```

## How `variance` is used

- The **drafter** may move within the variance without penalty (e.g. pick either documented hook opener).
- `style-match` **widens its tolerance** to the variance: a draft isn't dinged for a choice the profile lists as legitimate.
- Anything **outside** the variance and the modal template is a miss.

## Confidence

- `n_examples == 1` → `confidence: low`; the profile equals that one post's spec, no real variance yet.
- More examples → tighter modal template + honest variance → `high`.

## Rules

- Style only — no topics, claims, or named entities.
- Regenerable: deleting `profile.md` and recompiling from `examples/` must reproduce it.
