---
name: creators
description: Find and mine LinkedIn creators whose strategy a client should copy. Use when the user says "find influencers for [client]", "who should [client] copy", "copy this person's strategy" with a LinkedIn profile link, "mine this creator", "creator research for [client]", or pastes a list of creator names/handles. Discovers creators from the Supabase corpus and Apify (or skips discovery when given a link or list), then for each creator mines their 15 most recent posts and top viral posts, ranks lightly by consistency and engagement rate, and writes per-creator strategy cards to clients/<slug>/creators/ for the copy-post and scout machinery to consume. Strategy mining for content creation — NOT KOL outreach scoring.
---

# Creators

Mine creator strategies a client can copy. For each creator: their 15 most
recent posts, their top viral posts, and a strategy read (cadence, formats,
hooks, pillars) grounded in real scraped data — plus a client-specific "how to
copy this" section. Light qualification only; this skill never scores for
outreach, builds tiers, or drafts outreach messages.

This is a side door, like the graphic command — it never triggers the posting
pipeline, and the posting pipeline never triggers it.

## Data boundary — hard rules

- Corpus reads: Supabase project `jacob-content`, tables **`viral_posts_all`**
  and **`outlier`** ONLY. NEVER read `viral_posts` (the user's personal-content
  bank). `abm_posts` is not this skill's business.
- This skill is **SELECT-only**. It never INSERTs, UPDATEs, or migrates —
  mined posts do not enter the corpus from here (the weekly viral-scan owns
  ingestion).
- **No fabrication.** Every metric on a card traces to a real corpus row or a
  real API response. A field no source answered is written `[unverified]` —
  never estimated, never padded. This especially applies to follower counts,
  engagement rates, and "their best post": if you can't verify it, say so.
- Never write into the plugin directory. All output goes to the working
  folder (`clients/<slug>/creators/`).

## Step 0 — mode + client

Detect the mode from the request, in this order:

1. **Single-link** — the request contains one or more `linkedin.com/in/` URLs
   → skip discovery, mine those profiles.
2. **List** — the request contains a pasted list of creator names or handles
   (no profile URLs) → skip discovery. Resolve each name to a LinkedIn
   profile URL via web search (`<name> LinkedIn site:linkedin.com`), checking
   the headline against any context the user gave. Present a resolution
   table — name given, profile found, headline, URL — and **STOP: the user
   confirms before any mining.** Wrong-person mining wastes the whole budget.
3. **Discover** — neither → run the full discovery pipeline below.

Client: resolve the slug from the request against existing `clients/` folders.
If no client is named, ask one question and stop. All output is client-scoped
— the same creator mined for two clients gets two cards, because "how to copy
this" is client-specific.

## Step 1 — ground on context.md

- **Discover mode requires `clients/<slug>/context.md`** — niche keywords
  derive from its ICP and Pillars, and the competitor filter derives from its
  Canon/ICP. If it's missing or stale, say so and offer to build it first
  (read `${CLAUDE_PLUGIN_ROOT}/skills/client/SKILL.md` and follow it). Never
  web-guess an ICP to search on.
- **Single-link and list modes:** context.md is optional. If missing, warn in
  one line that competitor flagging and the "How to copy this" section will be
  generic, offer the client skill, and proceed if the user says go.

## Discover mode

### Keywords (STOP)

Derive 5–10 niche keywords from context.md — category terms, buyer language,
named problem spaces from ICP and Pillars. Not the client's brand name. Where
possible, map keywords onto the corpus tag vocabulary (real tags, by volume):
`ai_ml`, `personal_development`, `leadership`, `product`, `industry_news`,
`career`, `content_creation`, `marketing`, `entrepreneurship`, `hiring`,
`engineering`, `productivity`, `startups`, `health_wellness`, `strategy`,
`personal_brand`, `sales`, `data_analytics`, `culture`, `education`,
`operations`, `finance`, `sustainability`, `diversity_inclusion`,
`social_media`, `design_creative`, `cybersecurity`, `management`,
`supply_chain`, `growth`, `legal`, `fundraising`, `customer_success`,
`partnerships`, `remote_work`, `saas`, `ecommerce`. Keywords that don't map to
a tag still work via the text match below.

Present the keyword list (tags + free-text terms). The user approves or edits.
STOP.

### Corpus discovery

Aggregate creators (not posts). Run this shape against `viral_posts_all`, then
again against `outlier`, and merge on `creator_username`:

```sql
select creator_username,
       max(creator_first_name)  as first_name,
       max(creator_last_name)   as last_name,
       max(creator_headline)    as headline,
       max(creator_profile_url) as profile_url,
       count(*)                                 as matching_posts,
       count(*) filter (where is_outlier)       as outlier_posts,
       round(avg(coalesce(engagement_score,0))) as avg_engagement,
       max(coalesce(engagement_score,0))        as peak_engagement,
       max(posted_at)                           as last_seen
from viral_posts_all
where not is_deleted
  and not is_company_post
  and creator_username is not null
  and post_text is not null
  and (topic_tags && array['<tag1>','<tag2>']::text[]
       or post_text ilike any (array['%<kw1>%','%<kw2>%']))
group by creator_username
having count(*) >= 2
order by count(*) filter (where is_outlier) desc,
         avg(coalesce(engagement_score,0)) desc
limit 25;
```

Two learned gotchas, do not regress: `engagement_score` is null on many rows
and Postgres sorts nulls FIRST on `desc` — always wrap in `coalesce(..., 0)`.
And keep `having count(*) >= 2`: one viral post is a fluke, not a strategy —
a creator must show up more than once to be a strategy source.

### Live top-up (Apify) — only if the corpus yields < 8 candidates

Pinned actor: `harvestapi/linkedin-post-search` (id `buIWk2uOUzTmcLsuB`).
Check the input schema with `fetch-actor-details` before the first call of the
session. Discovery input:

```json
{"searchQueries": ["<kw1>", "<kw2>", "<kw3>"], "maxPosts": 10,
 "postedLimit": "month", "sortBy": "relevance", "profileScraperMode": "short"}
```

Max 2 discovery runs, maxItems ≤ 50 each. Group results by author; keep
authors with ≥ 2 posts clearing 300+ reactions (relevance sort applies no
engagement filter, so apply the floor strictly).

### Hard filters (drop, and record every drop in the index's Dropped section)

- **Dedupe** by normalized name (lowercase, strip punctuation/emoji/
  credentials) and by LinkedIn profile URL, across corpus and live results.
- **Inactive**: fewer than 5 posts in the last 90 days (corpus `posted_at`
  spread, or live feed when checked).
- **Competitor**: the creator is, or works for, a company in the client's
  competitive set (from context.md Canon/ICP) — match against headline and
  company strings. Borderline calls are kept but flagged on the card.
- **Company pages**: people only — `not is_company_post`, skip `/company/`
  URLs.

### Rank and pick (STOP)

Light ranking — a sort order, not a scoring product. Score /10:

- **Consistency 0–4** — distinct outlier posts (4 = 4+)
- **Engagement 0–3** — median reactions ÷ followers when followers are known;
  otherwise median reactions with the rate marked `[unverified]`
- **Activity 0–2** — posts per 90 days
- **Relevance 0–1** — keyword/pillar overlap in their matching posts

Present the ranked longlist as one table: rank, name, headline, matching
posts, outliers, avg engagement, last seen, source (corpus / live / both).
The user picks the shortlist — **default 5** (mining budget). More than 8
requires an explicit budget warning and confirmation. STOP.

## Mining — every mode converges here

One Apify run covers both the profile and the recent posts — pinned actor
`harvestapi/linkedin-post-search`, batching ≤ 3 creators per run:

```json
{"authorUrls": ["https://www.linkedin.com/in/<a>/", "https://www.linkedin.com/in/<b>/"],
 "maxPosts": 15, "profileScraperMode": "main"}
```

Two validated gotchas (2026-07-22), do not regress:

- **Do NOT pass `sortBy` or `postedLimit` with `authorUrls`** — the run
  succeeds but returns 0 items. Author feeds come back recent-first; sort
  client-side on the returned dates if needed.
- `profileScraperMode: "main"` embeds the FULL author profile in every post
  item (~50KB each). Never read the dataset raw — fetch with projected
  fields: one call with `limit: 1` and
  `fields: "author.name,author.headline,author.followerCount,author.about,author.location.linkedinText"`
  per creator for the profile, then one call with
  `fields: "linkedinUrl,content,postedAt.date,engagement.likes,engagement.comments,engagement.shares,type"`
  for the posts.

Per shortlisted creator, from that run:

1. **Profile** — `author.followerCount` (live), `author.headline`,
   `author.about`, `author.location.linkedinText`, current company from
   `author.experience` if needed. Any field the scrape doesn't return →
   web-search fallback, else `[unverified]`.
2. **15 most recent posts** — the post items: URL, full text, date, likes,
   comments, shares. The hook is the first line of `content`. Skip rows with
   empty `content`.

   Label engagement by source and never mix them in one stat: Apify reports
   `likes` (undercounts LinkedIn's full reaction total); the corpus reports
   `total_reactions`.
3. **Top viral posts (up to 5)** — union of two verified sources, deduped on
   `post_url`, top 5 by engagement:
   - Corpus lookup, run against BOTH `viral_posts_all` and `outlier`:

     ```sql
     select post_url, hook, hook_type, format_archetype, post_text,
            total_reactions, total_comments, total_reposts,
            coalesce(engagement_score,0) as engagement_score, is_outlier,
            posted_at, funnel_stage
     from viral_posts_all
     where (creator_username = '<username>'
            or creator_profile_url ilike '%/in/<username>%')
       and not is_deleted
     order by coalesce(engagement_score,0) desc,
              total_reactions desc nulls last
     limit 10;
     ```

   - Live outliers within the fetched recent sample: reactions ≥ 3× the
     creator's own sample median (follower-adjusted judgment allowed — state
     the reasoning on the card).
   - If neither yields anything, the card says "No verifiable viral posts
     found (corpus miss; live sample shows no outliers)." Never pad.

## Strategy read

Each card derives, from the mined rows only: cadence (posts/week from the
recent-sample dates), format mix (text/image/video/document split; corpus
`format_archetype` where available), hook patterns (quote 2–3 verbatim
opening lines and name the pattern), pillars (the topics they actually post
about), tone, CTA habits, and the outliers-vs-baseline delta — what their
viral posts do that their median post doesn't. Then "How to copy this for
<client>": which patterns transfer to the client's voice and pillars, what
NOT to copy, mapped to the client's actual pillar names from context.md.

## Output

- One card per creator: `clients/<slug>/creators/<creator-slug>.md` per
  `references/creator-card-template.md`. Creator slug = kebab-case full name;
  on collision, append the LinkedIn username.
- Update `clients/<slug>/creators/index.md` per
  `references/creator-index-template.md` — roster table, Dropped section,
  handoffs log.
- Save via `run-log` so every file carries its provenance header — the
  `command`/`skills`/`plugins`/`connectors` fields come from the telemetry
  resolver, never from memory.
- Re-mining a creator who already has a card: show a diff summary and ask
  before overwriting — same rule as context.md.
- In chat, present the compact summary table only. Full post texts live on
  the cards, not in chat.

## Budget

- Apify: ≤ 6 actor runs per session total (≤ 2 discovery + mining runs at
  ≤ 3 creators each), maxItems ≤ 50 each, `fetch-actor-details` once per
  session before the first call. If the shortlist would blow the budget,
  STOP and ask — split across sessions or shrink the list.
- Supabase: SELECT-only, result sets capped as shown above.

## Degradation order

Never fail the whole run because one source is down; every card states what
was skipped.

1. **Supabase down** → skip corpus discovery and corpus viral lookup;
   discover mode becomes Apify-only; "Top viral" limited to live-sample
   outliers, labeled "(live sample only — corpus unavailable)".
2. **Apify down** → corpus-only cards: no recent-15 (say so plainly),
   virals from corpus rows, profile from web search with followers
   `[unverified]`, card stamped "STALE — corpus data only, last seen
   <date>"; ask before proceeding.
3. **Both down** → nothing verifiable to mine; stop and say so.

## Handoffs — offers, never auto-run

After cards are saved, show the summary table, then offer as a plain
question:

1. **Compile <creator> into a reusable style profile** — copy the card's
   full-text winning posts into `styles/<creator-slug>/examples/` and run the
   copy-post `style-library` skill to compile `profile.md`.
2. **Turn their winners into format specs** — run the scout skill
   (`${CLAUDE_PLUGIN_ROOT}/skills/scout/SKILL.md`) to deconstruct chosen post
   URLs into specs for `content-library/virio/<lane>/` (never Emerging).
3. **Draft in their style for <client>** — run copy-post with a winning post
   as the example.
4. **Mine more creators / refresh a card** — rerun this skill.

"None" exits cleanly.

## Rules

- Stop at every marked decision point — keywords, longlist pick, list-mode
  resolution, card overwrite. The user chooses; you recommend.
- No pipeline coupling: never trigger the post orchestrator, and never let a
  card substitute for a format spec or a style profile — it feeds them.
- Purpose guard: if the user asks for outreach scoring, tiers, or outreach
  messages, say that's out of scope here and keep to strategy mining.
