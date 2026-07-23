---
client: <slug>
type: creator-card
date: <YYYY-MM-DD>
status: raw
title: "<Creator Name> — creator strategy card"
run_id: <YYYY-MM-DD-<client>-creators-NN>
command: </content-engine:creators | null>
skills: [<from run-log resolver>]
plugins: [<from run-log resolver>]
connectors: [<from run-log resolver — supabase|apify|exa, whichever actually answered>]
sources: [<queries run + URLs actually read>]
creator: <Creator Name>
creator_slug: <kebab-full-name>
linkedin_url: <https://www.linkedin.com/in/...>
followers: <n | "[unverified]">
mode: <discover | single-link | list>
score: <n>/10
---

# <Creator Name> — creator strategy card

Up: [Creator roster](index.md)

> 🕵️ Strategy card for <client>: <one line — who this is, why they made the cut, which sources answered, mined <YYYY-MM-DD>>.

## Profile

<Name, headline, company, followers, profile URL — each with its source
(apify author metadata | corpus row | web). `[unverified]` where no source
answered. Never estimated.>

## Metrics snapshot

<Posts/90d · median reactions across the recent sample · outlier count
(corpus + live) · engagement-rate proxy (marked `[unverified]` if followers
are) · score breakdown: consistency n/4 + engagement n/3 + activity n/2 +
relevance n/1. Every number traces to a row listed below.>

## 15 most recent posts

<Table, newest first. Fewer than 15 available → state the actual count and why.>

| # | Date | Hook (first line, verbatim) | Type | Reactions | Comments | URL | Source |
|---|---|---|---|---|---|---|---|

## Top viral posts

<Up to 5, best first. Per post: verbatim hook as a blockquote ·
reactions / comments / reposts · engagement_score (corpus rows only) ·
posted date · URL · source (corpus: viral_posts_all | outlier / live outlier)
· one line on why it hit. If nothing verifiable: "No verifiable viral posts
found (corpus miss; live sample shows no outliers)." Never padded.>

## Winning posts — full text

<Full post text verbatim for up to 5 winners, each under its own `### <hook>`
heading with the post URL. This is what feeds post-deconstruct / style-library
without re-scraping.>

## Strategy read

<Derived only from the rows above — no vibes:
- **Cadence** — posts/week from the recent-sample dates
- **Format mix** — text / image / video / document split; corpus `format_archetype` where available
- **Hook patterns** — quote 2–3 verbatim opening lines and name the pattern
- **Pillars** — the 3–5 topics they actually post about
- **Tone** — analyst / practitioner / provocateur / educator
- **CTA habits** — what they ask for, how often
- **Outliers vs baseline** — what separates their viral posts from their median post>

## How to copy this for <client>

<3–5 bullets: which patterns transfer to <client>'s voice and pillars, what
NOT to copy (off-ICP, off-voice, breaks a Canon hard constraint), and which
client pillar each transferable pattern maps to. If context.md was missing,
this section is generic and says so.>

## Provenance & caveats

<Queries run, sources that were down or returned thin, every `[unverified]`
field listed, shelf life (engagement data decays — re-mine after ~4 weeks).>
