#!/usr/bin/env python3
import os, sys
from datetime import datetime

def generate_index(directory):
    pdfs = [f for f in os.listdir(directory) if f.lower().endswith(".pdf")]
    pdfs.sort(key=lambda x: x.lower())
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    with open(os.path.join(directory, "index.html"), "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Compiled PDFs</title>
<style>
body {{ font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; background:#fafafa; color:#222; margin:2rem; }}
h1 {{ font-size:1.8rem; margin-bottom:1rem; }}
ul {{ list-style:none; padding:0; }}
li {{ margin:0.4rem 0; }}
a {{ color:#0066cc; text-decoration:none; word-break:break-word; }}
a:hover {{ text-decoration:underline; }}
footer {{ margin-top:2rem; font-size:0.9rem; color:#555; }}
.code {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; background:#fff; padding:0.2rem 0.4rem; border-radius:6px; border:1px solid #eee; }}
</style>
</head>
<body>
<h1>Compiled PDFs</h1>
<ul>
""")
        for pdf in pdfs:
            f.write(f'<li><a href="{pdf}">{pdf}</a></li>\n')
        f.write(f"""</ul>
<footer>Last updated: {now}</footer>
</body></html>
""")
    print(f"✅ index.html generated in {directory}")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    if not os.path.isdir(path):
        raise SystemExit(f"Not a directory: {path}")
    generate_index(path)
