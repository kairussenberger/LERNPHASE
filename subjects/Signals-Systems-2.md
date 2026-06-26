# Signals & Systems II (SigSys2 / Signal- und Systemtheorie II) — Study Hub

**Exam:** **Sat 15.08, 11:00–13:00** · HIL F 61 / F 41 · 227-0046-10S · Prof **F. Dörfler** *(new prof this year)*
**Allowed aids:** 🟡 **one A4 sheet, two-sided, handwritten notes**
**Format:** Written problems
**Starting point:** ~from zero, **but already read the PVK** ✅
**One-line strategy:** *Lock the ~3 core ideas + a tight A4 sheet, then spam old exams (esp. problems 2 & 4) and build raw writing speed.*

> **SigSys2 is examined late (Aug 15) — after EC (Aug 3) and DiskMath (Aug 5).** That gives it a **dedicated Aug 6–14 window**, so it can be lighter in P1 (lock theory + know the exam format) and finish with heavy exam-spam in August.

> **📋 PVK + example sets indexed → see [SigSys2_Playbook.md](SigSys2_Playbook.md).**
> **🎯 Decoded exam (from a peer's exam-tips page):** **4 problems × 25 pts · 120 min.** New prof Dörfler but **exam resembles previous years** (slides/problem sets unchanged). **P1** = model physical system → LTI → stability · **P2** = "most predictable" → **almost always controllability & observability** (⭐ grind this) · **P3** = frequency domain (hardest) · **P4** = nonlinear Lyapunov/LaSalle *(discrete-time lives inside P1)*.
> **Primary doc:** `PVK SigSys II.pdf` (complete theory + worked past-exam problems per chapter).
> ✅ **Old-exam archive found:** `your exams folder/Past Exams[ (Solutions)]/` = full SigSys2 exams **2008–2026 with keys**. Practice newest first (Fall_2026, Spring_2025…). See [playbook](SigSys2_Playbook.md).

---

## TL;DR — what actually moves the needle

1. **There are only ~3 big ideas.** Understand them deeply, then everything else is repetition: **stability**, **controllability/observability**, **time domain vs frequency domain**, **discrete systems** (+ a touch of **nonlinear/Lyapunov**).
2. **Do ONLY old exams** once theory is locked. Skip the problem sets, mostly skip the slides. The exams are repetitive — **problems 2 & 4 are the most repeatable**; other problems can get tricky with odd physics setups.
3. **Speed is a real skill here** — exams are tight on time. Practice writing the standard solutions *fast*; comfort comes from volume.
4. **New prof (Dörfler) caveat:** format may shift slightly, but the friend who had a new prof still says old exams are very similar — **pattern recognition is enough to pass.** Build a tight **A4 sheet** to lean on for the formula-heavy parts.

---

## Expert tips (verbatim synthesis)

**Friend A (text):**
> "Bei SigSys2 habt ihr einen **neuen Prof**, also könnte bisschen anders sein, aber wenn du einfach bestehen willst, würde ich trotzdem **alte Prüfungen spammen.** Sind schon recht ähnlich, und bei SigSys2 gibt's oft Aufgaben die sehr ähnlich sind. Hab's selber nie komplett gecheckt… aber für die Prüfung kann man bisschen mit **pattern recognition** arbeiten."

**Friend B (audio):**
> "Make sure you understand the **main branch of theory** — very big, broad ideas: stability, controllability, time domain, frequency domain, discrete systems. Nothing crazy. As you read through (the PVK, which is already a summary), understand all the **formulas and ideas** — there are only like **three ideas** in the whole course. Then start exams. The **exams are tight on time**, and time is really a skill — some people just write quickly even when unsure, so get quick. The exams are **repetitive, especially problems 2 and 4**; other problems can be trickier with a weird physics scenario. For SigSys2 I'd really say: **learn the core theory, then do only exams.** Don't even think about the problem sets. Don't look at the slides — maybe reference them for a harder problem from ~10 years ago, but it's not worth it. Just do exams and gain comfort over time."

✅ You've **already read the PVK** — that's the theory-lock step largely done. Next is exam volume.

---

## Topic map — the core ideas (Chapters 0–7)

| Big idea | Topics | Lectures |
|----------|--------|----------|
| **Modeling / state-space** | model physical systems (pendulum, RLC, amplifier, population), ODEs + linear algebra (eigenvalues/vectors, SVD), state-space form | L0–L2 |
| **① Stability (time domain)** | continuous LTI stability, zero-input response, e^{At}, eigenvalue criteria | L3 / L3-2 |
| **② Controllability & Observability** | controllability/observability tests, energy, **Kalman decomposition**, min-energy control | L4 / L4-1 / L4-RH |
| **③ Frequency domain** | **Laplace transforms**, transfer functions, **principle of the argument → Nyquist** criterion, **Bode plots**, 2nd-order TFs | L5-1 / L5-2 / L5-3 |
| **Discrete-time systems** | discrete LTI, sampled-data, value/time quantization, Euler-method stability | L6 |
| **Nonlinear (lighter)** | local linearization, **Lyapunov**, **LaSalle's invariance** | L7-1 / L7-2 |

**Exam-structure intel:** problems **2 & 4** are the most repeatable across years → drill those patterns hardest. Problems with bespoke physics scenarios are where time gets eaten.

---

## Document inventory (with priority)

### 🔴 Must-use
- **Old exams** (gather as many years as possible) — *the core activity.* Do under time; focus problems 2 & 4.
- **the PVK (`PVK SigSys II.pdf`)** — already read ✅; your theory backbone + raw material for the A4 sheet.
- **Peer notes (`SS2-exam-notes.pdf` + highlighted backup)** — key concepts, pitfalls, exam tips; second theory source.
- **Your A4 two-sided sheet** (to build) — see below.

### 🟡 Reference (only when a hard problem demands it)
- Annotated lecture slides L0–L7 — dip in for a specific derivation; otherwise skip.
- Example sets **U1–U10** — *the friend says skip problem sets* for exam prep; use at most to clarify a confusing method.

### ⚪ Skip
- Reading slides cover-to-cover; grinding all U1–U10. Low ROI vs old exams.

---

## Build this: the A4 two-sided sheet (allowed aid)

Tight, dense, organized by the core ideas so you can find a formula mid-problem:
- [ ] **Laplace transform** pairs + properties; partial-fraction recipe
- [ ] **Stability** tests (eigenvalues, Routh–Hurwitz); e^{At} via diagonalization/Jordan
- [ ] **Controllability/observability** matrices + rank tests; **Kalman decomposition**; min-energy control formula
- [ ] **Nyquist** procedure (principle of the argument) + **Bode** construction rules; 2nd-order TF parameters (ω_n, ζ)
- [ ] **Discrete-time**: sampling, z-relation, Euler-method stability region
- [ ] **Lyapunov / LaSalle** statements
- [ ] Standard **problem-2 and problem-4 templates** distilled from old exams (step skeletons)

---

## Strategy & sequence

**P1 (lighter — it has the Aug 6–14 window):**
1. **Solidify the 3 core ideas** from the PVK + a peer (mostly done). Make sure every formula/idea is understood, not memorized.
2. **Build the A4 sheet** as you review.
3. **Do a handful of recent old exams** to learn the format and identify the problem-2/4 patterns. Note speed gaps.

**P2 (SF):** light — re-read the A4 sheet, glance at one old exam. Low priority during the trip (exam is Aug 15).

**P3 (Aug 6–14 — its dedicated window, after DiskMath):** **spam old exams under strict time**, twice through the repeatable problem types; finalize the A4 sheet; relentless speed practice → **exam Sat Aug 15**.

## Resources to obtain (checklist)
- [ ] As many **old SigSys2 exams + solutions** as possible (check whether Dörfler released a sample/mock — new prof)
- [ ] Confirm exam covers the same chapter scope under the new prof (Dörfler) — verify against any released info

## Time budget
_Provisional P1: ~55–60 h (lower — theory already started + large dedicated August window). Finalized in the master schedule._
