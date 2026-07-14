---
description: Run the full ABM pipeline — library, format pick, client context, angles, drafts
argument-hint: [client / target account, plus anything else about the post]
---

Run the content engine's full pipeline with the post type already resolved to **abm**.

Read `${CLAUDE_PLUGIN_ROOT}/skills/post/SKILL.md` and follow it end to end. Step 0 is done — the type is abm; do not re-ask. Everything else applies unchanged: library pick, format pick, client context, angles, drafts, stopping at every decision point.

Request: $ARGUMENTS
