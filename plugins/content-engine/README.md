# Content Engine

One pipeline for every LinkedIn post type — ABM, TOFU, MOFU, BOFU — pulling viral formats from selectable libraries. Merges the former **abm-engine** and **funnel-engine** plugins; install this and remove those two.

## How it works

`/content-engine:post` is the front door — one command, the whole pipeline. Two
shortcuts skip the type question: `/content-engine:abm` (ABM preset) and
`/content-engine:funnel` (asks or infers TOFU/MOFU/BOFU). The pipeline:

1. **Post type** — resolves abm / tofu / mofu / bofu from your prompt, or asks one question if unclear.
2. **Library** — asks which format library to pull from: **Virio** (corpus-mined; refreshed on the maintainer's machine and shipped to you as plugin updates) or **Millie's list** (curated from `Viral_Content_Bank.xlsx`). Always asks unless you name one.
3. **Formats → format pick** (scout) — the 3 best-fitting specs, presented as cards.
4. **Client context** (client) — one shared `clients/` store for all lanes.
5. **Angles** (angles) — ranked format × subject × why-now options.
6. **Drafts** (draft) — 2–3 de-slopped, QA-gated candidates.

## Skills

| Skill | Job |
|---|---|
| post | Orchestrator / front door |
| scout | Mine and deconstruct formats into the library |
| client | Build/load client context (Virio settings, CRM, web) |
| angles | Ranked angles from format × context × moment |
| draft | Ship-ready candidates with de-slop + QA gate |

## Libraries

Bundled under `library/` and seeded to `content-library/` in your working folder on first run:

```
content-library/
├── virio/          tofu (15) · mofu (15) · bofu (15) · abm (15)   ← maintainer-refreshed
└── millies/        tofu (13) · mofu (9)  · bofu (0)  · abm (5)    ← curated, manual updates
```

Library updates ship with the plugin: `library/VERSION` is stamped per release, and on each run the engine compares it against your seeded copy and offers a non-destructive merge (new specs added, unpinned examples refreshed; your pins and edits are never touched).

Millie's BOFU is empty by design — her Bottom of Funnel tab is all ABM-style posts; those live in `millies/abm/`. Each populated lane folder has a `config.md` (directive + admission test + refresh policy) and an `index.md`; Millie's empty BOFU carries a redirect `config.md` instead. Millie's indexes list "unread candidates" — bank posts not yet deconstructed; say "deconstruct this post" to spec one.

## Migrating from the old plugins

- Client files: the engine reads legacy `abm-clients/` as a fallback and migrates into `clients/` on first touch.
- Existing `funnel-library/` and `abm-library/` folders are not read by this plugin; the seeded `content-library/` replaces them. Copy any hand-edited specs in before deleting.
- Update the scheduled refresh task to write into `content-library/virio/<lane>/` instead of `funnel-library/<stage>/` and `abm-library/`.

## Data boundaries

Funnel-lane discovery reads only `viral_posts_all` (Supabase, project `jacob-content`). ABM-lane discovery uses the curated ABM bank + Apify. Millie's library is never auto-refreshed.
