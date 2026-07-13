---
name: angles
description: Propose ranked post angles for a client by crossing chosen formats against the client's context, fresh market research, and the lane directive (abm/tofu/mofu/bofu). Use when the user says "give me angles", "what should [client] post", "pick an angle", or after scout and client have run inside the post pipeline.
---

# Angles

Cross the chosen format(s) × client context × market moment × lane directive. Output: ranked angles the user picks from.

## Inputs (load all; run the missing skill if absent)

- `content-library/<library>/<lane>/` format specs (scout) — when the pipeline's format-pick step already ran, use only the user's chosen format(s), not the whole library
- `clients/<slug>/context.md` (client)
- The lane directive from `content-library/<library>/<lane>/config.md` — it sets the post's job, CTA strength, and proof level; every angle must be doable within it

## Market research (fresh each run)

- 3–5 web searches, shaped by the lane:
  - **abm**: the client's named target accounts (recent launches, hires, campaigns, IPO/funding news), plus the client's category this week.
  - **tofu**: what the ICP is talking/arguing about right now.
  - **mofu**: the problems and tools the ICP is actively evaluating.
  - **bofu**: the client's own recent wins, launches, and proof moments.
- Check the context file's Live wires section for anything still warm (≤ 3 weeks old).
- An angle without a "why now" is weak — every angle must ride a datable moment or a durable fascination (a rise story stays good for months; a campaign reaction dies in days).

## Building angles

An angle = format × subject × why-now, shaped by the lane. For each viable pairing write:

- **Subject**: what the post is about. Lane check — abm: the named person, account, team, or campaign the post glorifies or targets (must map to the client's ICP or a named target account); tofu: a topic the whole ICP cares about, client-agnostic on the surface; mofu: a problem/approach the client has real standing on; bofu: the client's own proof.
- **Format**: which library spec it uses.
- **Why now**: the news peg or durable hook, date-stamped.
- **Payoff**: what this earns at THIS lane — abm: who at the target account sees/amplifies it and what that earns (reply, tag, meeting context); tofu: follows and reach inside the ICP; mofu: saves, comments, resource requests from evaluators; bofu: demo/call/trial intent.
- **Risk**: what could make it fall flat — pandering, a claim the Canon can't back, a CTA too hard for the lane.

## Ranking

Score each angle 1–5 on: subject heat (is the moment live), format fit (does the subject actually fill the skeleton), ICP proximity (how directly the subject matters to the client's pipeline), and lane fit (does it do this lane's job — for abm, low pandering/backfire risk; for funnel lanes, CTA strength within the directive). Rank by total; show the scores — the math is visible, the user decides.

## Output

Present 5–8 angles as a ranked table. STOP and let the user pick before any drafting. Do not auto-run draft.
