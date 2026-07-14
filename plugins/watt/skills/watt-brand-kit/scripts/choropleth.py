#!/usr/bin/env python3
"""
choropleth.py — color the base US map (Albers, AK/HI insets) from an index.

Import:
    from choropleth import colorize, legend_items, DEFAULT_SCALE
    svg = colorize({"FL":106,"WA":91,...})          # -> colored <svg> string
    items = legend_items()                            # -> [{"label","color"},...]

CLI:
    echo '{"states":{"FL":106,"WA":91}}' | python3 choropleth.py > map.svg
    python3 choropleth.py spec.json > map.svg

The default scale is a neutral diverging index centred on 100 (parity); each
story supplies its own `scale` with story-specific labels. States with a value
are bucketed by the scale; states omitted or set
to null render as "low sample" (the base map's default fill). The scale and
the low-sample style are overridable so the same map serves other indices.
"""
import json, re, sys
from pathlib import Path

BASE_MAP = Path(__file__).resolve().parent.parent / "assets" / "us-states.svg"

# Diverging index buckets, high index -> low index. min/max inclusive; None = open end.
DEFAULT_SCALE = [
    {"key": "over2",  "label": "Over-indexes (≥120)",    "color": "#8e7cc9", "min": 120,  "max": None},
    {"key": "over1",  "label": "Above average (105–119)", "color": "#d7d0f2", "min": 105,  "max": 119},
    {"key": "par",    "label": "On par (95–104)",         "color": "#eaeaea", "min": 95,   "max": 104},
    {"key": "under1", "label": "Below average (85–94)",   "color": "#ffa087", "min": 85,   "max": 94},
    {"key": "under2", "label": "Under-indexes (≤84)",     "color": "#ff6200", "min": None, "max": 84},
]
LOW = {"key": "low", "label": "Low sample", "color": "#cdc4a5"}


def bucket(value, scale=DEFAULT_SCALE):
    """Return the scale bucket a numeric value falls in, or None."""
    if value is None:
        return None
    for b in scale:
        lo, hi = b.get("min"), b.get("max")
        if (lo is None or value >= lo) and (hi is None or value <= hi):
            return b
    return None


def colorize(states, scale=DEFAULT_SCALE, low=LOW, base_map=None):
    """Return the base SVG with per-state fills set from `states` (USPS->value)."""
    svg = Path(base_map or BASE_MAP).read_text()
    svg = svg.replace("var(--map-low, #cdc4a5)", low["color"])  # default = low sample
    colors = {}
    for code, val in (states or {}).items():
        b = bucket(val, scale)
        if b:
            colors[code.upper()] = b["color"]

    def repl(m):
        code = m.group(1)
        fill = colors.get(code)
        return f'<path id="{code}" fill="{fill}" ' if fill else m.group(0)

    return re.sub(r'<path id="([A-Z]{2})" ', repl, svg)


def legend_items(scale=DEFAULT_SCALE, low=LOW, states=None, used_only=False):
    """Legend rows [{label,color}]. With used_only=True, keep only buckets present."""
    rows = [{"label": b["label"], "color": b["color"]} for b in scale]
    rows.append({"label": low["label"], "color": low["color"]})
    if used_only and states is not None:
        present = {bucket(v, scale)["key"] for v in states.values() if bucket(v, scale)}
        keep = [b["label"] for b in scale if b["key"] in present]
        rows = [r for r in rows if r["label"] in keep] + [{"label": low["label"], "color": low["color"]}]
    return rows


if __name__ == "__main__":
    raw = open(sys.argv[1]).read() if len(sys.argv) > 1 else sys.stdin.read()
    spec = json.loads(raw)
    scale = spec.get("scale", DEFAULT_SCALE)
    sys.stdout.write(colorize(spec.get("states", {}), scale, spec.get("low", LOW)))
