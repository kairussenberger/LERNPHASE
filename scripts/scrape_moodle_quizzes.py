#!/usr/bin/env python3
"""Scrape Moodle quiz activities (e.g. the Analysis II Serien, which live as
quizzes rather than file downloads) and render each to a self-contained PDF in
materials/.

Reads the moodle-dl token from materials/config.json. It only READS your quiz
questions (via existing attempts, or a fresh in-progress attempt as a last
resort — it never submits anything).

    python3 scripts/scrape_moodle_quizzes.py --course 27792 \
        --out "materials/401-0262-00L Analysis II FS2026/Moodle-Aufgaben (Quiz-Scrape)"

Options:
  --course ID       Moodle course id (required)
  --out DIR         output folder (required)
  --filter TEXT     only quizzes whose name contains TEXT (repeatable)
  --only-quizid ID  just this quiz (for testing)
  --html-only       write self-contained .html instead of rendering PDF
"""
import argparse, base64, json, os, re, ssl, subprocess, sys, tempfile, urllib.parse, urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CFG = os.path.join(REPO, "materials", "config.json")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
CTX = ssl.create_default_context()

cfg = json.load(open(CFG))
TOK, DOM = cfg["token"], cfg["moodle_domain"]
WSBASE = f"https://{DOM}{cfg.get('moodle_path','/')}webservice/rest/server.php"


def ws(fn, **p):
    q = {"wstoken": TOK, "wsfunction": fn, "moodlewsrestformat": "json"}
    q.update(p)
    with urllib.request.urlopen(WSBASE + "?" + urllib.parse.urlencode(q, doseq=True), context=CTX, timeout=120) as r:
        return json.load(r)


def extract_div(html, cls):
    """Inner HTML of the first <div> whose class contains `cls`."""
    m = re.search(r'<div[^>]*class="[^"]*' + re.escape(cls) + r'[^"]*"', html)
    if not m:
        return None
    start = m.start()
    depth = 0
    for t in re.finditer(r'<div\b|</div>', html[start:]):
        depth += 1 if t.group() != "</div>" else -1
        if depth == 0:
            open_end = html.find(">", start) + 1
            return html[open_end:start + t.start()]
    return None


def questions_for(quiz):
    qid = quiz["id"]
    at = ws("mod_quiz_get_user_attempts", quizid=qid, status="all").get("attempts", [])
    finished = [a for a in at if a.get("state") == "finished"]
    inprog = [a for a in at if a.get("state") == "inprogress"]
    if finished:
        aid = max(finished, key=lambda x: x["id"])["id"]
        return ws("mod_quiz_get_attempt_review", attemptid=aid).get("questions", [])
    aid = None
    if inprog:
        aid = max(inprog, key=lambda x: x["id"])["id"]
    else:
        st = ws("mod_quiz_start_attempt", quizid=qid)
        aid = (st.get("attempt") or {}).get("id")
    if not aid:
        return []
    out, seen = [], set()
    for page in range(0, 30):
        qs = ws("mod_quiz_get_attempt_data", attemptid=aid, page=page).get("questions", [])
        new = [q for q in qs if q["slot"] not in seen]
        if not new:
            break
        for q in new:
            seen.add(q["slot"]); out.append(q)
    return sorted(out, key=lambda q: q["slot"])


def embed_images(html):
    def repl(m):
        src = m.group(1).replace("&amp;", "&")
        if "pluginfile.php" not in src:
            return m.group(0)
        rest = src.split("pluginfile.php/", 1)[1].split("?", 1)[0]
        url = f"https://{DOM}/webservice/pluginfile.php/{rest}?token={TOK}"
        try:
            with urllib.request.urlopen(url, context=CTX, timeout=90) as r:
                data = r.read(); ct = r.headers.get("Content-Type", "image/png")
            return 'src="data:%s;base64,%s"' % (ct, base64.b64encode(data).decode())
        except Exception:
            return m.group(0)
    return re.sub(r'src="([^"]+)"', repl, html)


TEMPLATE = """<!doctype html><html lang="de"><head><meta charset="utf-8">
<title>{title}</title>
<script>window.MathJax={{tex:{{inlineMath:[['\\\\(','\\\\)']],displayMath:[['\\\\[','\\\\]']]}},svg:{{fontCache:'global'}}}};</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>
 body{{font:15px/1.55 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;color:#1a1a1a;max-width:820px;margin:0 auto;padding:28px}}
 h1{{font-size:20px;border-bottom:2px solid #333;padding-bottom:8px}}
 .src{{color:#888;font-size:12px;margin-bottom:22px}}
 .q{{padding:16px 0;border-top:1px solid #ddd}}
 .q:first-of-type{{border-top:0}}
 .qn{{font-size:11px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:#b45; margin-bottom:6px}}
 img{{max-width:100%;height:auto}}
 table{{border-collapse:collapse}} td,th{{border:1px solid #ccc;padding:3px 7px}}
</style></head><body>
<h1>{title}</h1><div class="src">{course} · aus Moodle-Quiz rekonstruiert (nicht offiziell) · {n} Aufgabe(n)</div>
{body}
</body></html>"""


def build_html(quiz, course_name):
    qs = questions_for(quiz)
    blocks = []
    for i, q in enumerate(qs, 1):
        inner = extract_div(q.get("html", ""), "qtext") or extract_div(q.get("html", ""), "formulation") or ""
        inner = embed_images(inner)
        if inner.strip():
            blocks.append(f'<div class="q"><div class="qn">Aufgabe {i}</div>{inner}</div>')
    if not blocks:
        return None
    return TEMPLATE.format(title=quiz["name"], course=course_name, n=len(blocks), body="\n".join(blocks))


def render_pdf(html, pdf_path):
    tmp = tempfile.mkdtemp()
    hp = os.path.join(tmp, "in.html"); open(hp, "w").write(html)
    op = os.path.join(tmp, "out.pdf")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                    f"--user-data-dir={os.path.join(tmp,'ud')}", "--no-first-run", "--no-default-browser-check",
                    "--virtual-time-budget=25000", "--run-all-compositor-stages-before-draw",
                    "--print-to-pdf-no-header", f"--print-to-pdf={op}", "file://" + hp],
                   capture_output=True, timeout=120)
    if os.path.exists(op) and os.path.getsize(op) > 0:
        os.replace(op, pdf_path); return True
    return False


def safe(name):
    return re.sub(r"[/:\\]+", "-", name).strip()[:120]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--course", type=int, required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--filter", action="append", default=[])
    ap.add_argument("--only-quizid", type=int)
    ap.add_argument("--html-only", action="store_true")
    a = ap.parse_args()

    course_name = os.path.basename(a.out.rstrip("/")) or str(a.course)
    quizzes = ws("mod_quiz_get_quizzes_by_courses", **{"courseids[0]": a.course}).get("quizzes", [])
    if a.only_quizid:
        quizzes = [q for q in quizzes if q["id"] == a.only_quizid]
    if a.filter:
        quizzes = [q for q in quizzes if any(f.lower() in q["name"].lower() for f in a.filter)]
    os.makedirs(a.out, exist_ok=True)
    print(f"{len(quizzes)} quiz(zes) to scrape -> {a.out}")
    ok = 0
    for q in quizzes:
        try:
            html = build_html(q, course_name)
        except Exception as e:
            print(f"  ✗ {q['name']}: {e}"); continue
        if not html:
            print(f"  – {q['name']}: no question content"); continue
        base = os.path.join(a.out, safe(q["name"]))
        if a.html_only:
            open(base + ".html", "w").write(html); print(f"  ✓ {q['name']}.html"); ok += 1
        else:
            if render_pdf(html, base + ".pdf"):
                print(f"  ✓ {q['name']}.pdf"); ok += 1
            else:
                open(base + ".html", "w").write(html); print(f"  ⚠ {q['name']}: PDF failed, wrote .html")
    print(f"done: {ok}/{len(quizzes)}")


if __name__ == "__main__":
    main()
