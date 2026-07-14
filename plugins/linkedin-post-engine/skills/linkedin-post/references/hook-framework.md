# Hook framework

The first 1–3 lines decide whether the post is read.

## Where the hook comes from

The hook is **part of the format being matched** — never invented independently:

- Matching an example / Style Spec: use the spec's **hook type and pattern** (extracted by `post-deconstruct`). `style-match` scores candidates on using the *same* hook type as the target; a different type is a fidelity miss.
- Working from a format spec (ABM/funnel): adapt the spec's **Hook pattern** field to the subject.

Candidates vary in **wording and the subject's entry point** — which detail, moment, or number leads — never in hook type or skeleton. Three candidates means three different ways into the same pattern, not three different patterns.

## Mechanics (every hook)

- **Mobile fold ≈ 140 characters**, desktop ≈ 210. The hook must land its punch before the fold.
- First line short and standalone. No greeting, no throat-clearing above it.
- No hashtags or links in the hook. (Links go in the first comment.)
- Never copy the example's sentences — fill the pattern with the client's substance.

## Checklist (per hook)

- [ ] Same hook type/pattern as the matched spec
- [ ] Under the mobile fold
- [ ] Entry point differs from the other candidates
- [ ] On a client Pillar, in the Author's voice
- [ ] No invented specifics (numbers/names must come from context or research)
