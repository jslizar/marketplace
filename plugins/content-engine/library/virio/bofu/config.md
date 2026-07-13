# BOFU library — config

## Stage directive

- **Job**: Convert existing intent. The reader is already evaluating — the post's job is to make choosing the client feel safe and obviously right.
- **Hook breadth**: Buyer-situation specific. Line one speaks to someone mid-decision.
- **Proof level**: Heavy — named results, real numbers, testimonials, side-by-side comparisons. Every claim traceable to the client's Proof section.
- **CTA**: Hard — demo, call, trial, "DM me". A BOFU draft with no CTA fails QA.

## Admission test

Does this move someone already evaluating — does it de-risk the decision with verifiable proof? Reach plays fail (TOFU); problem-education fails (MOFU). And if the post's engine is glorifying a specific named account, it's ABM — it belongs to the ABM engine, not here.

## Refresh policy

- Repo target: 15 format specs — accept fewer rather than admit weak specs.
- Freshness window: 21 days (the pool is thin; don't churn good specs for churn's sake).
- Source: `viral_posts_all` where `funnel_stage = 'BOFU'` — only ~676 rows, the thinnest pool. This is the ONE stage with an external fallback: when the corpus can't sustain the repo target, scout via Apify/web and write keepers back into `viral_posts_all` with `funnel_stage = 'BOFU'` so the corpus deepens.
- Example turnover: owned by the scheduled refresh task. Each spec carries exactly 2 source examples; pinned examples are never auto-replaced.
- ABM deconfliction applies hardest here: BOFU and ABM overlap most. The test — generic bottom-funnel proof (case study, testimonial, comparison) stays; named-account glorification goes to `abm_posts` territory.
