#!/usr/bin/env python3
"""
render_png.py — rasterize a square signal-story card HTML to a PNG.

    python3 render_png.py card.html -o card.png [--size 1080] [--scale 2]

Uses Chromium via Playwright and screenshots the `.card-canvas` element, so the
PNG is exactly square at `size * scale` px (default 1080 * 2 = 2160, retina —
the same resolution social platforms prefer). If Playwright/Chromium is not
installed it prints the one-line install rather than failing silently. The HTML
is self-contained, so it can also just be opened in a browser and exported.
"""
import argparse
from pathlib import Path


def via_playwright(html_path, out_path, size, scale):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--no-sandbox"])
        page = browser.new_page(viewport={"width": size, "height": size},
                                device_scale_factor=scale)
        page.goto(Path(html_path).resolve().as_uri(), wait_until="networkidle")
        el = page.query_selector(".card-canvas")
        (el or page).screenshot(path=str(out_path))
        browser.close()
    return "chromium (playwright)"


def render(html_path, out_path, size=1080, scale=2):
    try:
        return via_playwright(html_path, out_path, size, scale)
    except Exception as e:  # noqa: BLE001
        raise SystemExit(
            "No PNG renderer available. For the LinkedIn image install:\n"
            "  pip install playwright && playwright install chromium\n"
            "Or open the self-contained .html in a browser and export it.\n"
            f"Tried playwright: {str(e).splitlines()[0][:140]}"
        )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("-o", "--out", default=None)
    ap.add_argument("--size", type=int, default=1080)
    ap.add_argument("--scale", type=int, default=2)
    a = ap.parse_args()
    out = a.out or str(Path(a.html).with_suffix(".png"))
    used = render(a.html, out, a.size, a.scale)
    print(f"{out}  (via {used})")


if __name__ == "__main__":
    main()
