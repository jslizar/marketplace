#!/usr/bin/env python3
"""
conjoint.py — design a conjoint study and estimate part-worth utilities.

A language model can describe conjoint but cannot actually (a) build a balanced
fractional-factorial profile set or (b) run the part-worth regression. This does
both, in pure Python (no numpy).

Subcommands:
  design     Generate a balanced (near-orthogonal) set of product profiles to
             show respondents, from attributes x levels.
  estimate   From collected ratings, estimate part-worth utilities, attribute
             importance, and (if a price attribute is given) willingness-to-pay.

Examples
--------
  python conjoint.py design --attributes attrs.json --out design.csv
  python conjoint.py estimate --responses responses.csv --price-attr Price

attrs.json:
  {"Performance": ["Low","High"],
   "GPS": ["No","Yes"],
   "Price": ["39.99","54.99","69.99"]}

responses.csv (for estimate): the design columns plus a final numeric column of
average ratings (1-10 or share-of-preference). Header must match attribute names.
  Performance,GPS,Price,rating
  High,Yes,69.99,8.1
  Low,No,39.99,4.2
  ...
"""

import argparse
import csv
import itertools
import json
import random
import sys


# ----- pure-python linear algebra -------------------------------------------

def _matT(A):
    return [list(col) for col in zip(*A)]


def _matmul(A, B):
    Bt = _matT(B)
    return [[sum(a * b for a, b in zip(row, col)) for col in Bt] for row in A]


def _solve(A, b):
    """Solve A x = b for square A via Gauss-Jordan with partial pivoting.
    Adds a tiny ridge if singular."""
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(M[r][col]))
        if abs(M[piv][col]) < 1e-12:
            return None  # singular
        M[col], M[piv] = M[piv], M[col]
        pivval = M[col][col]
        M[col] = [v / pivval for v in M[col]]
        for r in range(n):
            if r != col and abs(M[r][col]) > 1e-15:
                factor = M[r][col]
                M[r] = [a - factor * b for a, b in zip(M[r], M[col])]
    return [M[i][n] for i in range(n)]


def _ols(X, y):
    Xt = _matT(X)
    XtX = _matmul(Xt, X)
    Xty = [sum(Xt[i][k] * y[k] for k in range(len(y))) for i in range(len(Xt))]
    beta = _solve(XtX, Xty)
    if beta is None:  # ridge fallback
        for i in range(len(XtX)):
            XtX[i][i] += 1e-6
        beta = _solve(XtX, Xty)
        if beta is None:
            sys.exit("estimate: design is not estimable (collinear). Add more/varied profiles.")
        print("  (note: applied tiny ridge to stabilize a near-singular design)\n")
    return beta


# ----- design ----------------------------------------------------------------

def _min_profiles(attrs):
    return 1 + sum(len(v) - 1 for v in attrs.values())


def _balance_cost(rows, names, attrs):
    cost = 0.0
    n = len(rows)
    # single-level balance
    for j, nm in enumerate(names):
        ideal = n / len(attrs[nm])
        counts = {}
        for r in rows:
            counts[r[j]] = counts.get(r[j], 0) + 1
        cost += sum((counts.get(lv, 0) - ideal) ** 2 for lv in attrs[nm])
    # pairwise balance (orthogonality proxy)
    for a in range(len(names)):
        for b in range(a + 1, len(names)):
            la, lb = len(attrs[names[a]]), len(attrs[names[b]])
            ideal = n / (la * lb)
            counts = {}
            for r in rows:
                key = (r[a], r[b])
                counts[key] = counts.get(key, 0) + 1
            for lva in attrs[names[a]]:
                for lvb in attrs[names[b]]:
                    cost += (counts.get((lva, lvb), 0) - ideal) ** 2
    return cost


def design(args):
    with open(args.attributes, encoding="utf-8") as fh:
        attrs = json.load(fh)
    names = list(attrs.keys())
    full = list(itertools.product(*[attrs[n] for n in names]))
    total = len(full)
    need = _min_profiles(attrs)

    print(f"Attributes: {', '.join(f'{n}({len(attrs[n])})' for n in names)}")
    print(f"Full factorial = {total} profiles. Minimum for estimability = {need}.\n")

    if args.profiles:
        N = args.profiles
    elif total <= 24:
        N = total
    else:
        N = max(2 * need, 16)
    N = min(N, total)
    if N < need:
        print(f"  ! {N} profiles < {need} needed to estimate all part-worths. Raising to {need}.")
        N = need

    if N == total:
        chosen = [list(r) for r in full]
        print(f"Using the full factorial ({N} profiles) — small enough to show in full.\n")
    else:
        rng = random.Random(args.seed)
        best, best_cost = None, float("inf")
        for _ in range(6000):
            cand = rng.sample(full, N)
            c = _balance_cost(cand, names, attrs)
            if c < best_cost:
                best, best_cost = cand, c
                if best_cost == 0:
                    break
        chosen = [list(r) for r in best]
        print(f"Selected a balanced {N}-profile fractional design "
              f"(balance cost {best_cost:.1f}, 0 = perfectly balanced).\n")

    header = ["profile_id"] + names
    print("  " + "  ".join(header))
    for i, r in enumerate(chosen, 1):
        print("  " + "  ".join([str(i)] + r))

    if args.out:
        with open(args.out, "w", newline="", encoding="utf-8") as fh:
            wr = csv.writer(fh)
            wr.writerow(header + ["rating"])
            for i, r in enumerate(chosen, 1):
                wr.writerow([i] + r + [""])
        print(f"\nWrote design -> {args.out}  (collect avg ratings in the 'rating' column, "
              "then run `estimate`).")


# ----- estimate --------------------------------------------------------------

def estimate(args):
    rows = list(csv.reader(open(args.responses, newline="", encoding="utf-8")))
    rows = [r for r in rows if r and any(c.strip() for c in r)]
    header, body = rows[0], rows[1:]
    resp_col = args.response_col or header[-1]
    if resp_col not in header:
        sys.exit(f"estimate: response column '{resp_col}' not in header {header}")
    ri = header.index(resp_col)
    attr_names = [h for k, h in enumerate(header) if k != ri and h != "profile_id"]
    attr_idx = {h: header.index(h) for h in attr_names}

    # collect levels per attribute (in order of appearance)
    levels = {a: [] for a in attr_names}
    for r in body:
        for a in attr_names:
            v = r[attr_idx[a]]
            if v not in levels[a]:
                levels[a].append(v)

    price_attr = args.price_attr
    if price_attr and price_attr not in attr_names:
        sys.exit(f"estimate: --price-attr '{price_attr}' not found.")

    # build design matrix: intercept + dummies (ref = first level) ; price numeric if flagged
    col_labels = ["(intercept)"]
    for a in attr_names:
        if a == price_attr:
            col_labels.append(f"{a}[numeric]")
        else:
            for lv in levels[a][1:]:
                col_labels.append(f"{a}={lv}")

    X, y = [], []
    for r in body:
        row = [1.0]
        for a in attr_names:
            val = r[attr_idx[a]]
            if a == price_attr:
                row.append(float(val))
            else:
                for lv in levels[a][1:]:
                    row.append(1.0 if val == lv else 0.0)
        X.append(row)
        y.append(float(r[ri]))

    beta = _ols(X, y)
    coef = dict(zip(col_labels, beta))

    print("Part-worth utilities (reference level = 0)\n")
    importance = {}
    price_coef = None
    for a in attr_names:
        if a == price_attr:
            price_coef = coef[f"{a}[numeric]"]
            print(f"  {a} (numeric): utility per unit price = {price_coef:+.4f}")
            importance[a] = abs(price_coef) * (max(float(l) for l in levels[a]) -
                                               min(float(l) for l in levels[a]))
            continue
        print(f"  {a}:")
        pw = {levels[a][0]: 0.0}
        for lv in levels[a][1:]:
            pw[lv] = coef[f"{a}={lv}"]
        for lv in levels[a]:
            print(f"      {lv:<16} {pw[lv]:+.3f}")
        importance[a] = max(pw.values()) - min(pw.values())

    tot = sum(importance.values()) or 1
    print("\nAttribute importance (share of total utility range):")
    for a in sorted(importance, key=importance.get, reverse=True):
        print(f"  {a:<18} {100*importance[a]/tot:5.1f}%")

    if price_coef is not None:
        print("\nWillingness-to-pay (price equivalent of each level vs. its reference):")
        if price_coef >= 0:
            print("  ! Price coefficient is non-negative — respondents 'prefer' higher price."
                  " Check the data; WTP is unreliable.")
        else:
            for a in attr_names:
                if a == price_attr:
                    continue
                for lv in levels[a][1:]:
                    wtp = coef[f"{a}={lv}"] / -price_coef
                    print(f"  {a}={lv:<14} {wtp:+.2f}  (vs {a}={levels[a][0]})")
    print("\nNEXT: choose the attribute configuration that maximizes utility within cost, "
          "and use WTP to anchor the price (template §7, §8).")


def main():
    p = argparse.ArgumentParser(description="Conjoint design & part-worth estimation.")
    sub = p.add_subparsers(dest="cmd", required=True)

    d = sub.add_parser("design")
    d.add_argument("--attributes", required=True)
    d.add_argument("--profiles", type=int)
    d.add_argument("--seed", type=int, default=42)
    d.add_argument("--out")
    d.set_defaults(func=design)

    e = sub.add_parser("estimate")
    e.add_argument("--responses", required=True)
    e.add_argument("--price-attr")
    e.add_argument("--response-col")
    e.set_defaults(func=estimate)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
