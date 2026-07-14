---
name: icp-research
description: >
  This skill should be used when the user wants to find target companies for a LinkedIn
  post — "find target companies", "research my ICP", "find ABM accounts for a client",
  "who should this post target", "find companies like a named account", or when an
  ABM-style example needs to be aimed at the client's ICP. It reads the ICP from the
  client's context.md, uses Clay and Exa (whichever is connected) to discover matching
  companies and a recent signal per account, and returns a target company set with a
  per-account angle for the drafter.
metadata:
  version: "0.1.0"
---

# icp-research

Find the companies a post should target and the angle for each. Powers the "ABM style → my ICP" path: take an account-aware post style and aim it at real companies that fit the client's ICP.

## Inputs

- The client's **ICP** block from `context.md` — Firmographics, **Example accounts**, Pains, Triggers. (Run `context-loader` first if not already loaded.)
- Or a **named account** (pure ABM): research that one company.

## Tools

**Clay** and **Exa** are the two research tools — use whichever is connected, and both when available. **Clay** builds and enriches the target company list (waterfalls across data providers, including firmographic filters); **Exa** does semantic look-alikes ("companies like X / doing Y") and pulls recent signals. If neither is connected, fall back to standard web search (rougher). Narrate what you searched and what came back.

## Workflow

1. **Seed from Example accounts.** Use the named Example accounts as look-alike seeds: Exa (semantic "similar to") or Clay (find + enrich similar companies), constrained by the Firmographics (segment, stage, size, geo). This is the highest-signal path — the user already told you what "good" looks like.
2. **Broaden with firmographics.** Run ICP-criteria searches (e.g. "Series A/B proptech companies building <category>") to widen beyond the seeds.
3. **De-dupe and shortlist.** Merge results, drop the client itself and obvious mismatches, keep the best 5–15 (or the count the user asked for).
4. **Pull a per-account signal.** For each shortlisted company, search Exa or Clay for a recent **trigger** (funding, hiring, launch, leadership change, public pain) that matches the ICP Triggers. This is what makes the post account-aware.
5. **Write the angle.** For each account, capture: the trigger, the pain it implies, and the hook into the client's offer. Keep it to a line or two.

Query patterns and the output shape are in `references/research-playbook.md`.

## Output: target company set

```
client: <name>
icp_summary: <one line>
targets:
  - company: <name>
    fit_reason: <why it matches the ICP / which seed it resembles>
    signal: <recent trigger, dated>
    angle: <pain → hook into the offer>
  - ...
sources: [<links>]
```

Hand this to `copy-post`, which can produce **one segment-level post** (speaks to the pattern across the set) or a **batch** (one account-aware post per target).

## Guardrails

- US-only, company targets that match the ICP stage — respect any Canon "who to exclude" (e.g. "not pre-seed, not enterprise").
- Don't invent signals. If no recent trigger is found for a company, say "no fresh signal" rather than inventing one — the drafter will fall back to a pain-based angle.
- Cite sources for every signal so the user can verify before posting.
