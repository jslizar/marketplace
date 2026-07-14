# content-interview

Client content-intake pipeline for LinkedIn. Four skills that turn a client conversation into draft-ready material:

```
interview-kit ──▶ icp-avatar ──▶ idea-inventory ──▶ writing-standards
  (interview)      (persona)      (20+ concepts)      (hooks → draft)
```

## Skills

- **interview-kit** — run the client content interview: prep, funnel-stage question banks, capture guidance, and the cadence for interview #2 and beyond.
- **icp-avatar** — build a deep emotional ICP avatar (pains, fears, desires, limiting beliefs, trigger moments, identity transformation) saved to `clients/<slug>/icp-avatar.md`.
- **idea-inventory** — mine an interview transcript into 20+ post concepts, each tagged with pillar, funnel stage, ICP, source quote, angle, and intent signal.
- **writing-standards** — draft from a chosen concept via the three-phase protocol (Hooks → Takeaways → Draft), using the 6 Hook Levers and 10 Takeaway Types, de-slopped against `references/ai-tells.md`.

## Notes

- Feeds the **content-engine** plugin downstream: inventory ideas become angles and drafts in its pipeline.
- Needs no MCP connections — everything runs on local files and the transcript you provide.
