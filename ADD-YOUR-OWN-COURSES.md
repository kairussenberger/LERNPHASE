# Make it your own — adding your courses

This repo is a **self-contained, file-based study hub** for a set of exams. There is no build step, no backend, and no database: it's Markdown notes plus a single static HTML dashboard whose progress is saved in your browser (`localStorage`). That makes it trivial to fork and retarget at *your* subjects.

This guide walks through everything you need to change to turn it into a hub for your own courses.

---

## 0. What's in here

```
.
├── README.md                  ← the template front door + study method
├── ADD-YOUR-OWN-COURSES.md    ← this guide (the deep-dive on dashboard setup)
├── EXAMPLE.md                 ← a real, filled-in plan (worked example)
├── subjects/                  ← one (or two) Markdown docs per subject
│   ├── <Subject>.md           ←   the strategy doc (what to study, why)
│   └── <Subject>_Playbook.md  ←   the deep-dive (problem index, decoded exam patterns)
├── assets/                    ← reusable study assets (flashcards, formula sheets)
│   ├── *_Anki_deck.txt        ←   import into Anki
│   └── *_sheet.md             ←   formula / cheat-sheet content plans
├── materials/                 ← your raw PDFs / slides / past exams (git-ignored)
├── schedule/
│   └── SESSIONS.md            ← a running log of study sessions
└── dashboard/
    └── index.html             ← the progress dashboard (heatmap + checklists)
```

Nothing is wired together by code except the dashboard. The Markdown files just link to each other. So you can adopt this incrementally — start by editing the dashboard, then swap docs in as you write them.

---

## 1. Fork / clone and run the dashboard

```bash
git clone https://github.com/<you>/LERNPHASE.git
cd LERNPHASE/dashboard
python3 -m http.server 8000
# open http://localhost:8000
```

Or just double-click `dashboard/index.html` — it works straight off the filesystem too. Progress (logged hours + ticked tasks) is stored per-browser in `localStorage`; use the **Export / Import** buttons to move it between machines.

> First thing to do after forking: open the dashboard, hit **Reset**, and clear the previous owner's logged hours/ticks.

---

## 2. Configure the dashboard — `dashboard/index.html`

Everything lives in one file. There are five things to change, all near the top of the `<script>` block (around line 248) or in the `<style>` block (top of file).

### 2a. Pick a short key per subject

Each subject has a **2-letter key** used in three places that must all agree: the CSS color, the exam list, and the checklist. The starter uses `ec`, `dm`, `ss`, `ti`. Choose your own (e.g. `ph`, `cs`, `ma`, `bio`).

### 2b. Colors — `<style>` block

Define an accent color per key. Search for these lines and edit them (there's a dark set and a light set):

```css
/* dark theme */
--ec:#f0883e; --dm:#3fb950; --ss:#58a6ff; --ti:#bc8cff;
/* light theme */
--ec:#cf6a1d; --dm:#2f9e41; --ss:#2f7fe0; --ti:#8a55e8;
```

…and the key→accent mapping just below:

```css
[data-subject="ec"]{--accent:var(--ec);--accent-soft:var(--ec-soft)}
[data-subject="dm"]{--accent:var(--dm);--accent-soft:var(--dm-soft)}
/* …one line per subject key… */
```

Rename `ec`/`dm`/`ss`/`ti` to your keys (or just keep the names and re-point them). Add or remove lines so there's exactly one per subject.

### 2c. Dates and phases — top of `<script>`

```js
const START = new Date(2026,5,25), END = new Date(2026,7,20);   // study window
const SF_START = new Date(2026,6,23), SF_END = new Date(2026,6,29); // a "light" sub-window
const HOURS = [0,2,5,8,11];   // hours mapped to heatmap intensity levels 0–4
```

> ⚠️ **JavaScript months are 0-indexed.** `new Date(2026,5,25)` is **25 June 2026** (month `5` = June). Off-by-one here is the #1 mistake.

- `START`/`END` bound the contribution-graph heatmap and the progress phases.
- `SF_START`/`SF_END` mark an optional reduced-intensity window (originally a trip). If you don't need it, set both to a date outside your range, or delete the `sf` logic.
- The phase labels ("P1 · Intensive build", etc.) are set in the small IIFE right below — rename them to taste.

### 2d. Exams — the `EXAMS` array

```js
const EXAMS = [
  {key:'ec', name:'Electronic Circuits',    date:new Date(2026,7,3)},
  {key:'dm', name:'Diskrete Mathematik',    date:new Date(2026,7,5)},
  {key:'ss', name:'Signals & Systems II',   date:new Date(2026,7,15)},
  {key:'ti', name:'Technische Informatik',  date:new Date(2026,7,20)},
];
```

One entry per exam. `key` must match a color key (2b) and a `TASKS` key (2e). The dashboard auto-computes the countdown ("X days"), the exam markers on the heatmap, and a per-exam progress bar.

### 2e. Checklists — the `TASKS` object

This is the heart of it. One entry per subject, keyed by the 2-letter key:

```js
const TASKS = {
  ec: { name:'Electronic Circuits', c:'ec', items:[
    {g:'Formula sheet'},                              // a group header
    {id:'ec-fs1', t:'MOSFET stages table CS/CG/CD', s:1},  // a tickable row, ⭐ high-yield
    {id:'ec-mt',  t:'Source the 2 midterms', f:1},    // a tickable row, "acquire" flag
    // …more items…
  ]},
  // …more subjects…
};
```

Item shapes:

| Field | Meaning |
|-------|---------|
| `{g:'…'}` | A **group header** (not tickable) — use to section a subject's checklist. |
| `{id:'…', t:'…'}` | A **tickable task**. `id` must be **globally unique** (it's the `localStorage` key) — prefix with the subject key, e.g. `ec-fs1`. `t` is the label. |
| `s:1` | Marks the task ⭐ **high-yield** (renders a star). |
| `f:1` | Marks the task as **`acquire`** — something you still need to source/find. |

Overall progress %, per-subject bars, and the stats row are all derived automatically from which `id`s are ticked. You don't touch any rendering code.

### 2f. (Optional) The "Start here" hero panel

Near line 197 there's a hardcoded `<section class="card hero">` describing "today's session." It's plain HTML — rewrite the steps for your own first session, or delete the whole `<section>` if you don't want it.

---

## 3. Replace the subject docs — `subjects/`

For each subject, the starter keeps up to two Markdown files. Keep, rename, or collapse to one — your call:

- **`<Subject>.md`** — the *strategy* doc: exam date + allowed aids, the few core ideas, what to prioritize and why, resource inventory.
- **`<Subject>_Playbook.md`** — the *deep dive*: an index of every problem set / past exam, decoded exam structure (what each problem tends to test), and a "guaranteed points" drill list.

These are just Markdown — write them however suits you. The only "wiring" is the relative links between docs and from the README; update those paths if you rename files.

A practical pattern that worked well: read **all** the past exams and problem sets for a subject once, then write the playbook as "what actually shows up + what to drill." Old exams tend to *be* the syllabus.

---

## 4. Study assets — `assets/`

Drop in anything reusable:

- **Anki decks** as tab-separated `.txt` (Front⇥Back per line) → import via Anki's *File ▸ Import*.
- **Formula / cheat-sheet plans** as Markdown — typeset to PDF when allowed-aids let you bring a sheet.

Reference them from the relevant subject doc and from the README's asset table.

---

## 5. Update the schedule log — `schedule/SESSIONS.md`

A lightweight running log: one block per study session (date, subject, what you did, what's next). Clear out the starter content and log your own as you go. Entirely optional.

---

## 6. Update the top-level `README.md`

The README is the front door. Update:

- The **exam table** (date · subject · doc link · allowed aids · one-line strategy).
- The **phases / time budget** and **week-by-week** plan to your own timeline.
- The **study-assets table**.
- The **operating principles** if your courses reward different habits.

---

## Conventions worth keeping

- **One fact / one purpose per file.** It keeps the hub skimmable.
- **`id`s are forever.** Renaming a task's `id` orphans its ticked state in `localStorage`. Change `t` (the label) freely; avoid changing `id`.
- **Keys must agree** across CSS color, `EXAMS`, and `TASKS`.
- **Star the high-yield few** (`s:1`) so the dashboard tells you where the points are at a glance.
- **Export before big edits.** The Export button gives you a JSON backup of hours + ticks.

That's it — fork, retarget the four config blocks in `index.html`, swap in your docs, and you've got a personal exam command-center.
