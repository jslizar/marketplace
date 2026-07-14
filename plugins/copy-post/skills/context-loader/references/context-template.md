# Context file schema — field meanings and downstream use

The canonical template lives at `clients/_template/context.md` — copy THAT file to scaffold a new client. This reference documents what each section means and which skill consumes it. Do not maintain a second template here; if the schema changes, change `clients/_template/context.md` and this doc together.

## Sections (seven, in this order)

1. **Canon** — what the company does in their own words; hard facts only (funding, customers, publicly claimed numbers). Also carries positioning lines and the guardrails:
   - `Conversion ask:` — the exact person + action that counts as a win; this is the BOFU CTA.
   - `Positioning:` / `Competitive:` — who they're against.
   - `Hard constraint:` / `INTERNAL ONLY` / `Do not post:` — non-negotiables; `post-qa` hard-blocks violations.
   Anything not in Canon or Proof may NOT appear as a claim in drafts.
2. **ICP / target accounts** — Firmographics, Decision makers, Example/named accounts (named accounts drive the ABM engine; personas drive the funnel engine), Pains, Triggers.
3. **Voice** — `Author:` (the only content face unless noted), Register, banned phrases + tone rules (HARD constraints; import Virio/Lineage tone verbatim when available), Signature moves, "Does NOT sound like", Watch-out.
4. **Pillars** — 3–5 content themes. If undocumented, say so and list `Likely…` themes to confirm.
5. **Proof** — real stats, case studies, named wins drafts may cite — or "None on record". Items marked `UNVERIFIED` are not citable until confirmed.
6. **Live wires** — date-stamped current news hooks. Volatile; refresh at draft time.
7. **History** — links to top 3–5 performing posts and what they share.

## How each field is used downstream

| Field | Used by | For |
|---|---|---|
| Canon → Conversion ask | `copy-post`, `funnel-draft` | The BOFU CTA |
| Canon → Hard constraint / Do not post / INTERNAL ONLY | `post-qa` | Hard block on violation |
| ICP → Example / named accounts | `icp-research`, ABM engine | Look-alike seeds; ABM subjects |
| ICP → Firmographics / Triggers | `icp-research` | Search filters + the angle |
| Voice → Author | `copy-post`, `post-qa` | Who the post speaks as; reject other voices |
| Voice → banned phrases | drafters, `post-qa` | Hard constraint check |
| Voice → Does NOT sound like | `post-qa` | Off-brand failure check |
| Pillars | `copy-post`, `funnel-angles` | Topic fit |
| Proof status | `post-qa` | "None on record" → block invented results |
| Live wires | `abm-angles`, `funnel-angles` | Why-now pegs |
| History | angles/drafters | What already performs for them |

## Honesty markers (keep these literal)

- `unknown` — section not yet built.
- `Not documented` — unknown; needs a strategy session or brand kit.
- `None on record` — confirmed empty (e.g. no case studies yet).
- `Likely …` — inferred, not confirmed. Usable but flagged.
- `not confirmed` / `UNVERIFIED` — an assumption or claim to verify before use.
