# Worked example — a real ETH block-exam study hub

> 📎 **This is a filled-in instance of the [LERNPHASE template](README.md)** — one person's plan for a 4-exam ETH block (August 2026). It's kept as a reference so you can see the *level of detail* that works in practice, then replace it with your own. New here? Start with the **[README](README.md)**, then the step-by-step **[ADD-YOUR-OWN-COURSES.md](ADD-YOUR-OWN-COURSES.md)**.

Single source of truth for the August block exams. This hub decides **what to do every day** to maximize exam output under tight time.

> **Status: full plan + study assets built.** Four subject docs, a P1 week-by-week plan, a P3 cram ladder, and three ready-to-use [study assets](#study-assets) — all built around the confirmed exam order. Scope confirmed: **4 subjects** (High-Speed Signal Propagation *excluded*). SF trip = laptop, a few hrs/day.

---

## The four subjects — in exam order

| Exam date | Subject | Doc | Aids allowed | One-line strategy |
|-----------|---------|-----|--------------|-------------------|
| **Mon 03.08** 15:30 | Electronic Circuits (EC) | [subjects/Electronic-Circuits.md](subjects/Electronic-Circuits.md) | 🟢 **10 pages** notes (typed OK) + calculator | Build the ultimate **R_in/R_out/A_v** compendium; drill problem sets + both midterms; Razavi for understanding. |
| **Wed 05.08** 16:00 | Diskrete Mathematik (DiskMath) | [subjects/Diskrete-Mathematik.md](subjects/Diskrete-Mathematik.md) | 🔴 **NONE** (all from memory) | **Memorize** number theory/algebra (flashcards); do *all* Übungen + solutions + Koch's old exams. |
| **Sat 15.08** 11:00 | Signals & Systems II (SigSys2) | [subjects/Signals-Systems-2.md](subjects/Signals-Systems-2.md) | 🟡 1 A4 sheet, 2-sided, handwritten | Lock the ~3 core ideas + A4 sheet, then **spam old exams** (esp. problems 2 & 4). Build speed. |
| **Thu 20.08** 09:30 | Technische Informatik (TIK) | [subjects/Technische-Informatik.md](subjects/Technische-Informatik.md) | 🔴 **NONE** (MC, no calculator) | Master *every* old-exam MC question (~100); read the kernel book; watch only the hardware/CPU lectures. |

> *Note:* **High-Speed Signal Propagation** (Tue 04.08, Bolognesi) appeared in the pasted block but is **out of scope** — you confirmed you're prepping only these 4. (If that changes, flag it: Aug 3–5 would become a 3-exam gauntlet.)

## Study assets

Ready-to-use, in [`assets/`](assets/). All are **starters from standard content — verify against your course notation/scope** before relying on them.

| Asset | File | Use |
|-------|------|-----|
| **DiskMath flashcards** | [`assets/DiskMath_Anki_deck.txt`](assets/DiskMath_Anki_deck.txt) | Import into Anki (File ▸ Import). ~60 high-yield cards: number theory, algebra, combinatorics, graphs, flows. **Run daily incl. SF** (no aids, exam Aug 5). |
| **EC formula compendium** | [`assets/EC_formula_sheet.md`](assets/EC_formula_sheet.md) | Backbone for your 10-page sheet: R_in/R_out/A_v master table (all configs), DC-bias recipe, diodes, cascode/mirror. Typeset → PDF, add schematics. |
| **SigSys2 A4 sheet** | [`assets/SigSys2_A4_sheet.md`](assets/SigSys2_A4_sheet.md) | Content plan for the 1 A4 handwritten sheet: state-space, stability, ctrb/obsv, Laplace/Nyquist/Bode, discrete, Lyapunov. |

### 📊 Progress dashboard (localhost)
GitHub-style contribution graph + tickable per-subject checklists, saved in your browser. Run:
```
cd dashboard && python3 -m http.server 8000
```
then open **http://localhost:8000** . (Or just double-click `dashboard/index.html`.) Click days to log study hours; tick tasks as you finish them.

### 📋 Per-subject playbooks (problem index + decoded exam patterns)
- [DiskMath](subjects/DiskMath_Serien-und-Pruefungen.md) · [Electronic Circuits](subjects/EC_Uebungen-und-Playbook.md) · [SigSys2](subjects/SigSys2_Playbook.md) · [TIK](subjects/TIK_Playbook.md)

### 🔴 Still to acquire (everything else is on disk)
- ✅ **SigSys2 old exams — FOUND** (full 2008–2026 archive + solutions in `your exams folder/Past Exams[ (Solutions)]/`).
- ✅ **EC old exams — FOUND** (5 in `your exams folder/SS2 exams/EC/`; HS 2024 closest). *(Two official midterms would still be the best predictor if you can get them.)*
- **TIK "MC bank" = past-exam + Übungsstunde questions** = the same material you're **reserving until end of July** (overfitting risk) — not a separate thing to acquire. You have `FS 2023` + the prof's example decks (03–11); grab more old TIK papers if you can, for the end-of-July-onward phase.
- *Note:* `2022 Control-Signals cheat-sheet` is a SigSys2/Control cheat-sheet (not EC); `ZusammenfassungenDerVorlesungsstunden.pdf` is DiskMath (not TIK).

---

## Time budget & phases

**Today: 2026-06-25. Exam window: Mon Aug 3 → Thu Aug 20.**

The exam order is the plan's spine: **EC (Aug 3)** and **DiskMath (Aug 5)** come first and back-to-back, while **SigSys2 (Aug 15)** and **TIK (Aug 20)** sit later with their own dedicated August windows. → **Front-load EC + DiskMath in P1; keep SigSys2 + TIK at "coverage" depth and finish them in August.**

| Phase | Dates | Days | Intensity | Purpose |
|-------|-------|------|-----------|---------|
| **P1 — Intensive build** | Jun 25 → Jul 22 | ~28 | 10 h/day | Learn everything. **EC + DiskMath to near-exam-ready**; SigSys2 + TIK to solid coverage. ~280 h. |
| **P2 — SF trip (laptop, light)** | Jul 23 → Jul 29 | ~7 | ~2–4 h/day | Daily **DiskMath Anki** (no aids, exam Aug 5!) + EC sheet review; **a few timed EC/DiskMath old-exam reps** on the laptop. No new theory. |
| **P3 — Exam-by-exam cram** | Jul 30 → Aug 20 | ~22 | 10 h/day | Each subject's final cram lands right before its exam (see ladder below). |

**The P3 cram ladder** (each subject peaks the day before its exam):

| Window | Days | Focus | → Exam |
|--------|------|-------|--------|
| Jul 30 – Aug 2 | 4 | **EC** final: timed midterms + mixed problems, rehearse navigating the 10-page sheet | → **EC Mon Aug 3 15:30** |
| Aug 3 (eve) – Aug 4 | ~1.5 | **DiskMath** final: both Koch exams timed, flashcard blitz, re-derive RSA/Euclid/CRT by hand | → **DiskMath Wed Aug 5 16:00** |
| Aug 5 (eve) – Aug 14 | ~9 | **SigSys2** big window: spam all old exams ×2, problems 2 & 4, speed drills, finalize A4 sheet | → **SigSys2 Sat Aug 15 11:00** |
| Aug 15 (eve) – Aug 19 | ~4.5 | **TIK** window: full MC bank ×2 timed, re-watch shaky hardware topics, PVK video + a peer's doc | → **TIK Thu Aug 20 09:30** |

**P1 split** (front-loaded toward the early exams):

| Subject | P1 hours | P1 target | Why |
|---------|----------|-----------|-----|
| Electronic Circuits | ~80 h | ~85% ready | First exam (Aug 3) + highest ROI; only 4 study days post-SF before it. Build the 10-page sheet now. |
| Diskrete Mathematik | ~75 h | ~80% ready | Exam Aug 5, **no aids** → memorization needs a long runway + spaced repetition through SF. |
| Technische Informatik | ~65 h | coverage (~55%) | Read kernel book + hardware lectures + MC bank pass #1 now; heavy MC drilling waits for the Aug 16–19 window. |
| Signals & Systems II | ~60 h | ~60% | Theory already started (the PVK); lock ideas + learn format now; exam-spam waits for the Aug 6–14 window. |

---

## P1 week-by-week (Jun 25 – Jul 22)

Use the [daily template](#daily-template-10-h-study--morning-gym) every day; the two **Deep blocks** go to that week's two priority subjects. Milestones, not minutes — if behind, protect EC + DiskMath first.

**Week 0 setup (Day 1, Jun 25):** gather everything → EC: Serien + both midterms + Razavi playlist + a classmate's R_in/R_out/A_v sheet. DiskMath: Übungen/Lösungen 1–13 + Koch SS25/WS25 + install **Anki**. TIK: the ~100-question MC bank + cebook + PVK video + a peer's AMIV doc + message **a strong peer**. SigSys2: all old exams + solutions.

| Week | Dates | EC (build) | DiskMath (build) | TIK (cover) | SigSys2 (cover) |
|------|-------|-----------|------------------|-------------|-----------------|
| **W1** | Jun 25–Jul 1 | Razavi **BJT small-signal**; Serien 2–6; start formula sheet (diodes, MOSFET basics) | **Number theory** V9–V10 (Euclid, congruences, **RSA**); Übungen 9–10; **start Anki** | Read cebook intro + **RISC-V/assembly**; first MC exposure | Re-lock 3 core ideas (the PVK); start **A4 sheet** |
| **W2** | Jul 2–Jul 8 | Serien 7–11 (MOSFET + BJT amps); **extend sheet to all configs**; Razavi MOSFET deltas | **Algebra** V11–13 (groups/rings/fields, Lagrange, coding); Übungen 11–13; Combinatorics V1–4 + Übungen 1–4 | cebook **kernel half** (buddy, virtual memory, paging) + matching MCs | Frequency domain (Laplace, Nyquist, Bode); grow A4 sheet |
| **W3** | Jul 9–Jul 15 | **Both midterms timed**; cascode/current mirror (Serien 12–13); **finalize sheet v1**; speed loops | **Graph theory/flows** V4–V8; Übungen 5–8; **Koch SS25 timed**; Anki daily | **Hardware lectures** (pipeline, caching, parallel exec) + RISC_V.pdf; MC pass on hardware | Discrete + nonlinear; **first old exam** |
| **W4** | Jul 16–Jul 22 | Redo weak Serien; **finalize 10-page sheet**; timed mixed problems → **~85%** | **Koch WS25 timed**; read **all Lösungen** (free points); flashcard mastery → **~80%** | Finish cebook; **full MC bank pass #1**; log weak areas | 2–3 old exams; problems 2 & 4 patterns; finalize A4 → **~60%** |

> **End-of-P1 checkpoint (Jul 22):** EC ~85%, DiskMath ~80%, TIK covered (~55%), SigSys2 ~60%. If you're behind, the two that *must* hit target are **EC and DiskMath** — they're examined first and you barely touch them after SF.

---

## Operating principles (how to study — applies to all four)

1. **Old exams are the syllabus.** For TIK, SigSys2, DiskMath the exam looks like past exams. *(EC is the exception — old exams differ; use problem sets + the two midterms instead.)*
2. **Active recall > rereading.** Don't passively read solutions — close the page and reproduce them. Make flashcards for anything memorized (DiskMath number theory above all).
3. **Speed is graded.** SigSys2 and EC reward writing fast. Once you know a pattern, **time yourself** and practice the mechanical workflow until it's reflex.
4. **Understand the few big ideas, then drill patterns.** Each course has a small conceptual core; the rest is repetition. Find the core (flagged in each doc), then pattern-match.
5. **Formula sheets win points.** Where a Formelsammlung is allowed, build it *yourself* — the act of building is studying, and a good sheet turns hard problems into lookups (critical for EC).
6. **One full pass in P1, spaced repetition in P2, timed mocks in P3.**

---

## Daily template (10 h study + morning gym)

A default day — adapt to energy and exam proximity. Two subjects/day keeps things fresh and exploits spacing.

| Block | Time | What |
|-------|------|------|
| Morning | — | **Gym** + breakfast |
| Deep block 1 | ~3 h | Hardest subject first (full focus, new theory or tough problems) |
| — | break | walk / lunch |
| Deep block 2 | ~3 h | Second subject — problem solving |
| — | break | — |
| Block 3 | ~2.5 h | Old exams / problem sets (timed where possible) |
| Evening | ~1.5 h | **Active recall**: flashcards, redo today's hardest problem from blank, log mistakes |

**Rules of thumb:** new/hard theory in the morning when fresh; pattern-drilling and old exams in the afternoon; recall + review at night. Rotate so each subject is touched every ~2 days (spacing beats cramming one subject for a week).

---

## Open items — all resolved ✅

✅ Exam dates + order, allowed aids per exam, current footing, scope (4 subjects, HSSP excluded), SF capacity (laptop, a few hrs/day), and the three study assets — all done.

**Next, when you're ready** (no action needed from me until you say go):
- **🔴 Pull the solution keys from Moodle** — neither the Serien nor the exam PDFs include solutions, and "understand all solutions" is the top friend tip. (DiskMath PVK solutions are on your Desktop as a stopgap.)
- **Same deep-ingest for EC / TIK / SigSys2** — all their materials are already on your Desktop (EC lectures 1–14, cebook + TIK slides, etc.). Say the word and I'll read them and build the same kind of problem index + exam-pattern playbook for each.
- Once you start studying, tell me where you're behind and I'll re-balance the week-by-week.
- I can expand any asset (more Anki cards, typeset the EC sheet to PDF, add solved problem-2/4 templates to the SigSys2 sheet).

---

## Changelog

- **2026-06-25** — Hub created: four subject docs from expert tips + document inventories. Exam dates received → P1 week-by-week + P3 cram ladder built around the real order (EC Aug 3 → DiskMath Aug 5 → SigSys2 Aug 15 → TIK Aug 20). Scope confirmed (4 subjects). Built three study assets (DiskMath Anki deck, EC formula compendium, SigSys2 A4 sheet).
- **2026-06-25 (later)** — **DiskMath deep-dive:** read all 13 Serien + all 3 exams (SS25/WS25/WS26). Built [DiskMath_Serien-und-Pruefungen.md](subjects/DiskMath_Serien-und-Pruefungen.md) (Serien index + decoded exam skeleton + guaranteed-points drill list); folded the official Koch syllabus into the subject doc; expanded the Anki deck to ~80 cards with exam-hotlist items. Flagged missing solution keys.
- **2026-06-25 (later 2)** — **EC/SigSys2/TIK deep-dive** (6 parallel readers): built playbooks for all three; key finds → EC formula sheet already exists in `ec pvk main doc complete.pdf` (Masterclass, R_in/R_out/A_v tables w/ page refs); SigSys2 exam decoded (4×25, P2=ctrb/obsv) but **old exams missing**; TIK MC templates indexed but **full MC bank missing**. DiskMath solutions now on disk. Built the **localhost progress dashboard** (`dashboard/index.html`).
- **2026-06-25 (later 3)** — Unzipped exam archives. **SigSys2 old exams FOUND** (2008–2026 + solutions) → analyzed 6 recent → **corrected structure: P1 modeling, P2 ctrb/obsv, P3 freq-domain, P4 nonlinear (Lyapunov/LaSalle); discrete-time is a P1 sub-part.** **EC old exams FOUND** (5; HS 2024 closest — diff-pair/CMRR surfaced). **TIK FS 2023 exam 🔒 quarantined** (reserved Aug 16–19, no questions read). Switched plan to **3-hour-session model**; added `schedule/SESSIONS.md` (today = EC kickoff) + a "Start here" panel on the dashboard.
