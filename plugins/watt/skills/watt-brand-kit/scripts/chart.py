#!/usr/bin/env python3
"""
chart.py — dependency-free, on-brand SVG charts for signal stories.

bar_chart(bars, baseline=None, unit="") -> SVG string (class="chart")
  bars: [{"label","value","display"?,"color"?}]  (horizontal bars)
  The largest bar is lime (the headline); the rest lavender-deep. An optional
  baseline draws a dashed reference line (e.g. 1× = no over-index). Use this as
  the story's visual whenever there's no map — "even if it's just the data."

Colors/fonts mirror tokens.css so the chart matches the report.
"""
import html

LIME = "#D1FF01"; INK = "#222222"; LAV = "#8E7CC9"; MUTED = "#6f6a5d"; HAIR = "#e2e0d8"
MONO = "'Geist Mono', ui-monospace, monospace"
SANS = "'Geist', system-ui, sans-serif"


def _esc(t):
    return html.escape("" if t is None else str(t))


def bar_chart(bars, baseline=None, unit="", width=684, row_h=34, gap=13,
              pad_l=150, pad_r=52, pad_t=14, pad_b=20):
    n = len(bars)
    if n == 0:
        return ""
    longest = max((len(str(b.get("label", ""))) for b in bars), default=0)
    pad_l = min(max(pad_l, int(longest * 7.4) + 16), int(width * 0.5))
    h = pad_t + n * row_h + (n - 1) * gap + pad_b
    plot_w = width - pad_l - pad_r
    vmax = max([b["value"] for b in bars] + ([baseline] if baseline else []))
    vmax = vmax * 1.04 or 1
    scale = plot_w / vmax
    topv = max(b["value"] for b in bars)

    p = [f'<svg class="chart" viewBox="0 0 {width} {h}" xmlns="http://www.w3.org/2000/svg" '
         f'font-family="{SANS}">']

    # baseline reference line
    if baseline:
        bx = pad_l + baseline * scale
        p.append(f'<line x1="{bx:.1f}" y1="{pad_t-4}" x2="{bx:.1f}" y2="{h-pad_b+4}" '
                 f'stroke="{INK}" stroke-width="1" stroke-dasharray="3 3"/>')
        p.append(f'<text x="{bx:.1f}" y="{pad_t-6}" font-family="{MONO}" font-size="9.5" '
                 f'fill="{MUTED}" text-anchor="middle" letter-spacing=".05em">'
                 f'{_esc((baseline if baseline!=int(baseline) else int(baseline)))}{_esc(unit)} BASELINE</text>')

    for i, b in enumerate(bars):
        y = pad_t + i * (row_h + gap)
        val = b["value"]
        blen = max(val * scale, 1.5)
        fill = b.get("color") or (LIME if val == topv else LAV)
        disp = b.get("display") or f"{val:g}{unit}"
        # label (mono, right-aligned in the left gutter)
        p.append(f'<text x="{pad_l-12}" y="{y+row_h/2}" font-family="{MONO}" font-size="11" '
                 f'fill="{INK}" text-anchor="end" dominant-baseline="central" '
                 f'letter-spacing=".02em">{_esc(b["label"])}</text>')
        # bar
        p.append(f'<rect x="{pad_l}" y="{y}" width="{blen:.1f}" height="{row_h}" fill="{fill}"/>')
        # value: inside if the bar is long, else just past its end
        if blen > plot_w * 0.78:
            tx, anc, tf = pad_l + blen - 10, "end", (INK if fill == LIME else "#fff")
        else:
            tx, anc, tf = pad_l + blen + 8, "start", INK
        p.append(f'<text x="{tx:.1f}" y="{y+row_h/2}" font-size="14" font-weight="800" '
                 f'fill="{tf}" text-anchor="{anc}" dominant-baseline="central" '
                 f'letter-spacing="-.01em">{_esc(disp)}</text>')

    p.append("</svg>")
    return "".join(p)
