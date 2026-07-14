---
description: Run the full funnel pipeline (TOFU/MOFU/BOFU) — library, format pick, client context, angles, drafts
argument-hint: [stage + client, plus anything else about the post]
---

Run the content engine's full pipeline for a funnel post.

Read `${CLAUDE_PLUGIN_ROOT}/skills/post/SKILL.md` and follow it end to end. Step 0 is constrained to the funnel lanes: resolve the type to tofu, mofu, or bofu from the request below (per the skill's Step 0 rules) — if it doesn't name or imply a stage, ask which of the three, then continue. Never resolve to abm from this command; if the request is actually an ABM play, say so and point to `/content-engine:abm`. Everything else applies unchanged, stopping at every decision point.

Request: $ARGUMENTS
