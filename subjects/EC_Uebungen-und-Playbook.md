# Electronic Circuits — Exercise Index + Playbook

Built from reading **Exercises 1–13** + the **`ec pvk main doc complete.pdf`** master doc. Companion to [Electronic-Circuits.md](Electronic-Circuits.md). Exam: **Mon 03.08, 15:30** · 10 pages of notes allowed.

> ## 🟢 Huge find: your formula sheet already exists
> **`ec pvk main doc complete.pdf`** is a 66-page handwritten **"EC Masterclass"** (by a student, exam-aligned, worked-example heavy). It contains the **exact R_in/R_out/A_v tables your friend said are "all that matters"**, plus worked problems:
> - **MOSFET stages** (CS, CS+degen, CG, CG+degen, CD/source-follower; λ=0 and λ≠0) → **pp. 30–31**
> - **MOSFET "impedance visions"** (looking into G/S/D, with/without degeneration; diode-connected) → **pp. 33–34**
> - **BJT "impedance visions"** (into C/E/B, with degeneration; diode-connected) → **pp. 42–43**
> - **BJT stages** (CE, CB, CC/emitter-follower; V_A=∞ and V_A≠∞) → **pp. 49–55**
> - **Cascode / GmRout / current mirrors** (MOS & BJT, copy-error, β-helper) → **pp. 57–64**
>
> **→ Your 10-page exam sheet is mostly a curation job:** print/condense Masterclass pp. 30–34, 42–43, 49–55, 57–64, cross-check against [the typed compendium](../assets/EC_formula_sheet.md), add schematic thumbnails + an index. This saves you days. *(Since machine-printed notes are allowed, you can even include cleaned-up versions of these pages directly.)*

> ⚠️ **Solutions gap:** the Exercise PDFs are problem statements only — **no solution keys.** The Masterclass doc is your de-facto answer key (its worked "ex." boxes solve the same circuit types and cross-reference the homework). Still worth sourcing official Serie solutions + **the two midterms** (not in your files) — the friend says the exam most resembles the midterms.

---

## The one workflow the whole exam tests
**DC bias (find operating point, verify region) → draw small-signal equivalent → look up R_in/R_out/A_v on your sheet → write the number.** Drill this until mechanical; the exam is a speed test. Easiest points: the DC-bias-then-small-signal problems where one formula from the sheet finishes it.

---

## Exercise index (what each Serie trains)

### Foundations & diodes (Ex 1–4) — *lower exam weight, but builds the method*
- **Ex 1 — Circuit theory recap.** Dividers, Thévenin/Norton, superposition, RC transfer function/Bode. (No transistors; underpins R_eq reasoning.)
- **Ex 2 — Diode models & rectifiers/limiters.** Exponential vs constant-V(0.8) vs zero-V models; piecewise transfer functions (diode ON/OFF); half-wave rectifier; voltage limiter.
- **Ex 3 — Small-signal concept (via diodes) + rectifiers.** First DC→small-signal→ΔV_out loop (diode r_d=V_T/I_D); ripple-voltage sizing; **Q7 = past-exam** 3-diode solve.
- **Ex 4 — Diode applications.** Non-ideal limiters, voltage doublers, waveform shifters, electronic switch; **Q7–Q8 = past-exam** multi-diode networks (solve V/I, ON/OFF by inspection).

### MOSFETs (Ex 5–8) — *core*
- **Ex 5 — MOSFET fundamentals.** Derive I_D quadratic; triode vs saturation; R_ON; DC bias + region check ("assume saturation → solve → verify V_DS≥V_ov").
- **Ex 6 — Large/small-signal models + PMOS.** Channel-length modulation (r_o), small-signal g_m; **Q5 = full loop on a PMOS CS stage** (bias → redraw small-signal → A_v).
- **Ex 7 — MOSFET amplifiers (CS/CG/CD).** ⭐ **The most concentrated R_in/R_out/A_v drill.** Q2 = explicit R_in/R_out per topology (λ=0 then λ≠0); Q3–Q6 = A_v + design (active/PMOS loads, cascode).
- **Ex 8 — MOSFET amps & load types.** CS/CG/CD with resistive/active/diode-connected loads; signal swing; spec-driven design (size W/L for target A_v + power).

### BJTs & multi-transistor (Ex 9–13) — *core + highest-value*
- **Ex 9 — ⭐ TWO PAST-EXAM MOS problems + BJT intro.** Q1 (CS w/ degeneration) & Q2 (8-resistor MOS stage) are **flagged "from past exam"** → **do these first, they're the closest thing to the real exam.** Q3–Q6 introduce BJT large-signal/biasing.
- **Ex 10 — BJT models & biasing.** Q-point (base-resistor, voltage-divider, self-bias, PNP); small-signal R_in/R_out with/without Early effect.
- **Ex 11 — Common-Emitter (+ cascode R_out).** CE gain/impedances, emitter resistor + bypass cap; Q4 derives the cascode R_out formula (reused in Ex 13).
- **Ex 12 — Common-Base & Common-Collector.** CB (R_in=1/g_m), CC/emitter-follower (A_v≈1, low R_out); symbolic R_in/A_v matching slide formulas.
- **Ex 13 — Cascodes, GmRout method, current mirrors.** A_v=−G_m·R_out; MOS & BJT mirrors (copy error, β-helper); full spec-driven CG design.

---

## Razavi — curated watch list (don't watch all ~80)
Playlist: **[Razavi Electronics — all lectures](https://www.youtube.com/watch?v=yQDfVJzEymI&list=PLyYrySVqmyVPzvVlPW-TTzHhNWg1J_0LU)** (Behzad Razavi, UCLA · *Fundamentals of Microelectronics*). Lecture titles indexed at infocobuild ("Electronic Circuits I, Behzad Razavi").
Friend's rule: *understand BJT small-signal really well, then get MOSFET "by difference" — don't overdo it.* So watch **Tier 1 fully**, **Tier 2 selectively**, **Tier 3 only if a topic feels shaky.**

**🎯 Tier 1 — core (this IS the exam skill: small-signal → R_in/R_out/A_v)**
- **Lec 15** — Biasing, Transconductance (g_m intuition)
- **Lec 16** — BJT I-V; Large- & Small-Signal Operation
- **Lec 17** — Small-Signal Model of the BJT, Early Effect ← *the keystone video*
- **Lec 20** — Common-Emitter Stage
- **Lec 21** — Common-Emitter: Input & Output Impedances ← *literally R_in/R_out/A_v*

**Tier 2 — the rest of the configs + MOSFET by difference**
- **Lec 18–19** — Early effect in the SS model, PNP, Intro to Amplifiers
- **~Lec 22–26** — Common-Base & Common-Collector / Emitter-Follower stages
- **Lec 29** — Introduction to MOSFETs
- **Lec 35** — CMOS Amplifiers: Common-Source topology
- **~Lec 36–41** — Common-Gate & Source-Follower (Lec 41 = Source Followers & Summary)

**Tier 3 — optional / on demand**
- Diodes & rectifiers (early lectures ~6–9) — only if **Ex 2–4** feel shaky
- **Cascodes & Current Mirrors** → switch to **Razavi *Electronics 2*** ("Lec 1: Cascode Current Sources" …) — pairs with **Ex 13**

**Skip:** the heavy semiconductor-physics opening lectures and anything past the course scope (frequency response, feedback, output stages) unless you're curious. If short on time, the single highest-leverage watch is **Lec 17 + Lec 21**.

## Old exams — `your exams folder/SS2 exams/EC/` (5 papers, "Halbleiter-Schaltungstechnik")
- **HS 2024 — drill thoroughly** (closest to the current course): **Task 2 = BJT CE** (DC→hybrid-π→R_in/R_out/A_v) and **Task 3 = NMOS differential pair** (A_d/A_cm/**CMRR**) are pure core-workflow. *(Tasks 1/4/5 = diode networks, Bode reading, Sallen-Key filters — in-scope but broader.)*
- ⚠️ **New topic surfaced: differential pair + CMRR** (HS 2024 Task 3) — light in the exercises; make sure you can do **half-circuit** diff-pair analysis.
- **2013/2014 (Huang era) — cherry-pick only.** Mostly legacy (op-amp filters, translinear references, switched-capacitor). Worth doing: FS 2013 T1/T4 (BJT amps); **HS 2013** (the "HS 2014"-named file, Jan 2014) T1/T4 = **best current-mirror practice** in the set. Skip the rest.
- ℹ️ None of these old exams has a clean **cascode** problem → rely on **Ex 13 + Masterclass** for cascode. Friend's "old EC exams differ" holds: prioritize problem sets + HS 2024.

## Prioritized drill plan (maps to the W1–W4 schedule)
1. **Curate the 10-page formula sheet** from the Masterclass (pp. 30–34, 42–43, 49–55, 57–64) **first** — everything else references it.
2. **Ex 9 (past-exam MOS) + Ex 7** — the closest-to-exam MOSFET material; do these to fluency.
3. **BJT block Ex 10–12** — CE/CB/CC R_in/R_out/A_v, the other half of the config table.
4. **Ex 13** — cascode/GmRout/mirrors (multi-transistor, high-value).
5. **Ex 5–6, 8** — fill MOSFET fundamentals/swing/design gaps.
6. **Diodes Ex 2–4** — lighter; nail rectifier ripple + the past-exam multi-diode solves.
7. **Razavi (Behzad) videos** — selectively, for BJT small-signal intuition, then MOSFET by difference.
8. **Source + redo both midterms** under time (best predictor) → then timed mixed problems for speed.

## Reference files (confirmed)
- **`ec pvk main doc complete.pdf`** — the Masterclass (formula sheet + worked solutions). Your #1 resource.
- **`Chapter_1_merged.pdf`** — Razavi *Fundamentals of Microelectronics* full slide deck (713 slides) = the textbook theory source (CH5 Bipolar Amplifiers most relevant). Reference only.
- *(`2022 Control-Signals cheat-sheet` is **not** EC — it's a Control/Signals cheat sheet; see SigSys2.)*
