# Content Engine

One pipeline for every LinkedIn post type — ABM, TOFU, MOFU, BOFU — pulling viral formats from selectable libraries. Merges the former **abm-engine** and **funnel-engine** plugins; install this and remove those two.

## How it works

`/content-engine` is the front door — one command, the whole pipeline (in the
CLI it's namespaced: `/content-engine:content-engine`, or use the `post` skill
directly). Two shortcuts skip the type question: `/content-engine:abm` (ABM
preset) and `/content-engine:funnel` (asks or infers TOFU/MOFU/BOFU). The
pipeline:

1. **Post type** — resolves abm / tofu / mofu / bofu from your prompt, or asks one question if unclear.
2. **Library** — asks which format libraries to pull from (**multi-select** — pick one, two, or all three): **Virio** (corpus-mined; refreshed on the maintainer's machine and delivered to you automatically — see below), **Millie's list** (curated from `Viral_Content_Bank.xlsx`), and/or **Emerging** (this week's LinkedIn winners, refreshed every Saturday by the maintainer's viral scan). Multiple selections pool into one candidate set — formats compete on fit and each carries its source-library label. Always asks unless you name them.
3. **Formats → format pick** (scout) — the 3 best-fitting specs, presented as cards.
4. **Client context** (client) — one shared `clients/` store for all lanes. A named client is resolved via Virio first (`content_publishers_list`) — it never web-guesses who they are when Virio knows them.
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
| creators | Discover and mine LinkedIn creators into per-client strategy cards (also `/content-engine:creators`) |

## Creator mining (side door)

`/content-engine:creators` mines creator strategies without running the
posting pipeline. Three modes, detected from your request:

- **Discover** — "find influencers for [client]": derives niche keywords from
  the client's context.md, discovers creators from the Supabase corpus (plus
  an Apify top-up when the corpus runs thin), filters out competitors,
  inactives, and one-hit wonders, and presents a ranked longlist. You pick
  the shortlist (default 5). Clients resolve via Virio first
  (`content_publishers_list`), like the rest of the engine — local `clients/`
  folders are working copies, not the roster; a missing context.md is built
  from Virio content settings via the client skill. Virio is context-only:
  all post/profile scraping is Apify.
- **Single-link** — "copy this person's strategy" + a LinkedIn profile URL:
  skips discovery, mines that person.
- **List** — paste creator names/handles: resolves each to a profile, you
  confirm, then it mines each one.

Every mined creator gets a strategy card at
`clients/<slug>/creators/<creator-slug>.md` — their 15 most recent posts, top
viral posts (verbatim hooks + full text), and a strategy read (cadence,
format mix, hook patterns, pillars, tone) with a client-specific "how to copy
this" section — plus a roster `index.md`. After the cards, you select what
to copy (whole creators, specific posts, or patterns) and the skill compiles
`clients/<slug>/creators/strategy.md`: the complete copy-this strategy —
post strategy mapped to the client's pillars, a posting schedule reconciled
with their cadence, example posts verbatim, and a library of posts to copy.
Cards and strategy feed the copy-post plugin (style profiles via
style-library) and scout (format specs); the skill offers those handoffs.
It is research, not a pipeline stage — it never drafts posts and never
scores creators for outreach.

## Libraries

Bundled under `library/` and seeded to `content-library/` in your working folder on first run:

```
content-library/
├── virio/          tofu (15) · mofu (15) · bofu (15) · abm (15)   ← maintainer-refreshed
│                   + up to 15/lane "Recent finds" rolled in weekly from Emerging
├── millies/        tofu (13) · mofu (9)  · bofu (0)  · abm (5)    ← curated, manual updates
└── emerging/       0–15 per lane — this week's LinkedIn winners   ← weekly scan (Saturdays)
```

Emerging holds spec-lites deconstructed from posts that performed in the last 7 days. Every
Saturday the maintainer's viral scan replaces its contents and rolls the outgoing batch into the
matching Virio lane as "Recent finds" (replacing the prior week's), so Virio carries the proven
core plus a rotating recent cohort. Lanes are quality-gated — a thin or empty week is normal.

Library updates reach you automatically — no plugin update needed. `library/VERSION` is stamped per release, and on each run the engine fetches the marketplace's remote `VERSION` (one small file); if it's newer than your seeded copy, it pulls the changed specs and merges them in silently (new specs added, unpinned examples refreshed; your pins and edits are never touched). Offline, it uses your local copy. So when the maintainer pushes new formats to the marketplace repo, everyone picks them up on their next run.

It also self-heals a stale local library: on each run it checks the one lane you're using against the marketplace's index, and if a `content-library/` left by an older plugin version is out of date or has the two libraries crossed, it repairs that lane (preserving your pins). VERSION matching alone is no longer trusted for the lane in use.

Millie's BOFU is empty by design — her Bottom of Funnel tab is all ABM-style posts; those live in `millies/abm/`. Each populated lane folder has a `config.md` (directive + admission test + refresh policy) and an `index.md`; Millie's empty BOFU carries a redirect `config.md` instead. Millie's indexes list "unread candidates" — bank posts not yet deconstructed; say "deconstruct this post" to spec one.

## Migrating from the old plugins

- Client files: the engine reads legacy `abm-clients/` as a fallback and migrates into `clients/` on first touch.
- Existing `funnel-library/` and `abm-library/` folders are not read by this plugin; the seeded `content-library/` replaces them. Copy any hand-edited specs in before deleting.
- Update the scheduled refresh task to write into `content-library/virio/<lane>/` instead of `funnel-library/<stage>/` and `abm-library/`.

## Data boundaries

Funnel-lane discovery reads only `viral_posts_all` (Supabase, project `jacob-content`). ABM-lane discovery uses the curated ABM bank + Apify. Millie's library is never auto-refreshed. Creator mining reads `viral_posts_all` and `outlier` read-only — it never writes to the corpus, and never touches `viral_posts`.
