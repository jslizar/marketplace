# Style-match rubric

How to score a draft's fidelity to the target style. Weighted 0–100. Default ship threshold: **80**.

| Dimension | Weight | Pass when | How to measure |
|---|---:|---|---|
| **Hook type** | 20 | Draft's hook is the target type (or a variance alternate) | Classify the draft hook; compare to `hook.types_seen` |
| **Block sequence** | 25 | Draft follows the modal skeleton or a documented alternate | Tag draft blocks in order; diff against `template` sequence |
| **Length band** | 10 | Total chars within `total_chars` band | Count characters |
| **Rhythm** | 20 | avg sentence words within band **and** one-line-paragraph % within ±15 pts | Count words/sentence; count one-line paragraphs |
| **Formatting** | 15 | Same glyph set + emoji policy + line-break rhythm | Compare glyphs, emoji, break pattern to `formatting_map` |
| **Open/close** | 10 | Hook under the mobile fold (~140 chars) **and** close matches the target close pattern | Measure first line; classify the close |

## Scoring

- Each dimension is scored **full / half / zero** (clean pass / close-but-off / clear miss), times its weight.
- Sum → 0–100.
- `>= 80` → **SHIP**. `65–79` → revise the flagged dimensions. `< 65` → the draft isn't in the style; rebuild from the template.

## Tolerances

- Widen any dimension to the profile's **variance** (a listed alternate hook type or skeleton is a pass).
- Rhythm is a band, not a point — don't over-fit to a single example's exact averages; ±15 percentage points on one-line ratio, ± the stated word range.
- Formatting: the **glyph** (→ vs • vs —) and **emoji policy** matter most; exact spacing is a half-miss at worst.

## Fixes

For every miss, return a **specific, mechanical fix** the drafter can apply without rethinking the content:

- rhythm → "split sentences in blocks 3–4 to ~10 words; convert 2 paragraphs to one-liners"
- formatting → "replace `•` with `→`"
- block_sequence → "add the missing takeaway block before the CTA"
- open_close → "cut the hook to ≤140 chars; end on a question to comments"

Never rewrite the content to hit a score — only adjust structure/format. If a miss can't be fixed without changing meaning, flag it for the user.
