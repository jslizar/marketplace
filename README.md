# Jacob's ABM marketplace

Claude plugin marketplace for the ABM content engine.

## Install (coworkers)

1. In Claude Code / Cowork: `/plugin marketplace add jslizar/abm-marketplace`
2. Install the `abm-engine` plugin.
3. Make sure the Virio MCP connector is enabled (you already have it).
4. Run `/abm` — that's it. The 15 viral-format specs ship with the plugin and update automatically when this repo updates.

## How the library stays fresh

`plugins/abm-engine/library/` holds 15 format specs, each with a full example post.
Jacob refreshes them twice a month from the curated post bank; pushing to `main`
rolls the update out to everyone. Do not edit the library directly — file an issue
or ask Jacob.

## Versioning

Plugin behavior changes bump the version in `plugins/abm-engine/.claude-plugin/plugin.json`.
Library content updates are just commits — no version bump needed.
