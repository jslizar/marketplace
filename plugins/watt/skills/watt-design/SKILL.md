---
name: watt-design
description: >
  Apply the Watt visual brand and design system when creating, formatting, or restyling any Watt-branded
  artifact — slide decks, reports, one-pagers, HTML pages, landing pages, social graphics, charts, or data-viz.
  Triggers when the user asks to build or format something "for Watt", "on-brand", "Watt-branded", a
  "Watt deck / report / one-pager / page", wants Watt colors, fonts, or styling applied, says "make this look
  like Watt" or "format this for Watt", or types /watt-design. Loads the full system: electric-lime-plus-warm-
  neutral color rules, Geist typography, flat zero-radius shape language, component specs, the chevron-wave
  pattern, black-and-lime data-viz, and brand voice.
---

# Watt Design System

Apply this system to any Watt-branded artifact so output matches the brand instead of approximating it.
Source of truth: https://wattdata.ai/brand · Brand line: "Turn the world's data into signal."

When this skill is active, treat the rules below as binding. For exhaustive detail (every token, every
component spec, the full type scale) read `references/watt-design-system.md`. When building anything in HTML,
read and paste from `references/foundation.css` — do not re-derive the CSS from memory.

## Gut-check before shipping anything

Four questions. If any answer is "no," it is off-system — fix it before delivering:

1. Is the one accent **electric lime `#D1FF01`**, and is it **never on pure white**?
2. Are the fonts **Geist Sans + Geist Mono**?
3. Are the corners **square** — zero border-radius everywhere except buttons (6px)?
4. Are there **no gradients, drop shadows, bevels, or glows**? Borders do the work.

## Color — lime earns attention, neutrals do the work

Foundation tokens: `--lime #D1FF01` (signature — primary CTAs, key metric callouts, logomark, data
highlights) · `--white #FFFFFF` · `--dark #222222` (primary dark surface **and** primary text) ·
`--taupe #A29A7E` (secondary text, warm editorial surface).
Extended neutrals: `--gray #ECECEC` (card fills on white, dividers) · `--black #000000` (high-impact /
print only) · `--sand #CDC4A5` (warm editorial surface, pull-quotes).
Accents — **data-viz and patterns only**: `--sage #B8C3AE` · `--lavender #D7D0F2` ·
`--lavender-pale #E8E4F5` · `--coral #FFA087` · `--orange #FF6200` (rare).

Invariant color rules — never break these:

1. **Lime is never on pure white.** Valid lime surfaces: dark, black, taupe, sand, or an accent tier. On a
   white section, get emphasis from weight, dark, or a sand/dark block — not lime.
2. **Watt's data is always lime; competitors, baselines, and everything else are always black.** Never flips.
3. **Accents never pair with each other.** An accent pairs only with white, taupe, or sand (never coral + lavender).
4. **Use lime sparingly.** It is a spotlight, not a background.

## Typography — Geist, three weights, scale does the work

Load: `https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap`.
Fallbacks: `'Geist', -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif` and
`'Geist Mono', ui-monospace, 'SF Mono', monospace`.

- **Display tier is regular 400, not bold** — large and calm (64–112px). Tighten letter-spacing on big type (~ -0.03em).
- **500 medium** structures headings and UI (H1 56 → H5 18). **600 semibold** is rare and deliberate.
- Body 400 (16–20px). **Geist Mono** is for eyebrows, section meta, axis labels, and data values — set
  **uppercase with ~0.13em tracking**. Optional eyebrow bracket style: `[ 01 — COLOR ]`.

Full px scale is in the reference.

## Shape & layout — flat and square (this is where Watt reads as Watt)

- **Zero border-radius** on surfaces, cards, inputs, sections. The only exception is **buttons at 6px**.
- **No gradients, shadows, bevels, or glows.** Borders do the work: 1px `--gray` on white, 1px `--dark` on dark.
- Generous padding (cards 32px).
- **Surface rhythm sets the mood:** white = neutral/default · sand = warm editorial · dark `#222` or black =
  high-impact. Alternate surfaces down a page.

## Components (quick spec — full detail in reference)

- **Buttons.** Primary: `--lime` fill, dark text, Geist 500 · 14px, padding 16×28, radius 6px. Secondary:
  outlined 1px `--dark`, hover → fill lime.
- **Cards.** White, 1px `--gray` border, zero radius, 32px padding. Dark variant: solid `#222`, white text.
- **Inputs.** 1px solid `--dark`, radius 0, 14×16 padding, Geist 16, placeholder `--taupe`, focus = lime outline.
- **Nav.** 72px height, `--dark` background, lime mark 28px, mono labels 13px white/70, primary lime button right.
- **Eyebrow / section meta.** Geist Mono, uppercase, ~0.13em tracking, taupe or dark-42%.

## The mark

Lightning bolt, solid form. **Lime on dark is canonical**; dark on lime is the inverse; taupe on sand is the
editorial voice. Clear space = the height of the mark. Min digital height 20px. Never recolor outside
lime/dark/taupe, never stretch/skew/rotate, never place on a non-lime accent background, never render on busy
imagery without a solid backdrop.

## Data-viz — two tones, one signature color

Every chart is **black + lime**. **Watt is always the lime one; competitors/baselines are black.** No
gradients, shadows, or bevels. Geist Sans for the headline number, Geist Mono for values and axes. Surface
picks the mood (white neutral, sage report, taupe editorial, dark hero).

## Pattern — the chevron wave

A repeating chevron wave, **two-tone always, same-temperature always**. Colorways: lime + white (loudest) ·
lime + taupe (signature/premium) · sage + white (calm report) · lavender pair (quiet) · coral + orange (rare).
It is a standalone surface — never layer it under strong type or photography. A self-contained CSS version
(no PNG) is in `references/foundation.css`.

## Photography

Infrastructure as metaphor: transmission towers, power lines — low-angle, sky negative space, high contrast.
**No humans. No AI-generated imagery, ever.** If there is no real photo asset, use the chevron pattern
instead — do not generate imagery.

## Voice (brand baseline)

"Break it open. Compete your heart out. Real talk." Anti-establishment with purpose.

- **Do:** name the enemy ("a handful of companies hoard the world's signals") · name the thing
  (**Signal Graph**, **Signal Engineer** — not "platform/user") · lead with numbers (145,000 signals on
  people, 55,000 on businesses — always split people/business) · admit limits first · short sentences.
- **Never:** revolutionize, democratize, empower, seamless, next-gen, unlock · em-dashes · "not X, it's Y"
  contrasts.

For deep founder voice (Jared) and the antislop pass, the **watt-voice** plugin skills go further; this is the
brand-level baseline.

## How to apply

1. Identify the artifact's surface/mood (white neutral, sand editorial, or dark/black high-impact) and build
   the palette from that surface.
2. For HTML, start from `references/foundation.css` — paste the `:root` tokens and base styles, then build on
   them. Never invent hexes or fonts.
3. Place lime only on a valid surface, and only where one thing should win attention.
4. Keep everything flat and square; let borders and surface changes create structure.
5. Run the four-question gut-check before delivering. Report any deliberate exceptions.
