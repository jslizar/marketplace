# TOFU library — config

## Stage directive

- **Job**: Earn reach with the ICP; be worth following. The post is client-agnostic on the surface — the ICP shares it because it's good, not because it sells.
- **Hook breadth**: Broad, category-level. Anyone in the ICP's world should feel addressed by line one.
- **Proof level**: Light — a POV, an observation, one striking number. No case studies, no client results.
- **CTA**: None, or follow-level at most ("follow for more"). A TOFU draft with a demo/call/resource ask fails QA.

## Admission test

Would a cold ICP member — someone who has never heard of the client — share this? If the post only works for people who already know the brand, it fails.

## Refresh policy

- Repo target: 15 format specs.
- Freshness window: 14 days — specs with source examples older than this are flagged stale.
- Source: `viral_posts_all` where `funnel_stage = 'TOFU'` (34K+ rows — the deepest pool; be picky, prefer `is_outlier = true`).
- Example turnover: owned by the scheduled refresh task. Each spec carries exactly 2 source examples; pinned examples are never auto-replaced.
- ABM deconfliction: posts whose engine is a specific named account/person/campaign go to the abm lane, not here.
