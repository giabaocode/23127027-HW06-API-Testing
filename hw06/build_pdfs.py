#!/usr/bin/env python3
"""
build_pdfs.py
Generates polished, professional PDF deliverables from Markdown documents
using Python markdown and Google Chrome headless printing.
"""

import os
import subprocess
import markdown
import pypdf

CHROME_BIN = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CSS_STYLES = """
@page {
    size: A4;
    margin: 18mm 14mm 18mm 14mm;
    @bottom-center {
        content: counter(page);
    }
}
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 10.5pt;
    line-height: 1.55;
    color: #24292f;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
}
h1, h2, h3, h4, h5, h6 {
    color: #1f2328;
    font-weight: 600;
    margin-top: 1.2em;
    margin-bottom: 0.6em;
    page-break-after: avoid;
}
h1 {
    font-size: 19pt;
    border-bottom: 2px solid #0969da;
    padding-bottom: 6px;
    color: #0969da;
}
h2 {
    font-size: 14pt;
    border-bottom: 1px solid #d0d7de;
    padding-bottom: 4px;
    color: #1f2328;
}
h3 {
    font-size: 12pt;
    color: #24292f;
}
p {
    margin-top: 0;
    margin-bottom: 10px;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin-top: 12px;
    margin-bottom: 16px;
    font-size: 9pt;
    page-break-inside: avoid;
}
table, th, td {
    border: 1px solid #d0d7de;
}
th, td {
    padding: 6px 10px;
    text-align: left;
    vertical-align: top;
}
th {
    background-color: #f6f8fa;
    font-weight: 600;
    color: #24292f;
}
tr:nth-child(even) {
    background-color: #fcfcfc;
}
blockquote {
    margin: 12px 0;
    padding: 8px 16px;
    color: #57601a;
    background-color: #f6f8fa;
    border-left: 4px solid #0969da;
    border-radius: 2px;
}
code {
    font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Monaco, Consolas, "Liberation Mono", monospace;
    font-size: 8.8pt;
    background-color: #eff1f3;
    padding: 2px 4px;
    border-radius: 3px;
}
pre {
    background-color: #f6f8fa;
    border: 1px solid #d0d7de;
    border-radius: 6px;
    padding: 10px 14px;
    overflow-x: auto;
    font-size: 8.5pt;
    line-height: 1.45;
    page-break-inside: avoid;
}
pre code {
    background-color: transparent;
    padding: 0;
    border-radius: 0;
}
hr {
    border: 0;
    height: 1px;
    background: #d0d7de;
    margin: 20px 0;
}
ul, ol {
    margin-top: 0;
    margin-bottom: 10px;
    padding-left: 24px;
}
li {
    margin-bottom: 4px;
}
img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 14px auto;
    border: 1px solid #d0d7de;
    border-radius: 4px;
}
"""

def md_to_pdf(md_path, pdf_path):
    print(f"Building PDF: {md_path} -> {pdf_path}")
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    html_body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "toc"]
    )

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{os.path.basename(md_path)}</title>
<style>
{CSS_STYLES}
</style>
</head>
<body>
{html_body}
</body>
</html>"""

    tmp_html = pdf_path.replace(".pdf", ".tmp.html")
    with open(tmp_html, "w", encoding="utf-8") as f:
        f.write(full_html)

    cmd = [
        CHROME_BIN,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        tmp_html
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if os.path.exists(tmp_html):
        os.remove(tmp_html)

    # Validate with pypdf
    reader = pypdf.PdfReader(pdf_path)
    page_count = len(reader.pages)
    size_kb = os.path.getsize(pdf_path) / 1024
    print(f"  ✓ Created {pdf_path} ({size_kb:.1f} KB, {page_count} pages)")

def main():
    targets = [
        ("hw06/docs/main-report.md", "hw06/docs/main-report.pdf"),
        ("hw06/docs/ai-critique.md", "hw06/docs/ai-critique.pdf"),
        ("hw06/docs/ai-audit.md", "hw06/docs/ai-audit.pdf"),
        ("hw06/docs/cicd-report.md", "hw06/docs/cicd-report.pdf")
    ]
    for md, pdf in targets:
        if os.path.exists(md):
            md_to_pdf(md, pdf)
        else:
            print(f"Warning: Missing source markdown: {md}")

if __name__ == "__main__":
    main()
