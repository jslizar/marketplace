# Content Engine

One pipeline for every LinkedIn post type — ABM, TOFU, MOFU, BOFU — pulling viral formats from selectable libraries. Merges the former **abm-engine** and **funnel-engine** plugins; install this and remove those two.

## How it works

`/content-engine` is the front door — one command, the whole pipeline (in the
CLI it's namespaced: `/content-engine:content-engine`, or use the `post` skill
directly). Two shortcuts skip the type question: `/content-engine:abm` (ABM
preset) and `/content-engine:funnel` (asks or infers TOFU/MOFU/BOFU). The
pipeline:

1. **Post type** — resolves abm / tofu / mofu / bofu from your prompt, or asks one question if unclear.
2. **Library** — asks which format library to pull from: **Virio** (corpus-mined; refreshed on the maintainer's machine and delivered to you automatically — see below) or **Millie's list** (curated from `Viral_Content_Bank.xlsx`). Always asks unless you name one.
3. **Formats → format pick** (scout) — the 3 best-fitting specs, presented as cards.
4. **Client context** (client) — one shared `clients/` store for all lanes.
5. **Angles** (angles) — ranked format × subject × why-now options.
6. **Drafts** (draft) — 2–3 de-slopped, QA-gated candidates.
7. **Pick the winner** — choose the candidate to go forward with.
8. **Graphic prompt** (graphic-prompt, offered) — a paste-ready prompt for Claude to build a graphic for the chosen post as an artifact. Skippable.

## Skills

| Skill | Job |
|---|---|
| post | Orchestrator / front door |
| scout | Mine and deconstruct formats into the library |
| client | Build/load client context (Virio settings, CRM, web) |
| angles | Ranked angles from format × context × moment |
| draft | Ship-ready candidates with de-slop + QA gate |
| graphic-prompt | Turn the chosen post into a Claude graphic-build prompt (also `/content-engine:graphic`) |

## Libraries

Bundled under `library/` and seeded to `content-library/` in your working folder on first run:

```
content-library/
├── virio/          tofu (15) · mofu (15) · bofu (15) · abm (15)   ← maintainer-refreshed
└── millies/        tofu (13) · mofu (9)  · bofu (0)  · abm (5)    ← curated, manual updates
```

Library updates reach you automatically — no plugin update needed. `library/VERSION` is stamped per release, and on each run the engine fetches the marketplace's remote `VERSION` (one small file); if it's newer than your seeded copy, it pulls the changed specs and merges them in silently (new specs added, unpinned examples refreshed; your pins and edits are never touched). Offline, it uses your local copy. So when the maintainer pushes new formats to the marketplace repo, everyone picks them up on their next run.

It also self-heals a stale local library: on each run it checks the one lane you're using against the marketplace's index, and if a `content-library/` left by an older plugin version is out of date or has the two libraries crossed, it repairs that lane (preserving your pins). VERSION matching alone is no longer trusted for the lane in use.

Millie's BOFU is empty by design — her Bottom of Funnel tab is all ABM-style posts; those live in `millies/abm/`. Each populated lane folder has a `config.md` (directive + admission test + refresh policy) and an `index.md`; Millie's empty BOFU carries a redirect `config.md` instead. Millie's indexes list "unread candidates" — bank posts not yet deconstructed; say "deconstruct this post" to spec one.

## Migrating from the old plugins

- Client files: the engine reads legacy `abm-clients/` as a fallback and migrates into `clients/` on first touch.
- Existing `funnel-library/` and `abm-library/` folders are not read by this plugin; the seeded `content-library/` replaces them. Copy any hand-edited specs in before deleting.
- Update the scheduled refresh task to write into `content-library/virio/<lane>/` instead of `funnel-library/<stage>/` and `abm-library/`.

## Data boundaries

Funnel-lane discovery reads only `viral_posts_all` (Supabase, project `jacob-content`). ABM-lane discovery uses the curated ABM bank + Apify. Millie's library is never auto-refreshed.
