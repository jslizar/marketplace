---
name: watt-brand-kit
description: >
  The Watt signal-story design system — color tokens, typography, the reusable
  HTML/CSS components (masthead, stat cards, signal-composition box, US
  choropleth + legend, cluster columns, callout, method note, footer), and the
  scripts that color the map and render HTML to PDF. Use when building any
  on-brand Watt deliverable, or when the user wants to re-skin or restyle a
  signal story — "change the Watt brand colors", "swap the accent / fonts",
  "adjust the map scale", "use the Watt design system". The signal-story skill
  depends on this kit; load it directly only to restyle or to reuse the
  components for a new format.
---

# Watt Brand Kit

The visual layer for Watt signal stories. Recovered from the Pizza Hut
reference. Other skills (e.g. `signal-story`) compose these pieces; this skill
owns the **look** and the **map**.

## What's here

```
assets/
  tokens.css        CSS variables (verbatim from the report template): Geist type
                    scale, palette, diverging scale, square/flat shape, geometry
  components.css    every component class (dark hero, square 1px-black cards, …)
  fonts/            Geist + Geist Mono woff2 (base64-embedded at build time)
  us-states.svg     base US map, Albers projection with AK/HI insets,
                    one <path id="XX"> per state (USPS code), viewBox 0 0 975 610
scripts/
  choropleth.py     color the base map from a {state: index} table
  render_pdf.py     HTML -> PDF (Chromium if present, else WeasyPrint)
  gen_base_map.js   (authoring only) regenerate us-states.svg from us-atlas
references/
  design-system.md  the full token + component catalog
```

## Re-skinning

All color, type, and rhythm live in **`assets/tokens.css`**. To restyle every
signal story at once, edit a token there — e.g. change `--lime` for a different
accent, or the `--map-*` ramp for a different index palette. Never hardcode
colors into a story spec; change the token. After editing, re-render the story.

## Coloring the map

`choropleth.py` turns a per-state index into a colored SVG.

```python
import sys; sys.path.insert(0, "scripts")
from choropleth import colorize, legend_items
svg  = colorize({"FL":106, "WA":91, "TX":96})   # omitted states render "low sample"
rows = legend_items()                             # [{"label","color"}, …] for the legend
```

Values are bucketed by `DEFAULT_SCALE` (≥104 purple, 101–103 lavender, 99–100
grey, 96–98 salmon, ≤95 orange). Pass a custom `scale=[…]` to re-bucket for a
different index. The map is US states only (50 + DC).

## Rendering to PDF

`render_pdf.py` picks the best available backend and prints which it used. The
page size (US Letter) and margins come from the `@page` rule in `components.css`,
so output is identical across backends. WeasyPrint is the reliable default;
Chromium (via Playwright) gives the highest fidelity if installed.

## Component reference

See `references/design-system.md` for the exact tokens, every component's class
names and required HTML structure, and the two-page layout rules.
