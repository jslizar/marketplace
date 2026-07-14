---
name: client
description: Load or build a client's context for content. Use when the user says "set up [client]", "load [client]'s context", "research this customer", or when angles needs client context that doesn't exist yet. Resolves against the shared clients/ store (with legacy abm-clients/ as read fallback), merging Virio content settings (ICP/tone/strategy), CRM data (HubSpot/Attio), and live web research into one context file that serves every lane.
---

# Client context

Build one authoritative context file per client at `clients/<client-slug>/context.md` in the user's working folder. One store serves ALL lanes (abm, tofu, mofu, bofu) — a client researched once serves every post type.

The client can be the user themselves. "My content" / "personal post" → slug is the user; don't ask which client. The Virio `content_*` tools default to the caller's own settings when no user is passed, so the same build flow below applies unchanged.

## Resolution order

1. `clients/<slug>/context.md` — if it exists, load it. Updated within 30 days → offer to reuse as-is; otherwise refresh the volatile sections (news, live wires).
2. `abm-clients/<slug>/context.md` (legacy store from the old abm-engine) — same schema; if it exists, reuse it verbatim as the starting point and write the merged result to `clients/<slug>/context.md` (leave the legacy copy untouched).
3. Neither exists → build new into `clients/<slug>/context.md`.

## Sources — merge, don't pick one

1. **Virio content settings**: If the client is a Virio publisher (check `content_publishers_list`), pull `content_settings_get` for their strategy, tone rules (banned phrases, formality, AI-tell flags, custom instructions), and ICPs. Tone rules from Virio are HARD constraints downstream.
2. **CRM**: If HubSpot or Attio is connected, search for the client's company and recent deals/notes — pull industry, size, named target accounts, target segments, open opportunities.
3. **Live web research**: Company site, recent funding/product news, the client's own recent LinkedIn posts (via `read_linkedin_uri` on their profile — what already performs for them), competitors, and the accounts/categories they sell into.

## Context file sections (all required; write "unknown" rather than inventing)

- **Canon**: what the company does, one paragraph, in their own words. Hard facts only (funding, customers, numbers they publicly claim). Anything not here may NOT appear as a claim in drafts.
- **ICP / target accounts**: personas AND named accounts if known (named accounts drive the abm lane; personas drive the funnel lanes).
- **Voice**: tone rules, banned phrases, formatting habits, first-person quirks. Import Virio tone verbatim when available.
- **Proof**: real stats, case studies, named wins that drafts may cite. BOFU drafts lean on this section hardest — flag when it's thin.
- **Live wires**: current news hooks — their launches, their targets' launches, industry moments. Date-stamp each.
- **History**: links to their top 3–5 performing posts and what those have in common.

## Rules

- Never overwrite an existing context file without showing the diff summary and asking.
- Time-box live research: ~5 searches per client refresh unless the user asks for a deep dive.
- Close by presenting the context file path and a 3-line summary, then hand back to the pipeline.
