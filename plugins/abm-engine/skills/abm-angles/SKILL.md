---
name: abm-angles
description: Propose ranked ABM post angles for a client by crossing viral formats against the client's context and fresh market research. Use when the user says "give me angles", "what should [client] post", "pick an angle for [account]", or after abm-scout and abm-client have run inside the abm pipeline.
---

# ABM angles

Cross the format library × client context × market moment. Output: ranked angles the user picks from.

## Inputs (load both; run the missing skill if absent)

- `abm-library/` format specs (abm-scout) — when the pipeline's format-pick step already ran, use only the user's chosen format(s), not the whole library
- `abm-clients/<slug>/context.md` (abm-client)

## Market research (fresh each run)

- 3–5 web searches: the client's named target accounts (recent launches, hires, campaigns, IPO/funding news), plus the client's category this week.
- Check the context file's Live wires section for anything still warm (≤ 3 weeks old).
- An angle without a "why now" is weak — every angle must ride a datable moment or a durable fascination (a rise story stays good for months; a campaign reaction dies in days).

## Building angles

An angle = format × subject × why-now. For each viable pairing write:

- **Subject**: the named person, account, team, or campaign the post glorifies or targets. Must map to the client's ICP or a named target account — the subject's org (or its aspirants) is who the post is FOR.
- **Format**: which library spec it uses.
- **Why now**: the news peg or durable hook, date-stamped.
- **ABM payoff**: who at the target account sees/amplifies it and what that earns the client (reply, tag, meeting context).
- **Risk**: what could make it fall flat or read as pandering.

## Ranking

Score each angle 1–5 on: subject heat (is the moment live), format fit (does the subject's story actually fill the skeleton), ICP proximity (how directly the target account matters to pipeline), and safety (low pandering/backfire risk). Rank by total; show the scores — the math is visible, the user decides.

## Output

Present 5–8 angles as a ranked table. STOP and let the user pick before any drafting. Do not auto-run abm-draft.
