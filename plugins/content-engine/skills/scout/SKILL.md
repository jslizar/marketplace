---
name: scout
description: Mine winning post formats for a lane (abm/tofu/mofu/bofu) from the selected library (Virio or Millie's list). Use when the user says "find viral formats", "refresh the format library", "what formats are working", "scout formats for [lane]", or "deconstruct this post" with a URL. Works from the local content-library (Virio lanes kept fresh by scheduled refresh; Millie's lanes curated), plus the Supabase corpus, Apify, and web search for discovery; deconstructs winners into reusable format specs.
---

# Scout

Find winning posts for a lane, deconstruct them into reusable format specs, and save them to that lane's library.

Requires a lane (abm | tofu | mofu | bofu) and a library (virio | millies). If either is unset, resolve via the post skill's Step 0 / Step 1.

## Data boundary — hard rule

Funnel-lane (tofu/mofu/bofu) corpus discovery reads Supabase project `jacob-content`, table **`viral_posts_all`** — nothing else. NEVER read `viral_posts` (the user's personal-content bank). ABM-lane discovery uses the user's curated ABM post bank, Apify, and web search — never `viral_posts_all` mining for ABM. Millie's library is NEVER auto-refreshed from any corpus — it changes only when the user ships a new bank.

## Source order — try each, fall through on failure

1. **The local library** (preferred — `content-library/<library>/<lane>/` in the user's working folder). On first run, seed by copying `${CLAUDE_PLUGIN_ROOT}/library/` into `content-library/` (including `library/VERSION`). On every run, auto-refresh from the marketplace via the run-start remote VERSION check described in the post skill (fetch the remote `library/VERSION`; if newer, pull the changed specs and merge, preserving pins/edits; silent; offline falls back to local). That version check is the ONE allowed external call during a normal run — it is a cheap distribution mechanism, not format discovery. Otherwise treat the library as authoritative: do not query any format-discovery source (corpus, Apify, web) during a pipeline run unless the user explicitly asks for new formats.
   - Virio lanes: refreshed on the maintainer's machine, pushed to the marketplace, and delivered to everyone automatically by the run-start version check — the local library is current by definition. Only if this machine runs the scheduled refresh task (i.e., the user is the library maintainer) and specs exceed the lane config's freshness window, flag that the refresh likely failed and offer sources 2–4. Otherwise never diagnose a failed refresh; if the user wants fresher formats, offer source 2 (their own URLs) or whichever of sources 3–4 their connections support.
   - Millie's lanes: curated, no freshness window. Never flag staleness. If the user wants formats beyond it, offer the Virio library or discovery sources — but save new specs to Virio's lane, not Millie's, unless the user says otherwise.
2. **Specific URLs**: If the user supplied post URLs, read each with the Virio MCP `read_linkedin_uri` tool.
3. **Corpus / bank discovery** (when the user explicitly wants NEW formats beyond the library; requires corpus access — Supabase project `jacob-content` for funnel lanes, the curated ABM bank for abm. These live on the maintainer's setup; if this user's connections can't reach them, say so and fall through):
   - Funnel lanes: query `viral_posts_all` — always this shape:

     ```sql
     select post_url, creator_first_name, creator_last_name, creator_headline,
            total_reactions, total_comments, engagement_score, hook, hook_type,
            format_archetype, target_persona, tone, is_lead_magnet, posted_at,
            post_text
     from viral_posts_all
     where funnel_stage = '<STAGE>'          -- 'TOFU' | 'MOFU' | 'BOFU', uppercase
       and not is_deleted
       and post_text is not null
       and post_text_length between 400 and 3000
     order by coalesce(engagement_score, 0) desc, total_reactions desc nulls last
     limit 30;
     ```

     Two learned gotchas, do not regress: `engagement_score` is null on many rows and Postgres sorts nulls FIRST on `desc` — always wrap in `coalesce(..., 0)`; and filter `post_text_length` to skip stubs. For archetype variety, partition by `format_archetype` and take the top 1–2 per archetype.
   - ABM lane: the user's curated ABM post bank (maintained outside this pipeline by the scheduled refresh task).
4. **Apify / web search** (requires the Apify MCP — skip if not connected): Use the Apify MCP: `search-actors` for a LinkedIn post-search actor (and X for the abm lane); check the input schema with `fetch-actor-details` before calling; cap maxItems ≤ 50. ABM search terms: ABM markers only — "how did [x] go from", "the team behind", "playbook", "campaign breakdown", open letters to companies — plus the client's category keywords. Funnel lanes: BOFU only, when the corpus can't sustain the lane's repo target; write keepers back into `viral_posts_all` with `funnel_stage = 'BOFU'`.

## Selecting winners (sources 2–4; library specs skip this)

Keep a post only if it clears ALL bars:

- **Engagement outlier**: reactions well above the author's follower-adjusted norm. When follower counts are unavailable, use raw engagement > 300 reactions on LinkedIn, > 500 on X, as a rough floor — prefer `is_outlier = true` rows from the corpus.
- **Lane admission test**: the test in `content-library/<library>/<lane>/config.md`. A viral post that fails its lane's test doesn't enter that lane's library, no matter the numbers. Corpus stage labels are hints, not verdicts — if a row labeled TOFU reads as MOFU on deconstruction, spec it under the lane whose test it passes.
- **Lane deconfliction**: if the post's engine is glorifying or targeting a specific named account, person, team, or campaign (rise stories, campaign anatomies, credit rolls, open letters), it belongs to the abm lane — spec it there regardless of stage label. Generic thought leadership never enters the abm lane.

## Deconstruction

For each winner, write a format spec using `references/format-spec-template.md`. The spec captures the reusable SHAPE, not the content. Name each format memorably.

## Library

- Layout: `content-library/<library>/<lane>/` — one `.md` file per format spec plus `index.md` (table: name, archetype, source, engagement, date added) and `config.md` (lane directive, admission test, refresh policy).
- Append new specs; never overwrite an existing spec without asking. Update `index.md` on every change.
- Dedupe: if a new post matches an existing format's skeleton, treat it as a candidate example for that spec instead of creating a new file.
- Never tag a spec with a lane other than its folder's — a format that works at two lanes gets one spec per lane.
- Millie's indexes carry an "Unread candidates" section — posts from the bank not yet deconstructed. "Deconstruct this post" against a candidate: read it via `read_linkedin_uri`, spec it, move it out of the candidates list.

## Maintaining examples

- Virio lanes: example turnover is owned by the scheduled refresh task, not pipeline runs. If an example looks stale or dead, note it in chat and leave it.
- Millie's lanes: examples change only when the user's bank changes.
- **Pinning** (both libraries): when the user says "add this to the [format] library" / "keep this one" with a post or URL, save it as a pinned example on that spec (mark it `(pinned)`). Pinned examples are never auto-replaced; a pin displaces the weaker unpinned example. Max 2 pins per format.
- If a great post fits no existing format, deconstruct it into a new spec (with the user's go-ahead).

## Output

Present found formats as a compact table (name, archetype, source post, engagement, why it works) and say what was added to the library. Do not dump full post texts into chat.
