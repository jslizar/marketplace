# LinkedIn Post Engine

Reverse-engineer an example LinkedIn post, pull what you know about a client (or your own account), and draft a post that matches the example's style — classified to a funnel stage, personalized to an ICP, and de-slopped before it ships.

Built for ghostwriting across multiple clients. Each client is a `context.md` file you maintain; connectors are used only for research.

## What it does

Front-door skill **`linkedin-post`** runs the full loop; each stage is also a skill you can run on its own.

| Skill | What it does |
|---|---|
| `linkedin-post` | Front door. Runs context → style → classify → research → draft → **match** → QA and returns 3 candidates. |
| `post-deconstruct` | Turns example post(s) into a reusable **Style Spec + fill-in template** (hook, skeleton, rhythm, formatting, CTA, length, AI-tells). |
| `post-structure` | Structural-copying specialist — maps skeleton, transitions, whitespace, rhythm, and close. Counterpart to the hook framework. |
| `style-library` | Swipe file. Compiles multiple examples per author into a reusable **Style Profile**, shared across clients. |
| `style-match` | Scores a draft against the example/profile (0–100) per dimension and returns fixes — the **format-fidelity gate**. |
| `context-loader` | Reads / validates / scaffolds a client's `context.md`. |
| `funnel-classify` | Classifies the post as TOFU / MOFU / BOFU and sets structure, CTA strength, and proof level. |
| `icp-research` | Finds target companies for an ICP or named account (ABM) via Clay or Exa, with a recent signal per account. |
| `post-qa` | De-slop + guardrail gate. Hard-blocks drafts that break a Canon constraint or invent Proof. |

## Setup

**Client files.** Put a `clients/` folder inside your Cowork **project folder** — the plugin auto-discovers it:

```
<your Cowork project folder>/
  clients/
    <client-name>/
      context.md      # the spine — you maintain this
      examples/       # swipe posts you upload
      style-specs/    # saved post-deconstruct outputs
```

Create the project with **Use an existing folder** (or **Start from scratch**) pointed at the folder that holds `clients/`. Because a Cowork project is backed by that local folder, the skills read `clients/<name>/context.md` directly — no path to configure. Use a local-folder-backed project, not the "link a chat project / paste a URL" context type (that's reference material, not a scannable filesystem). The `context.md` format is in `skills/context-loader/references/context-template.md`.

**Connectors (research only — optional).** The plugin reads context from your files, not from connectors. Connectors enhance `icp-research`:

| Job | Primary | Also |
|---|---|---|
| Build + enrich a target company list | **Clay** | Exa |
| Semantic look-alikes ("companies like X / doing Y") | **Exa** | Clay |
| Recent trigger/signal per account | **Exa** or **Clay** | web fetch |
| Exact firmographic filters | **Clay** | — |
| Audience profiling | Watt | — |

If neither Clay nor Exa is connected, `icp-research` falls back to standard web search. No environment variables required.

## Usage

- "Draft a LinkedIn post for AICRO from this example: …" → `linkedin-post`
- "Reverse-engineer this post" → `post-deconstruct`
- "Set up a new client / check this context file" → `context-loader`
- "Is this TOFU, MOFU, or BOFU?" → `funnel-classify`
- "Find ABM accounts for AICRO's ICP" → `icp-research`
- "QA this draft" → `post-qa`

## Notes

- Examples can be **screenshots** — the deconstructor reads the text and visual formatting straight from the image. Expand the post's "…more" before capturing so nothing's cut off.
- `skills/linkedin-post/references/hook-framework.md` holds a **placeholder 6-lever hook framework**. Swap in your coworker's exact levers from the `linkedin-hook-generator` skill to make it faithful.
- v1 defaults: 3 candidate drafts, Canon-driven QA gate, Clay + Exa research.
