---
name: signal-story
description: >
  Turn Watt audience data into a branded two-page "signal story" — the
  Pizza-Hut-style strategy case study (masthead, stat cards, signal-composition
  box, US choropleth, market-playbook columns, recommendations, method note) as
  a self-contained HTML file plus a print-ready PDF. Use when the user says
  "signal story", "make a signal story", "turn this Watt data into a report /
  case study", "build the Pizza Hut style report", "Watt narrative / one-pager",
  "write up this audience", or pastes/uploads a Watt report or audience data and
  wants it formatted. Pulls numbers from a live Watt session in the chat or from
  a pasted/uploaded report; renders through the watt-brand-kit design system.
---

# Signal Story

Build a Watt **signal story**: a two-page, on-brand strategy document generated
from audience data. Output is a single self-contained `.html` file and a
matching `.pdf`. The look (colors, type, components) is fixed by the
`watt-brand-kit` skill; this skill owns the **storyline** and the **data
mapping**.

## The fixed storyline

Every signal story follows this arc. Keep the order; drop a beat only if there
is genuinely no data for it.

1. **Masthead** — eyebrow tag, headline, one-line dek.
2. **The audience** — 3 stat cards (measured reach, the required "gate" signal,
   signals kept "X of Y") + a composition box (required signal, kept signals as
   chips, and the *why* for what was dropped).
3. **The channel reality** — a cross-audience read: 2–3 stat cards (e.g. two
   crossed reaches and their ratio).
4. **The visual** — the data-fit graphic for the finding: a `map` (a geographic
   index), a `chart` (a comparison or trend), or a `table` (a small matrix). Use
   the choropleth only when the story is actually about geography.
5. **Market playbook** — 2–3 cluster columns grouping states into plays.
6. **Recommendations** — bold-lead bullets addressed to the client, plus an
   optional lavender callout that adds nuance.
7. **Method** — the monospace methodology note.

Page 1 holds beats 1–4; page 2 holds beats 5–7. This mirrors the reference and
fits US Letter at the brand-kit's density.

## ICP targeting

A signal story can be drafted **for a specific reader** — an ICP. The data never
bends to the ICP; the *story* does. Same reach, same map, same composition — but
which finding leads, how it's worded, and what action it drives are tuned to who's
reading. Profiles live in `references/icps/` (see `references/icps/_schema.md`);
two ship today — `dtc-agency` and `dtc-brand`.

Two modes, and the order matters:

- **Framing (default).** The ICP is a lens on the *editorial* blocks only —
  masthead, recs, callout, the beat you lead with. A draft-layer move; it needs no
  new data, and this is where ICP targeting lives by default.
- **Evidence (only if asked for).** When framing isn't enough and the report needs
  a *hard ICP-specific number*, the profile's `evidence_hook` names one additive
  Watt cross-read. It is layered on the honest finding and labelled as an ICP read
  — never a reweighting of the core audience.

**The core search stays ICP-blind.** Build the audience for what it actually is
*before* any ICP is chosen — letting the ICP steer the search is how you start
fishing for the evidence that flatters it. Choose the ICP after the data is in.

## The square summary card

Alongside the two-page report, the same spec renders a **square (1:1) summary
card** — a social one-pager for LinkedIn in the same design system: the dark
hero, the lime hero-stat, the choropleth, and the WATT footer on a 1080×1080
canvas. It's built by `scripts/build_card.py` from the *same* story spec, so the
report and the card never drift.

Curate it with an optional top-level `card` object (schema in
`references/data-model.md`): a social-tuned `eyebrow`/`title`/`dek`, a **stat
trio** (the three most postable numbers — often punchier than the report's
audience stats), a left `footer`, and a right `footer_right` (e.g. the index
formula). With no `card` object it falls back to the masthead, the first stats
block, and the map. ICP variants get their own card — the same lens applies. The
card is a curated *summary*, never a new analysis: every number on it still
traces to the report's data.

## Workflow

### 1. Get the data in
Two input modes — use whichever fits:

- **Live Watt session (same chat).** After a `/watt:audience` run the working
  directory holds record CSVs (e.g. `watt-audience-*.csv`) with the signal
  stack (roles, names, reach) and any roster/group output; the conversation has
  the measured reaches, cross-audience counts, and any state index. Read those
  files and scroll the transcript for the numbers. List what you found.
- **Pasted / uploaded report.** Parse the report or data dump the user provides
  (text, CSV, PDF, screenshot). Pull the same fields.

### 2. Choose the ICP (who is this for?)
With the data in hand, decide who the story is drafted for. Open a pop-up
(`AskUserQuestion`) listing the profiles in `references/icps/` plus **No ICP
(generic)** and **Describe a new one** — make it **multi-select**, because one
story can fan out into several reader-specific variants in a single pass. For each
ICP the user picks you produce its own variant; the data blocks are authored once
and reused, only the editorial blocks change. **No ICP** drafts the generic story
as before. If a chosen profile names a `serves:` reader, offer its white-labelled
second variant too.

### 3. Fill the narrative — through the ICP lens
Some beats are editorial, not in the data: headline, dek, the recommendation
bullets, the callout, the client name, the method wording. Draft them from the
data and the user's context, then confirm with the user before rendering. Do not
invent numbers — only numbers that came from Watt or were derived from it.

When an ICP is chosen, author those beats **through its profile** (the field →
block map is in `references/icps/_schema.md`): `jtbd` shapes the masthead title and
dek; `lead_with` sets which finding goes first; `kpis` and the reader's world shape
the recs; `objection` becomes the callout; `cta` is the closing recommendation;
`vocabulary` colours every line; `label` is stamped into the eyebrow and footer
("PREPARED FOR …"). The numbers in the stat cards, map, and composition are
identical across every variant.

### 4. ICP re-search — optional, additive
Only when the user wants a hard ICP-specific number the base data doesn't hold, and
the profile has an `evidence_hook`. Emit **one** additive `/watt:audience`
cross-read (the audience × the hook) as a slash-command-tagged block; if the Watt
plugin is in the session, offer to run it directly. Fold the result back as **one
extra** stat or chart whose label marks it as an ICP read (e.g. "Skincare buyers in
the audience · your client's category"). Never let it change the core composition,
reach, or map — it sits on top of the honest finding. Skip this step entirely for
framing-only variants.

### 5. Voice pass: de-slop and put it in Watt's voice
Before the copy goes into the spec, run every editorial field through the voice
references — the bundled `watt-antislop` skill plus `references/voice/`:

- **`${CLAUDE_PLUGIN_ROOT}/skills/watt-antislop/`** (`SKILL.md` plus its
  `references/`) strips AI tells. A report is generic copy (not a Jared post), so
  apply the full ruleset and drop the Watt exceptions. Kill on sight: em-dashes and
  "not X, it's Y" contrasts. Then clear throat-clearing, adverbs, passive and false
  agency, vague declaratives, and business jargon.
- **`watt-voice.md`** sets Watt's register: direct and specific, name the incumbents
  as a category (never trash a named smaller rival), show the math, admit the
  limitation. Skip the corporate-speak caution words. Say *signal*, not data.

Apply it to every editorial field (masthead, section leads, stat labels, the
composition note, chart and table notes, cluster labels and descriptions, recs,
callout, method) and to the card copy. It touches the editorial layer only, never a
measured number.

The render step enforces this with a deterministic gate, `scripts/voice_check.py`:
it scans the spec and fails the render on any em-dash or "not X, it's Y," so a tell
cannot reach a report. Fix the flagged lines, then render.

### 6. Write the story spec
Author a JSON spec following **`references/data-model.md`** (full block schema +
the Watt-field → block mapping). Start from `references/example-pizzahut.json`, or
`references/example-pizzahut--dtc-agency.json` for an ICP variant. Record the ICP
in the top-level `icp` field. Save the spec next to the outputs, named for the
audience — `signal-story-<name>.json`, or `signal-story-<name>--<icp>.json` for a
variant.

### 7. Render the report — and the square card
Render the two-page report (it inlines the brand kit and renders the PDF in one
step), once per variant:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/signal-story/scripts/build_story.py" \
  signal-story-<name>--<icp>.json -o signal-story-<name>--<icp>.html --pdf
```

Then render the **square summary card** from the *same spec* — a 1:1 social
one-pager (hero, the stat trio, the map, the WATT footer) for LinkedIn:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/signal-story/scripts/build_card.py" \
  signal-story-<name>--<icp>.json -o signal-story-<name>--<icp>-card.html --png
```

The report PDF auto-selects Chromium, else WeasyPrint (`render_pdf.py`); the
card's `--png` rasterizes a 2160px square via Playwright (`render_png.py`). Each
writes its matching files; if a renderer is missing it prints the one-line
install. The card reads the optional top-level `card` object to curate its
headline, stat trio, and footer — otherwise it falls back to the masthead, the
first stats block, and the map.

### 8. Verify, then deliver
Render the PDF pages to images and look at them before handing off — confirm it is
**two pages**, nothing clips, the map is colored, and the legend matches. If page 1
overflows, shorten the dek/leads or trim a recommendation; if a heading wraps
oddly, shorten it. For the card, also confirm the hero, the three stats, and the map fit the square with nothing clipping. Then present every variant to the user — the two-page report and its square card together. When you fanned out
multiple ICPs, deliver them as a set and name the reader each one is for.

## Rules

- **Two pages, on a budget.** A tight two-up: about four beats on page 1, the
  rest on page 2. A tall visual (a map) needs room — keep page 1 light around it
  or move it to page 2. If content overflows, rebalance the pages or cut copy
  rather than spilling to a third page.
- **Always include a visual — the one the data fits, not a default.** Choose by
  the finding: a `map` for a geographic index, a `chart` for a comparison or trend
  (lifts, sizes, rates), a `table` for a small matrix. A story is **not** required
  to carry a map; only reach for the choropleth when the finding is genuinely
  geographic. Never ship with no graphic — but never force one that doesn't fit.
- **Categories get the colored cards, never a table.** Any section that breaks the
  story into named groups — a playbook, a set of audiences, tiers, personas,
  segments — renders as the `clusters` block: the colored category cards (a
  top-border colour, chips, and a one-line read), the same format as the playbook.
  Never present a set of categories as a `table`; reserve `table` for a flat matrix
  that isn't a set of groups.
- **Real numbers only.** Every figure traces to Watt data or a stated
  derivation. Never fabricate reach, index, or state values.
- **The ICP reframes, it never re-counts.** The lens reorders which finding leads
  and rewords the editorial beats. It never changes, drops, or invents a number,
  and the core audience is built before any ICP is chosen. Every variant of the
  same story shares identical stat cards, map, and composition.
- **Re-search is additive and labelled.** An `evidence_hook` read adds at most one
  extra stat/chart, marked as an ICP read; it never reweights the base audience.
- **No AI tells, no corporate-speak.** Every editorial line clears the voice pass
  (`${CLAUDE_PLUGIN_ROOT}/skills/watt-antislop/` plus `references/voice/`): no
  em-dashes, no "not X, it's Y," none of the
  Salesforce-press-release words. The render gate (`scripts/voice_check.py`)
  enforces the two kill-on-sight tells and will not render copy that carries one.
- **US adults, person audiences.** Same ground rules as Watt; the map is US
  states only (50 + DC).
- **Re-skinning** (different accent, fonts, map scale) is the brand kit's job —
  edit its tokens, do not hardcode styles in the spec.
- This skill works best right after a Watt audience run; if there is no data
  yet, point the user to `/watt:audience` first.

See `references/data-model.md` for the spec schema and the Watt mapping, and
`references/icps/` for the ICP profiles and how to add your own, and
`${CLAUDE_PLUGIN_ROOT}/skills/watt-antislop/` and `references/voice/` for the
de-slop and Watt-voice rules the copy must clear.
