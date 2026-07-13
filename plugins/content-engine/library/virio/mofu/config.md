# MOFU library — config

## Stage directive

- **Job**: Make the ICP's problem urgent and the client's approach credible. The reader should finish thinking "this is exactly my situation, and these people get it."
- **Hook breadth**: Problem/solution specific. Line one names a pain or a decision the ICP is actually in.
- **Proof level**: Medium — data, frameworks, worked examples, before/after mechanics. Enough substance to be saved, not yet a sales pitch.
- **CTA**: Soft — a gated resource, a comment-to-receive prompt, a "which do you use?" question. No demo/call asks.

## Admission test

Does this reframe or sharpen a problem the ICP has, in a way that builds the author's standing on it? Pure inspiration fails (that's TOFU); pure pitch fails (that's BOFU).

## Refresh policy

- Repo target: 15 format specs.
- Freshness window: 14 days.
- Source: `viral_posts_all` where `funnel_stage = 'MOFU'` (~5.4K rows). Note the pool skews promotional (`promotional_post` and `announcement` dominate by count) — filter hard on the admission test, and prefer `is_lead_magnet = true` rows for gated-resource formats.
- Example turnover: owned by the scheduled refresh task. Each spec carries exactly 2 source examples; pinned examples are never auto-replaced.
- ABM deconfliction: named-account posts go to the ABM engine, not here.
