#!/usr/bin/env python3
"""
build_story.py — assemble a Watt signal story into ONE self-contained HTML file
that matches the Signal Story Report Template (Geist, dark hero, square
1px-black cards, US Letter 816x1056).

    python3 build_story.py story.json -o out.html [--pdf]

The brand layer (tokens.css, components.css, embedded Geist woff2, base map,
choropleth) is pulled from the sibling watt-brand-kit skill and inlined, so the
output is a single portable file.
"""
import argparse, base64, html, json, re, sys
from pathlib import Path

BRAND = Path(__file__).resolve().parents[2] / "watt-brand-kit"
sys.path.insert(0, str(BRAND / "scripts"))
import choropleth as cp  # noqa: E402
import chart as ch  # noqa: E402

FONT_FACES = [
    ("Geist", 400, "Geist-Regular.woff2"), ("Geist", 500, "Geist-Medium.woff2"),
    ("Geist", 600, "Geist-SemiBold.woff2"), ("Geist", 700, "Geist-Bold.woff2"),
    ("Geist", 800, "Geist-Black.woff2"),
    ("Geist Mono", 400, "GeistMono-Regular.woff2"), ("Geist Mono", 500, "GeistMono-Medium.woff2"),
    ("Geist Mono", 700, "GeistMono-Bold.woff2"),
]


def inline(t):
    if t is None:
        return ""
    t = str(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\w)\*(.+?)\*(?!\w)", r"<em>\1</em>", t)
    t = re.sub(r"(?<!\w)_(.+?)_(?!\w)", r"<em>\1</em>", t)
    return t


def esc(t):
    return html.escape("" if t is None else str(t))


def font_css():
    out = []
    fdir = BRAND / "assets" / "fonts"
    for fam, wt, fn in FONT_FACES:
        p = fdir / fn
        if not p.exists():
            continue
        b64 = base64.b64encode(p.read_bytes()).decode()
        out.append(f"@font-face{{font-family:'{fam}';font-style:normal;font-weight:{wt};"
                   f"font-display:swap;src:url(data:font/woff2;base64,{b64}) format('woff2');}}")
    return "\n".join(out)


# ---------- block renderers (template markup) ----------
def r_masthead(b):  # rendered as the dark hero
    return (f'<header class="hero"><span class="badge">{esc(b.get("eyebrow",""))}</span>'
            f'<h1>{inline(b.get("title",""))}</h1>'
            f'<p>{inline(b.get("dek",""))}</p></header>')


def r_section_head(b):
    out = [f'<h2>{inline(b.get("title",""))}</h2>']
    if b.get("lead"):
        out.append(f'<p class="lead">{inline(b["lead"])}</p>')
    return "".join(out)


def r_stats(b):
    cards = []
    for it in b.get("items", []):
        cls = "stat lime" if it.get("hero") else "stat"
        cards.append(f'<div class="{cls}"><div class="n">{inline(it.get("num",""))}</div>'
                     f'<div class="l">{inline(it.get("label",""))}</div></div>')
    return f'<div class="grid">{"".join(cards)}</div>'


def r_composition(b):
    pills = "".join(f'<span class="pill a">{esc(c)}</span>' for c in b.get("kept", []))
    req = b.get("required", {})
    reqhtml = ""
    if req:
        tag = (f' <span style="color:var(--muted);font-weight:400;">{esc(req.get("tag",""))}</span>'
               if req.get("tag") else "")
        reqhtml = f'<span class="req">{esc(req.get("name",""))}{tag} &times;</span>'
    note = f'<p class="note-sm">{inline(b["note"])}</p>' if b.get("note") else ""
    return (f'<div class="card"><div class="label">{esc(b.get("title","Composition"))}</div>'
            f'<div class="comp-row">{reqhtml}{pills}</div>{note}</div>')


def r_map(b):
    intro = f'<p class="lead">{inline(b["intro"])}</p>' if b.get("intro") else ""
    scale = b.get("scale", cp.DEFAULT_SCALE)
    low = b.get("low", cp.LOW)
    states = b.get("states", {})
    svg = cp.colorize(states, scale, low)
    rows = cp.legend_items(scale, low, states, b.get("legend_used_only", False))
    leg = "".join(f'<span><span class="sw" style="background:{r["color"]}"></span>{esc(r["label"])}</span>'
                  for r in rows)
    return (f'{intro}<div class="maprow"><div class="legend-v">{leg}</div>'
            f'<div class="visual">{svg}</div></div>')


CLUSTER = {
    "over": ("a", "#3b2f63"), "mid": ("b", "#5c5640"), "under": ("c", "#6e2a12"),
    "dinein": ("a", "#3b2f63"), "hybrid": ("b", "#5c5640"), "ghost": ("c", "#6e2a12"),  # legacy aliases
}


def r_clusters(b):
    cols = []
    for c in b.get("items", []):
        cls, color = CLUSTER.get(c.get("theme", "hybrid"), ("b", "#5c5640"))
        pills = "".join(
            f'<span class="pill {cls}">'
            + esc((ch.get("name", "") if isinstance(ch, dict) else ch))
            + (f' {esc(ch["value"])}' if isinstance(ch, dict) and ch.get("value") is not None else "")
            + '</span>' for ch in c.get("chips", []))
        desc = f'<p>{inline(c.get("desc",""))}</p>' if c.get("desc") else ""
        cols.append(f'<div class="mkt {cls}"><h3 style="color:{color};">{esc(c.get("label",""))}</h3>'
                    f'<div class="pills">{pills}</div>{desc}</div>')
    return f'<div class="cols">{"".join(cols)}</div>'


def r_recs(b):
    head = r_section_head(b) if b.get("title") else ""
    lis = "".join(f'<li><strong>{inline(it.get("lead",""))}</strong> {inline(it.get("body",""))}</li>'
                  for it in b.get("items", []))
    return f'{head}<ul class="clean">{lis}</ul>'


def r_callout(b):
    lead = f'<strong>{inline(b["lead"])}</strong> ' if b.get("lead") else ""
    return f'<div class="note">{lead}{inline(b.get("body",""))}</div>'


def r_method(b):
    return f'<div class="method">{inline(b.get("text",""))}</div>'


def r_chart(b):
    if b.get("title"):
        head = r_section_head(b)
    else:
        head = f'<p class="lead">{inline(b["lead"])}</p>' if b.get("lead") else ""
    svg = ch.bar_chart(b.get("bars", []), baseline=b.get("baseline"), unit=b.get("unit", ""))
    note = f'<p class="note-sm">{inline(b["note"])}</p>' if b.get("note") else ""
    return f'{head}<div class="card">{svg}{note}</div>'


def r_table(b):
    head = r_section_head(b) if b.get("title") else (
        f'<p class="lead">{inline(b["lead"])}</p>' if b.get("lead") else "")
    cols = "".join(f"<th>{esc(c)}</th>" for c in b.get("columns", []))
    body = ""
    for row in b.get("rows", []):
        body += "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>"
    note = f'<p class="note-sm">{inline(b["note"])}</p>' if b.get("note") else ""
    return f'{head}<table class="dtable"><thead><tr>{cols}</tr></thead><tbody>{body}</tbody></table>{note}'


RENDER = {"masthead": r_masthead, "section_head": r_section_head, "stats": r_stats,
          "composition": r_composition, "map": r_map, "clusters": r_clusters,
          "recs": r_recs, "callout": r_callout, "method": r_method, "chart": r_chart, "table": r_table}


def render_block(b):
    fn = RENDER.get(b.get("type"))
    if not fn:
        raise SystemExit(f"Unknown block type: {b.get('type')!r}")
    return fn(b)


def build(spec):
    style = font_css() + "\n"
    style += (BRAND / "assets" / "tokens.css").read_text()
    style += (BRAND / "assets" / "components.css").read_text()

    pages = spec.get("pages", [])
    foot_label = esc(spec.get("footer", ""))
    n = len(pages)
    sheet = []
    for i, pg in enumerate(pages, 1):
        blocks = pg.get("blocks", [])
        hero = ""
        body = blocks
        if blocks and blocks[0].get("type") == "masthead":
            hero = r_masthead(blocks[0])
            body = blocks[1:]
        pad_style = "" if hero else ' style="padding-top:44px;"'
        content = "".join(render_block(b) for b in body)
        foot = (f'<div class="foot"><span>{foot_label}</span>'
                f'<span>Page {i} / {n}</span></div>')
        sheet.append(f'<div class="page">{hero}<div class="pad"{pad_style}>{content}</div>{foot}</div>')

    title = esc(spec.get("title", "Watt Signal Story"))
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{title}</title><style>{style}</style></head>'
            f'<body><div class="sheet">{"".join(sheet)}</div></body></html>')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec")
    ap.add_argument("-o", "--out", default=None)
    ap.add_argument("--pdf", action="store_true", help="also render a PDF next to the HTML")
    ap.add_argument("--no-voice-check", action="store_true", help="skip the AI-tell lint gate")
    a = ap.parse_args()
    spec = json.loads(Path(a.spec).read_text())
    if not a.no_voice_check:
        import voice_check
        fails, _ = voice_check.check(spec)
        if fails:
            for kind, path, text in fails:
                print(f"FAIL [{kind}] {path}: {text}", file=sys.stderr)
            raise SystemExit(f"voice_check: {len(fails)} AI-tell(s) in the copy. "
                             "Run the voice pass (references/voice/), or pass --no-voice-check.")
    out = a.out or str(Path(a.spec).with_suffix(".html"))
    Path(out).write_text(build(spec))
    print(out)
    if a.pdf:
        import render_pdf
        pdf_out = str(Path(out).with_suffix(".pdf"))
        print(render_pdf.render(out, pdf_out), "->", pdf_out)


if __name__ == "__main__":
    main()
