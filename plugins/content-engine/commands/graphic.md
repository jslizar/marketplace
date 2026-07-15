---
description: Turn a chosen post into a paste-ready Claude graphic prompt
argument-hint: [paste the post, or name the draft to make a graphic for]
---

Generate a graphic prompt for a post without running the full pipeline.

Read `${CLAUDE_PLUGIN_ROOT}/skills/graphic-prompt/SKILL.md` and follow it. The post to make a graphic for is in $ARGUMENTS — the pasted post text, or a reference to a saved draft in `clients/<slug>/drafts/`. If it's empty or ambiguous which post, ask which one and stop.

Request: $ARGUMENTS
