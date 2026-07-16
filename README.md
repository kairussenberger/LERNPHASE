# LERNPHASE — a study-block command center

**A fork-and-go template for surviving an intense block of exams.** Plan what to do every day, turn your course materials into a tickable checklist, and track your progress on a local dashboard — all from plain files, with no build step, no backend, and no account.

> *Lernphase* (German) = "study phase": the focused weeks before exams when you have a stack of subjects, a pile of PDFs, and not enough time. This repo gives that period a structure.

---

## What you get

Three layers, each independently useful:

1. **A Markdown knowledge base** — one *strategy doc* + one *playbook* per subject. The strategy doc says **what to prioritize and why**; the playbook is the deep dive (problem index, decoded exam patterns, "guaranteed points").
2. **Reusable study assets** — flashcard decks, formula/cheat-sheet plans — that you build once and drill repeatedly.
3. **A progress dashboard** — a single static HTML file: a GitHub-style activity heatmap + per-subject checklists, saved in your browser. No server required.

It ships with a **complete worked example** — a real 4-exam ETH block — in [`subjects/`](subjects/), [`assets/`](assets/), and **[EXAMPLE.md](EXAMPLE.md)**. Browse it for the level of detail that works, then replace it with your own.

---

## Quick start

```bash
git clone https://github.com/<you>/LERNPHASE.git
cd LERNPHASE

# open the dashboard
cd dashboard && python3 -m http.server 8000
# → http://localhost:8000   (or just double-click dashboard/index.html)
```

Then work through **[Make it your own](#make-it-your-own)** below. Progress (logged hours + ticked tasks) is stored per-browser; the dashboard's **Export / Import** buttons move it between machines.

---

## Repository structure

```
.
├── README.md                  ← you are here — the template front door + study method
├── ADD-YOUR-OWN-COURSES.md    ← step-by-step setup guide (incl. the dashboard internals)
├── EXAMPLE.md                 ← a real, filled-in plan (the worked example)
│
├── subjects/                  ← one or two Markdown docs per subject
│   ├── <Subject>.md           ←   strategy: what to study, why, allowed aids, core ideas
│   └── <Subject>_Playbook.md  ←   deep dive: problem index + decoded exam patterns
├── assets/                    ← reusable study assets (committed — they're yours)
│   ├── *_Anki_deck.txt        ←   tab-separated flashcards → import into Anki
│   └── *_sheet.md             ←   formula / cheat-sheet content plans
├── materials/                 ← drop your raw PDFs, slides, past exams here (git-ignored)
├── schedule/
│   └── SESSIONS.md            ← a running log of study sessions
└── dashboard/
    └── index.html             ← the progress dashboard (heatmap + checklists)
```

Only the dashboard contains logic. Everything else is Markdown that links to itself — so you can adopt this incrementally.

---

## Make it your own

Five steps, roughly in order. None take long; the value is in keeping them current as you study.

### 1 · List your subjects & exams

Replace the table below with yours — one row per exam, in the order you sit them. The exam order is the spine of the whole plan: it tells you what to front-load.

> Exam dates are set (FS2026 Sommersession). **Allowed aids per exam are still TBD** — confirm the Hilfsmittel in the exam info / myStudies and update the 🟡/🔴 column.

| Exam date | Subject | Doc | Aids allowed | One-line strategy |
|-----------|---------|-----|--------------|-------------------|
| **Aug 3** | Physik – MAVT | [subjects/Physik-MAVT.md](subjects/Physik-MAVT.md) | 🟡 own cheat sheet (Julia, 10 p.) | 15 past Blockprüfungen *with solutions* — drill timed |
| **Aug 5** | Informatik II | [subjects/Informatik-II.md](subjects/Informatik-II.md) | 🟡 own cheat sheet (ZSF Info 2) | ZF + Übungen; it's a coding course — write code, then drill past exams |
| **Aug 7** | Mechanik II | [subjects/Mechanik-II.md](subjects/Mechanik-II.md) | 🟡 provided Formelsammlung | ~25 past exams are the syllabus — drill Klausuren FS20–25 timed |
| **Aug 11** | Lineare Algebra II | [subjects/Lineare-Algebra-II.md](subjects/Lineare-Algebra-II.md) | 🔴 TBD (likely closed-book) | 72 past Basisprüfungen + Repetition summaries |
| **Aug 13** | Maschinenkonstruktion | [subjects/Maschinenkonstruktion.md](subjects/Maschinenkonstruktion.md) | 🟡 TBD (formula/tables) | Learn each element's design recipe; do every Übung |
| **Aug 19** | Analysis II | [subjects/Analysis-II.md](subjects/Analysis-II.md) | 🔴 TBD (likely closed-book) | Old Ana II exams + Integral-Trainer daily |

> Tip: capture **allowed aids** explicitly per exam — they change everything. A closed-book exam means flashcards and spaced repetition; an open-book exam means *build the best possible reference sheet*.

The same subject list also drives the dashboard's countdown and checklists — see step 4.

### 2 · Import your files & summaries

This repo tracks your **plan and your notes**, not your raw course files. Keep large or copyrighted material (lecture PDFs, recorded past exams, scanned scripts) **out of git** and reference it from your notes.

**Where things go:**

| You have… | Put it in… | Committed to git? |
|-----------|-----------|-------------------|
| Lecture PDFs, slides, past-exam papers, scanned scripts | `materials/` | **No** — git-ignored, stays on your machine |
| A summary/cheat-sheet *you wrote* (PDF or handwritten) | `materials/` + index it in a playbook | No (the PDF); yes (the index) |
| Summaries you want to *write or maintain as text* | `subjects/<Subject>.md` or a `_Notes.md` | **Yes** — searchable, linkable, diff-able |
| Flashcards, formula-sheet plans | `assets/` | **Yes** — reusable, low-risk to share |

**How to "import":**

1. Drop everything into [`materials/`](materials/) — it's git-ignored (see [`.gitignore`](.gitignore)), so your private files never get pushed. Sub-folder it however you like (`materials/<subject>/...`).
2. In each subject doc, **reference the source by name** so your plan points back at the material, e.g. *"DC-bias recipe → see `Exercise_5.pdf`; full archive in `materials/`."*
3. Turn a raw pile into a usable map by writing a **playbook**: read the past exams and problem sets once, then record *what actually shows up* and *what to drill*. That decoding is the highest-leverage thing you'll do — see the example playbooks in [`subjects/`](subjects/).
4. **Summaries:** if you already have one, store the file in `materials/` and write a short index/decode of it in the playbook. If you're writing your own, write it as Markdown in `subjects/` so it's versioned and linkable.

> Why git-ignore raw materials? They're often big, copyrighted, or personal, and they bloat the repo. The structured *thinking* about them — what to drill, in what order — is what's worth committing and sharing.

### 3 · Write a strategy doc + playbook per subject

For each subject, keep up to two files in [`subjects/`](subjects/):

- **`<Subject>.md`** — the strategy: exam date + allowed aids, the few core ideas, what to prioritize and why, and an inventory of your resources.
- **`<Subject>_Playbook.md`** — the deep dive: an index of every problem set / past exam, the decoded exam structure (what each problem tends to test), and a "guaranteed points" drill list.

Collapse to one file if you prefer. These are just Markdown — the only wiring is the relative links between docs; update paths if you rename files.

### 4 · Turn your materials into dashboard checklists

The dashboard ([`dashboard/index.html`](dashboard/index.html)) gives every exam a live countdown and every subject a tickable checklist + progress bar. You configure it by editing a few clearly-marked blocks at the top of that one file: subject keys & colors, the study window dates, the `EXAMS` list, and the `TASKS` checklists.

👉 **Full, step-by-step instructions (with the exact code to change) are in [ADD-YOUR-OWN-COURSES.md](ADD-YOUR-OWN-COURSES.md).**

Rule of thumb: make checklist items **granular** — one checkbox per problem set, past exam, lecture, or summary chapter. Granular tasks make progress visible and tell you exactly what's left.

### 5 · Add assets and log your sessions

- Build **flashcards** (`assets/*.txt`, tab-separated, import into Anki) for anything you must memorize.
- Build **formula/cheat-sheet plans** (`assets/*.md`) for open-book exams — *building the sheet is itself studying.*
- Keep a lightweight log in [`schedule/SESSIONS.md`](schedule/SESSIONS.md): one block per session (date, subject, what you did, what's next).

---

## The study method this template encodes

These principles are baked into the structure above. They generalize across most university exams:

1. **Old exams are the syllabus.** For most courses the real exam looks like past exams. Decode their structure and drill it. *(Some courses are exceptions — where past exams diverge, lean on problem sets instead. Flag which is which per subject.)*
2. **Active recall beats rereading.** Don't passively read solutions — close the page and reproduce them. Flashcards for anything you must memorize.
3. **Understand the few big ideas, then drill patterns.** Every course has a small conceptual core and a lot of repetition. Find the core, then pattern-match.
4. **Speed is graded.** Many exams reward writing fast. Once you know a pattern, time yourself and rehearse the mechanical workflow until it's reflex.
5. **Build your own reference sheet.** Where aids are allowed, *make the sheet yourself* — the act of building is studying, and a good sheet turns hard problems into lookups.
6. **One full pass, then spaced repetition, then timed mocks.** Phase your effort (next section).

### A phase framework

Most study blocks fit three phases. Adapt the lengths to your timeline:

| Phase | Purpose |
|-------|---------|
| **P1 — Build** | Learn everything once. Front-load the subjects whose exams come first. |
| **P2 — Maintain** | Lighter window (travel, work, fatigue). Spaced repetition only — flashcards, sheet review, a few timed reps. No new theory. |
| **P3 — Cram, exam-by-exam** | Each subject's final push lands right before *its* exam. Timed mocks, weak-spot repair. |

A **cram ladder** falls out of this: order your final pushes by exam date so each subject peaks the day before you sit it. See [EXAMPLE.md](EXAMPLE.md) for a fully worked phase plan, week-by-week schedule, and cram ladder.

### A default day

| Block | What |
|-------|------|
| Deep block 1 (~3 h) | Hardest subject first — new theory or tough problems, while fresh |
| Deep block 2 (~3 h) | A second subject — problem solving |
| Block 3 (~2.5 h) | Old exams / problem sets, timed where possible |
| Evening (~1.5 h) | Active recall: flashcards, redo the day's hardest problem from blank, log mistakes |

Rotate so each subject is touched every ~2 days — spacing beats cramming one subject for a week.

---

## In short

1. **Fork / clone**, open the dashboard, hit **Reset** to clear the example's logged progress.
2. Fill in your **subjects & exam dates** (README table + dashboard).
3. Drop your PDFs into **`materials/`**; decode them into **playbooks**.
4. Build your **checklists, flashcards, and sheets**.
5. Study. Tick tasks, log hours, and re-balance when you fall behind.

Detailed walkthrough: **[ADD-YOUR-OWN-COURSES.md](ADD-YOUR-OWN-COURSES.md)** · Worked example: **[EXAMPLE.md](EXAMPLE.md)**

---

*Built with [Claude Code](https://claude.com/claude-code). Dashboard is self-contained vanilla HTML/CSS/JS; progress lives in `localStorage`. No data leaves your browser.*
