# De-slop pass — rewrite the clones before they're seen

Runs on every drafted candidate, immediately after drafting and before `style-match` and `post-qa`. This is an **active rewrite**: fix everything in place, don't just flag it.

**The list of tells lives in ONE place: `post-qa/references/ai-tells.md`.** Apply that list here in full — the "Kill on sight" items unconditionally, the "Cut" and "Rewrite" items per its guidance, and its "Don't over-correct" rules to protect the Author's deliberate craft. Do not keep a local copy of the list; if a new tell shows up, add it there.

## How this pass differs from post-qa's check

- Here: rewrite in place, every candidate, no report needed.
- post-qa: the final backstop — flags anything that survived, and hard-blocks fabricated numbers/names.
- Both passes use the same canonical list, so nothing can pass the gate that the drafting pass would have killed.

## After the pass

Re-check the hook is still under the mobile fold (~140 chars) and the structure still matches the blueprint — a rewrite that breaks fidelity gets caught by `style-match` next, so fix it here first.
