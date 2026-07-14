# ICP research playbook

Query patterns and output detail for `icp-research`. Default: Clay or Exa (whichever is connected).

## Query patterns

**Look-alike from a seed account** (highest signal):
- `companies similar to <Example account> in <segment>`
- `<segment> startups like <Example account A> and <Example account B>`
- Add firmographic constraints: `... Series A or B ... US`

**Firmographic discovery** (broaden):
- `<stage> <segment> companies building <category>`
- `recently funded <segment> startups <year>`
- `<segment> companies hiring <role that implies the pain>`

**Per-account signal** (make it account-aware):
- `<company> funding round` · `<company> new <role> hire` · `<company> product launch`
- `<company> <pain keyword>` (e.g. `<company> outbound / pipeline / GTM`)
- Prefer recent results; record the date.

## Choosing the engine

| Need | Use |
|---|---|
| Build + enrich a target company list | **Clay** |
| "Find companies like X / doing Y" | **Exa** (semantic) |
| Recent trigger per account | Exa or Clay, then web fetch the source |
| Exact size/stage/geo/tech filters | Clay |
| Audience size / profiling | Watt (if connected) |
| No research connector available | Standard web search (rougher) |

## Output detail

For each target, fill all four fields. If a field can't be filled honestly, say so:

- **company** — the legal/brand name.
- **fit_reason** — tie to a specific ICP criterion or the seed it resembles ("like Parspec — Series A proptech, document-heavy workflow").
- **signal** — a dated, sourced trigger. If none found: `no fresh signal — use pain-based angle`.
- **angle** — `<trigger or pain> → <hook into the client's offer>`. One or two lines, no fabricated specifics.

## Anti-fabrication rules

- Never invent funding, headcount, customers, or quotes. Cite or omit.
- If the ICP names "Example accounts" that no longer fit (acquired, pivoted), flag it.
- Keep targets inside the Canon stage band; drop anything the client said to exclude.
