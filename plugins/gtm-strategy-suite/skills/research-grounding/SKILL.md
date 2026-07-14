---
name: research-grounding
description: >
  This skill should be used whenever a GTM/strategy document needs facts,
  figures, market sizes, growth rates, competitor data, or benchmarks — i.e.,
  any quantitative or factual claim. Triggers: "research the market", "what's
  the TAM", "market size for", "competitor research", "ground these numbers",
  "fact-check the strategy", "cite sources", "is this number real". It enforces
  research-before-write, routes each fact to the right source, and logs every
  number in a claims ledger as sourced or an explicit assumption.
metadata:
  version: "0.1.0"
---

# Research Grounding

Stop the single most damaging failure in strategy docs: confidently stated
numbers that were invented. Use this for every factual/quantitative section of a
GTM plan (template §3, §4, §8, and the benchmark inputs to §11–§12).

## The core rule

**No quantitative claim gets written from memory.** Market sizes, growth rates,
shares, competitor prices, and benchmarks are either (a) retrieved from a named
source, or (b) tagged `[ASSUMPTION]` with the reasoning shown. A model's prior is
not a source — prices, leaders, and market figures change, and the model's
training is stale by the time it's used.

## Workflow

1. **List the claims the section needs first** — before drafting, enumerate the
   numbers/facts required (e.g., "industry size, YoY growth, top-3 competitor
   shares, average price").
2. **Route each to the right source** — see
   `references/connector-routing.md` for which connector/tool answers which kind
   of fact. Prefer the client's own data and live tools over web search; prefer
   web search over memory; never use memory alone for a number.
3. **Retrieve, then record** — capture the value, the source, and the date into
   the claims ledger below.
4. **Tag the gaps** — anything you cannot source becomes an explicit
   `[ASSUMPTION: value — basis]` so the reader can challenge it. Assumptions are
   fine; *hidden* assumptions are not.
5. **Date-stamp anything time-sensitive** — prices, headcounts, market sizes,
   "current leader" facts. Note the as-of date inline.

## Claims ledger (keep this, put it in the appendix)

| # | Claim / figure | Value | Source (name, date, URL) | Confidence | Used in § |
|---|---|---|---|---|---|
| 1 | Industry size | `$X` | `[source, 2025]` | High / Med / Low | §4.1 |
| 2 | YoY growth | `X%` | `[source]` | … | §4.2 |
| 3 | Competitor A price | `$X` | `[source]` | … | §8.5 |
| 4 | `[ASSUMPTION]` win rate | `X%` | reasoning | Assumption | §11 |

Every number in the document should trace to a row here.

## Sizing discipline (TAM / SAM / SOM)

When sizing a market, show the method and prefer **bottom-up** (accounts × ACV,
or units × price) over top-down (a % slice of a big industry number) because
bottom-up is defensible and auditable. State TAM (everyone who could buy), SAM
(who you can serve), SOM (what you can win near-term) separately, each with its
own math and sources. Triangulate top-down and bottom-up when possible — if they
disagree wildly, dig before publishing.

## Competitor facts

Pull competitor positioning, pricing, and share from current sources (their site,
recent filings/news, a competitive-intel tool), not recollection. Name the source
and date for each. Distinguish "list price" from "street price" when relevant.

## Graceful degradation

If no connectors are wired in, fall back to web search and clearly label
estimates. If a fact cannot be obtained at all, say so and tag it
`[ASSUMPTION]` — never paper over the gap with a confident guess.

## Output

A document where every figure is either sourced or visibly an assumption, plus a
claims ledger in the appendix. Pair with gtm-benchmarks for sales/channel
benchmark inputs (which are themselves a curated, sourced reference).
