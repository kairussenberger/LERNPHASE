# Technische Informatik — Question-Type Index + Playbook

Built from reading the professor's **example-question decks** (`03 Basic CPU`, `05 Parallel`, `06 Pipeline`, `11 Caching`, `04 Buddy`, `07 Paging`, `08 Demand paging`, `09 User mode`, `10 Multiprocessing`) + the **`(TECHINF)__RISC_V.pdf`** textbook. Companion to [Technische-Informatik.md](Technische-Informatik.md). Exam: **Thu 20.08, 09:30** · no aids · multiple choice.

> ## ⏳ The "MC bank" = the reserved past-exam questions
> Your friend's tip: *"~100 MC questions, ~80 recycled from **past exams + Übungsstunden** — learn them all."* So the "bank" **is** old TIK exam questions — i.e. **the same material you're reserving until end of July** (overfitting risk). There's nothing separate to hunt down.
> - **Before end of July** → study TIK from **`cebook`** (kernel) + the **hardware lectures** + the prof's **example-question decks** (03–11 below). These decks are *teaching examples, not past-exam papers*, so they're safe to use early for concept practice (no answer keys — self-check vs the P&H textbook).
> - **From end of July** → it's fair game to work the real **past-exam + Übungsstunde MC questions** (`Technische Informatik FS 2023.pdf` + any more old TIK papers you can get). That's your "bank."
>
> ℹ️ **Mislabeled file:** `ZusammenfassungenDerVorlesungsstunden.pdf` is **NOT TIK** — it's **Diskrete Mathematik** (Koch) lecture summaries.

---

## Two halves, two methods (friend's tip, confirmed)
- **Hardware / CPU design** (RISC-V, datapath, pipelining, caching) → **watch the lectures**, pause to see how concepts chain. Computational, drillable.
- **Kernel construction / OS** (`cebook.pdf` + jake kernel on RISC-V Sv48) → **read the book** (lectures are word-for-word the book). Mechanism/concept recall.
- Exam is **MC, no calculator** → it's recall + quick mental computation + pattern recognition.

---

## Hardware half — the must-drill computational skills
*(Every one is directly modeled by an example deck — these are the question templates.)*

| Skill | Question template (real examples) | Master |
|-------|-----------------------------------|--------|
| **Single-cycle control signals** | "Which signals =1 for a `lw`?" (MemRead, MemToReg, ALUSrc, RegWrite); "modify datapath to skip every 2nd instruction" (PC+4→+8); what each mux/ImmGen does | per-instruction-class signal table (R/lw/sw/beq/jal/jalr) |
| **Pipeline timing** | "200 MHz, ImmGen now 10 ns critical path — how long does `addi` take?" (→ 5×10=50 ns) | cycle = slowest stage; latency = stages×cycle; CPI; rebalancing |
| **Data hazards / stalls** | "Max bubbles inserted successively?" (write-first/read-second-half reg file → 2); count cycles of a snippet with/without forwarding | bubbles for RAW; **load-use = 1 stall even with forwarding**; total = #instr + (stages−1) + stalls |
| **Forwarding paths** | "Which forwarding path is NOT used in this snippet?" (EX/MEM→EX, MEM/WB→EX, MEM/WB→MEM store-data); what extra metadata pipeline regs need | the 4 forwarding paths + forwarding-unit compare logic |
| **Hazard classification** | "When is flushing useful?" (control hazards + exceptions); largest pipeline register (ID/EX) | control/data/structural + remedies |
| **Branch prediction / OOO** | concept MC: misprediction flush penalty; reservation stations, register renaming, superscalar | P&H Ch 4.8/4.10 concepts |
| **Cache mapping & misses** | address split tag/index/offset; "offset bits in high position — viable?" (loses spatial locality); **count misses in a loop** (include instruction fetches!) | #sets=size/(line×ways); compulsory/capacity/conflict; AMAT=hit+miss_rate×penalty |
| **Cache policy/geometry** | write-back vs write-through (stores-to-same-line benefit write-back); wayness → slower hit; line size → spatial locality | trade-offs |
| **RISC-V encoding** | encode/decode R/I/S/B/U/J formats; register ABI names | Green Card |

## Kernel half — the must-know mechanisms (jake on Sv48)

| Topic | Question template (real examples) | Master |
|-------|-----------------------------------|--------|
| **Buddy allocator** | purpose of `buddy_blocks` vs `buddy_free_lists`; naive free-list "99 problems, which is NOT one"; find buddy via bit-flip; handle a broken-MiB gap | orders/powers-of-two, split/coalesce, buddy=flip one bit, fragmentation, why it beats naive |
| **Paging / Sv48** | segmentation drawbacks; `satp` turns MMU on (physical→virtual); "max page-table pages in the tree?" (1+512+512²+512³) | 4 levels, 9 bits/level=512 entries, 8-byte PTEs, 4 KiB pages, valid/perm/PPN bits |
| **Demand paging** | VMA-only (jake) vs pre-built invalid PTEs; **max memory allocated on a soft (huge-page) fault** = (3+512)·4 KiB; `pt_jump_to_high` SP/PC-relative pitfalls; page sharing (different VAs ok, per-map perms, ≥2 apps) | soft vs hard faults, fault-handler page-table walk, huge pages, swapping |
| **User mode** | how kernel is mapped (shared physical kernel, entered via syscall); user VA space < 2⁴⁸; min PTEs before user mode | privilege levels, user/supervisor perm bits, syscall transition |
| **Multiprocessing/scheduling** | round-robin: which workload suffers least (CPU-bound π); cooperative vs preemptive energy while blocked on IO; why `satp` unchanged on trap (kernel mapped in every space) | ELF, fork/exec, context-switch cost, timer interrupts, yield |

---

## Prioritized drill plan (TIK is examined LAST — Aug 20)
1. **Read `cebook.pdf` (kernel half)** in P1 → after each topic, do the matching example deck (04/07/08/09/10) and mark uncertainties.
2. **Watch the hardware lectures** (basic CPU, pipeline, parallel exec, caching) → do decks 03/05/06/11; **drill the computational templates** above (pipeline timing, cache miss counting, forwarding) until automatic.
3. **From end of July** → start the **real past-exam questions** (FS 2023 + any more old TIK papers): run under time, write a one-line "why" for every wrong answer, convert misses to flashcards. Keep going through to Aug 20. *(Reserved until then — don't peek early.)*
4. **PVK video** for any topic still shaky.

## Reference files (confirmed)
- **`cebook.pdf`** — "Kernel Construction on Modern Systems" = kernel-half textbook (read instead of those lectures).
- **`(TECHINF)__RISC_V.pdf`** — Patterson & Hennessy full textbook (reference; Ch 2 encoding, Ch 4 processor/pipeline, Ch 5 memory/cache, Appendix A logic, Green Card). Not an MC bank.
- Example decks 03/04/05/06/07/08/09/10/11 — style-matched practice MC (no keys).
