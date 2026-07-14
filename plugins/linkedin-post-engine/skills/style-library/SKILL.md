---
name: style-library
description: >
  This skill should be used when the user wants to save, build, or reuse a post style —
  "save this as a style", "write like this author", "load the saved style", "add this to
  my swipe file", "build a style profile from these posts", "what styles do we have". It
  manages a styles/ library at the project root: each style is a folder of example posts
  plus a compiled Style Profile (averaged template + variance) that is reusable across
  every client, so a style is captured once and matched many times.
metadata:
  version: "0.1.0"
---

# style-library

A durable swipe file. A **style** is a reusable profile compiled from one or more example posts by the same author — captured once, matched across any client. Matching a single ad-hoc example is brittle; a profile built from several posts is robust.

## Location (auto-discover)

Styles live in a `styles/` folder at the **project root**, sibling to `clients/`:

```
styles/
  <style-slug>/          # e.g. justin-welsh, founder-story, our-house-style
    examples/            # the swipe posts (raw text)
    profile.md           # the compiled Style Profile
```

Glob the project for `**/styles/*/profile.md`. Match the requested style by slug ("write like Justin Welsh" → `justin-welsh`). Styles are **cross-client** — never nest them under a client.

## Operations

- **Add** — save a new example post into `styles/<slug>/examples/` (create the style if new). Never overwrite an existing example; add a numbered file.
- **Compile / refresh** — run `post-deconstruct` (which calls `post-structure`) across **all** examples in the style, average the template, record variance, and write `profile.md`. Re-run whenever examples are added.
- **Load** — read `profile.md` and hand the template + variance to `linkedin-post` for drafting or to `style-match` for scoring.
- **List** — show available styles with their example counts and tags.

## Compile logic

1. Deconstruct each example into a Style Spec + template.
2. Average the quantified fields (hook length band, block sequence, rhythm targets, length band); keep the **modal** block sequence and note alternates.
3. Record **variance** — where the author legitimately varies (e.g. "opens on a question or a stat").
4. Merge the `avoid` lists (union) and the formatting map (intersection of what's always true).
5. Write `profile.md` per `references/style-profile-schema.md`.

## Reuse

The drafter loads a profile by name instead of re-deconstructing: "write like `founder-story`." The profile's variance tells the drafter where it has room to move and tells `style-match` what tolerance to allow.

## Rules

- The user owns the files. Add, don't overwrite; profiles are regenerable from examples.
- A profile captures **style only** — no topics, claims, or named entities.
- If a style has just one example, say so — the profile is usable but low-confidence until more are added.
