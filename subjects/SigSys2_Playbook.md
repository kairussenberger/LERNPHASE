# Signals & Systems II — PVK Map + Example-Set Index + Playbook

Built from reading **`PVK SigSys II.pdf`**, **`SS2-exam-notes.pdf`**, and example sets **U1–U10**. Companion to [Signals-Systems-2.md](Signals-Systems-2.md). Exam: **Sat 15.08, 11:00** · one A4 two-sided handwritten sheet · Prof Dörfler.

> ## ✅ Old-exam archive found (2008–2026, WITH solutions)
> `your exams folder/Past Exams/` + `Past Exams (Solutions)/` = the **full SigSys2 exam archive** (Spring/Fall 2008–2026, confirmed = Signal & System Theory II). This *is* the strategy now — old-exam spam with keys.
> **Practice priority (current format, verified):** **Fall_2026 → Spring_2025 → Fall_2025 → Spring_2024**, then the rest. *(On-disk filenames are shifted vs the actual sitting date, but all are 4×25 same-format.)* The 2008–2015 papers are bonus volume — check topic overlap first.

> ## 🎯 Decoded exam structure (a peer's tips, **confirmed across the real 2023–2026 exams**)
> - New prof **Dörfler**, but the exam **resembles previous years** (slides + problem sets unchanged). **Old exams remain valid.**
> - **4 problems × 25 pts = 100 pts** (~120 min — verify the official time/aids; the reference-copy PDFs don't state them). Rock-solid layout (6/6 recent exams):
> - **P1 — MODELING** ⭐ physical system → state-space LTI → equilibria → stability. *(Often + a **discretization** sub-part: forward/backward Euler + discrete stability — this is where discrete-time lives, NOT P4.)*
> - **P2 — CONTROLLABILITY / OBSERVABILITY** ⭐⭐ the single most predictable slot: parametric LTI (for which param is it ctrb/obsv/stabilizable?), recover x(0) from y(0),ẏ(0), observer gain L, **+ a short proof** (Gramian-singular ⇒ rank P<n, or PBH) in the newest exams.
> - **P3 — FREQUENCY DOMAIN** derive G(s), Bode sketch, **Nyquist + stable-gain range**, gain/phase margin, FVT tracking error, time-delay margin.
> - **P4 — NONLINEAR** equilibria → linearize (often inconclusive) → **Lyapunov → LaSalle** (largest invariant set) → domain of attraction; + phase-portrait / α-matching tail.

> ## Your two primary docs
> - **`PVK SigSys II.pdf`** (Inés Lezamiz Oleaga, 83 pp.) — a complete, exam-aligned theory source, 7 chapters mirroring the syllabus, **each chapter ends with worked past-exam problems.** Use it as your single theory + worked-solution source. *(You've already read it once — now mine the worked problems.)*
> - **`SS2-exam-notes.pdf`** — intuition, pitfalls, and the exam-tips page above. Heavy highlighter overlay but headers/formulas/tips legible.
> - *(`2022 Control-Signals cheat-sheet` — a dense 2-page Control/Signals cheat sheet; a good **style template** for your own A4 sheet.)*

---

## The ~3 core ideas (everything reduces to these)
1. **Stability** — eigenvalues: continuous Re λ<0 (asymp); discrete |λ|<1. + Hurwitz, Lyapunov.
2. **Controllability & Observability** — rank tests (P, Q), PBH, Gramians, min-energy, observer design. *(= Problem 2.)*
3. **Time domain ↔ Frequency domain** — e^{At} / transfer function G(s)=C(sI−A)⁻¹B+D / Nyquist / Bode; plus the **discrete-time** mirror (z-transform, ZOH, Euler).

---

## Chapter map (PVK) — what to lock
- **Ch 1 Modeling** — the 5-step recipe (inputs/outputs/states/ẋ/y); electrical (L,C) & mechanical (spring/damper) element→state; → A,B,C,D. *(Problem 1.)*
- **Ch 2 Linear algebra/ODE** — eigen, diagonalizability, Cayley-Hamilton, nilpotent; Lipschitz ⇒ existence/uniqueness (LTI always has unique solution).
- **Ch 3 Time-domain LTI** ⭐ — x(t)=Φx₀+∫Φ(t−τ)Bu dτ; **3 ways to get e^{At}** (diagonalize / nilpotent finite sum / D+N); stability (diag vs non-diag), **Hurwitz** (deg-2 same sign; deg-3 α,β,γ>0 & αβ>γ), Lyapunov AᵀQ+QA=−R.
- **Ch 4 Controllability/Observability/Energy** ⭐⭐ *(= Problem 2)* — P & Q rank tests, PBH, stabilizable/detectable (unstable λ only), min-energy u_m, observer ė=(A−LC)e.
- **Ch 5 Frequency domain** ⭐ *(= Problem 3, hardest)* — Laplace + G(s); internal vs BIBO stability (equal iff no pole-zero cancellation); **Nyquist N=Z−P**; **Bode** margins (GM/PM) + building-block table; 2nd-order resonance.
- **Ch 6 Discrete-time** *(= Problem 4)* — A_d=e^{AT}, B_d=∫…; **stability uses |λ|<1**; deadbeat (all λ=0); z-transform G(z); **forward Euler** stable ⟺ |1+λδ|<1.
- **Ch 7 Nonlinear** *(= Problem 4)* — equilibria f(x̂)=0; **Lyapunov indirect** (Jacobian eigenvalues; inconclusive if imaginary/zero) & **direct** (V>0, V̇≤0; +radially unbounded ⇒ global); **LaSalle** (largest invariant set in {V̇=0}).

---

## Example-set index (U1–U10) — *problem sets, no solutions; a recurring "Cart-Pole" thread runs through all of them*
| Set | Core idea | Focus |
|-----|-----------|-------|
| **U1** | Modeling | quarter-car, RLC, two-tank → state-space; MATLAB intro |
| **U2** | Linear algebra/ODE | det/eigen proofs, Cayley-Hamilton, nilpotent, Lipschitz/uniqueness |
| **U3** | Time domain + **stability** | interconnections, change of basis, e^{At} cases, feedback eigenvalue placement |
| **U4** | **Controllability/Observability** ⭐ | "a bit of everything" (FS22 final), observer design, min-energy ("pirate ship") |
| **U5** | Controllability (cont.) | reachability/min-energy *(if the file opens — one reader couldn't load it)* |
| **U6** | **Frequency domain** | Laplace→G(s), Nyquist, FVT steady-state error |
| **U7** | **Bode** | Bode plots, margins, loop shaping, 10/(1+s)^k cases |
| **U8** | **Discrete-time** | ZOH discretization, controllability/observability invariance, forward Euler |
| **U9** | Recap ⭐ | **3 past MIDTERM problems** (2015/2021/2024) — your only exam-grade practice here |
| **U10** | **Nonlinear** | limit cycles, Lyapunov + LaSalle, PLL |

---

## A4 sheet — build from [the asset](../assets/SigSys2_A4_sheet.md)
It already encodes the high-value formulas. Make sure it has: the **3 ways to compute e^{At}**, the **stability table** (diag/non-diag × continuous |Reλ| / discrete |λ|), **Hurwitz** deg-2/3, **P/Q/PBH** tests + **min-energy** formula, **Laplace pairs** + **Nyquist N=Z−P** + **Bode building-block table** + margins, **ZOH/Euler** discretization + |1+λδ|<1, **Lyapunov/LaSalle** statements.

## Prioritized drill plan
1. **Lock the 3 core ideas** from PVK (mostly done) + finalize the A4 sheet.
2. **Problem 2 = controllability/observability** — drill U4 (+U5) and PVK Ch 4 worked problems until automatic. Highest, most predictable yield.
3. **Mine PVK's worked past-exam problems** chapter by chapter (it's your only solved-exam source until you get real exams).
4. **Spam the old-exam archive** (you have it, with keys) under strict timing — newest first (**Fall_2026, Spring_2025, Fall_2025, Spring_2024**). Drill the recurring **P2** (ctrb/obsv + the new "prove equivalent conditions" mini-proof) and **P4** (Lyapunov/LaSalle) archetypes. Build speed.
5. Use **U9's midterm problems** + the solution keys to self-check.
