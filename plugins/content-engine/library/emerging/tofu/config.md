# Emerging — tofu config

## Lane directive

- **Job**: Earn reach with the ICP — broad, relatable, contrarian.
- **What "emerging" means**: every entry here is a spec-lite deconstructed from a post that
  performed on LinkedIn IN THE LAST 7 DAYS. This is the live-signal lane — freshest, least
  proven over time. Same lane job as Virio tofu; the difference is recency, not intent.

## Admission test

The weekly scan's filters ARE the admission test: posted within the last 7 days; business-focused
(no memorial/feelings posts, no engagement bait); > 300 reactions or a clear follower-adjusted
outlier; post_text 350–3000 chars; classified into this lane by the funnel-classify test (ABM
deconfliction first). Quality-gated up to 15 — a thin week is honest, never padded.

## Refresh policy

- Owned ENTIRELY by the weekly viral-scan task (`scripts/viral-scan/`, Saturdays 8am). No other
  process writes here; the library-refresh task never touches this lane.
- Contents = current week only. Each Saturday the outgoing batch rolls into `virio/tofu/` as
  `cohort: rolled` ("Recent finds" section, replacing the prior week's rolled batch), and this
  lane refills from the fresh scrape.
- Entries carry `cohort: emerging` and `scan_week` frontmatter. Pins: if the user pins an
  emerging entry, the rollover keeps it in Virio permanently (a pin survives the weekly recycle).
