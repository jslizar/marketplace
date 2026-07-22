---
client: <slug>
type: creator-index
date: <YYYY-MM-DD of last update>
status: raw
title: "<Client> — creator roster"
run_id: <run that last touched this>
command: </content-engine:creators | null>
skills: [<from run-log resolver>]
plugins: [<from run-log resolver>]
connectors: [<from run-log resolver>]
---

# <Client> — creator roster

Up: [<Client>](../context.md)

> 🗺️ Creators mined for <client> — <N> carded, <N> dropped. Each row links to its strategy card. Updated <YYYY-MM-DD>.

## Roster

<Sorted by score, best first. "Last mined" tells you when a card goes stale.>

| Creator | Headline | Score | Outliers | Cadence | Last mined | Card |
|---|---|---|---|---|---|---|

## Dropped

<Every creator that discovery surfaced but the hard filters removed, with the
reason — so the next run doesn't resurface them and the filters stay auditable.>

| Creator | Reason |
|---|---|
| <name> | competitor — <company> is in <client>'s competitive set |
| <name> | inactive — <n> posts in last 90d |
| <name> | duplicate of <name> |

## Handoffs done

<Which creators got compiled into style profiles or format specs, with links —
so the same handoff isn't rebuilt twice.>

- <Creator> → style profile: [styles/<creator-slug>/profile.md](../../../styles/<creator-slug>/profile.md) (<YYYY-MM-DD>)
- <Creator> → format spec: [<spec name>](../../../content-library/virio/<lane>/<spec>.md) (<YYYY-MM-DD>)
