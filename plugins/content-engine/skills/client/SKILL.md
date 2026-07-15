---
name: client
description: Load or build a client's context for content. Use when the user says "set up [client]", "load [client]'s context", "research this customer", "post for [name] from [company]", or when angles needs client context that doesn't exist yet. Resolves a named client against Virio publishers FIRST (content_publishers_list), then merges CRM (HubSpot/Attio) and live web research into one context file that serves every lane.
---

# Client context

Build one authoritative context file per client at `clients/<client-slug>/context.md` in the user's working folder. One store serves ALL lanes (abm, tofu, mofu, bofu) — a client researched once serves every post type.

The client can be the user themselves. "My content" / "personal post" → slug is the user; don't ask which client. The Virio `content_*` tools default to the caller's own settings when no user is passed, so the same build flow below applies unchanged.

## Step 0 — resolve the client in Virio FIRST (before any web search)

When the request names a person or company ("post for Doug from AICRO", "set up Vendelux"), your FIRST action is `content_publishers_list`, matched on the name, email, or company. This is the identity source of truth for our clients. It resolves who they are, which company they belong to, and — via `content_settings_get` — their strategy, tone, and ICPs, authoritatively.

- **Do NOT web-search to figure out who a named client is, and do NOT ask the user to disambiguate a company, before checking Virio.** Virio usually already knows. (Example: "Doug from AICRO" → `content_publishers_list` returns Doug Shankman / `doug@aicro.co`; his record even names the reference site, aicro.co. No web guess, no "which AICRO?" needed.)
- **Match found** → pull `content_settings_get`. That record is the SPINE of the context: strategy overview, active topics, banned topics, tone rules (formality, rhythm, banned phrases, AI-tells, custom instructions), and ICP personas. CRM and web research only fill gaps it doesn't cover.
- **No match, or the Virio connector is not connected** → say so in one line ("[name] isn't in Virio" or "the Virio connector isn't enabled here — turn it on in Customize → Connectors for grounded client resolution"), THEN fall back to CRM + web research. Never silently skip Virio and web-guess the identity.

## Resolution order

1. `clients/<slug>/context.md` — if it exists, load it. Updated within 30 days → offer to reuse as-is; otherwise refresh the volatile sections (news, live wires).
2. `abm-clients/<slug>/context.md` (legacy store from the old abm-engine) — same schema; if it exists, reuse it verbatim as the starting point and write the merged result to `clients/<slug>/context.md` (leave the legacy copy untouched).
3. Neither exists → build new into `clients/<slug>/context.md`.

## Sources — merge, don't pick one

1. **Virio content settings** (the spine — resolved in Step 0): `content_settings_get` for the matched publisher's strategy, tone rules (banned phrases, formality, AI-tell flags, custom instructions), and ICPs. Tone rules from Virio are HARD constraints downstream. This is not optional when the client is a Virio publisher — it is the first and primary source, not a maybe.
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

- Never identify or disambiguate a named client by web search before checking Virio. `content_publishers_list` is the client identity source of truth; web research is for gaps, not identity.
- Never overwrite an existing context file without showing the diff summary and asking.
- Time-box live research: ~5 searches per client refresh unless the user asks for a deep dive.
- Close by presenting the context file path and a 3-line summary, then hand back to the pipeline.
