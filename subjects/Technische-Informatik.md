# Technische Informatik (TIK) — Study Hub

**Exam:** **Thu 20.08, 09:30–11:30** · ONA E 7 · 227-0013-00S · Profs **K. Razavi / A. Hajiabadi / P. Jattke**
**Allowed aids:** 🔴 **None — no written aids, no calculator.** Pure recall.
**Format:** **Multiple choice** (≈100 MC tasks, ~80 of them drawn from old exams / Übungsstunden)
**Starting point:** ~from zero
**One-line strategy:** *Master every old-exam MC question until automatic; read the kernel book; watch only the hardware/CPU lectures.*

> **TIK is examined LAST (Aug 20)** → it gets a dedicated Aug 16–19 cram window after SigSys2. So in P1 the goal is *coverage* (read the book, watch hardware lectures, first pass of the MC bank); the heavy MC drilling lands in August.
> ⚠️ Your TIK prof is **Kaveh Razavi** (systems security). This is **not** the "Razavi videos" your friends mention for Electronic Circuits — that's **Behzad Razavi** (analog IC). Don't mix them up.

> **📋 Question-types indexed → see [TIK_Playbook.md](TIK_Playbook.md)** — the exact MC templates per topic (pipeline timing, cache-miss counting, forwarding paths, buddy allocator, Sv48 paging math, demand paging, scheduling) with real example questions.
> **⏳ The "MC bank" = the reserved past-exam questions.** Your friend's ~100-MC tip refers to old-exam + Übungsstunde questions — i.e. the same material you're reserving until **end of July**. So before then, study from **`cebook` + hardware lectures + the prof's example decks (03–11)** (teaching examples, safe to use; no keys). From **end of July**, work the real past exams (`FS 2023` + any more you get). 🔒 Don't peek early.
> ℹ️ `ZusammenfassungenDerVorlesungsstunden.pdf` is **mislabeled — it's DiskMath** (Koch), not TIK.

---

## TL;DR — what actually moves the needle

1. **Old-exam MC is ~80% of your grade surface.** Get the full collection of old-exam + Übungsstunde MC questions (~100). Learn the solution to **every single one** and *understand why*. This is the #1 lever.
2. **Two halves of the course:**
   - **Kernel Construction / OS** (`cebook.pdf`): the **book == the lectures**, word-for-word. → **Read the book, skip those lectures** (double-dipping).
   - **CPU Design / Hardware** (RISC-V, pipelining, caching): annoying but concept-chained. → **Watch these lectures**, pausing to see how ideas build on each other.
3. **It's MC** — partial understanding + pattern recognition still scores. But to be genuinely *good* takes a lot of time, so prioritize ruthlessly: old exams first, then book, then hardware lectures.
4. **Grab the two known good resources:** the **PVK video** and **a peer's AMIV document**. Both rated good by the friends.

> Reality check from a friend: scored **5.5 without bonus** having done *nothing* in the semester — i.e. a solid pass is reachable in Lernphase **if** you drill the old questions. Going for a 6 needs "crazy" time.

---

## Expert tips (verbatim synthesis)

**Friend A (text):**
> "TIK war komplett cooked. Es gab so ein Video von nem PVK das fand ich gut und so ein Dokument von einem Kollegen bei AMIV das war auch gut. Das Buch, das der Prof geschrieben hat ist auch nicht schlecht. Gibt leider nur wenig alte Prüfungen. Am Ende ist ja nur MC und hab auch echt viel geraten… um TIK wirklich gut zu sein muss man crazy viel Zeit investieren. Kannst da sonst einen Kollegen fragen, der war ziemlich gut."

**Friend B (audio, got 5.5 w/o bonus):**
> "Es gibt insgesamt 100 MC-Aufgaben, 80 MC-Aufgaben von old exams, Übungsstunden… das ist basically deine ganze Sammlung von old exam questions. **Lern wirklich die Lösungen zu allen diesen Aufgaben und probier sie auch zu verstehen.**"
> "Das Buch **ist** die Vorlesungen → schau nicht alle Vorlesungen an, wenn du auch das Buch liest."
> "Eine große Teil von TIK ist, in das Mindset von den Dozenten zu kommen — viele Concepts bauen aufeinander auf. Für **Hardware Design** lohnt es sich, die Lectures anzuschauen (pausieren, larger connections überlegen). Für **Kernel Construction** sind die Lectures word-to-word das Gleiche wie im Buch → lieber das Buch durchlesen (double dipping)."
> "Probier auch das Code ein bisschen durchzulesen — wichtiger als durchlesen ist **verstehen** (Ideen). Wird nicht direkt geprüft, hilft aber."

**Action:** message **a strong peer** for their TIK question bank / notes (friends rate him highly here).

---

## Topic map

The course is the hardware↔software interface on **RISC-V** with the **"Jake"** educational kernel.

| Half | Block | Topics | Source | Watch lectures? |
|------|-------|--------|--------|-----------------|
| **A. CPU Design / Hardware** | Assembly | RISC-V ISA, register file x0–x31, instruction fields, shifts/bit ops | `RISC_V.pdf` (Computer Organization & Design) + Assembly slides | ✅ yes |
| | Basic CPU | logic gates, truth tables, datapath, control signals per instruction type | `03. Basic CPU design` | ✅ yes |
| | Pipelining | 5 stages IF/ID/EX/MEM/WB, hazards, forwarding, timing diagrams | `06. Pipeline design` | ✅ yes |
| | Parallel execution | branch prediction, out-of-order, reservation stations, cycle counts | `05. Parallel instruction execution` | ✅ yes |
| | Caching | cache hierarchy, locality, hit/miss rate, direct-mapped vs associative | `11. CPU caching / Caching` | ✅ yes |
| **B. Kernel Construction / OS** | Physical memory | DRAM, heaps, **buddy allocator** (free lists, struct block, magic values) | `cebook.pdf` + Buddy slides | ❌ read book |
| | Virtual memory / paging | MMU bootstrap, multi-level page tables (RISC-V), relocation regs | `07/08. Virtual memory`, `Paging` | ❌ read book |
| | Demand paging | soft page faults, demand paging logic, page sharing, VMAs, huge pages, swapping | `08. Demand paging` | ❌ read book |
| | User mode | privilege levels, exception handling, syscalls, sandboxing | `09. User mode` | ❌ read book |
| | Multiprocessing | ELF format, fork/exec, context switching, **CPU scheduling** | `10. Multiprocessing` | ❌ read book |

---

## Document inventory (with priority)

### 🔴 Must-use
- **Old-exam + Übungsstunde MC question collection** (~100) — *the single most important asset.* (Pull from AMIV / a peer / course Moodle.)
- **`cebook.pdf`** — "Kernel Construction on Modern Systems" → the textbook for **Half B**. Read it instead of the kernel lectures.
- **`(TECHINF)__RISC_V.pdf`** — "Computer Organization and Design" excerpts → reference for **Half A** (RISC-V, pipelining, memory hierarchy).
- **Hardware/CPU lecture slides** (`03 Basic CPU`, `05 Parallel`, `06 Pipeline`, `11 Caching`, `01/02 Assembly` Moodle) → watch + pause.
- **PVK video** + **a peer's AMIV document** — both flagged as good.

### 🟡 Reference (read for understanding, not memorization)
- Buddy slides/exercises, Virtual memory slides, Demand paging questions, User-mode, Multiprocessing slides — covered by `cebook.pdf`; use slides to clarify a confusing point.
- Practical assignment PDFs (Assembly, Paging, Multiprocessing) — skim the *ideas*; reading kernel code helps understanding (per Friend B) but isn't directly tested.

### ⚪ Low value / skip
- Kernel-half lecture videos (word-for-word the book — double-dip).
- `571dd164…_EC_LERNPLAN.pdf` — appears mislabeled (says "EC" but sits in the TIK set). Open once to check what it actually is; likely ignore.

---

## Strategy & sequence (P1)

1. **Build the question bank first.** Collect all old exams + Übungsstunde MCs into one place. This defines the target.
2. **First pass — Half B (Kernel) via `cebook.pdf`.** Read a chapter → immediately do the matching old-exam MCs → mark wrong ones. The book and exam are close.
3. **First pass — Half A (Hardware) via lectures + `RISC_V.pdf`.** Watch a topic's lecture, pause to map dependencies → do the matching MCs. Pipelining/caching/parallel-execution questions are very pattern-based.
4. **Second pass — pure MC drilling.** Cycle through the full ~100 questions repeatedly. For each: answer cold, then check, then write a one-line "why" for the wrong ones. Convert recurring mistakes into flashcards.
5. **Understand, don't just memorize answers** — exams reshuffle numbers/wording. Knowing *why* the answer is right beats memorizing the letter.

**P2 (SF):** flashcards of the MC patterns + tricky kernel facts on phone.
**P3 (cram):** full timed run through all ~100 MCs, twice; re-watch any hardware topic still shaky.

---

## Resources to obtain (checklist)
- [ ] Full old-exam + Übungsstunde **MC question bank** (~100 Q)
- [ ] **PVK video** (the one the friend liked)
- [ ] **a peer's AMIV TIK document**
- [ ] Ask **a strong peer** for their notes/questions
- [ ] Confirm `cebook.pdf` is the current edition

## Time budget
_Provisional P1: ~70 h. Final allocation set once exam order is known (see README)._
