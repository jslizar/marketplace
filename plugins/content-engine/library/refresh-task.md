# Content-engine library refresh — task spec (private; never published)

Refresh the content-engine Virio library (abm, tofu, mofu, bofu) from the Supabase corpus, then
publish to jslizar/marketplace so every install picks up the new examples on its next run.
Library maintenance only — never draft posts.

> This file is the source prompt for the local scheduled refresh. It is NOT published to the
> marketplace (rsync excludes it — only `library/` ships). Editing it changes the next run.

## Environment

- Runs headless (local cron via `scripts/library-refresh/run.sh`) inside the content-agent repo with
  real filesystem + git credentials. No cowork mount, no `request_cowork_directory`.
- MCP available: `supabase` (`execute_sql`), `apify`. No claude.ai connectors, no github MCP —
  publishing is shell `git` in the marketplace clone.
- This task owns the CORE Virio specs only; pipeline runs read the library. The weekly viral-scan
  task (`scripts/viral-scan/`, Saturdays) is the corpus's ingestion layer — it inserts fresh finds
  into `abm_posts` and `viral_posts_all` that this refresh then consumes — and it owns the
  `emerging/` library plus the `cohort: rolled` entries inside `virio/<lane>/` ("Recent finds").
  NEVER touch those: skip any spec whose frontmatter carries `cohort: emerging` or `cohort: rolled`
  in the per-spec example-refresh loop, and never edit `emerging/`. Expect the corpus's newest
  `posted_at` to advance weekly; the stale-snapshot alarm below self-resolves once scans are
  landing.

## Autonomy — this is an unattended scheduled run

- Do NOT pause to ask for confirmation. There is no human watching; a question just ends the run
  with nothing done. When a step's trigger fires, execute the bounded default action and record what
  you did in the report.
- The Apify top-up (step 4) is **pre-authorized** within its `maxItems ≤ 50` cap and the `> 60 days`
  staleness trigger. Run it automatically when triggered — do not treat billable scraping or the
  public push as needing sign-off; the caps ARE the sign-off. Publishing the refreshed library to
  `jslizar/marketplace` is the intended end state of every run that changes something.
- It self-limits: once the top-up inserts fresh rows, `newest posted_at` is no longer > 60 days, so
  later runs stop triggering on staleness. Read-only lanes (tofu/mofu) never top up.

## Paths

- Edit here (source of truth): `tools/content-engine/library/virio/<lane>/` — per lane: `config.md`,
  `index.md`, one `.md` per spec — and root `tools/content-engine/library/VERSION`.
- Publish target: `$MARKETPLACE_CLONE/plugins/content-engine/` (remote `jslizar/marketplace`, `main`).
  `$MARKETPLACE_CLONE` is exported by `run.sh`.
- Never touch: the retired `abm-marketplace/` & `funnel-marketplace/` trees, the legacy root
  `abm-library/` & `funnel-library/`, or any seeded runtime `content-library/` working copy
  (regenerated on run).
- **`millies/` is off-limits.** Never read, query, swap, or edit anything under
  `tools/content-engine/library/millies/` — Millie's library is curated by hand and never
  corpus-refreshed. This task operates on `virio/` only. (The publish rsync mirrors the whole plugin,
  so `millies/` ships unchanged as a byte-identical passthrough — never as an edit.)

## Data boundaries (Supabase project jacob-content = `bqvsughoqemcbjemytma`)

- abm lane → table `abm_posts`. tofu/mofu/bofu → `viral_posts_all` filtered by `funnel_stage`.
- NEVER read `viral_posts`. Never cross tables between lanes (no `abm_posts` for funnel lanes, no
  `viral_posts_all` for abm).
- Writes: abm lane MAY insert scouted keepers into `abm_posts`; bofu lane MAY insert keepers into
  `viral_posts_all` with `funnel_stage = 'BOFU'`. Never update or delete existing rows. No migrations
  (use `execute_sql`, never `apply_migration`).

## Per lane (run abm, then tofu, mofu, bofu)

1. Read the lane `config.md` (directive, admission test, refresh policy) and each spec's
   Source-examples section.
2. Query top matches per spec archetype:
   - **funnel lanes**: `where funnel_stage = '<STAGE>' and not is_deleted and post_text is not null
     and post_text_length between 400 and 3000` + the spec's archetype filter,
     `order by coalesce(engagement_score,0) desc, total_reactions desc nulls last` limit 5.
   - **abm lane**: same shape on `abm_posts` (archetype column is `format_archetype`),
     `where coalesce(is_deleted,false) = false and quality_score >= 3` + the spec's archetype filter.
   - The `coalesce(engagement_score,0)` wrapper is mandatory — `engagement_score` is null on many
     rows and Postgres sorts nulls first on plain `desc`.
3. Refresh each spec's 2 source examples:
   - `(pinned)` examples are NEVER replaced.
   - Fill any `(second example: to be filled ...)` placeholder slot first.
   - Replace an unpinned example only when the table has a higher-ranking match that ALSO passes the
     lane's admission test AND the ABM deconfliction rule (a post whose engine glorifies or targets a
     specific named account, person, team, or campaign belongs to the abm lane — skip it in the
     funnel lanes).
   - When a spec's top example changes, ALSO replace its `## Top example — full post text` block with
     the new top post's complete verbatim `post_text` and source line.
   - Annotate every refreshed example: author, reactions/comments, date, engagement_score, refresh date.
4. Top-up:
   - **abm lane (top-up path)**: if `abm_posts` can't sustain 2 fresh matches for a spec, OR the
     newest `posted_at` is > 60 days old, execute this automatically (pre-authorized, see Autonomy):
     scout via Apify (LinkedIn/X post-search actor —
     `fetch-actor-details` before calling, maxItems ≤ 50, ABM markers only: "how did [x] go from",
     "the team behind", "playbook", "campaign breakdown", open letters to companies) → INSERT keepers
     into `abm_posts` (dedupe on `post_url`/`provider_urn`; winner bars: engagement outlier AND ABM
     mechanic) → re-query and redo step 3.
   - **bofu lane**: same via `viral_posts_all` with `funnel_stage = 'BOFU'` (existing path).
   - **tofu / mofu**: read-only, no top-up.
5. Update the lane `index.md` (top example, peak engagement, refresh date).

## Finalize

6. If any spec changed: bump `tools/content-engine/library/VERSION` (`YYYY-MM-DD.N`; increment `N` on
   same-day reruns) and mirror the bump in the marketplace clone's
   `.claude-plugin/marketplace.json` content-engine entry. **MANDATORY** — a new example inside an
   existing spec file does NOT reach installs unless VERSION bumps (the client bulk-refresh only
   fires on "remote newer").
7. Publish: `rsync -a --delete --exclude='.DS_Store' tools/content-engine/
   "$MARKETPLACE_CLONE"/plugins/content-engine/`, then in the clone:
   `git add -A && git commit -m "content-engine library refresh YYYY-MM-DD"`.
   `run.sh` performs the `git push` (the one network step).
8. Report: per lane — examples swapped in/out (URLs + scores), examples kept, placeholder slots
   filled, top-up inserts (count + source), and newest `posted_at` + staleness flag (> 60 days).
   Overall: VERSION old→new, commit + push status. Concise, no fluff.
9. **Stale-snapshot alarm**: `viral_posts_all` and `abm_posts` are static bulk snapshots (each loaded
   in a single burst — check: `count(distinct date_trunc('day', created_at)) = 1`), not
   continuously-fed tables. `posted_at` is the post's original publish date, NOT an ingestion date —
   a newest `posted_at` >60 days old means the snapshot's *content* is aged, not that anything broke.
   If ALL four lanes (including read-only tofu/mofu) share a >60-day-old newest `posted_at`, the
   corpus needs a fresh bulk load to advance — the abm/bofu Apify top-up is the only in-task path that
   pulls newer posts, and it can't reach tofu/mofu. Lead the report with a one-line ⚠️ note saying the
   snapshot needs reloading; don't let recurring no-ops hide that the content has stopped advancing.
