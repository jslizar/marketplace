# Jacob's plugin marketplace

Claude plugin marketplace for the team. Current plugins:

| Plugin | What it does |
|---|---|
| `content-engine` | Unified LinkedIn content engine — one pipeline for ABM, TOFU, MOFU, and BOFU posts. Picks viral formats from a selectable library (Virio corpus or Millie's curated list), builds client context, proposes ranked angles, drafts de-slopped QA-gated candidates. Requires the Virio MCP connector. |
| `abm-engine` | **Deprecated — install `content-engine` instead.** Kept so existing installs keep working. ABM-only predecessor of content-engine. |

## Install (coworkers)

1. In Claude Code / Cowork: `/plugin marketplace add jslizar/marketplace`
2. Install `content-engine`. If you had `abm-engine` (or `funnel-engine`) installed, remove them — content-engine replaces both.
3. Make sure the Virio MCP connector is enabled (you already have it).
4. Run `/content-engine:post` — that's it. It walks you through post type → format library → format pick → client → angles → drafts.

## Format libraries

`plugins/content-engine/library/` ships two libraries, seeded into a `content-library/` folder in your working directory on first run:

- **virio/** — corpus-mined specs (tofu, mofu, bofu, abm), refreshed by Jacob's scheduled task.
- **millies/** — curated from Millie's viral content bank; updated only when a new bank ships. No BOFU lane by design (her BOFU tab is all ABM-style posts).

Each lane folder has a `config.md` (lane directive + admission test) and an `index.md`.
Pushing library updates to `main` rolls them out to everyone. Do not edit the
library directly — file an issue or ask Jacob.

## Adding a plugin

Drop it under `plugins/<name>/` and add an entry to `.claude-plugin/marketplace.json`.

## Versioning

Plugin behavior changes bump the version in the plugin's `.claude-plugin/plugin.json`.
Library content updates are just commits — no version bump needed.
