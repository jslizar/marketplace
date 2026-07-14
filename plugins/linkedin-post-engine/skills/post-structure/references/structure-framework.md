# Structure framework

The structural vocabulary for reading and reproducing a post's shape. Counterpart to `hook-framework.md`.

## Skeleton archetypes

| Archetype | Block sequence | Feels like |
|---|---|---|
| **PAS** | problem → agitate → solve | "here's a pain, here's why it's worse than you think, here's the fix" |
| **Story-arc** | setup → tension → turn → resolution → lesson | a short first-person story with a takeaway |
| **Listicle** | hook → N parallel points → takeaway | "5 things I learned…" |
| **Contrarian-reframe** | claim → why the common view is wrong → reframe → proof → CTA | a hot take defended |
| **Before/After** | old world → shift → new world | transformation |
| **How-to** | promise → steps → payoff | tactical, numbered |
| **Observation→insight** | noticed X → what it means → implication | pattern-spotting |
| **Myth-bust** | "everyone says X" → why it fails → what's true instead | corrective |

Name the archetype the example uses; it dictates the block sequence.

## Transitions (how blocks connect)

- **One-line pivot** — a standalone short line that turns the post ("Then everything changed.").
- **Question pivot** — a question that hands off to the next block ("So what actually works?").
- **"But / Here's the thing" turn** — contrast connector.
- **Numbered progression** — 1 / 2 / 3 carrying the reader down.
- **Callback** — the close loops to the hook's phrase.

## Whitespace architecture

LinkedIn rewards a scannable single column. Capture:

- **One-idea-per-line** vs. multi-sentence paragraphs.
- **Double line breaks** between blocks (the most common rhythm) vs. tight blocks.
- **Fragment lines** used for emphasis ("Every time.").
- Where the **fold** falls (~first 2–3 lines on mobile) and what's above it.

## Close patterns

question-to-comments · restate-the-stakes · hard CTA (the Conversion ask) · mic-drop one-liner · loop-back to the hook · "so if you're X, do Y".

Match the example's close type — it's the second-most-copied element after the hook.

## Rhythm metrics (quantify, don't adjective)

- **avg_sentence_words** — count them; report a range.
- **sentence-length variance** — does it mix 3-word punches with 20-word runs, or stay even?
- **pct_one_line_paragraphs** — share of paragraphs that are a single line.
- **total_chars** — the length band.

These numbers become `rhythm_targets` in the template and the tolerances in `style-match`.

## Extraction method

1. Number every line of the example.
2. Tag each line with a role (hook / pivot / point / proof / takeaway / cta / whitespace).
3. Collapse tagged lines into the block sequence.
4. Read transitions between blocks; read the close.
5. Measure the rhythm metrics.
6. Emit the blueprint (see SKILL.md output).

## Reproduction rules

- Preserve **sequence, transitions, whitespace, close, and rhythm**; swap only the content.
- Do not import the example's topic, claims, names, or numbers — those come from context/ICP.
- If the client's Style differs from the example on a fixed constraint (e.g. Author never uses emoji), the Author's Canon wins.
