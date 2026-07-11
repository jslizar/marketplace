# ABM Engine

Find viral ABM post formats, research your client and their market, propose angles, and draft posts.

## Skills

| Skill | What it does |
|---|---|
| `abm` | Front door — runs the full pipeline: formats → format pick (3 of 15) → client → angles → drafts |
| `abm-scout` | Works from the local swipe library (kept fresh by your scheduled refresh task), scouts new formats via Apify/web, deconstructs winners into format specs |
| `abm-client` | Builds/refreshes a client context file from Virio settings, HubSpot/Attio, and live web research |
| `abm-angles` | Crosses formats × client × market moment into ranked, scored angles |
| `abm-draft` | Drafts 2–3 de-slopped candidates from a chosen angle, QA-gated |

## Connectors

- **Apify** (scouting new formats at scale)
- **Virio MCP** (client settings + `read_linkedin_uri` post reads)
- **HubSpot / Attio** (optional — client enrichment)

This engine is ABM-only: every format it collects or drafts against must target, glorify, or engage a specific named account, person, team, or campaign.

## Files it manages (in your working folder)

- `abm-library/` — the swipe library, seeded from this plugin's starter formats; example turnover is owned by your scheduled refresh task (see abm-library/config.md)
- `abm-clients/<client>/context.md` — one context file per client
- `abm-clients/<client>/drafts/` — saved drafts

## Quick start

Say: "Run the ABM engine for [client]" — or jump in anywhere: "find viral ABM formats", "set up [client]", "give me angles for [client]", "draft the credit-roll post about [campaign]".
