# watt

Watt voice, brand, and signal-story toolkit — a merger of three plugins
(`watt-voice`, `watt-design`, `watt-signal-story`) into one. Draft and de-slop
copy in the founder voice, apply the Watt design system to any artifact, and
turn Watt audience data into branded signal-story reports and social cards.

## Skills

| Skill | What it does |
|---|---|
| `watt-voice-match` | Rewrite or draft copy in Jared Parker's (CEO) voice — lanes, calibration, canonical facts. |
| `watt-antislop` | Strip AI tells (em-dashes, "not X, it's Y", jargon, adverbs, throat-clearing). The canonical antislop ruleset for every skill here. |
| `watt-voice-review` | Audit a draft against Jared's voice: severity-ranked flags with before/after fixes, plus a ship verdict. |
| `watt-design` | Apply the Watt visual brand (electric lime + warm neutrals, Geist) to decks, pages, graphics, and data-viz. |
| `dissect` | Read an article or trend piece, extract candidate audiences, compare them in Watt, and find the surprising-audience story. |
| `signal-story` | Turn Watt audience data into a two-page branded HTML/PDF report plus a square social summary card. |
| `watt-brand-kit` | The report-renderer design system: tokens/components CSS, Geist fonts, US choropleth, and the PDF/PNG render scripts. |

## Commands

| Command | What it does |
|---|---|
| `/watt:post` | Full voice pipeline: watt-voice-match → watt-antislop → watt-voice-review, returning a ship-ready post and verdict. |
| `/watt:deslop` | One-pass de-slop of any text using the watt-antislop ruleset. |

## Requirements

- **watt MCP connector** — `dissect` and `signal-story` pull audience data
  (trait search, entity find/enrich, lifts) from the Watt MCP tools.
- **Python 3** with **WeasyPrint or Playwright/Chromium** — `signal-story`
  renders the report PDF (Chromium first, WeasyPrint fallback) and the square
  card PNG (Playwright).
- The `/watt:audience` and `/watt:explore` commands mentioned inside
  `signal-story` and `dissect` come from the separate Watt data-platform
  plugin — they are **not bundled** here. When that plugin is absent, the
  skills can call the watt MCP tools directly instead.
