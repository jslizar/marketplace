# content-interview

Client content-intake pipeline for LinkedIn. Four skills that turn a client conversation into draft-ready material:

```
interview-kit ──▶ icp-avatar ──▶ idea-inventory ──▶ writing-standards
  (interview)      (persona)      (20+ concepts)      (hooks → draft)
```

## Skills

- **interview-kit** — prep and run the client content interview. Say "prepare for a content interview with [name]" and it researches the FOC in Virio (strategy, tone, ICPs, banned topics), pulls the account's Notion context (past meetings, content pillars, strategy docs), and reads their recent LinkedIn posts, then builds a tailored question set: cutting what the record already answers AND what earlier interviews already mined, flagging the gaps to fill, adding fresh probes from recent syncs, and deriving questions from their real ICP personas. Also carries the funnel-stage question banks, capture guidance, and the cadence for interview #2 and beyond.
- **icp-avatar** — build a deep emotional ICP avatar (pains, fears, desires, limiting beliefs, trigger moments, identity transformation) saved to `clients/<slug>/icp-avatar.md`.
- **idea-inventory** — mine an interview transcript into 20+ post concepts, each tagged with pillar, funnel stage, ICP, source quote, angle, and intent signal.
- **writing-standards** — draft from a chosen concept via the three-phase protocol (Hooks → Takeaways → Draft), using the 6 Hook Levers and 10 Takeaway Types, de-slopped against `references/ai-tells.md`.

## Notes

- Feeds the **content-engine** plugin downstream: inventory ideas become angles and drafts in its pipeline.
- **Virio + Notion connectors recommended.** They power interview prep, both read-only (the skill never writes back to either):
  - **Virio** — `content_publishers_list` resolves the FOC, `content_settings_get` reads their strategy/tone/ICPs, `read_linkedin_uri` pulls what they've already posted.
  - **Notion** — pulls the account's context from the Virio workspace: the account card, Content Pillars and strategy docs (Strategy DB), and past meetings (Meetings DB) — including prior Content Interviews, so #2+ never re-mines covered ground. HubSpot/Attio add account context if connected.
- **Works without any connector.** With none, interview-kit falls back to the generic question banks plus web research, and the other three skills run entirely on local files and the transcript you provide.
