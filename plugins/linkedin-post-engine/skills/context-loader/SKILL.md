---
name: context-loader
description: >
  This skill should be used when the user wants to load, check, or set up a client's
  context for LinkedIn content — "load context for a client", "set up a new client",
  "create a context file", "what do we know about this client", "check this context file",
  or whenever another LinkedIn Post Engine skill needs a client's context. It reads the
  client's context.md file, validates the required sections, honestly flags gaps, and
  can scaffold a new context file from the template. It never overwrites the file without
  asking — the user owns it.
metadata:
  version: "0.1.0"
---

# context-loader

Load and maintain the per-client `context.md` that every other LinkedIn Post Engine skill reads. The user owns this file; this skill reads it, checks it, and can scaffold a new one — it does not silently rewrite it.

## Locate the file (auto-discover — don't ask for a path)

Context files live in a `clients/` folder inside the **Cowork project folder** (the local folder backing the project). A Cowork project is backed by that folder, so it's readable by path. Find the file without making the user paste a path:

1. Glob the connected project folder for `**/clients/*/context.md` (also check a top-level `clients/<name>/context.md`).
2. Match the requested client to a folder slug (`aicro`, `self`, …); resolve obvious variants ("AICRO" → `aicro`).
3. If exactly one match, use it. If several, list them and ask which. If the project has no `clients/` folder at all, then — and only then — ask the user where it lives, or offer to scaffold it. Remember the resolved location for the session.

If the named client file does not exist, offer to scaffold one (see **Scaffold a new client**).

## Read and parse

A `context.md` has seven sections. Parse each:

1. **Canon** — hard facts and guardrails: what the company does in their own words, positioning, funding, publicly claimed numbers. Pull the `Conversion ask:` line (this is the BOFU CTA), any `Positioning:`/`Competitive:` line, and any hard guardrails (`Hard constraint:`, `INTERNAL ONLY`, `Do not post:`). Anything not in Canon/Proof may NOT appear as a claim in drafts.
2. **ICP / target accounts** — Firmographics, Decision makers, **Example accounts / named accounts** (seeds for `icp-research`; named accounts drive the ABM engine), Pains, Triggers.
3. **Voice** — **Author** (the only content face unless noted), Register, banned phrases and tone rules (HARD constraints, often imported verbatim from Virio/Lineage), Signature moves, "Does NOT sound like", Watch-out.
4. **Pillars** — 3–5 content themes (may be undocumented + "likely" themes).
5. **Proof** — real stats, case studies, named wins drafts may cite — or "None on record". Watch for `UNVERIFIED` items: not citable until confirmed.
6. **Live wires** — date-stamped current news hooks. Usually "unknown — refresh at draft time"; treat as volatile.
7. **History** — links to their top performing posts and what they share. Often "unknown" until seeded.

The canonical template is `clients/_template/context.md`; `references/context-template.md` documents how each field is used downstream.

## Honesty convention — treat gaps as gaps

The format deliberately marks what is **known**, **inferred** ("Likely…"), or **missing** ("Not documented", "None on record", "not confirmed"). Preserve that distinction:

- Never fabricate to fill a gap. If Proof says "None on record", downstream drafts must not invent case studies or metrics.
- Treat "Likely…" pillars/competitors as provisional — usable, but flag them as unconfirmed when handed downstream.
- Surface gaps to the user rather than silently papering over them.

## Validate and report

After parsing, give the user a short readout:

- Which sections are solid, which are inferred, which are missing.
- Any `Hard constraint:` lines (these become hard blocks in `post-qa`).
- The Author (so drafts speak as the right person) and the Conversion ask.
- The top 1–2 gaps worth filling before drafting (e.g., "Proof is empty — drafts can't cite results").

Keep it tight. Do not lecture; just orient the next step.

## Scaffold a new client

When setting up a new client, copy `clients/_template/context.md` to `clients/<name>/context.md` and fill in whatever the user provides. Leave unknown fields with explicit honesty markers ("Not documented", "None on record") rather than guesses. Create the companion `examples/` and `style-specs/` folders. Confirm the file with the user before treating it as authoritative.

## Maintain — never auto-overwrite

The user owns the file. You may **suggest** edits (e.g., "add the case study you just mentioned to Proof") and, only with explicit confirmation, apply them. Append, don't replace, unless asked. When in doubt, show the proposed change and wait.

## Hand off

Return the parsed context to the requesting skill: Author + Voice for drafting, ICP + Example accounts for `icp-research`, Pillars for topic fit, Conversion ask (from Canon) for BOFU CTAs, Live wires for angle freshness, and Canon guardrails + Voice banned phrases + Proof status for `post-qa`.
