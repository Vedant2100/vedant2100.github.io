#!/usr/bin/env python3
"""Guard against dangling project write-ups and missing archive links."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
site = root / "_site"
projects = (root / "_data/projects.yml").read_text(encoding="utf-8")
blogs = re.findall(r'^  blog: "([^"]+)"$', projects, flags=re.MULTILINE)
if len(blogs) < 10 or len(blogs) != len(set(blogs)):
    sys.exit("Expected 10+ projects and unique project-to-blog URLs")
if "undefined" in projects:
    sys.exit("Unresolved link value in project registry")
index = (site / "blog" / "index.html").read_text(encoding="utf-8")
project_index = (site / "projects" / "index.html").read_text(encoding="utf-8")
home = (site / "index.html").read_text(encoding="utf-8")
for url in blogs:
    page = site / url.strip("/") / "index.html"
    if not page.is_file():
        sys.exit(f"Missing project write-up: {url}")
    if url not in project_index:
        sys.exit(f"Project page missing link to {url}")
    if url not in index:
        sys.exit(f"Blog archive missing article {url}")
for url in ("/projects/", "/blog/"):
    if url not in home:
        sys.exit(f"Homepage missing {url}")
for required in (site / "robots.txt", site / "sitemap.xml"):
    if not required.is_file():
        sys.exit(f"Missing {required.name}")
for pattern in ("_posts/*blog-post*.md", "_posts/*future-post*.md"):
    if list(root.glob(pattern)):
        sys.exit(f"Template content remains: {pattern}")
print(f"OK: {len(blogs)} projects each linked to a generated, archived blog page.")
