---
name: graphic-prompt
description: Turn a chosen LinkedIn post into a paste-ready prompt for Claude to build a graphic for it. Use when the user has picked a draft and wants a visual, or says "make a graphic prompt for this post", "create a graphic for this", "design prompt for this post", "turn this into a graphic". Recommends the best graphic type for the post, features only text the post already contains, and emits a self-contained prompt the user pastes into Claude to build the graphic as an artifact.
---

# Graphic prompt

Produce a single, self-contained prompt that the user pastes into a fresh Claude to build a graphic for a chosen post. Claude builds it as an artifact (HTML/SVG), so the prompt must stand entirely on its own — the target Claude has none of this run's context.

You produce the PROMPT, not the graphic.

## Inputs

- **The selected post** — the winning draft from the pipeline (its `picked:` candidate), or the post the user pasted/pointed at when invoked standalone. If it's ambiguous which post, ask which one; never guess.
- **Client context** (`clients/<slug>/context.md`) if it exists — for any visual or voice cues. Optional.

## Steps

1. **Recommend the graphic type for THIS post.** Read the post and pick the type its content actually wants, then say why in one line:
   - one number carrying the post → **stat card**
   - a sharp line or contrarian claim → **quote card**
   - a step list, framework, or numbered body → **carousel** (one beat per frame) or a **checklist card** if short
   - a before/after or comparison → **split card**
   - a process or relationship → **simple diagram**
   The user can override the type.

2. **Pull the featured content from the post, verbatim.** The exact hook, stat, or pull-quote to render — lifted word-for-word from the selected post. HARD RULE: the graphic may feature ONLY text, numbers, and claims the post already contains. Never invent a stat, a tagline, a logo, or a fact for the visual. Carousel frames come from the post's existing beats, not new material. If a type would need content the post doesn't have, pick a different type or say what's missing.

3. **Brand cues.** If the client context carries visual notes (colors, typography, do/don'ts) or a clear voice, fold them in. Otherwise specify clean, neutral, legible defaults and say the graphic uses defaults because no brand system is on file. (For Watt posts, point the user at the `watt` plugin's design system instead of inventing one.)

4. **Write the prompt.** A self-contained brief for Claude to build the graphic as an artifact. Include, in plain prose:
   - **What to build** — the graphic type and that it should be a self-contained artifact (inline HTML/SVG), text rendered as real text (not an image of text).
   - **Dimensions** — LinkedIn-appropriate: 1080x1080 square or 1080x1350 portrait for a single frame; a carousel is N frames at 1080x1350. State the exact size.
   - **Exact copy** — the verbatim text to render, labeled by role (headline, stat, caption, per-frame text for carousels). Nothing outside this may appear as a claim.
   - **Layout & hierarchy** — what leads, what supports, reading order.
   - **Color & type direction** — from brand cues or the stated neutral defaults.
   - **Constraints** — legible at feed thumbnail size, high contrast, generous margins, no fabricated logos/faces/brands, no lorem text, real text only.

5. **Save and present.** Save the prompt via `run-log` to `clients/<slug>/drafts/<lane>/YYYY-MM-DD-<slug>-graphic.md` (frontmatter `type: graphic-prompt`, and `for:` pointing at the post file it came from). Then show the prompt in a copy-ready block with a one-line note on the type you recommended and why.

## Rules

- The prompt stands alone. Assume the target Claude sees only what you paste — restate the copy in full; don't reference "the post above."
- Feature only what the post says. This is the same Canon/Proof discipline as drafting: a graphic that adds a claim the post doesn't make is invalid.
- One post, one prompt. For a carousel, it's still one prompt describing all frames.
- Don't build the graphic here or open an artifact — hand back the prompt for the user to run in Claude.
