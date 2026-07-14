#!/usr/bin/env python3
"""
segment_tree.py — deterministic segmentation engine for GTM strategy work.

Three subcommands:

  enumerate   Cross every segmentation axis into the full MECE leaf set
              (this is how a real segmentation generates 50+ candidates).
  validate    Take a segment x attribute matrix and flag pairs that are
              identical / near-identical so they get COLLAPSED (the step
              a general model skips). Also flags non-discriminating
              attributes (zero variance).
  score       Take a criterion x segment matrix with weights and compute
              weighted attractiveness totals, ranked, normalized 0-100.

All input is CSV/JSON, stdlib only. No external dependencies.

Examples
--------
  python segment_tree.py enumerate --axes axes.json --out segments.csv
  python segment_tree.py validate --matrix validation.csv
  python segment_tree.py score --matrix evaluation.csv

Input formats
-------------
axes.json (enumerate):
  {"Type": ["Personal","Commercial"],
   "Use":  ["Professional","Recreational"],
   "Income": ["Low/Mid","High"]}

validation.csv (validate): first column = segment label, header row =
attribute names, cells = 1-10 scores.
  segment,PriceSens,Durability,Performance,TechSavvy
  Seg A,8,5,6,2
  Seg B,8,5,6,2

evaluation.csv (score): first column = criterion, second column = weight,
remaining columns = one per segment, cells = 1-10 scores.
  criterion,weight,Seg A,Seg B,Seg C
  Market Size,9,5,8,7
  Growth,8,6,5,7
"""

import argparse
import csv
import itertools
import json
import sys


def _read_csv(path):
    with open(path, newline="", encoding="utf-8") as fh:
        return [row for row in csv.reader(fh) if row and any(c.strip() for c in row)]


def enumerate_segments(axes_path, out_path=None):
    with open(axes_path, encoding="utf-8") as fh:
        axes = json.load(fh)
    if not isinstance(axes, dict) or not axes:
        sys.exit("axes file must be a non-empty JSON object of {axis: [values]}")
    names = list(axes.keys())
    value_lists = [axes[n] for n in names]
    combos = list(itertools.product(*value_lists))

    header = ["segment_id"] + names
    rows = [[str(i + 1)] + list(c) for i, c in enumerate(combos)]

    total_space = 1
    for v in value_lists:
        total_space *= len(v)

    print(f"Axes ({len(names)}): {', '.join(names)}")
    print("Levels per axis: " + ", ".join(f"{n}={len(axes[n])}" for n in names))
    print(f"Full combinatorial space = {' x '.join(str(len(v)) for v in value_lists)}"
          f" = {total_space} candidate segments\n")
    w = [max(len(h), max((len(r[i]) for r in rows), default=0)) for i, h in enumerate(header)]
    print("  ".join(h.ljust(w[i]) for i, h in enumerate(header)))
    for r in rows[:60]:
        print("  ".join(r[i].ljust(w[i]) for i in range(len(header))))
    if len(rows) > 60:
        print(f"... ({len(rows) - 60} more — see CSV)")

    if out_path:
        with open(out_path, "w", newline="", encoding="utf-8") as fh:
            wr = csv.writer(fh)
            wr.writerow(header)
            wr.writerows(rows)
        print(f"\nWrote {len(rows)} segments -> {out_path}")
    print("\nNEXT: narrow with a one-line rationale per branch you drop, then run `validate`.")
    return rows


def validate(matrix_path, threshold=1):
    data = _read_csv(matrix_path)
    header, body = data[0], data[1:]
    attrs = header[1:]
    labels = [r[0] for r in body]
    try:
        vecs = [[float(x) for x in r[1:]] for r in body]
    except ValueError:
        sys.exit("validate: all attribute cells must be numeric (1-10).")

    # range check
    for lbl, v in zip(labels, vecs):
        for a, x in zip(attrs, v):
            if not (1 <= x <= 10):
                print(f"  ! {lbl}/{a} = {x} is outside 1-10")

    # duplicate / near-duplicate detection (Manhattan distance)
    print("\nDuplicate / near-duplicate check (collapse these into a parent):")
    found = False
    for i in range(len(labels)):
        for j in range(i + 1, len(labels)):
            dist = sum(abs(a - b) for a, b in zip(vecs[i], vecs[j]))
            if dist <= threshold:
                found = True
                tag = "IDENTICAL" if dist == 0 else f"near (L1={dist:g})"
                print(f"  - {labels[i]}  ==  {labels[j]}   [{tag}] -> COLLAPSE")
    if not found:
        print("  none — all segments are distinct. Good.")

    # non-discriminating attributes (zero variance)
    print("\nNon-discriminating attributes (drop or rethink — they don't separate anyone):")
    flagged = False
    for k, a in enumerate(attrs):
        col = [v[k] for v in vecs]
        if max(col) == min(col):
            flagged = True
            print(f"  - {a}: every segment scored {col[0]:g}")
    if not flagged:
        print("  none — every attribute discriminates.")


def score(matrix_path):
    data = _read_csv(matrix_path)
    header, body = data[0], data[1:]
    if header[1].strip().lower() != "weight":
        sys.exit("score: second column header must be 'weight'.")
    segs = header[2:]
    crit, weights, scores = [], [], []
    for r in body:
        crit.append(r[0])
        try:
            weights.append(float(r[1]))
            scores.append([float(x) for x in r[2:]])
        except ValueError:
            sys.exit("score: weight and all score cells must be numeric.")

    for ci, row in zip(crit, scores):
        for x in row:
            if not (1 <= x <= 10):
                print(f"  ! {ci}: score {x} outside 1-10")

    totals = {s: 0.0 for s in segs}
    for w, row in zip(weights, scores):
        for si, s in enumerate(segs):
            totals[s] += w * row[si]
    max_possible = sum(weights) * 10 or 1
    ranked = sorted(totals.items(), key=lambda kv: kv[1], reverse=True)

    print(f"Weighted attractiveness (max possible = {max_possible:g}):\n")
    print(f"  {'rank':<5}{'segment':<28}{'score':>9}{'/100':>9}")
    for rank, (s, t) in enumerate(ranked, 1):
        print(f"  {rank:<5}{s:<28}{t:>9.1f}{(100 * t / max_possible):>9.1f}")

    spread = ranked[0][1] - ranked[-1][1]
    if spread < 0.15 * max_possible:
        print("\n  ! Low spread between best and worst — your weights or scores may be"
              "\n    too compressed (everything looks equally attractive). Re-anchor scores.")
    print("\nNEXT: carry the top segments into Targeting (template §6). Keep the table for the appendix.")


def main():
    p = argparse.ArgumentParser(description="Deterministic segmentation engine.")
    sub = p.add_subparsers(dest="cmd", required=True)

    pe = sub.add_parser("enumerate", help="cross axes into the full leaf set")
    pe.add_argument("--axes", required=True)
    pe.add_argument("--out")

    pv = sub.add_parser("validate", help="flag duplicate segments & dead attributes")
    pv.add_argument("--matrix", required=True)
    pv.add_argument("--threshold", type=float, default=1,
                    help="L1 distance at/under which two segments are 'near-identical' (default 1)")

    ps = sub.add_parser("score", help="weighted attractiveness scoring")
    ps.add_argument("--matrix", required=True)

    args = p.parse_args()
    if args.cmd == "enumerate":
        enumerate_segments(args.axes, args.out)
    elif args.cmd == "validate":
        validate(args.matrix, args.threshold)
    elif args.cmd == "score":
        score(args.matrix)


if __name__ == "__main__":
    main()
