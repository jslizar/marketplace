# Dissect — worked example (the hard case)

Input: a **markets** story — *"Wendy's Shares Jump 42% as Meme Traders Rally
Behind Fast-Food Chain."* The literal subject (a stock squeeze, short interest)
isn't Watt's domain. The skill's job is to treat the article as a **seed**, pull
the **whos** out of it, and let a **comparison** pick the story.

## 1. Extract the whos (not a summary)
Audiences latent in the article:
- **Assumed who** — *nostalgic Gen-X brand lovers*. The analysts' explanation:
  "classic American brand," "Where's the Beef?", fond memories drive the rally.
- **Actor who** — *the retail-trading / WallStreetBets crowd* doing the buying.
  No literal signal → proxy: **retail-investing / active-trader / brokerage-app /
  crypto-curious interest** (labeled).
- **Adjacent who** — *crypto + gaming* (the meme-stock crowd's usual traveling
  companions; prior targets were GameStop, Krispy Kreme, Opendoor).
- **Actual-customer who** — *who eats Wendy's now*: value-seekers, late-night,
  families with teens.

## 2. Name the gap
The article quietly assumes the **traders = nostalgic brand lovers** (the actor
who is the assumed who). The surprising possibility: **the people squeezing the
stock and the people in the drive-thru are different crowds.** That gap is the
story.

## 3. The decider (the comparison)
Cross the **retail-trader who × the Wendy's-customer who**; read the **lift vs. a
demographic-matched base rate**. One number decides it.

## 4. Pre-written branch headlines
- **Lift ≫ 1 →** "Coming from inside the drive-thru" — the traders really are the
  customers; the nostalgia story is true, and here's where they cluster.
- **Lift ≈ 1 →** "Squeezing a brand they never eat at" — trader energy and burger
  loyalty are different worlds; the rally is pure float mechanics wearing a
  nostalgia costume.
Both are strong. The data picks; we don't.

## 5. Confidence gate
**Provisional, not solid — and here's why it would be easy to ship anyway:**
- The "meme trader" who is a **proxy** (retail-investing/active-trader/crypto),
  not a literal signal — at best provisional.
- **Confound:** young men over-index on *both* day-trading *and* fast food, so a
  naive cross will show a high lift that's just shared demographics, not a real
  Wendy's-specific relationship. **Control:** read lift against a demographic-
  matched base before believing "they love the brand."
- Until that control is run, do **not** lead with "the traders are nostalgic
  fans" — it would be *interesting-because-well-framed*, not *because-real*.

## 6. Runnable prompts (after the user picks this comparison)

**1 — confirm the who signals**
```
/watt:explore
US adults: what signals exist for retail-investing / active-trading / crypto interest, and for Wendy's / fast-food / QSR affinity — how big, how fresh, what's adjacent.
```
**2 — build each who**
```
/watt:audience
Build a US-adult audience: retail investors / active traders / crypto-curious. Objective: widest credible reach. Report reach and composition (age, gender, other affinities).
```
```
/watt:audience
Build a US-adult audience: Wendy's / fast-food customers (value, late-night, families with teens). Objective: widest credible reach. Report reach and composition.
```
**3 — the decider: cross for lift (controlled)**
```
/watt:audience
Cross the retail-trader audience with the Wendy's / fast-food audience; report both reaches, the overlap, and the lift vs. a base matched on age and gender (control the young-male skew).
```
**4 — by state**
```
/watt:audience
Break the overlap audience down by state as an index; leave low-sample states uncolored. Capture sample sizes, refresh date, and the index formula.
```

→ Run in Watt, then render with `signal-story`. The headline writes itself once
the controlled lift comes back.
