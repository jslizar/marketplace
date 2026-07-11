---
name: abm-scout
description: Mine viral ABM post formats from LinkedIn and X. Use when the user says "find viral ABM formats", "scout viral posts", "what ABM formats are working", "refresh the format library", or "deconstruct this post" with a URL. Works from the local abm-library (kept fresh by a scheduled refresh task), plus Apify scrapers and web search; deconstructs winners into reusable format specs and saves them to the swipe library.
---

# ABM scout

Find viral ABM-style posts, deconstruct them into reusable format specs, and save them to the library.

This engine is ABM-only. Every source below feeds ABM-style posts exclusively; generic thought leadership never enters the library.

## Source order — try each, fall through on failure

1. **The local swipe library** (preferred — `abm-library/` in the user's working folder). Its format specs and source examples are maintained OUTSIDE this pipeline by a scheduled refresh task that pulls from the user's own curated post bank (see `abm-library/config.md` for the refresh policy). Treat the library as authoritative: do not query any external database during a pipeline run. If the library looks stale (specs older than 14 days), flag it to the user — the scheduled refresh has likely failed — and offer sources 2–4 below instead.
2. **Specific URLs**: If the user supplied post URLs, read each with the Virio MCP `read_linkedin_uri` tool.
3. **Apify** (discovery at scale, when the user explicitly wants NEW formats beyond the library). Use the Apify MCP: `search-actors` for a LinkedIn post-search actor and an X/Twitter search actor. Check the input schema with `fetch-actor-details` before calling. Search terms: ABM markers only — "how did [x] go from", "the team behind", "playbook", "campaign breakdown", open letters to companies — plus the client's category keywords. Cap results (maxItems ≤ 50 per run) to control cost.
4. **Web search**: for roundups of high-performing ABM/B2B LinkedIn posts as leads, then read the actual posts via `read_linkedin_uri`.

## Selecting winners (sources 2–4; library specs skip this)

Keep a post only if it clears BOTH bars:
- **Engagement outlier**: reactions well above the author's follower-adjusted norm (a 1,000-reaction post from a 5k-follower author beats 2,000 from a 500k-follower author). When follower counts are unavailable, use raw engagement > 300 reactions on LinkedIn, > 500 on X, as a rough floor.
- **ABM mechanics**: the post targets or glorifies a specific named account, person, team, or campaign (rise stories, campaign anatomies, credit rolls, open letters to a company, teardown-as-tribute). Generic thought leadership fails this bar.

## Deconstruction

For each winner, write a format spec using `references/format-spec-template.md`. The spec captures the reusable SHAPE, not the content. Name each format memorably (e.g. "executive rise deep-dive", "campaign anatomy + credit roll").

## Library

- The swipe library lives at `abm-library/` in the user's working folder — one `.md` file per format spec plus `index.md` (table: name, archetype, source, engagement, date added). All formats are BOFU by definition — never tag a library entry TOFU or MOFU.
- On first run, seed the library by copying the starter specs from `${CLAUDE_PLUGIN_ROOT}/library/` into `abm-library/`.
- Append new specs; never overwrite an existing spec without asking. Update `index.md` on every change.
- Dedupe: if a new post matches an existing format's skeleton, treat it as a candidate example for that spec instead of creating a new file.

## Maintaining examples — the scheduled refresh owns them

Each format spec carries exactly 2 source examples, kept current:

- Example turnover is handled by the user's scheduled refresh task, not by pipeline runs. Do not replace examples mid-pipeline; if an example looks stale or dead, note it in chat and leave it for the next scheduled refresh.
- **Pinning**: when the user says "add this to the [format] library" / "I like this one, keep it" with a post or URL, save it as a pinned example on that spec (mark it `(pinned)`). Pinned examples are never auto-replaced; a pin displaces the weaker unpinned example. Max 2 pins per format.
- If a great post fits no existing format, deconstruct it into a new spec (with the user's go-ahead) rather than forcing it into one.

## Output

Present found formats as a compact table (name, archetype, source post, engagement, why it works) and say what was added to the library. Do not dump full post texts into chat.
