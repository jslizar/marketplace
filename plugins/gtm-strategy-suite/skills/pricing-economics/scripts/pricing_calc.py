#!/usr/bin/env python3
"""
pricing_calc.py — deterministic pricing & unit-economics math for GTM work.

Subcommands:
  breakeven   Contribution margin, CMR, breakeven units & $ (multi-scenario).
  evc         Economic Value to the Customer waterfall + value-based price band.
  unit-econ   LTV, LTV:CAC, CAC payback with health flags.
  elasticity  Arc price elasticity from two points + revenue direction.

Stdlib only. Run any subcommand with -h for its arguments.

Examples
--------
  python pricing_calc.py breakeven --price 69.99 --vc 6.00 --fixed 2900000
  python pricing_calc.py breakeven --scenarios scenarios.csv
  python pricing_calc.py evc --reference 49.99 --gains 20 --losses 2
  python pricing_calc.py unit-econ --arpa 12000 --gm 0.80 --cac 9000 --churn 0.15
  python pricing_calc.py elasticity --p1 50 --q1 1000 --p2 60 --q2 820
"""

import argparse
import csv
import sys


def _money(x):
    return f"${x:,.2f}"


def breakeven_one(price, vc, fixed, label=None):
    cm = price - vc
    if cm <= 0:
        print(f"  {label or 'scenario'}: contribution margin <= 0 "
              f"(price {_money(price)} <= variable cost {_money(vc)}). "
              "No breakeven — fix the cost structure or price.")
        return
    cmr = cm / price
    units = fixed / cm
    dollars = units * price
    head = f"  {label}: " if label else "  "
    print(f"{head}price {_money(price)} | var cost {_money(vc)} | fixed {_money(fixed)}")
    print(f"      contribution margin = {_money(cm)}   CMR = {cmr*100:.1f}%")
    print(f"      breakeven = {units:,.0f} units  =  {_money(dollars)} in sales")


def breakeven(args):
    print("Breakeven analysis\n")
    if args.scenarios:
        rows = list(csv.DictReader(open(args.scenarios, encoding="utf-8")))
        need = {"scenario", "price", "variable_cost", "fixed_costs"}
        if not rows or not need.issubset({k.strip() for k in rows[0]}):
            sys.exit("scenarios.csv needs columns: scenario,price,variable_cost,fixed_costs")
        for r in rows:
            breakeven_one(float(r["price"]), float(r["variable_cost"]),
                          float(r["fixed_costs"]), r["scenario"])
            print()
    else:
        if None in (args.price, args.vc, args.fixed):
            sys.exit("provide --price --vc --fixed, or --scenarios <csv>")
        breakeven_one(args.price, args.vc, args.fixed)
    print("NEXT: compare breakeven units/$ against a realistic projected volume — "
          "the gap is your margin of safety (template §8.7).")


def evc(args):
    ref = args.reference
    gains = args.gains
    losses = args.losses
    value = ref + gains - losses
    print("Economic Value to the Customer (EVC)\n")
    print(f"  Reference price (next-best alternative).... {_money(ref)}")
    print(f"  + Positive differentiation value.......... {_money(gains)}"
          "   (savings, productivity, risk reduced)")
    print(f"  - Negative differentiation value.......... {_money(losses)}"
          "   (switching cost, missing features)")
    print(f"  = EVC (the ceiling a rational buyer pays).. {_money(value)}\n")
    if value <= ref:
        print("  ! EVC <= reference: you have not yet shown net value over the alternative."
              " Strengthen the differentiation before pricing at a premium.")
        return
    surplus = value - ref
    print("  Value-based price band (capture a share of the surplus over the alternative):")
    for cap in (0.3, 0.5, 0.7):
        print(f"    capture {int(cap*100)}% -> price {_money(ref + cap*surplus)}"
              f"   (buyer keeps {_money(surplus*(1-cap))} of value)")
    print("\n  Rule of thumb: price leaves enough value on the buyer's side to make the"
          " switch obvious. Capturing 100% of EVC gives the buyer no reason to move.")


def unit_econ(args):
    arpa, gm, cac = args.arpa, args.gm, args.cac
    if args.lifetime:
        years = args.lifetime
        churn_note = f"{years:g} yr assumed lifetime"
    elif args.churn:
        if not (0 < args.churn <= 1):
            sys.exit("--churn must be an annual rate in (0,1].")
        years = 1 / args.churn
        churn_note = f"{args.churn*100:.0f}% annual churn -> {years:.1f} yr lifetime"
    else:
        sys.exit("provide --lifetime <years> or --churn <annual rate>")

    gross_per_year = arpa * gm
    ltv = gross_per_year * years
    ratio = ltv / cac if cac else float("inf")
    payback = cac / (gross_per_year / 12) if gross_per_year else float("inf")

    print("Unit economics\n")
    print(f"  ARPA (annual)............. {_money(arpa)}")
    print(f"  Gross margin.............. {gm*100:.0f}%  -> {_money(gross_per_year)}/yr gross")
    print(f"  Lifetime.................. {churn_note}")
    print(f"  CAC....................... {_money(cac)}\n")
    print(f"  LTV  = {_money(arpa)} x {gm*100:.0f}% x {years:.2f} yr = {_money(ltv)}")
    print(f"  LTV:CAC = {ratio:.2f} : 1   {'OK (>=3)' if ratio >= 3 else 'LOW (<3) — acquisition too expensive or value too low'}")
    print(f"  CAC payback = {payback:.1f} months   "
          f"{'OK' if payback <= 18 else 'LONG (>18 mo) — watch cash'}")
    print("\n  Benchmarks: LTV:CAC >= 3:1 healthy; payback <= 12 mo (SMB) to <= 24 mo (enterprise).")


def elasticity(args):
    p1, q1, p2, q2 = args.p1, args.q1, args.p2, args.q2
    if p1 == p2:
        sys.exit("p1 and p2 must differ.")
    dq = (q2 - q1) / ((q1 + q2) / 2)
    dp = (p2 - p1) / ((p1 + p2) / 2)
    e = dq / dp
    ae = abs(e)
    print("Price elasticity (arc method)\n")
    print(f"  ({p1:g}, {q1:g}) -> ({p2:g}, {q2:g})")
    print(f"  elasticity = {e:.2f}  (|e| = {ae:.2f})\n")
    if ae > 1:
        kind, lever = "ELASTIC", "cutting price raises total revenue; raising price lowers it"
    elif ae < 1:
        kind, lever = "INELASTIC", "raising price raises total revenue; you have pricing power"
    else:
        kind, lever = "UNIT-ELASTIC", "revenue is roughly flat to price changes (revenue-max point)"
    print(f"  Demand is {kind}: {lever}.")
    rev1, rev2 = p1 * q1, p2 * q2
    print(f"  Revenue: {_money(rev1)} -> {_money(rev2)} "
          f"({'+' if rev2 >= rev1 else ''}{(rev2-rev1)/rev1*100:.1f}%)")


def main():
    p = argparse.ArgumentParser(description="Deterministic pricing & unit-economics math.")
    sub = p.add_subparsers(dest="cmd", required=True)

    b = sub.add_parser("breakeven")
    b.add_argument("--price", type=float)
    b.add_argument("--vc", type=float)
    b.add_argument("--fixed", type=float)
    b.add_argument("--scenarios")
    b.set_defaults(func=breakeven)

    e = sub.add_parser("evc")
    e.add_argument("--reference", type=float, required=True)
    e.add_argument("--gains", type=float, default=0.0)
    e.add_argument("--losses", type=float, default=0.0)
    e.set_defaults(func=evc)

    u = sub.add_parser("unit-econ")
    u.add_argument("--arpa", type=float, required=True)
    u.add_argument("--gm", type=float, required=True, help="gross margin as a fraction, e.g. 0.80")
    u.add_argument("--cac", type=float, required=True)
    u.add_argument("--lifetime", type=float, help="customer lifetime in years")
    u.add_argument("--churn", type=float, help="annual churn rate (0-1); lifetime = 1/churn")
    u.set_defaults(func=unit_econ)

    el = sub.add_parser("elasticity")
    for a in ("p1", "q1", "p2", "q2"):
        el.add_argument(f"--{a}", type=float, required=True)
    el.set_defaults(func=elasticity)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
