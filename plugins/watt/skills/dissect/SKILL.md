---
name: dissect
description: >
  Find the surprising who. Reads a news article, report, or trend piece, extracts
  the candidate audiences (whos) latent in it, compares them in Watt, and lets the
  lift between them pick a surprising-audience story — the gap between who a brand
  thinks its audience is and who it actually is. Use when the user says "dissect",
  "break down this article", "what's the angle", "who's the real audience", "find
  the who", "turn this article into a Watt brief", or pastes/uploads an article and
  asks what to research. The front of the signal-story pipeline: hand the prompts
  to /watt:audience, then render with /signal-story.
---

# Dissect

Find the **surprising who**. An article is a **seed, not the subject** — your job
is to pull the audiences hidden inside it, compare them in Watt, and let the
numbers pick a story about the **gap between who a brand *thinks* its audience is
and who it *actually* is**. That gap is the story. (PBR's real fans turned out to
be bike messengers, not the retirees the ads chased — the gap *was* the story.)

This skill runs on five rules. Follow them in order; they are what keep the output
strong and consistent run-to-run:

1. **Lead with the surprising who, not the obvious one.** The story is the *gap*
   between the assumed audience and the actual one. Confirming who a brand already
   thinks it serves is not a story.
2. **Several whos beat one.** Always extract *multiple* candidate audiences and
   compare them. Never profile a single audience.
3. **The lift picks the headline.** Run the comparison first; the overlap/lift
   number chooses the narrative. High overlap and low overlap are *both* punchy —
   opposite stories. The data decides the angle, not you.
4. **Confidence gate.** A well-framed angle sounds great even on garbage data.
   Before shipping, separate "interesting because *real*" from "interesting
   because *well-framed*." Never lead with a thin finding.
5. **Extract, don't summarize.** The first move is "what whos are latent here?" —
   not a recap of the article.

`dissect` produces the **candidate audiences and the comparison plan, never
numbers**. Watt supplies the numbers.

## Workflow

### 1. Extract the whos (not a summary)
Mine the article for every audience latent in it — aim for **3–6 candidate whos**.
Always capture:
- **The assumed who** — who the brand, article, or conventional wisdom thinks it's
  about.
- **Candidate actual whos** — who might *really* be driving the story (the
  surprising ones, including audiences the article only hints at).

Each who is a US-adult consumer audience Watt can measure, or its closest labeled
proxy. Do not stop at the obvious one — the surprising whos are the point.

### 2. Name the gap
State the tension as **assumed who vs. candidate actual who(s)**. The story lives
in that gap. If the obvious audience really is the audience (no gap), say so and
find a sharper sub-gap — a hidden segment, a second affinity to cross, or a
geography.

### 3. Set up the comparison (this is the experiment)
The core move is **comparing audiences**, not profiling one. Choose the two (or
three) whos whose relationship decides the story, and design the Watt comparison:
cross them and measure **overlap / lift vs. the base rate**. This runs *first* —
its result selects the narrative.

### 4. Pre-write the branch headlines
Before any data, write the headline for **each outcome**, because both directions
are a story (see the lift→headline map in `references/method.md`):
- **Overlap ≫ base** → the surprising who *is* the assumed one after all
  ("coming from inside the drive-thru").
- **Overlap ≈ base / low** → they're different crowds ("they never set foot in one").
- **Split** → the gap is regional or segment-bound.

The lift number picks which headline ships. Do not pre-decide it.

### 5. Run the confidence gate
Score the finding's **validity, not its punchiness**:
- Are these **real Watt signals**, or a stretched/invented proxy? How loose is it?
- **Sample** sufficient on both sides of the comparison?
- Is the lift **beyond noise**, or a rounding artifact?
- Is the gap a **confound** (e.g., a young-male skew that inflates *both* sides),
  not a real relationship? Name the control — read lift vs. a demographic-matched
  base.

Label confidence **solid / provisional / thin**. A *thin* finding may not be run,
and is never presented as the headline. This is the guard against "great format,
garbage signal."

### 6. Map to Watt + emit prompts
Translate into Watt operations (observational — prevalence, lift, geographic skew;
not causation): build each who (reach + composition), run the **cross/lift
comparison** (the decider), then group by state for the map. Then **open a pop-up**
(`AskUserQuestion`) to let the user pick which comparison to run and whether to run
it in Watt now or take the prompts. Emit the chosen comparison's prompts as
separated, slash-command-tagged blocks (templates in `references/method.md`); if
the Watt plugin is in the session and they chose run-now, invoke it directly.

### 7. Output order — surprising who first
1. **The gap** — assumed who vs. the surprising candidate, in one line.
2. **The whos** — the candidate audiences you extracted.
3. **The decider** — the comparison + both branch headlines (what publishes if
   overlap is high vs. low).
4. **Confidence** — solid / provisional / thin, and the one check that firms it up.
5. The pop-up, then the prompts.

Caveats live inside the confidence read — never open with what Watt can't do.

## Rules
- **Extract, don't summarize.** First output is the whos, not a recap.
- **Multiple whos, always compared.** Never ship a single-audience profile.
- **The data picks the angle.** Pre-write both branch headlines; let the lift
  choose. Don't pre-decide the narrative.
- **Confidence gate is mandatory.** Flag thin findings; never lead with one.
- **Lead with the surprising who**, grounded in audiences Watt can measure (or a
  labeled proxy). The article is a seed — keep its subject, find the people under
  it, and do not pivot to a generic audience profile.

See `references/method.md` for the lift→headline mapping, the confidence rubric,
the Watt-operation map, and the prompt set; `references/example-teardown.md` for
the Wendy's worked example.
