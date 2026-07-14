#!/usr/bin/env python3
"""
voice_check.py — lint a signal-story spec for AI tells and off-brand words
before it renders. Hard-fails on the two tells Watt kills on sight: prose
em-dashes and "not X, it's Y" contrasts. Warns on corporate-speak caution words
and spaced dashes. Numeric-range en-dashes (e.g. 106-117 written with an en-dash)
are allowed.

    python3 voice_check.py spec.json              # report; exit 1 on hard-fail
    python3 voice_check.py spec.json --warn-only   # report only, never exit 1

Editorial copy only: data fields (numbers, codes, colors) carry no prose, so the
checks never fire on them. Pairs with references/voice/ (antislop + watt-voice).
"""
import argparse, json, re, sys
from pathlib import Path

EM_HARD = re.compile(r"—|--")                      # em-dash or double hyphen
DASH_WARN = re.compile(r"\s[–-]\s")                # spaced en-dash/hyphen used as a dash
CONTRAST = [
    re.compile(r"\bnot\b[^.!?\n]{0,60}?[,—:]\s*(it'?s|its|it is|they'?re|that'?s|we'?re|you'?re)\b", re.I),
    re.compile(r"\bisn'?t\b[^.!?\n]{0,60}?[,—:]\s*(it'?s|its|it is)\b", re.I),
    re.compile(r"\bnot just\b[^.!?\n]{0,60}?\bbut\b", re.I),
    re.compile(r"\bnot because\b[^.!?\n]{0,60}?\bbut\b", re.I),
    re.compile(r"\bnot\b[^.!?\n]{0,40}?,\s*but\b", re.I),
]
CAUTION = [re.compile(p, re.I) for p in [
    r"\bleverage", r"\bsynergiz", r"\bdemocratiz", r"\bempower", r"\bgame-?changer",
    r"\brevolutionary\b", r"\binnovative\b", r"\bdisrupt", r"\bthought leader",
    r"\bbest-in-class\b", r"\bworld-class\b", r"\bcutting-edge\b", r"\bnext-gen",
    r"\bseamless\b", r"\bfrictionless\b", r"\bscalable\b", r"\bai-powered\b",
    r"\bdata-driven\b", r"\binsights\b", r"\bexcited to share\b", r"\bdeep dive\b",
    r"\blean into\b", r"\bdouble down\b", r"\bcircle back\b", r"\bunpack\b",
    r"\bnavigate\b", r"\bmoving forward\b", r"\bdata broker\b"]]

# fields that are data, not prose
DATA_KEYS = {"num","value","display","unit","theme","color","baseline","min","max",
             "id","trait_hash","hero","legend_used_only","states","scale","low","icp"}

def walk(node, path="", out=None):
    if out is None: out = []
    if isinstance(node, dict):
        for k, v in node.items():
            if k in DATA_KEYS: continue
            walk(v, f"{path}.{k}", out)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk(v, f"{path}[{i}]", out)
    elif isinstance(node, str):
        out.append((path.lstrip("."), node))
    return out

def check(spec):
    fails, warns = [], []
    for path, text in walk(spec):
        if EM_HARD.search(text):
            fails.append(("em-dash", path, text))
        for rx in CONTRAST:
            if rx.search(text):
                fails.append(("not-X-its-Y", path, text)); break
        if DASH_WARN.search(text):
            warns.append(("spaced dash", path, text))
        for rx in CAUTION:
            m = rx.search(text)
            if m:
                warns.append((f"caution: {m.group(0).strip()}", path, text)); break
    return fails, warns

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec"); ap.add_argument("--warn-only", action="store_true")
    a = ap.parse_args()
    spec = json.loads(Path(a.spec).read_text())
    fails, warns = check(spec)
    for kind, path, text in fails:
        print(f"FAIL [{kind}] {path}: {text}")
    for kind, path, text in warns:
        print(f"warn [{kind}] {path}: {text[:90]}")
    print(f"\nvoice_check: {len(fails)} hard-fail(s), {len(warns)} warning(s)")
    if fails and not a.warn_only:
        print("Fix the lines above (run the voice pass, references/voice/) before rendering.")
        sys.exit(1)

if __name__ == "__main__":
    main()
