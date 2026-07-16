---
name: post
description: Front door of the unified content engine. Use when the user says "make a post", "run the content engine", "ABM post for [client]", "TOFU/MOFU/BOFU post", "awareness post", "nurture post", "conversion post", "find a viral format and write a post for [client/account]", or wants the full pipeline from format research through drafted posts. Replaces the former abm and funnel front doors. Orchestrates scout, client, angles, and draft in sequence.
---

# Content engine (orchestrator)

Run the full pipeline: post type → library → formats → format pick → client context → angles → drafts. Each stage is its own skill; read its SKILL.md when you reach it. Pause for a user decision between stages — never run the whole pipeline silently.

## Step 0 — resolve the post type FIRST

Nothing runs until the type is set. One of: **abm | tofu | mofu | bofu**. Resolve in this order:

1. **Explicit**: the user named ABM, TOFU, MOFU, or BOFU → use it.
2. **Inferable**: the ask maps cleanly — glorify/target a specific named account, person, team, or campaign → ABM; "awareness"/"reach"/"go viral" → TOFU; "nurture"/"problem"/"educate the ICP" → MOFU; "convert"/"close"/"case study post"/"demo" → BOFU. Propose the type in one line and proceed.
3. **Ambiguous**: ask one question — which type, with a one-line job description per option (ABM: make a named target amplify it; TOFU: earn reach with the ICP; MOFU: make the problem urgent and the approach credible; BOFU: convert existing intent).

The resolved type threads through everything below as `<lane>` (abm | tofu | mofu | bofu).

## Step 1 — pick the library

The engine reads formats from `content-library/<library>/<lane>/`. Three libraries ship with the plugin:

- **Virio** — corpus-mined library (from `viral_posts_all` for funnel lanes; the curated ABM post bank for the abm lane), kept fresh by the scheduled refresh task. Each lane holds the 15 curated specs plus up to 15 "Recent finds" — last week's Emerging batch, rolled in weekly (`cohort: rolled` in the spec frontmatter, listed in a separate index section).
- **Millie's list** — the curated bank from `Viral_Content_Bank.xlsx`; no auto-refresh, updated only when a new bank ships. Note: Millie's has no bofu formats (her BOFU tab is all ABM) — if the user picks Millie's + bofu, say so and offer Virio bofu or Millie's abm instead.
- **Emerging** — this week's proven posts: spec-lites deconstructed from LinkedIn winners of the last 7 days, refreshed every Saturday by the maintainer's viral scan. The live-signal option — freshest, least proven over time. Lanes are quality-gated and can run thin (or empty between install and the next scan) — if the picked lane is short, say so and offer Virio.

Resolution: if the user named a library ("use Millie's list", "from Virio", "emerging", "what's working this week") → use it. Otherwise ALWAYS ask — one question, three options, with a one-line description of each. Never silently default.

### Library seeding and auto-refresh (no plugin update required)

On first run (no `content-library/` in the working folder), seed ALL THREE libraries by copying `${CLAUDE_PLUGIN_ROOT}/library/` into `content-library/`, including `library/VERSION`.

On EVERY run (including the first, right after seeding), auto-refresh from the marketplace so the user never has to update the plugin to get new formats:

1. Fetch the remote version — one small file — with WebFetch:
   `https://raw.githubusercontent.com/jslizar/marketplace/main/plugins/content-engine/library/VERSION`
2. Compare it to local `content-library/VERSION`:
   - **Remote newer** → fetch each lane's remote `index.md` (`.../library/<library>/<lane>/index.md`), diff against the local index, and pull only the new/changed spec files from the same raw base (`.../library/<library>/<lane>/<file>.md`). Merge them into `content-library/`, then write the new value into `content-library/VERSION`. Apply silently — just one line afterward: "Refreshed format library to `<version>`." Additions and unpinned-example refreshes on unmodified specs auto-apply; ONLY pause to ask if a remote change would overwrite a spec the user pinned or edited (show that diff).
   - **Equal** → do nothing here, but still run the per-lane integrity check below. Equal VERSION does NOT mean the local library is correct — a `content-library/` seeded by an older plugin version can be stale or have the two libraries crossed while still carrying the current VERSION.
   - **Fetch fails** (offline, sandbox, rate limit) → use the local `content-library/` silently. No error, no nag. The bundled `${CLAUDE_PLUGIN_ROOT}/library/` is the offline/first-run fallback.

This version check is a cheap distribution mechanism (one file per run), not corpus mining — it is always allowed, unlike the external format-discovery sources which run only on explicit request.

### Per-lane integrity check (runs every request, even when VERSION matched)

Once the library and lane are chosen (Step 1 above + the lane from Step 0), verify the local lane against the source before reading formats from it. This is what heals a stale `content-library/` left by an older version — VERSION equality alone is not trusted for the lane you're about to use.

1. Fetch the remote lane index: `.../library/<library>/<lane>/index.md`. Compare its spec list to the actual `.md` files in `content-library/<library>/<lane>/`.
2. **Local matches the index** → proceed.
3. **Local is missing the folder, is empty while the index lists specs, or its spec filenames don't match the index** (the signature of a stale or crossed seed — e.g. `millies/tofu/` holding Virio's specs) → re-pull that lane's specs from the remote raw base (`.../library/<library>/<lane>/<file>.md`), overwrite the local lane to match the index, and write one line: "Repaired the `<library>` `<lane>` library." Preserve any spec the user pinned or edited (never clobber a pin).
4. **Remote index is 404 / has no specs** → this lane is intentionally empty (e.g. Millie's BOFU). That is not "broken": leave it, and apply the normal empty-lane handling (Millie's + BOFU → offer Virio BOFU). Never fabricate specs to fill it.
5. **Remote unreachable AND the local lane looks wrong** (empty/missing/mismatched) → re-seed just that lane from the bundled `${CLAUDE_PLUGIN_ROOT}/library/<library>/<lane>/`, which always matches the installed plugin version. Never fall through to a stale copy.

Cost is one index file for the single lane in use. The VERSION check handles bulk updates across all lanes; this catches the one lane you're using being stale or crossed.

## Pipeline

1. **Formats** (scout): Ensure `content-library/<library>/<lane>/` exists and has specs (seed + auto-refresh per Step 1). The local library is authoritative for the run — Virio lanes are refreshed on the maintainer's machine, pushed to the marketplace, and reach everyone else automatically via the run-start version check, so a non-maintainer's library is current by definition; never tell a non-maintainer their refresh failed. Only flag staleness (per the lane config's freshness window) when this machine runs the scheduled refresh task. Millie's lanes are curated — never flag staleness.
2. **Format pick**: The lane library is a repo of format specs. Choose the 3 best-fitting specs for THIS run and present them — each with its name, archetype, one source example (author, engagement, link), and a one-line "why it works". Selection rules: (a) fit first — match the client's ICP, the market moment, the lane directive, and anything the user said about the post's goal; (b) variety — the 3 must be structurally different (never three list-shaped or three story-shaped formats); (c) rotation — check recent drafts in `clients/<slug>/drafts/<lane>/` (each draft records its format in `format:` frontmatter) and avoid re-showing a format used in the client's last 2 runs at this lane unless it's clearly the best fit. Present the pick as an on-screen selection form, not a bare-names picker. If the visualize widget tool is available (mcp__visualize__show_widget): first call mcp__visualize__read_me with modules ["elicitation"], then render an elicitation form ('Format details' header) with a single-select card group — one card per format, each card carrying the format name (13px/500), a one-line archetype subtitle, a third line with the hook pattern plus the top example's author and engagement, AND a collapsed full-example block: a div (class "fmt-full") containing the entire example post text from the spec's "Top example — full post text" section, hidden by default and revealed when the card is selected. Add one small style block to wire the reveal: `.fmt-full{display:none; white-space:pre-wrap; font-size:12px; line-height:1.5; color:var(--text-secondary); margin-top:10px; padding:10px 12px; border-radius:8px; background:var(--surface-0); border:0.5px solid var(--border); max-height:340px; overflow-y:auto}` and `.elicit-pill[aria-pressed="true"] .fmt-full{display:block}`. The link to the original post goes in the card's TOP-RIGHT corner, always visible: the card's first row is a flex row with the title/subtitle block on the left and `<a href="{post_url}" style="font-size:11px; white-space:nowrap; margin-left:auto">View post ↗</a>` on the right. Include an 'Other' escape-hatch option ("Show me other formats"). The user selects a card and submits. If the widget tool is NOT available, fall back to printing a compact format card per option in chat followed by the question tool with those cards as option previews. Either way: STOP — the user picks one (or more) before anything else runs. If the user skips the form, proceed with the FIRST card (the best-fit format) and state that choice in one line before continuing — never a random pick, never a re-ask.
3. **Client context** (client): Load or build the client's context file from the shared `clients/` store. When a client or person is named, the client skill resolves them via Virio (`content_publishers_list`) FIRST — before any web search or company disambiguation. Only ask the user to clarify if Virio returns no match and the name is genuinely ambiguous; never web-guess a named client's identity when Virio can answer.
4. **Angles** (angles): Cross the CHOSEN format(s) — not the whole library — against the client context, market research, and the lane directive from `content-library/<library>/<lane>/config.md`. Present the angles as a compact ranked TABLE in the chat (rank, subject, format it pairs with, why-now, payoff, score) — never as a widget or card form. Ask for the pick with a plain question. STOP — the user picks the angle(s).
5. **Drafts** (draft): Draft 2–3 candidates for each chosen angle, shaped by the lane directive. De-slop, QA, then present every candidate in full in the chat, each with a one-line note.
6. **Pick the winner**: The candidates were just presented IN FULL in the chat by the draft step — every candidate's complete text on screen, labeled (A/B/C) with its hook phrase and one-line note. Never hide a draft behind a card, a collapsed reveal, or a "tap to read" — the user must be able to read every candidate without interacting. Then ask which one to ship with a PLAIN question (the question tool, short option labels only: "A — <hook phrase>"; no draft text inside the options, and never the elicitation widget at this stop). STOP — the user picks. Record the choice in the run's `picked:` field via `run-log`. If the user skips, treat the first candidate as picked and say so in one line.
7. **Graphic prompt** (graphic-prompt, offered — default yes): Offer to generate a paste-ready Claude graphic prompt for the selected post. If the user wants it, run the graphic-prompt skill on the picked draft. "No graphic" skips cleanly — never force it.

## Rules

- The on-screen elicitation widget is used at exactly ONE stop: the format pick (Step 2). Every other decision point — angles, winner pick, graphic offer — puts its content directly in the chat (tables, full draft text) and asks with a plain question. Anything the user needs to READ to decide must be visible without tapping.
- Ask which client before doing anything else (after type + library resolution) if it isn't obvious from the request.
- If the user enters mid-pipeline (e.g. "draft a MOFU post for Acme in the gated-playbook format from Millie's list"), skip completed stages — a named format skips the formats stage and the format pick; a named type skips Step 0; a named library skips Step 1.
- Surface intermediate outputs compactly: formats as a short table (name, archetype, engagement, why it works), angles as a ranked list with the format each pairs with.
- Every stage that produces a file saves into the user's working folder, never into the plugin directory.
- Data boundaries are hard: funnel-lane discovery reads ONLY `viral_posts_all` in Supabase — never `viral_posts` (the user's personal-content bank). ABM-lane discovery uses the curated ABM bank and Apify. Millie's library is never auto-refreshed from any corpus. Emerging is written only by the maintainer's weekly viral scan — pipeline runs never add to it; deconstructing a new post mid-run specs into Virio, not Emerging.
