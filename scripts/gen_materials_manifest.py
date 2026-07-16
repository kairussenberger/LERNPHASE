#!/usr/bin/env python3
"""Generate dashboard/materials.js — a manifest of the local study files so the
dashboard's "Materials" tab can browse them.

The PDFs live in the git-ignored materials/ folder, so this manifest is also
git-ignored and only exists on your machine. Re-run after syncing new material:

    python3 scripts/gen_materials_manifest.py
"""
import os, json

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DASH = os.path.join(REPO, "dashboard")
ROOTS = ["materials", "assets"]                 # folders to expose in the browser
SKIP_NAMES = {".DS_Store", "config.json", "running.lock", "moodle_state.db"}
SKIP_EXT = {".db", ".log", ".lock"}             # never expose the moodle-dl token/db/logs


def build(abs_dir):
    node = {"name": os.path.basename(abs_dir), "dirs": [], "files": []}
    try:
        entries = sorted(os.listdir(abs_dir), key=str.lower)
    except OSError:
        return node
    for e in entries:
        if e in SKIP_NAMES or e.startswith("._"):
            continue
        p = os.path.join(abs_dir, e)
        if os.path.isdir(p):
            child = build(p)
            if child["dirs"] or child["files"]:
                node["dirs"].append(child)
        else:
            if os.path.splitext(e)[1].lower() in SKIP_EXT:
                continue
            node["files"].append({
                "name": e,
                "rel": os.path.relpath(p, DASH),     # e.g. ../materials/<subject>/<file>
                "size": os.path.getsize(p),
            })
    return node


def count(node):
    return len(node["files"]) + sum(count(d) for d in node["dirs"])


roots = []
for r in ROOTS:
    d = os.path.join(REPO, r)
    if os.path.isdir(d):
        roots.append(build(d))

with open(os.path.join(DASH, "materials.js"), "w") as f:
    f.write("window.MATERIALS=" + json.dumps(roots, ensure_ascii=False) + ";\n")

total = sum(count(r) for r in roots)
print(f"wrote dashboard/materials.js — {total} files across {len(roots)} root folder(s)")
