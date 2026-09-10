#!/usr/bin/env python3
"""Render PLAN.md into page.template.html and write the two published files.

    python3 build.py

Outputs:
  index.html     the standalone page for GitHub Pages, with a full <head>
  artifact.html  the same body without the wrapper, for the Claude artifact

PLAN.md is the single source for the plan text. Edit it, re-run this, commit both outputs.
"""

import html
import re
from pathlib import Path

ROOT = Path(__file__).parent
PLACEHOLDER = "<!--PLAN-->"

HEAD = """<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#F6F0E1">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'><text y='14' font-size='14'>&#127755;</text></svg>">
<style>
  html { color-scheme: light; }
  body { margin: 0; }
  img { max-width: 100%; }
  [hidden] { display: none !important; }
</style>
"""


def inline(text):
    """Escape, then re-introduce the few inline marks the plan actually uses."""
    out = html.escape(text, quote=False)
    out = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
                 r'<a href="\2" target="_blank" rel="noopener">\1</a>', out)
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    return out


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def is_divider(line):
    return bool(re.fullmatch(r"\|[\s:|-]+\|", line.strip()))


def render(md):
    lines = md.split("\n")
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped.startswith("#"):
            level = len(stripped) - len(stripped.lstrip("#"))
            out.append(f"<h{level}>{inline(stripped[level:].strip())}</h{level}>")
            i += 1
            continue

        if re.fullmatch(r"-{3,}", stripped):
            out.append("<hr>")
            i += 1
            continue

        # table: a header row, a divider, then body rows
        if stripped.startswith("|") and i + 1 < len(lines) and is_divider(lines[i + 1]):
            head = split_row(stripped)
            i += 2
            body = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                body.append(split_row(lines[i]))
                i += 1
            out.append('<div class="tablewrap"><table>')
            if any(head):
                cells = "".join(f"<th>{inline(c)}</th>" for c in head)
                out.append(f"<thead><tr>{cells}</tr></thead>")
            out.append("<tbody>")
            for row in body:
                cells = "".join(f"<td>{inline(c)}</td>" for c in row)
                out.append(f"<tr>{cells}</tr>")
            out.append("</tbody></table></div>")
            continue

        if re.match(r"[-*] ", stripped):
            out.append("<ul>")
            while i < len(lines):
                cur = lines[i].strip()
                if re.match(r"[-*] ", cur):
                    item = [cur[2:]]
                    i += 1
                    # a wrapped continuation line is indented and not a new bullet
                    while (i < len(lines) and lines[i].startswith("  ")
                           and lines[i].strip() and not re.match(r"[-*] ", lines[i].strip())):
                        item.append(lines[i].strip())
                        i += 1
                    out.append(f"<li>{inline(' '.join(item))}</li>")
                elif not cur:
                    break
                else:
                    break
            out.append("</ul>")
            continue

        if stripped.startswith(">"):
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append(f'<p class="quote">{inline(" ".join(quote))}</p>')
            continue

        para = []
        while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith(("#", "|", ">", "- ", "* ")):
            para.append(lines[i].strip())
            i += 1
        out.append(f"<p>{inline(' '.join(para))}</p>")

    return "\n".join(out)


def main():
    template = (ROOT / "page.template.html").read_text(encoding="utf-8")
    if PLACEHOLDER not in template:
        raise SystemExit(f"{PLACEHOLDER} not found in page.template.html")

    body = template.replace(PLACEHOLDER, render((ROOT / "PLAN.md").read_text(encoding="utf-8")))

    marker = '<div class="sheet">'
    if body.count(marker) != 1:
        raise SystemExit(f'expected exactly one {marker}')
    doc = HEAD + body.replace(marker, "</head>\n<body>\n" + marker, 1) + "\n</body>\n</html>\n"

    (ROOT / "index.html").write_text(doc, encoding="utf-8")
    (ROOT / "artifact.html").write_text(body + "\n", encoding="utf-8")
    print(f"index.html {len(doc)} bytes, artifact.html {len(body)} bytes")


if __name__ == "__main__":
    main()
