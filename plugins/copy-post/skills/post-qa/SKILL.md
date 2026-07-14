---
name: post-qa
description: >
  This skill should be used when the user wants to QA, de-slop, or brand-check a LinkedIn
  draft — "QA this post", "check this draft", "de-slop this", "is this on brand", "review
  this LinkedIn post before I publish". It enforces the client's context.md: it HARD-BLOCKS
  drafts that break a Canon hard constraint, invent Proof, or use the wrong voice, and
  FLAGS softer issues (AI-tells, style-spec drift, hook past the fold). Runs automatically
  inside copy-post before candidates are shown.
metadata:
  version: "0.1.0"
---

# post-qa

The gate. Check a draft against the client's `context.md` and the Style Spec, then return a clean draft plus a pass/flag report. Two severities: **hard block** (must fix or drop) and **flag** (fix if you can).

This gate serves ALL three engines: `copy-post` runs it as its final step, and `abm-draft` / `funnel-draft` run it as their QA gate (passing their engine-specific checks as extra flags).

## Inputs

- The draft (or candidates).
- The client context (Author, Proof status, Canon guardrails incl. `Conversion ask:` / `Do not post:`, Voice banned phrases, "Does NOT sound like"). Run `context-loader` if not already loaded.
- The Style Spec for the example being matched (the `avoid` list + skeleton), if one exists.
- The stage directive (from `funnel-classify` / `funnel-library` config), when the post has a funnel stage — this is what the CTA-mismatch flag checks against.
- Any engine-specific checks passed by the calling drafter (e.g. ABM payoff intact, skeleton match, names verified this run).

## Hard blocks (do not present a draft that fails these)

1. **Canon Hard constraint violated** — e.g. generic GTM advice with no proptech angle when Canon requires one. Block and say which constraint.
2. **Invented Proof** — any case study, metric, customer name, or result that isn't in context, when Proof is "None on record" or doesn't contain it. Block.
3. **Wrong voice** — speaks as someone other than the Author, or as the "Does NOT sound like" failure mode (e.g. an agency pitch when the brand is founder-to-founder). Block.
4. **Style-not-topic leakage** — reuses the example post's specific claims, names, numbers, or story as if they were the client's. Block.
5. **Out-of-scope target** — names or addresses an audience the Canon excludes (wrong stage, wrong geo). Block.

## Flags (fix in place, note what changed)

- **AI-tells** — run the full canonical list in `references/ai-tells.md` (the single source of truth for every engine; the drafters rewrite against it first, this is the backstop). Preserve any *intentional* staccato that the Style Spec marks as a signature move.
- **Hook past the fold** — first line over ~140 chars; tighten it.
- **Structural fidelity** — owned by `style-match`, which runs before this. Only re-flag here if a QA fix you made (e.g. trimming the hook, cutting an invented stat) broke the structure; otherwise trust the match score.
- **CTA mismatch** — CTA strength doesn't match the stage directive (a BOFU draft with no CTA, a TOFU draft with a demo ask). Fix to the directive; if the right CTA needs info you don't have (e.g. the Conversion ask is unknown), surface it instead.
- **Link in body** — move it to a first comment.

## Output

Return:

1. The **cleaned draft** (flags fixed).
2. A short **report**: hard blocks (with the rule and the fix needed), then flags fixed, then anything the user must decide.

If a hard block can't be fixed without information you don't have (e.g. a real metric to replace an invented one), do **not** silently rewrite it away — surface it and ask.
