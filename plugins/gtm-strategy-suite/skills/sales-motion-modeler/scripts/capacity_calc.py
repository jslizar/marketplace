#!/usr/bin/env python3
"""
capacity_calc.py — deterministic sales-motion math for GTM work.

Subcommands:
  motion       Recommend a motion archetype from ACV (+ optional rep cost),
               and sanity-check deals-per-rep feasibility.
  capacity     Headcount from a revenue target: AEs, SDRs, SEs, CSMs, and
               the pipeline coverage required.
  comp         Quota:OTE ratio and base/variable split sanity check.
  channel-fit  Weighted channel-selection scoring, ranked (CSV in).

Stdlib only. Run any subcommand with -h for arguments.

Examples
--------
  python capacity_calc.py motion --acv 40000 --rep-cost 160000
  python capacity_calc.py capacity --target 6000000 --quota 800000 --ramp 0.6 \
         --sdr-per-ae 1 --se-per-ae 0.33 --book 6000000 --csm-book 2000000
  python capacity_calc.py comp --ote 240000 --base-pct 0.5 --quota 800000
  python capacity_calc.py channel-fit --matrix channels.csv
"""

import argparse
import csv
import math
import sys


def _money(x):
    return f"${x:,.0f}"


def motion(args):
    acv = args.acv
    print("Motion archetype recommendation\n")
    if acv < 2000:
        arch = "Self-serve / PLG"
        why = "ACV too low to fund any human in the deal — the product must sell itself."
    elif acv < 30000:
        arch = "Inside / SMB sales-led (consider PLG + sales-assist)"
        why = "Light evaluation; demos close it; win on volume of smaller deals."
    elif acv < 100000:
        arch = "Mid-market sales-led"
        why = "A small buying group and an ROI case; full-cycle or pod AEs."
    else:
        arch = "Enterprise / field"
        why = "Formal buying committee, security/legal/procurement, custom terms."
    print(f"  ACV {_money(acv)}  ->  {arch}")
    print(f"  {why}\n")

    rep_cost = args.rep_cost
    implied_quota = rep_cost * args.quota_multiple
    deals = implied_quota / acv if acv else float("inf")
    print(f"  Feasibility check (rep cost {_money(rep_cost)} x {args.quota_multiple:g} "
          f"= {_money(implied_quota)} quota):")
    print(f"    a rep would need to close ~{deals:,.0f} deals/year at this ACV")
    if deals > 200:
        print("    ! That is implausible for a human motion — push toward self-serve, "
              "partner, or a much higher ACV/packaging.")
    elif deals < 5:
        print("    Very few deals per rep — fine for enterprise; make sure pipeline & "
              "TAM support that few, large deals.")
    else:
        print("    Reasonable deal count for a human-led motion.")
    print("\n  Then document deal economics (cycle, win rate, CAC, payback) and the "
          "buying committee (template §11.1).")


def capacity(args):
    target, quota, ramp = args.target, args.quota, args.ramp
    eff_quota = quota * ramp
    aes = target / eff_quota
    aes_ceil = math.ceil(aes)
    print("Capacity / headcount model\n")
    print(f"  New revenue target........ {_money(target)}")
    print(f"  Quota per AE.............. {_money(quota)}")
    print(f"  Ramp productivity........ {ramp*100:.0f}%  -> effective quota {_money(eff_quota)}")
    print(f"  AEs needed............... {aes:.1f}  -> hire {aes_ceil}")
    print(f"  SDRs ({args.sdr_per_ae:g}/AE)............ {math.ceil(aes_ceil*args.sdr_per_ae)}")
    print(f"  SEs ({args.se_per_ae:g}/AE)............. {math.ceil(aes_ceil*args.se_per_ae)}")
    if args.book and args.csm_book:
        print(f"  CSMs (book {_money(args.book)} / {_money(args.csm_book)} per CSM)"
              f"... {math.ceil(args.book/args.csm_book)}")
    cov = target * args.coverage
    print(f"\n  Pipeline coverage needed.. {args.coverage:g}x target = {_money(cov)} open pipeline")
    print("\n  NEXT: set comp so each role's variable pay aligns to the metric it controls "
          "(run `comp`).")


def comp(args):
    ote, base_pct, quota = args.ote, args.base_pct, args.quota
    base = ote * base_pct
    variable = ote * (1 - base_pct)
    ratio = quota / variable if variable else float("inf")
    print("Compensation sanity check\n")
    print(f"  OTE...................... {_money(ote)}")
    print(f"  Base : Variable.......... {base_pct*100:.0f}:{(1-base_pct)*100:.0f}"
          f"  ({_money(base)} base / {_money(variable)} variable)")
    print(f"  Quota.................... {_money(quota)}")
    print(f"  Quota : Variable......... {ratio:.1f}x")
    if ratio < 4:
        print("    ! Below ~4x — comp is rich relative to quota; margins suffer.")
    elif ratio > 8:
        print("    ! Above ~8x — quota may be unreachable; reps churn. Re-check.")
    else:
        print("    Within the healthy ~4x-6x range.")
    print("\n  Typical splits: AE 50:50, SDR ~70:30, CSM ~80:20. Align variable to the "
          "metric each role controls.")


def channel_fit(args):
    with open(args.matrix, newline="", encoding="utf-8") as fh:
        data = [r for r in csv.reader(fh) if r and any(c.strip() for c in r)]
    header, body = data[0], data[1:]
    if header[1].strip().lower() != "weight":
        sys.exit("channel-fit: second column header must be 'weight'.")
    chans = header[2:]
    totals = {c: 0.0 for c in chans}
    wsum = 0.0
    for r in body:
        w = float(r[1])
        wsum += w
        for i, c in enumerate(chans):
            v = float(r[2 + i])
            if not (1 <= v <= 5):
                print(f"  ! {r[0]}/{c} = {v} outside 1-5")
            totals[c] += w * v
    maxp = wsum * 5 or 1
    ranked = sorted(totals.items(), key=lambda kv: kv[1], reverse=True)
    print("Channel-fit ranking (weighted)\n")
    print(f"  {'rank':<5}{'channel':<26}{'score':>9}{'/100':>9}")
    for i, (c, t) in enumerate(ranked, 1):
        print(f"  {i:<5}{c:<26}{t:>9.1f}{100*t/maxp:>9.1f}")
    print("\n  Primary = top scorer(s); make secondary/experiment from the mid band; cut "
          "the bottom. Concentrate effort — don't run them all (template §12.3).")


def main():
    p = argparse.ArgumentParser(description="Deterministic sales-motion math.")
    sub = p.add_subparsers(dest="cmd", required=True)

    m = sub.add_parser("motion")
    m.add_argument("--acv", type=float, required=True)
    m.add_argument("--rep-cost", type=float, default=150000,
                   help="fully-loaded annual cost of a quota-carrying rep (default 150000)")
    m.add_argument("--quota-multiple", type=float, default=5.0,
                   help="quota as a multiple of rep cost (default 5)")
    m.set_defaults(func=motion)

    c = sub.add_parser("capacity")
    c.add_argument("--target", type=float, required=True)
    c.add_argument("--quota", type=float, required=True)
    c.add_argument("--ramp", type=float, default=0.7, help="new-rep productivity factor (default 0.7)")
    c.add_argument("--sdr-per-ae", type=float, default=1.0)
    c.add_argument("--se-per-ae", type=float, default=0.0)
    c.add_argument("--book", type=float, help="ARR to support with CSMs")
    c.add_argument("--csm-book", type=float, help="ARR managed per CSM")
    c.add_argument("--coverage", type=float, default=3.5, help="pipeline coverage multiple (default 3.5)")
    c.set_defaults(func=capacity)

    cm = sub.add_parser("comp")
    cm.add_argument("--ote", type=float, required=True)
    cm.add_argument("--base-pct", type=float, required=True, help="base as a fraction, e.g. 0.5")
    cm.add_argument("--quota", type=float, required=True)
    cm.set_defaults(func=comp)

    cf = sub.add_parser("channel-fit")
    cf.add_argument("--matrix", required=True)
    cf.set_defaults(func=channel_fit)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
