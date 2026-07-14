# Funnel stage map

How each stage shapes a LinkedIn post. Use this to turn a stage into drafting constraints.

This is the canonical cross-stage mapping for classification and drafting directives. The per-stage `funnel-library/<stage>/config.md` files carry the operational version of the same directive next to the format specs (plus library-only concerns: admission tests, refresh policy) — if either changes, keep the other consistent.

| Dimension | TOFU (reach) | MOFU (trust) | BOFU (convert) |
|---|---|---|---|
| **Job** | Get seen and resonate with a broad slice of the ICP | Show how you think; earn credibility | Move a warm reader to act |
| **Audience temp** | Cold | Warming | Warm / in-market |
| **Topic** | Relatable truth, contrarian take, industry observation | Teaching, frameworks, "how we do X" | Specific outcome, offer, case |
| **Skeleton bias** | hook → story/observation → takeaway | hook → problem → method → takeaway | hook → result/claim → proof → ask |
| **CTA strength** | None or soft ("what's your take?") | Soft (follow, comment, gated resource — no demo/call asks) | Hard — the client's Conversion ask (demo, call, trial, "DM me") |
| **Proof** | Optional | Soft (method, anonymized example) | Required — named result or credible process |
| **Voice** | Most personal / story-driven | Operator-teaching | Confident, specific |
| **Failure mode** | So broad it's generic | Reads like a brochure | Pitching a cold room |

## Tells (for the Check mode)

- **TOFU**: no offer named, ends open or with a discussion prompt, designed to be shared.
- **MOFU**: teaches a repeatable approach, hints at the offer without selling, soft CTA.
- **BOFU**: names the offer/result, has a clear ask (book a call, reply, link in first comment).

## Proof-empty rule (applies to all stages, bites hardest at BOFU)

If the client's `context.md` Proof section is "None on record":

- Do **not** invent metrics, case studies, or named wins.
- For BOFU, pivot the proof slot to **credibility/process** — the author's first-hand experience, the method, the specificity of the diagnosis — and flag to the user that no results can be cited yet.

## ABM note

For an ABM post built from `icp-research`, the stage is usually MOFU or BOFU and the post is account-aware (names the target's situation or trigger). Keep the CTA matched to how warm that account actually is — don't open with the hard ask to an account that's never heard of the client.
