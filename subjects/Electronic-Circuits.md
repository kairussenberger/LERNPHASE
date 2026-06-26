# Electronic Circuits (EC) — Study Hub

**Exam:** **Mon 03.08, 15:30–17:30** · ONA/HIL (HIL F 75 / G 75 / G 61) · 227-0077-10S · Profs **H. Wang / A. Wang**
**Allowed aids:** 🟢 **5 A4 sheets double-sided = 10 pages of notes (handwritten OR machine-printed) + pocket calculator** (non-communicating)
**Format:** Written problems
**Starting point:** ~from zero
**One-line strategy:** *Build the ultimate 10-page formula compendium, then drill the workflow `DC bias → small-signal → look up formula` until it's reflex.*

> **EC is examined FIRST (Aug 3) — it must peak by then.** It's also the highest-ROI subject to grind. Treat it as a top-2 priority in P1.

> **📋 Exercises + Masterclass indexed → see [EC_Uebungen-und-Playbook.md](EC_Uebungen-und-Playbook.md).**
> **🟢 Big find:** `ec pvk main doc complete.pdf` is a 66-page handwritten **"EC Masterclass"** that already contains the **complete R_in/R_out/A_v tables** (MOSFET stages pp.30–31, MOSFET impedances pp.33–34, BJT impedances pp.42–43, BJT stages pp.49–55, cascode/GmRout/mirrors pp.57–64) **plus worked solutions**. → Your 10-page sheet is mostly **curating those pages** (machine-print allowed). Highest-value MOSFET practice = **Exercise 9 (two past-exam problems)** and **Exercise 7**.
> ⚠️ Exercise PDFs have **no solutions** (Masterclass is the de-facto key). The **two midterms are NOT in your files** — source them (best exam predictor).

---

## TL;DR — what actually moves the needle

1. **You get 10 pages of notes — and machine-printed is allowed.** This is enormous. Your formula sheet basically *is* the course. **Build a typeset compendium** with **R_in, R_out, A_v for every configuration** (CS, CG, CD, CE, CB, CC), cascode, current mirror — plus a worked DC-bias template. The friends are unanimous: *the R_in / R_out / A_v table is the bulk of the material.*
2. **The exam is a speed test.** The grade comes from executing fast: identify circuit → DC analysis to find biasing → draw small-signal equivalent → **find the matching circuit on your sheet and write the formula.** Practice this loop until mechanical.
3. **Problem sets > old exams for EC** (unlike your other subjects). Old EC exams differ significantly from the current course; problem sets are "a lot better this year." **Do every Serie + both midterms** — the exam will most resemble the midterms.
4. **Razavi videos for understanding — selectively.** Watch enough to truly grasp **small-signal BJT**; once that clicks, you can infer MOSFET behavior from the differences instead of watching every video. Don't overdo Razavi.
   - ⚠️ *This is **Behzad Razavi** (UCLA analog-IC lectures on YouTube) — not your TIK professor Kaveh Razavi. Different person.*

---

## Expert tips (verbatim synthesis)

**Friend A (text):**
> "EC ist das einzige Fach vom Block wo ich wirklich viel gelernt habe… razavi Videos für Verständnis, aber sonst auf **Aufgaben** konzentrieren. Die Prüfung wird ähnlich wie die beiden **Midterms** — mach die auf jeden Fall nochmal. Die Serien sind teilweise bisschen lost, aber schau sie an. Am einfachsten Punkte holst du bei Aufgaben wo man erst **DC analysis** macht um rauszufinden wie die Transistoren gebiased sind, dann **small-signal equivalent**, dann reicht meistens **eine Formel aus der Formelsammlung**. Deine Formelsammlung sollte so viele circuits wie möglich haben, dass du zur Not einfach einen findest der gleich/ähnlich aussieht und die Formel aufschreibst."

**Friend B (audio, got a strong grade):**
> "My EC exam was basically a test of going quick. Problem sets are a lot better this year — good, because the old exams are significantly different. Watch **Razavi**, but some people overdo it — understand the **main ideas**. If you can truly say 'I understand small-signal of BJTs,' you don't need all the MOSFET videos; you see the differences and move on. The old Zusammenfassungen did **not** have a sheet with **R_in, R_out, A_v** — and from my understanding of the course, *that was all that mattered.* Make sure your Zusammenfassung has an **R_in / R_out / A_v table for every config** (CS, CG, CD…). **a classmate** had one last year. If not, make it yourself. I did all the derivations myself once — good to learn, but make sure you can **quickly reference R_in, R_out, A_v.**"

---

## Topic map (course arc: linear foundations → single transistors → multi-transistor blocks)

| Block | Topics | Lectures |
|-------|--------|----------|
| Circuit theory review | KVL, KCL, Thévenin, S-domain, **Bode plots** | L1–L2 |
| Diodes | I/V curves, exponential vs constant-voltage-drop models, **rectifiers**, limiters, voltage doublers, AC-DC | L2–L4 |
| MOSFETs | structure, voltage-dependent current source, **regions**, **biasing** (incl. supply-independent), channel-length modulation, NMOS/PMOS | L4–L7 |
| MOSFET amplifiers | **Common-Source, Common-Gate, Common-Drain**, signal swing, active/diode-connected loads | L6–L8 |
| BJTs | structure, collector current, NPN/PNP, large- vs small-signal models | L8–L9 |
| BJT amplifiers | input/output impedance, **biasing**, emitter degeneration, **Common-Emitter / Common-Base / Common-Collector** | L10–L12 |
| Multi-transistor blocks | **Cascode** stages, **current mirrors** (scaling, error analysis), G_m·R_out method | L13 |
| Review | exam structure | L14 |

---

## Document inventory (with priority)

### 🔴 Must-use
- **Exercises 2–13 (Serien)** — *the primary training set.* Do all, understand all.
- **The two midterms** — exam most resembles these; redo them under time.
- **`ec pvk main doc complete.pdf`** — master summary; backbone for building your formula sheet.
- **Razavi (Behzad) YouTube lectures** — selectively, for small-signal intuition (BJT first).
- **Your 10-page Formelsammlung** (to be built — see below). The single biggest asset given the aid rule.

### 🟡 Reference
- Lecture slides L1–L14 — consult for a specific derivation or model you're shaky on.
- **a classmate's** last-year R_in/R_out/A_v sheet — hunt for it as a template (then verify/extend).

### ⚪ Low value
- Old EC *exams* (pre-current-course) — differ significantly; don't over-invest. Use only to rehearse timing once.
- `organization2025…pdf` — admin only.

---

## The Formelsammlung — build this first (highest leverage)

Because **10 machine-printed pages are allowed**, make it comprehensive and *navigable* (you must find the right circuit in seconds under time pressure):

- [ ] **Master table:** for each config (CS, CG, CD, CE, CB, CC) → **R_in, R_out, A_v** (with and without source/emitter degeneration, with channel-length modulation on/off). One row per circuit, with a thumbnail schematic.
- [ ] **Cascode** + **current mirror**: G_m·R_out method, output resistance, mirror error/scaling.
- [ ] **Small-signal model card:** g_m, r_o, r_π definitions; BJT vs MOSFET parameter map.
- [ ] **DC-bias template:** step-by-step "find the operating point" recipe + region conditions (MOSFET triode/saturation, BJT active).
- [ ] **Diode/rectifier** formulas: ripple voltage, half/full-wave, limiters, doublers.
- [ ] **Bode** rules cheat-strip.
- [ ] **Worked example** of the full `DC → small-signal → A_v` loop on one CE and one CS stage, as a pattern to copy in the exam.
- [ ] Index/edge-tabs so any circuit is findable instantly.

---

## Strategy & sequence (P1, finishing right before Aug 3)

1. **Razavi BJT small-signal block** + skim MOSFET differences → get the core intuition (don't binge all videos).
2. **Work Serien 2–13 in order**, building the formula sheet *as you go* — every new circuit/result goes onto the sheet immediately.
3. **Redo both midterms under time.** These predict the exam best.
4. **Speed reps:** repeatedly run the `DC bias → small-signal → look up formula` loop on mixed problems until it's automatic.
5. **Finalize + index the 10-page sheet.** Rehearse *finding* formulas on it, not just having them.

**P2 (SF):** review the formula sheet; mentally walk circuit patterns. **P3:** Jul 30–Aug 2 final timed problem-set/midterm reps → **exam Mon Aug 3**.

## Resources to obtain (checklist)
- [ ] **a classmate's** R_in/R_out/A_v sheet (template)
- [ ] Both **midterm** papers + solutions
- [ ] Confirm calculator is allowed-model & charged

## Time budget
_Provisional P1: ~80 h (top priority — first exam + highest ROI). Finalized in the master schedule._
