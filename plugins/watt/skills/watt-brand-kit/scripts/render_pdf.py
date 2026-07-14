#!/usr/bin/env python3
"""
render_pdf.py — render a signal-story HTML file to PDF.

    python3 render_pdf.py story.html -o story.pdf

Tries renderers in order of fidelity and prints which one was used:
  1. Chromium via Playwright  (best: matches the original Chromium render)
  2. WeasyPrint               (reliable fallback, pure-Python deps)
  3. wkhtmltopdf              (last resort, if installed)

The page size (US Letter) and margins come from the @page rule in the CSS, so
every backend produces the same two-up layout. If none is available the script
explains how to install one rather than failing silently.
"""
import argparse, shutil, subprocess, sys
from pathlib import Path


def via_playwright(html_path, out_path):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--no-sandbox"])
        page = browser.new_page()
        page.goto(Path(html_path).resolve().as_uri(), wait_until="networkidle")
        page.pdf(path=str(out_path), prefer_css_page_size=True, print_background=True)
        browser.close()
    return "chromium (playwright)"


def via_weasyprint(html_path, out_path):
    from weasyprint import HTML
    HTML(str(html_path)).write_pdf(str(out_path))
    return "weasyprint"


def via_wkhtmltopdf(html_path, out_path):
    if not shutil.which("wkhtmltopdf"):
        raise RuntimeError("wkhtmltopdf not on PATH")
    subprocess.run(
        ["wkhtmltopdf", "--enable-local-file-access", "--print-media-type",
         "--page-size", "Letter", "--margin-top", "0", "--margin-bottom", "0",
         "--margin-left", "0", "--margin-right", "0", str(html_path), str(out_path)],
        check=True, capture_output=True,
    )
    return "wkhtmltopdf"


def render(html_path, out_path):
    errors = []
    for fn in (via_playwright, via_weasyprint, via_wkhtmltopdf):
        try:
            return fn(html_path, out_path)
        except Exception as e:  # noqa: BLE001
            errors.append(f"  - {fn.__name__}: {str(e).splitlines()[0][:120]}")
    raise SystemExit(
        "No PDF renderer available. Install one of:\n"
        "  pip install weasyprint        # reliable, recommended\n"
        "  pip install playwright && playwright install chromium   # best fidelity\n"
        "Tried:\n" + "\n".join(errors)
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("-o", "--out", default=None)
    a = ap.parse_args()
    out = a.out or str(Path(a.html).with_suffix(".pdf"))
    used = render(a.html, out)
    print(f"{out}  (via {used})")


if __name__ == "__main__":
    main()
