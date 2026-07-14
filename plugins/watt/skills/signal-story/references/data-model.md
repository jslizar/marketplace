# Signal-story spec — schema & Watt mapping

A story spec is one JSON object. `build_story.py` turns it into the two-page
HTML. Inline markup in any text field: `**bold**`, `*italic*`, `_italic_`; raw
HTML is allowed too. Use real characters (→ ÷ × ≤ ·) to match the reference.

## Top level

```json
{
  "title":  "Winning back the pizza buyer",     // <title> + fallback
  "footer": "CASE STUDY: PIZZA HUT MARKETING STRATEGY",  // left footer, every page
  "icp":    { "id": "dtc-agency", "label": "DTC marketing agency" },  // optional reader
  "pages":  [ { "blocks": [ ... ] }, { "blocks": [ ... ] } ]
}
```

`pages` is an ordered list; each page renders as one US-Letter sheet with an
auto footer (`PAGE i / n`). Default split: page 1 = masthead → map, page 2 =
playbook → method.

## Block types

Each entry in a page's `blocks` array has a `type`. Fields per type:

### masthead
```json
{ "type":"masthead", "eyebrow":"WATT · CUSTOMER STRATEGY",
  "title":"Winning back the pizza buyer",
  "dek":"A high-intent audience for Pizza Hut, and a state-by-state read …" }
```

### section_head — lime square bullet + heading + optional lead paragraph
```json
{ "type":"section_head", "title":"The audience", "lead":"The widest credible pool …" }
```

### stats — a row of 3 stat cards (`hero:true` paints one lime)
```json
{ "type":"stats", "items":[
  {"num":"13.2M","label":"US adults · measured reach","hero":true},
  {"num":"Pizza","label":"Required of everyone (the gate)"},
  {"num":"4 of 8","label":"Signals kept, rest dead weight"} ] }
```

### composition — the signal stack
```json
{ "type":"composition", "title":"Composition",
  "required":{"name":"Pizza interest","tag":"(required)"},
  "kept":["Value shoppers","Coupon enthusiasts","Households with teens","Food-delivery users"],
  "note":"Curbside pickup … were dropped: each added under 5% new reach …" }
```

### map — choropleth + legend
```json
{ "type":"map",
  "intro":"(optional lead line above the map)",
  "states":{"FL":106,"WA":91,"TX":96, "...":0},
  "legend_used_only":false }
```
- `states`: USPS code → numeric index. Omitted/`null` states render tan
  ("low sample").
- Default scale (neutral, centred on an index of 100): `≥120` over-indexes (purple),
  `105–119` above average, `95–104` on par, `85–94` below average, `≤84` under-indexes
  (orange). The default is deliberately **story-agnostic** — pass your own `scale` with
  story-specific labels (the dine-in/delivery names live in the Pizza Hut example, not
  the engine). Override per story:
  ```json
  "scale":[{"label":"High (≥120)","color":"#8e7cc9","min":120,"max":null}, …],
  "low":{"label":"No data","color":"#cdc4a5"}
  ```
- `legend_used_only:true` shows only buckets that actually appear.

### chart — on-brand bar chart (the visual when there's no map)
```json
{ "type":"chart",
  "title":"The lift, side by side",          // optional → renders a section head
  "lead":"One line on what the bars show.",   // optional
  "bars":[ {"label":"Value shoppers","value":33,"display":"33×"},
           {"label":"Fast food","value":3.8,"display":"3.8×"} ],
  "baseline":1, "unit":"×",                   // optional dashed reference line
  "note":"Lift vs the US-adult base; 1× = no over-index." }
```
Horizontal bars; the largest is lime, the rest lavender. `display` overrides the
printed value. Every story should have a `map`, a `chart`, or a `table` — never zero visuals,
and never a map that isn't a geographic finding.

### table — a compact data table (the visual for a small matrix)
```json
{ "type":"table",
  "title":"Top states by index",          // optional → renders a section head
  "lead":"One line on what the rows show.", // optional
  "columns":["State","Index","Read"],
  "rows":[["Wisconsin","125","Rally hotbed"],["California","70","Cold"]],
  "note":"Optional footnote." }
```
Mono uppercase headers, hairline rows. Use it when the finding is a small set of
rows — not a geography (`map`) and not a comparison/trend (`chart`). **Never** use a `table` for a set of
categories or segments — those are the colored cards (`clusters`). Reserve `table`
for a flat matrix that isn't a grouping.

### clusters — 2–3 playbook columns
```json
{ "type":"clusters", "items":[
  {"theme":"dinein","label":"Lead with dine-in",
   "chips":[{"name":"Florida","value":106},{"name":"Ohio","value":103}],
   "desc":"Keep and refresh physical restaurants …"},
  {"theme":"hybrid","label":"Hybrid footprint","chips":["New York","Illinois"],"desc":"…"},
  {"theme":"ghost","label":"Lead with ghost kitchens","chips":[{"name":"Texas","value":96}],"desc":"…"} ] }
```
`theme` ∈ `over | mid | under` sets the column's top-border + chip colors (legacy
`dinein | hybrid | ghost` still accepted). This is the format for **any** set of named categories or
segments — a playbook, a set of audiences, tiers, personas — not only a geographic
playbook. Categories are always these colored cards, never a `table`.
A chip is `{"name","value"}` or a bare string.

### recs — recommendation bullets (optional `title` renders a section head)
```json
{ "type":"recs", "title":"What we'd recommend to LongRange", "items":[
  {"lead":"Re-acquire on value, not novelty.","body":"The audience is anchored on …"} ] }
```

### callout — lavender pull-quote
```json
{ "type":"callout", "lead":"Read the map as format mix, not presence.","body":"Texas and California …" }
```

### method — monospace methodology note
```json
{ "type":"method", "text":"METHOD: Audience and channel splits measured on the Watt Signal Graph …" }
```

## ICP targeting

A story can be drafted for a specific reader — an **ICP**. The reader is recorded
in an optional top-level `icp` object and is otherwise expressed *through the
existing editorial blocks*: there is no ICP-specific block type, and the builder
treats `icp` as provenance (it reads only `title`, `footer`, `pages`).

```json
"icp": { "id": "dtc-agency", "label": "DTC marketing agency", "for": "Maxwell & Vine" }
```

- `id` — matches a profile in `references/icps/`; also the `--<icp>` suffix on the
  output filename.
- `label` — the reader, stamped into the masthead `eyebrow` and/or `footer`.
- `for` *(optional)* — a named account, e.g. the agency or brand this copy is for.

**What the ICP changes — and what it never does.** The lens rewrites only the
editorial fields (`masthead` title/dek/eyebrow, `recs`, `callout`, `clusters`
labels and `desc`, `footer`, and which beat leads). The data fields (`stats`
numbers, `composition`, `map.states`, `chart.bars`) are **identical across every
variant of the same story** — same evidence, re-narrated. The field → block map for
a profile is in `references/icps/_schema.md`.

**Additive ICP evidence (optional).** When a report needs a hard ICP-specific
number, a profile's `evidence_hook` adds one extra `stats` card or `chart` from a
single additive Watt cross-read. Mark it as an ICP read in its `label` so it reads
as layered on top of the base finding — never folded into the core composition or
reach.

## The summary card (`card`)

An optional top-level `card` object curates the **square social summary**
(`build_card.py`) — the 1:1 LinkedIn one-pager. It changes nothing about the
report; it selects and tunes what the card shows.

```json
"card": {
  "eyebrow": "Case study · Pizza Hut marketing strategy",
  "title": "Winning back the pizza buyer",
  "dek": "A state-by-state read on where to defend dining rooms versus run ghost kitchens.",
  "stats": [
    { "num": "13.2M", "label": "High-intent US audience", "hero": true },
    { "num": "~4×",   "label": "Delivery over dine-in intent" },
    { "num": "23",    "label": "States scored on the index" }
  ],
  "footer": "WATT · CASE STUDY",
  "footer_right": "Index = dine-in share ÷ delivery share × 100"
}
```

- `eyebrow` / `title` / `dek` — the hero; default to the `masthead`'s. Keep the
  dek tighter than the report's — it's a social caption.
- `stats` — the **three** cards (`hero:true` paints one lime). Pick the most
  postable numbers; they need not match the report's audience stats, but each
  must still trace to the data. Defaults to the first `stats` block.
- `footer` (left, with the lime tick) and `footer_right` (e.g. the index
  formula). Mono labels are uppercased by the design system — write sentence case.
- `map` *(optional)* — override the map block for the card; defaults to the
  story's map, and falls back to the first `chart` block when there's no map.

The card is square (1080×1080) and self-contained; `build_card.py --png`
rasterizes a 2160px image for posting.

## Voice (editorial fields)

Every editorial field (titles, deks, leads, stat labels, notes, cluster labels and
descriptions, recs, callout, method, and the `card` copy) clears the **voice pass**
before it ships: the antislop rules in
`${CLAUDE_PLUGIN_ROOT}/skills/watt-antislop/` and the Watt-voice rules in
`references/voice/`. No
em-dashes, no "not X, it's Y," no corporate-speak; say *signal*, not data. The
render gate `scripts/voice_check.py` enforces the two kill-on-sight tells, and the
renderers refuse to build a spec that carries one. Data fields (numbers, codes,
colors) are exempt.

## Mapping Watt outputs → blocks

| Story field | Where it comes from in Watt |
|---|---|
| `stats` reach (audience) | the measured reach from `audience-generate` / the record file's `reach` header |
| `composition.required` / `kept` | the signal-stack record CSV: `role=must-have/defining` → required/kept; `role=…` names ride beside the hashes |
| `composition.note` (dropped + why) | signals considered but cut for <X% marginal reach — from the assembly trace / your generate notes |
| channel `stats` (crossed reaches, ratio) | two cross-audiences (e.g. pizza×delivery vs pizza×dine-in) measured in the session; ratio = one ÷ the other |
| `map.states` index | a `group`/`analyze` step by state, or raw per-state shares you convert to an index `(share_A ÷ share_B) × 100` |
| `clusters` | bucket the same per-state index into 2–3 strategic plays |
| `recs`, `callout`, `title`, `dek` | editorial — draft from the data + client context, or through the chosen ICP profile (`references/icps/`), then confirm |
| `method` | how the audiences were measured (sample sizes, refresh date, index formula); keep honest about low-sample states |

Never invent figures. If a beat has no data, omit it rather than guessing.
