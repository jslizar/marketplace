# Jacob's plugin marketplace

Claude plugin marketplace for the team. Current plugins:

| Plugin | What it does |
|---|---|
| `content-engine` | Unified LinkedIn content engine — one pipeline for ABM, TOFU, MOFU, and BOFU posts. Picks viral formats from a selectable library (Virio corpus or Millie's curated list), builds client context, proposes ranked angles, drafts de-slopped QA-gated candidates. Requires the Virio MCP connector. |
| `abm-engine` | **Deprecated — install `content-engine` instead.** Kept so existing installs keep working. ABM-only predecessor of content-engine. |

## Install in Cowork (Claude desktop app) — once

- Open the Claude desktop app → **Cowork** tab
- Open **Customize** → **Plugins** tab
- Under **Personal plugins**, click **+** → **Add marketplace** → **Add from a repository**
- Paste: `https://github.com/jslizar/marketplace`
- Find **content-engine** in the new marketplace → click **Install**
- Check **Customize → Connectors** — the **Virio** connector must be enabled (required)
- Optional: connect HubSpot/Attio for richer client context

## Install in Claude Code (CLI / web) — once

- Run: `/plugin marketplace add jslizar/marketplace`
- Run: `/plugin install content-engine@jslizar-marketplace`
- Had `abm-engine` or `funnel-engine`? Remove them — content-engine replaces both
- Enable the **Virio MCP** connector (claude.ai → Settings → Connectors) — required

## Use

- Pick a working folder and use the **same folder every time** — the plugin keeps your clients, format library, and drafts there
- Type **/** and pick **content-engine:post** — or just ask in plain words: *"TOFU post for Acme"*
- The pipeline pauses for your pick at each step:
  - **Post type** — abm / tofu / mofu / bofu
  - **Library** — Virio (corpus-mined) or Millie's list (curated)
  - **Format** — 3 best-fit format cards, each with a real viral example
  - **Client** — loads or builds the client's context file
  - **Angles** — ranked format × subject × why-now options
  - **Drafts** — 2–3 de-slopped, QA-gated candidates
- Skip steps by naming them up front: *"MOFU gated-playbook post for Acme from Millie's list"* jumps straight to drafting
- First run seeds `content-library/` and `clients/` into your working folder — yours to keep and edit
- Updates: update the plugin (Cowork: **Customize → Plugins**); new library releases trigger a one-time merge offer — your edits and pins are never touched

## Format libraries

`plugins/content-engine/library/` ships two libraries, seeded into a `content-library/` folder in your working directory on first run:

- **virio/** — corpus-mined specs (tofu, mofu, bofu, abm), refreshed on Jacob's machine by a scheduled task.
- **millies/** — curated from Millie's viral content bank; updated only when a new bank ships. No BOFU lane by design (her BOFU tab is all ABM-style posts).

Each lane folder has a `config.md` (lane directive + admission test) and an `index.md`.
Library updates reach you through plugin updates: `library/VERSION` is stamped per
release, and on each run the engine compares it with your seeded `content-library/`
copy and offers a non-destructive merge (your pinned examples and edits are never
touched). Update the plugin to pick up new library releases. Do not edit the bundled
library in this repo directly — file an issue or ask Jacob.

## Adding a plugin

Drop it under `plugins/<name>/` and add an entry to `.claude-plugin/marketplace.json`.

## Versioning

Plugin behavior changes bump the version in the plugin's `.claude-plugin/plugin.json`.
Library content updates are just commits — no version bump needed.
