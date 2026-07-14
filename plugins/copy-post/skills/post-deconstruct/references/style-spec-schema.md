# Style Spec schema

The output of `post-deconstruct`. Store as markdown with this YAML block; show the user a compact prose summary, not the raw block.

```yaml
source: <author or theme; URL/paste note>
examples_used: <n>

hook:
  type: contrarian | curiosity-gap | bold-claim | story-open | question | confession | list-tease | callout
  pattern: <the hook as a fill-in template, e.g. "After {timespan}, I just finished — {artifact}">
  length_chars: <int>          # target the example's range; mobile fold ≈ 140

skeleton: [hook, turn, story, takeaway, cta]   # the actual moves, in order

rhythm:
  avg_sentence_len: <short | medium | long, ~N words>
  paragraphs: one-line | multi-line | mixed
  whitespace: light | medium | heavy

pov: first-person-singular | first-person-plural | third-person

tone:
  register: <e.g. plain-spoken operator>
  signature_moves: [short declaratives, rhetorical questions, numbered lists, em-dash asides]

formatting:
  emoji: none | sparse | heavy
  lists: none | dashes | arrows | numbers
  emphasis: none | bold | caps
  link_placement: body | first-comment | none

cta:
  style: <e.g. soft question to comments>
  strength: none | soft | hard
  placement: body-end | first-comment

length_band_chars: <min>-<max>

avoid: [em-dash overuse, "not X, it's Y" antithesis, throat-clearing, hashtag stuffing, ...]

# The executable part — what the drafter fills and style-match scores:
template:
  - {block: hook,       intent: contrarian-claim,   constraint: "<=120 chars, one line, before fold"}
  - {block: whitespace, intent: "",                 constraint: "blank line"}
  - {block: reframe,    intent: 1-2-sentence-turn,  constraint: "short sentences, ~8-12 words"}
  - {block: list,       intent: 3-parallel-points,  constraint: "arrow glyph, each <=90 chars"}
  - {block: takeaway,   intent: personal-one-liner, constraint: "1 line"}
  - {block: cta,        intent: stage-dependent,    constraint: "soft question | hard ask"}

formatting_map:
  line_breaks: double-between-blocks | single | none
  glyphs: ["→", "•", "—"]            # the actual bullet/separator glyphs used
  emoji: none | sparse | heavy
  caps_or_bold: none | sparing

rhythm_targets:
  avg_sentence_words: <range, e.g. 8-12>
  pct_one_line_paragraphs: <e.g. ~60%>
  total_chars: <band, e.g. 700-1100>

variance_notes: <only when multiple examples; where the author varies>
```

## Field notes

- **hook.pattern** is what the drafter fills — the example's hook as a template with the specifics blanked out. Candidates keep the type and pattern; they vary the entry point (see `skills/copy-post/references/hook-framework.md`).
- **skeleton** must name the post's real structure, not a generic template. If the post is a single unbroken story with no list, say so.
- **avoid** is descriptive of this author (what they never do), and becomes a checklist in `post-qa`. Always include the universal AI-tells from `skills/post-qa/references/ai-tells.md`.
- Keep topic, claims, and named entities **out** of the spec — those come from the client context and ICP research, not the example.
- **template / formatting_map / rhythm_targets** are the executable layer: the drafter fills the blocks in order honoring each constraint, and `style-match` scores a draft against them. Use quantified constraints (real character counts, glyphs, word ranges), not adjectives.
