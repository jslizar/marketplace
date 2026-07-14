# Dissect — method reference

How to extract whos, let the lift pick the headline, and gate on confidence.

## Extracting whos

An article names one audience out loud (the **assumed who**) and hints at others.
Pull **3–6 candidate audiences**, each a US-adult consumer audience Watt can
measure or a clearly-labeled proxy:

- **The assumed who** — who the brand / article / conventional wisdom thinks it's
  about. Always list it; it's the baseline the surprise is measured against.
- **The actors in the story** — whoever is *doing* the thing the article describes
  (buyers, traders, posters, switchers), even if the article treats them as a
  faceless force.
- **The adjacent affinities** — crowds the same behavior usually travels with
  (a meme-stock crowd ↔ crypto / gaming; a DIY crowd ↔ high-tech early adopters).
- **The legacy/nostalgia who** — who the brand *used* to be for.

If a who isn't directly measurable (e.g. "people who traded this stock"), name the
**closest Watt proxy** and flag it (e.g. "retail-investing / active-trader /
crypto-curious interest" as a proxy for "meme traders"). Proxies are allowed;
unlabeled proxies are not.

## The comparison decides the story (lift → headline)

Never profile one who. Pick the two whose relationship *is* the story, cross them,
and read the **lift** = (overlap rate) ÷ (the base rate you'd expect by chance,
ideally demographic-matched). The number picks the headline:

| Lift result | What it means | Headline shape |
|---|---|---|
| **Lift ≫ 1** (high overlap) | the surprising who *is* the assumed/actor who | "Coming from inside the drive-thru" — they're the same people |
| **Lift ≈ 1** (overlap = chance) | the two crowds are unrelated | "They're squeezing a brand they never eat at" — different worlds |
| **Lift < 1** (avoidance) | the crowds actively diverge | "The fans the brand forgot it had" — inverse audience |
| **Split by geo/segment** | overlap only in places/segments | "Real in five states, noise everywhere else" |

Pre-write the headline for the two most likely branches **before** running it, so
the data — not your taste — chooses. Both directions are publishable; that is the
point.

## Confidence gate (interesting-because-real vs. interesting-because-framed)

A signal story's format makes any angle *sound* good. Gate on validity before
shipping. Score the finding:

| Confidence | Looks like | What you may do |
|---|---|---|
| **Solid** | real named Watt signals; sample sufficient both sides; lift clearly beyond noise; confound checked against a matched base | lead with it as the headline |
| **Provisional** | a labeled proxy *or* moderate sample *or* confound not yet controlled | run it, but frame as "early read"; name the one check that would firm it |
| **Thin** | invented/over-stretched signal, tiny sample, lift within rounding, or an obvious unchecked confound | do **not** lead with it; flag it; often don't run it at all |

The classic confound to control: a shared **demographic skew** (e.g. young men
over-index on *both* day-trading and fast food) can manufacture a high lift that
isn't a real relationship. Always read lift against a demographic-matched base,
not the national base, before calling a who-overlap "real."

## Watt operation → what it gives you

| Operation | Yields | Use |
|---|---|---|
| `explore` | which who signals exist, size, freshness | confirm the whos are real before building |
| `audience` build per who | reach + composition | size each candidate who; feeds the audience beat |
| `audience` cross (who A × who B) | overlap + lift | **the decider** — picks the headline (channel-reality beat) |
| `audience` group by state | per-state index | the choropleth + playbook |

## Runnable prompt set (separated by slash command)

After the user picks a comparison in the pop-up, emit these as **separate
copy-ready blocks**, one per step, in run order. Plain English — Watt takes
*signal / must-have / exclusion / audience / size band / objective*, never boolean
operators.

**1 — confirm the who signals exist**
```
/watt:explore
US adults: what signals exist for <who A> and <who B>, how big and how fresh, and what's adjacent.
```

**2 — build each who (reach + composition)**
```
/watt:audience
Build a US-adult audience: <who A description>. Objective: widest credible reach. Must include: <gate signal>. Report reach and composition.
```
(repeat for who B)

**3 — the decider: cross them for lift**
```
/watt:audience
Cross <who A> with <who B>; report both reaches, the overlap, and the lift vs. a demographic-matched base rate (control for <the confound, e.g. age/gender skew>).
```

**4 — group by state (drives the map)**
```
/watt:audience
Break the overlap audience down by state as an index; leave low-sample states uncolored. Capture sample sizes, refresh date, and the index formula.
```

If Watt is in the session and the user chose **run now**, invoke `watt:explore` /
`watt:audience` directly with block 1, walk the flow, then the rest. Bring the
reaches, the lift, and the per-state index back for `signal-story`.
