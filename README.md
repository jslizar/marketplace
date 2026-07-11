# Jacob's plugin marketplace

Claude plugin marketplace for the team. Current plugins:

| Plugin | What it does |
|---|---|
| `abm-engine` | ABM content engine — drafts LinkedIn posts from a curated library of 15 viral ABM formats, researches the client and market, proposes angles, drafts posts. Requires the Virio MCP connector. |

## Install (coworkers)

1. In Claude Code / Cowork: `/plugin marketplace add jslizar/marketplace`
2. Install the plugin(s) you want, e.g. `abm-engine`.
3. For abm-engine: make sure the Virio MCP connector is enabled (you already have it).
4. Run `/abm` — that's it. The format library is fetched live from this repo on every run, so updates reach you automatically.

## How the ABM library stays fresh

`plugins/abm-engine/library/` holds 15 format specs, each with a full example post.
Jacob refreshes them twice a month from the curated post bank; pushing to `main`
rolls the update out to everyone instantly (the plugin live-fetches from this repo).
Do not edit the library directly — file an issue or ask Jacob.

## Adding a plugin

Drop it under `plugins/<name>/` and add an entry to `.claude-plugin/marketplace.json`.

## Versioning

Plugin behavior changes bump the version in the plugin's `.claude-plugin/plugin.json`.
Library content updates are just commits — no version bump needed.
