---
name: gtm-benchmarks
description: >
  This skill should be used when a GTM strategy needs sales or channel
  benchmark numbers — "what's a good win rate", "typical sales cycle", "average
  CAC payback", "quota to OTE ratio", "SDR to AE ratio", "cold email reply
  rate", "webinar conversion", "channel CAC", "is this conversion rate normal",
  "pipeline coverage", "NRR benchmark". It supplies curated, sourced benchmark
  ranges instead of guessed or stale numbers.
metadata:
  version: "0.1.0"
---

# GTM Benchmarks

Supply benchmark numbers from a curated, dated reference — not from memory. Use
to sanity-check or fill sales and channel figures in template §11 (Sales Motion)
and §12 (Channel Strategy), and conversion assumptions anywhere in the funnel.

## Why this skill exists

Benchmark numbers are exactly where a general model is unreliable: it confidently
recites win rates, cycle lengths, ratios, and channel conversion figures that are
either invented or remembered stale. This skill holds a vetted set of **ranges**,
organized so the right one is easy to find, and dated so staleness is visible.

## How to use

1. **Prefer the client's own numbers.** If the client's CRM has the real win
   rate, cycle, or CAC, use that (via research-grounding). Benchmarks are for when
   the real figure isn't available, or to sanity-check one that looks off.
2. **Open the library:** read
   `references/benchmark-library.md` and pick the row matching the client's model
   and ACV band. The benchmarks are segmented by motion/ACV because a $5k SMB
   deal and a $150k enterprise deal have completely different norms.
3. **Quote a range, not a point.** Present "win rate typically 15–30% for this
   band" — then state where this client likely sits and why.
4. **Refresh time-sensitive figures.** Each section is dated. For anything that
   moves fast (paid CAC, cold-email reply rates), verify against a live source
   before relying on it, and update the inline date.

## What's in the library

- SaaS sales benchmarks by ACV band (win rate, cycle, CAC payback, quota:OTE,
  SDR:AE, ramp time).
- Funnel conversion benchmarks (lead → MQL → SQL → win).
- Outbound benchmarks (cold email open/reply/positive-reply, cold-call connect,
  meetings per SDR).
- Channel benchmarks (webinar reg→attend→SQL, content/SEO timelines, paid CAC
  ranges, event ROI expectations).
- Efficiency benchmarks (pipeline coverage, NRR, magic number, Rule of 40, LTV:CAC).

## Important honesty rule

These are industry rules-of-thumb with real variance. Always label them as
benchmarks, cite the library (and a live source for anything time-sensitive), and
never present a benchmark as if it were this client's measured result. When a
client's actual metric contradicts a benchmark, investigate — don't "correct" the
real number to match the benchmark.
