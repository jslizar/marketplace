---
type: format-spec
lane: mofu
format: failure-modes-mirror
archetype: "framework-walkthrough"
platform: LinkedIn
funnel_stage: MOFU
peak_engagement: 561
added: 2026-07-16
refreshed: 2026-07-16
pinned: false
cohort: emerging
scan_week: 2026-07-16
---

# Failure-modes mirror

- **Archetype**: framework-walkthrough
- **Funnel stage**: MOFU — diagnoses the reader's org, then hands them the fix; authority through pattern recognition.
- **Stage mechanic**: Contrarian diagnosis hook (it's not the technology, it's the org chart), a numbered list of failure modes the reader will recognize, then the same numbers again as fixes — a 1:1 mirror that makes the prescription feel inevitable. Closes by naming the real problem ("the operating model underneath it").
- **Platform**: LinkedIn
- **Source examples**: (this week's scan, second pass — author-seeded; two same-author variants)
  - https://www.linkedin.com/posts/andreashorn1_ai-programs-dont-fail-because-of-the-technology-activity-7483027157154312192-i-Ke — Andreas Horn, 561 reactions / 142 comments, 2026-07-15 (scanned 2026-07-16)
  - https://www.linkedin.com/posts/andreashorn1_the-hardest-part-of-enterprise-ai-is-everything-activity-7482305386054729728-gqt8 — Andreas Horn, 336 reactions / 83 comments, 2026-07-13 (variant: failure list without the mirrored fixes)
- **Hook pattern**: "{Initiatives} don't fail because of {expected culprit}.\n\nThey die in {unexpected place}, and the pattern is remarkably consistent."
- **Skeleton** (block sequence):
  1. Two-line contrarian diagnosis hook
  2. Numbered failure modes (4–5), each: bold name + two-sentence sketch the reader recognizes
  3. The turn: winners aren't using better {tools}, they fix the {system}
  4. The same numbers as fixes, mirrored 1:1 against the failures
  5. Zoom-out law ("maturity has very little to do with technology")
  6. Mirror-check close ("If this org chart looks familiar…")
  7. Newsletter PS (soft, optional)
- **Rhythm & formatting**: Numbered blocks with bold-style leads, one blank line between beats, no emojis. ~350 words.
- **Why it works**: Recognition does the persuasion — the reader self-diagnoses in the failure list, so the mirrored fixes read as *their* conclusion. The 1:1 structure signals rigor without citations.
- **Adaptation notes**: The failure modes must come from patterns the client has genuinely seen (Canon/Proof); invented failure modes read hollow to practitioners immediately.
- **Watch-outs**: Fixes must map exactly onto failures — a fix list that drifts breaks the format's spine. Cap at five; seven reads as a listicle.

## Top example — full post text

```
AI programs don't fail because of the technology. 

They die in the org chart, and the pattern is remarkably consistent. The four failure modes I keep seeing:

1 - Fragmented ownership. 
A CAIO, a CTO, a CIO, and a COO all have a stake, and nobody has accountability. AI becomes a political football rather than a business capability.

2 - Strategy follows spend. 
Licenses get bought, pilots get launched, and months later someone finally asks what measurable problem this was supposed to solve. Nobody has a good answer.

3- Data blindness. 
Every GenAI use case hits the same quality, access, and governance wall. The people who know how to fix the data are usually the last ones invited to the strategy room.

4 - Shadow execution. 
The most valuable AI work in the building is often a solo side project living in an Excel file. No sponsor, no budget, no path to scale.

What is interesting is that the organizations actually getting returns are not using better models. They are fixing the operating model, and the fixes map almost exactly onto the failures:

1 - Clear ownership. 
One person with budget, mandate, and accountability for outcomes. Not a committee, not a council, one owner.

2 - Business-first use cases. 
Every initiative tied to a measurable revenue, cost, or risk number before any license gets bought. If you cannot name the metric, you do not have a use case yet.

3 - Embedded governance. 
Data quality and access treated as a design principle from day one, with the data people in the room when the strategy is written, not after it fails.

4 - Proper resourcing. 
The Excel-file experiments get found, funded, and given a path to scale. Execution teams treated as core work rather than a hobby.

AI maturity, as far as I can tell, has very little to do with technology. If this org chart looks familiar, the problem is probably not your AI strategy. It is the operating model underneath it.

P.S.: I write about patterns like this every week und how to get unstuck in my newsletter, Human in the Loop: https://lnkd.in/dbf74Y9E
```
