#!/usr/bin/env python3
"""
build_card.py — assemble a 1:1 SOCIAL SUMMARY card from a signal-story spec.

    python3 build_card.py story.json -o card.html [--png] [--pdf]

A square (1080x1080) one-pager for LinkedIn and the like: the same dark hero,
lime hero-stat, choropleth, and WATT footer as the two-page report, in the Watt
design system. It reads the SAME spec the report uses and pulls the headline
beats — masthead, a stat trio, the map — so one spec drives both deliverables.

Curate the card with an optional top-level `card` object (see data-model.md);
absent that, it falls back to the masthead, the first stats block, and the first
map (or chart) block. The brand layer is inlined, so the HTML is portable. With
--png it rasterizes via Playwright (see watt-brand-kit/render_png.py); --pdf
renders a square single page via render_pdf.py.
"""
import argparse, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_story as bs  # noqa: E402  (reuse font_css, inline, esc, BRAND, cp, ch)

cp = bs.cp
ch = bs.ch
BRAND = bs.BRAND


def find_block(spec, btype):
    for pg in spec.get("pages", []):
        for b in pg.get("blocks", []):
            if b.get("type") == btype:
                return b
    return {}


def style():
    s = bs.font_css() + "\n"
    s += (BRAND / "assets" / "tokens.css").read_text()
    s += (BRAND / "assets" / "card.css").read_text()
    return s


def r_stats(items):
    cards = []
    for it in items[:3]:
        cls = "c-stat lime" if it.get("hero") else "c-stat"
        cards.append(f'<div class="{cls}"><div class="n">{bs.inline(it.get("num",""))}</div>'
                     f'<div class="l">{bs.inline(it.get("label",""))}</div></div>')
    return f'<div class="c-stats">{"".join(cards)}</div>'


def r_visual(card, spec):
    mp = card.get("map") or find_block(spec, "map")
    if mp:
        scale = mp.get("scale", cp.DEFAULT_SCALE)
        low = mp.get("low", cp.LOW)
        states = mp.get("states", {})
        svg = cp.colorize(states, scale, low)
        rows = cp.legend_items(scale, low, states, mp.get("legend_used_only", False))
        leg = "".join(
            f'<span><span class="sw" style="background:{r["color"]}"></span>{bs.esc(r["label"])}</span>'
            for r in rows)
        return (f'<div class="c-maprow"><div class="c-legend">{leg}</div>'
                f'<div class="c-visual">{svg}</div></div>')
    ct = card.get("chart") or find_block(spec, "chart")
    if ct:
        svg = ch.bar_chart(ct.get("bars", []), baseline=ct.get("baseline"), unit=ct.get("unit", ""), row_h=52, gap=18, pad_t=16, pad_b=20)
        return f'<div class="c-maprow c-hug"><div class="c-visual">{svg}</div></div>'
    tb = card.get("table") or find_block(spec, "table")
    if tb:
        cols = "".join(f"<th>{bs.esc(c)}</th>" for c in tb.get("columns", []))
        body = ""
        for row in tb.get("rows", []):
            body += "<tr>" + "".join(f"<td>{bs.inline(c)}</td>" for c in row) + "</tr>"
        return f'<div class="c-maprow c-hug"><div class="c-visual"><table class="dtable"><thead><tr>{cols}</tr></thead><tbody>{body}</tbody></table></div></div>'
    return ""


def build(spec):
    card = spec.get("card", {})
    mast = find_block(spec, "masthead")
    eyebrow = card.get("eyebrow", mast.get("eyebrow", ""))
    title = card.get("title", mast.get("title", spec.get("title", "")))
    dek = card.get("dek", mast.get("dek", ""))
    stats_block = card.get("stats") or find_block(spec, "stats").get("items", [])
    foot_l = card.get("footer", "WATT · CASE STUDY")
    foot_r = card.get("footer_right", "")

    body = (
        f'<header class="c-hero"><span class="c-badge">{bs.esc(eyebrow)}</span>'
        f'<h1 class="c-title">{bs.inline(title)}</h1>'
        f'<p class="c-dek">{bs.inline(dek)}</p></header>'
        f'<div class="c-body">{r_stats(stats_block)}{r_visual(card, spec)}</div>'
        f'<div class="c-foot"><span><span class="sq"></span>{bs.esc(foot_l)}</span>'
        f'<span>{bs.esc(foot_r)}</span></div>'
    )
    title_tag = bs.esc(card.get("title", title))
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{title_tag}</title><style>{style()}</style></head>'
            f'<body><div class="card-canvas">{body}</div></body></html>')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec")
    ap.add_argument("-o", "--out", default=None)
    ap.add_argument("--png", action="store_true", help="also rasterize a square PNG")
    ap.add_argument("--pdf", action="store_true", help="also render a square PDF")
    ap.add_argument("--no-voice-check", action="store_true", help="skip the AI-tell lint gate")
    a = ap.parse_args()
    spec = json.loads(Path(a.spec).read_text())
    if not a.no_voice_check:
        import voice_check
        fails, _ = voice_check.check(spec)
        if fails:
            import sys
            for kind, path, text in fails:
                print(f"FAIL [{kind}] {path}: {text}", file=sys.stderr)
            raise SystemExit(f"voice_check: {len(fails)} AI-tell(s) in the copy. "
                             "Run the voice pass (references/voice/), or pass --no-voice-check.")
    out = a.out or str(Path(a.spec).with_suffix(".html"))
    Path(out).write_text(build(spec))
    print(out)
    if a.png:
        import render_png
        png_out = str(Path(out).with_suffix(".png"))
        print(render_png.render(out, png_out), "->", png_out)
    if a.pdf:
        import render_pdf
        pdf_out = str(Path(out).with_suffix(".pdf"))
        print(render_pdf.render(out, pdf_out), "->", pdf_out)


if __name__ == "__main__":
    main()
