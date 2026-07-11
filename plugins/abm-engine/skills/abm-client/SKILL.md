---
name: abm-client
description: Load or build a client's context for ABM content. Use when the user says "set up [client] for ABM", "load [client]'s context", "research this customer", or when abm-angles needs client context that doesn't exist yet. Merges the saved client file, Virio content settings (ICP/tone/strategy), CRM data (HubSpot/Attio), and live web research into one context file.
---

# ABM client context

Build one authoritative context file per client at `abm-clients/<client-slug>/context.md` in the user's working folder.

## Source order — merge, don't pick one

1. **Existing file**: If `abm-clients/<slug>/context.md` exists, load it. If updated within 30 days, offer to reuse as-is; otherwise refresh the volatile sections (news, live wires).
2. **Virio content settings**: If the client is a Virio publisher (check `content_publishers_list`), pull `content_settings_get` for their strategy, tone rules (banned phrases, formality, AI-tell flags, custom instructions), and ICPs. Tone rules from Virio are HARD constraints downstream.
3. **CRM**: If HubSpot or Attio is connected, search for the client's company and recent deals/notes — pull industry, size, named target accounts, open opportunities.
4. **Live web research**: Company site, recent funding/product news, the client's own recent LinkedIn posts (via `read_linkedin_uri` on their profile — what already performs for them), competitors, and the accounts they're selling into.

## Context file sections (all required; write "unknown" rather than inventing)

- **Canon**: what the company does, one paragraph, in their own words. Hard facts only (funding, customers, numbers they publicly claim). Anything not here may NOT appear as a claim in drafts.
- **ICP / target accounts**: personas AND named accounts if ABM targets are known.
- **Voice**: tone rules, banned phrases, formatting habits, first-person quirks. Import Virio tone verbatim when available.
- **Proof**: real stats, case studies, named wins that drafts may cite.
- **Live wires**: current news hooks — their launches, their targets' launches, industry moments. Date-stamp each.
- **History**: links to their top 3–5 performing posts and what those have in common.

## Rules

- Never overwrite an existing context file without showing the diff summary and asking.
- Time-box live research: ~5 searches per client refresh unless the user asks for a deep dive.
- Close by presenting the context file path and a 3-line summary, then hand back to the pipeline.
