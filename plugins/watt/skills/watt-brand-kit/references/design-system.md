> Canonical brand catalog: ../../watt-design/references/watt-design-system.md — this file covers the report-renderer specifics.

# Watt Report — design system catalog

Sourced verbatim from the Signal Story Report Template. Everything is driven by
`assets/tokens.css`; `assets/components.css` consumes the tokens; Geist woff2
files in `assets/fonts/` are base64-embedded at build time.

## Typography — Geist

- `--font-sans`: **Geist** (system-grotesque fallbacks). `--font-mono`: **Geist Mono**.
  Both embedded (weights 400/500/600/700/800 sans; 400/500/700 mono).
- Tight scale (816px page): hero title `--type-h1` **28px / 800 / -.025em**; section
  header `--type-h2` **19px / 700 / -.015em**; stat numeral `--type-stat`
  **24px / 800 / -.02em**; body **14px**, line-height **1.55**; lede **13.5px** muted;
  hero subtitle **14px**.
- Mono labels are ALWAYS uppercase: badge 10.5px/.14em, card label 10.5px/.08em,
  market-card title 12.5px/.04em, method 11.5px/lh1.7, footer 10px/.1em.

## Color tokens

| Token | Hex | Role |
|---|---|---|
| `--lime` | `#D1FF01` | signature accent — hero badge, section ticks, hero stat, rule |
| `--ink` | `#222222` | text **and dark surfaces (the hero)**; all card borders |
| `--white` | `#FFFFFF` | page + card surface |
| `--muted` | `#6f6a5d` | lede / secondary text, labels |
| `--hero-sub` | `#cbc7bd` | subtitle text on the dark hero |
| `--hairline` | `#e2e0d8` | footer divider |
| `--taupe` | `#A29A7E` | neutral / hybrid card accent |
| `--gray` | `#ECECEC` | balanced fills / neutral pills |
| `--sand` | `#CDC4A5` | low-sample data |
| `--sage` | `#B8C3AE` | spare neutral-green (optional scale color) |

Diverging index scale (pole A lavender → pole B orange):
`--scale-a2 #8E7CC9` · `--scale-a1 #D7D0F2` · `--scale-mid #ECECEC` ·
`--scale-b1 #FFA087` · `--scale-b2 #FF6200` · `--scale-null #CDC4A5`.
Callout bg `--lavender-pale #E8E4F5`. On-color text: `--on-lime #4a5400`,
`--on-lavender #3b2f63`, `--on-coral #6e2a12`.

## Shape language

Flat. **Square corners** (`--radius: 0`) on every container; pills are the only
rounded element (`--radius-pill: 6px`). **Every stat/card/market card has a 1px
solid black border** (`--border`). Market cards add a 5px colored top border;
the hero has a 7px lime bottom rule; the method note a 1px black top rule.

## Components (class → role)

- **`.sheet`** screen wrapper (bg `#e9e9e9`); **`.page`** fixed **816×1056**,
  white, `overflow:hidden`, drop-shadow on screen, page-break in print.
- **`header.hero`** — dark `#222` block: `.badge` (lime mono pill) + `h1` + `p`
  (hero-sub), 7px lime bottom rule. Page 1 only. Other pages: `.pad` with
  `padding-top:44px`.
- **`h2`** — section header; lime 13px tick via `::before`. **`.lead`** muted intro.
- **`.grid` > `.stat`** (`.stat.lime` = lime hero) > `.n` numeral + `.l` mono label.
- **`.card` > `.label`** + `.comp-row` (`.req` + `.pill.a`) + optional `.note-sm`.
- **`.maprow`** = `.legend-v` (170px vertical legend, 13px `.sw` swatches) +
  `.visual` (the choropleth `svg.us-map` or any chart/image).
- **`.cols` > `.mkt.{a|b|c}`** — colored top border (lavender-deep / taupe /
  orange); `h3` mono; `.pills` with `.pill.{a|b|c}`.
- **`ul.clean`** recs (lavender-deep bullets). **`.note`** callout (lavender-pale,
  4px lavender-deep left border). **`.method`** mono footnote. **`.foot`**
  absolute-bottom mono row, hairline top.

## Layout rules

US Letter, fixed-height pages (no reflow). Keep each page within 1056px — the page
clips overflow, so curate density (hero + ~2 sections of stats/composition +
one visual on page 1; playbook + recs + callout + method on page 2). Headings use
an inline-block tick (not flex) so they don't shrink-wrap under WeasyPrint.
