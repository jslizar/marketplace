# Watt Design System — full reference

Reusable build reference for any Watt-branded artifact (decks, reports, one-pagers, HTML, social graphics).
Pulled from the canonical brand site so future work matches the system instead of approximating it.

**Source of truth:** https://wattdata.ai/brand
**Brand line:** "Turn the world's data into signal."
**Last synced:** June 2026

> Quick gut-check before shipping anything: is the one accent **electric lime** (never on white)? Are the fonts **Geist**? Are the corners **square** (flat, zero-radius)? If any answer is no, it is off-system.

---

## 01 · Color

Built on a single signature color, electric lime, held by warm neutrals. **Lime earns attention. Neutrals do the work.**

### Foundation
| Token | Hex | Use |
|---|---|---|
| `--lime` | `#D1FF01` | Signature color. Primary CTAs, key metric callouts, logomark, data highlights. |
| `--white` | `#FFFFFF` | Primary light surface. Default page background in light mode. |
| `--dark` | `#222222` | Primary dark surface **and** primary text. |
| `--taupe` | `#A29A7E` | Secondary text, muted UI, warm editorial surface. |

### Extended neutrals
| Token | Hex | Use |
|---|---|---|
| `--gray` | `#ECECEC` | Tertiary surface. Card fills on white, dividers, disabled states. |
| `--black` | `#000000` | High-impact only. Full-bleed hero, print/export. |
| `--sand` | `#CDC4A5` | Soft editorial surface. Pull-quotes, warm content sections. |

### Accent — data-viz & patterns only
| Token | Hex | Use |
|---|---|---|
| `--sage` | `#B8C3AE` | Primary data-viz surface. Calm, report-grade. |
| `--lavender` | `#D7D0F2` | Secondary data-viz. Cool, quiet. |
| `--lavender-pale` | `#E8E4F5` | Lavender pattern pairing. |
| `--coral` | `#FFA087` | Warm accent. Supporting data-viz. |
| `--orange` | `#FF6200` | Loudest warm. High-energy announcements (rare). |

### Invariant color rules
1. **Lime is never on pure white.** Valid lime surfaces: dark, black, taupe, sand, or an accent tier. On a white section, get emphasis from weight, dark, or a sand/dark block — not lime.
2. **Watt's data is always lime. Competitors, baselines, and everything else are always black.** This never flips.
3. **Accents never pair with each other.** An accent pairs only with white, taupe, or sand (never coral + lavender).
4. **Use lime sparingly.** It is a spotlight, not a background.

---

## 02 · Typography

**Geist Sans + Geist Mono. Three weights.** Scale does the work of weight: **400 regular carries the display tier**, **500 medium** structures headings and UI, **600 semibold** is rare and deliberate.

```html
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">
```
Fallbacks: `'Geist', -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif` · `'Geist Mono', ui-monospace, 'SF Mono', monospace`.

| Tier | Font · weight · px |
|---|---|
| Display XL | Geist 400 · 112 |
| Display L | Geist 400 · 88 |
| Display M | Geist 400 · 64 |
| H1 | Geist 500 · 56 |
| H2 | Geist 500 · 44 |
| H3 | Geist 500 · 32 |
| H4 | Geist 500 · 24 |
| H5 | Geist 500 · 18 |
| Body L | Geist 400 · 20 |
| Body M | Geist 400 · 16 |
| Mono M | Geist Mono 400 · 13 (section meta) |
| Mono S | Geist Mono 400 · 11 (axis/caps labels) |

Rules: display tier is **regular 400, not bold** — large and calm. Tighten letter-spacing on big type (~ -0.03em). Mono is for eyebrows, section meta, axis labels, and data values, set uppercase with ~0.13em tracking.

---

## 03 · The Mark

A lightning bolt, solid form. **Lime on dark is canonical.** Dark on lime is the inverse. Taupe on sand is the editorial voice. Nothing else.

- Official lockups: `/brand/logo/lockup-lime-white.svg` (on dark) · `/brand/logo/lockup-lime-dark.svg` (on light). Mark-only stamp also exists.
- Clear space = the height of the mark. Min digital size 20px height. Favicon = simplified single-color 32×32.
- **Don't:** recolor outside lime/dark/taupe · stretch, skew, or rotate · place on any accent background except lime (inverse) · render on busy imagery without a solid backdrop.

---

## 04 · Shape language & layout

This is where Watt reads as Watt. **Flat and square.**

- **Zero border-radius** on surfaces, cards, inputs, sections. The *only* exception is buttons at **6px**.
- **No gradients, no drop shadows, no bevels, no glows.** Borders do the work: 1px `--gray` on white, 1px `--dark` on dark.
- Generous padding (cards 32px).
- **Surface rhythm picks the mood:** white = neutral/default · sand = warm editorial · dark `#222` or black = high-impact. Alternate them down a page.

---

## 05 · Components

- **Buttons.** Primary: `--lime` fill, dark text, Geist 500 · 14px, padding 16×28, radius 6px. Secondary: outlined 1px `--dark`, hover → fill lime.
- **Cards.** Default: white, 1px `--gray` border, **zero radius**, 32px padding. Dark: solid `#222`, white text, for dense/high-impact. Accent: a sage/sand surface for data-viz or featured content.
- **Inputs.** 1px solid `--dark`, radius 0, 14×16 padding, Geist 16, placeholder `--taupe`, focus = lime outline.
- **Nav.** 72px height, `--dark` background, lime mark 28px, mono labels 13px white/70, primary lime button right-aligned.
- **Eyebrow / section meta.** Geist Mono, uppercase, ~0.13em tracking, taupe or dark-42%. Optional bracket style: `[ 01 — COLOR ]`.

---

## 06 · Pattern (the motif)

A repeating **chevron wave** — warm, technical, ownable. Two-tone always, same-temperature always.

Colorways: **lime + white** (launch/loudest) · **lime + taupe** (signature, premium/editorial) · **sage + white** (calm report) · **lavender pair** (quiet support) · **coral + orange** (rare, high energy). Pattern is a standalone surface — never layered under strong type or photography. Preserve wave amplitude/rhythm; scale can flex.

---

## 07 · Data viz

**Two tones. One signature color.** Every chart is **black + lime**. Watt is always the lime one; competitors/baselines are black. No gradients, shadows, or bevels. Geist Sans for the headline number, Geist Mono for values and axes. Surface picks the mood (white neutral, sage report, taupe editorial, dark hero). Reference figure on the brand site: signal density — Watt 145,000 (lime) vs ZoomInfo 400, Apollo 300, Clearbit 250 (black).

---

## 08 · Photography

Infrastructure as metaphor: **transmission towers, power lines** — electricity's literal infrastructure reframed as AI's. Low-angle, sky negative space, high contrast. **No humans. No AI-generated imagery, ever.** If there is no real photo asset, use the chevron pattern instead — do not generate imagery.

---

## 09 · Voice (copy)

"Break it open. Compete your heart out. Real talk." Anti-establishment with purpose: direct about the enemy, warm about who we fight for, bold claims backed by specific numbers.

**Do:** name the enemy ("a handful of companies hoard the world's signals") · name the thing (**Signal Graph**, **Signal Engineer**, not "platform/user") · lead with numbers (145,000 signals on people, 55,000 on businesses — always split people/business) · real talk (admit limits first) · short sentences (two clauses → two sentences).

**Never:** revolutionize, democratize, empower, seamless, next-gen, unlock · em-dashes · "not X, it's Y" contrasts.

For deep founder voice (Jared) and the antislop pass, use the **watt-voice** plugin skills. This section is the brand-level baseline.

---

## 10 · Ready-to-use CSS foundation

The paste-ready stylesheet lives next to this file as `foundation.css`. Read that file and paste its `:root`
tokens and base styles into any new Watt HTML build, then build on top. It includes the color tokens, type
variables, flat zero-radius surfaces and cards, the button (the only 6px-radius element), the black + lime
data-viz bars, and the self-contained chevron-wave motif (no PNG needed).

---

## Sources
- https://wattdata.ai/brand — canonical visual system (color, type, mark, patterns, photography, data-viz, components, voice)
- `watt-voice` plugin — founder voice (Jared), antislop, voice review
