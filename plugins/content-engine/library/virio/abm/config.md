# Virio — ABM config

## Lane directive

- **Job**: Glorify or target a specific named account, person, team, or campaign so the target sees it, amplifies it, and owes you a warm reply. All ABM formats are BOFU by definition — never tag a spec here TOFU or MOFU.
- **Proof level**: Heavy specificity — real names, real numbers, insider detail. A rise story with vague plays is dead.
- **CTA**: The post itself is the CTA — the ABM payoff is the target engaging.

## Admission test

Would the named target be glad this post exists? The post's engine must be a specific named account, person, team, or campaign (rise stories, campaign anatomies, credit rolls, open letters, teardown-as-tribute). Generic thought leadership fails.

## Refresh policy

- Repo target: ~15 format specs.
- Freshness window: 14 days — specs with source examples older than this are flagged stale.
- Source: the `abm_posts` bank (Supabase `jacob-content`), maintained by the scheduled refresh task (runs as a local Claude Code cron — `scripts/library-refresh/run.sh`, not a desktop task).
- Top-up path: when `abm_posts` can't sustain 2 fresh matches for a spec, or its newest `posted_at` is older than 60 days, the refresh task scouts new posts via Apify (LinkedIn/X post-search actors, maxItems ≤ 50, ABM markers only) and INSERTs keepers back into `abm_posts` (dedupe on `post_url`/`provider_urn`; winner bars: engagement outlier AND ABM mechanic), then re-queries. Never updates or deletes existing rows.
- Example turnover: owned by the scheduled refresh task. Each spec carries exactly 2 source examples; pinned examples are never auto-replaced.
