# DiskMath — Serien Index + Exam Playbook

Built from reading **all 13 Serien** (`Serie 1–13.pdf`) and **all 3 past exams** (`your exams folder/Prüfung SS25, WS25, WS26.pdf`). This is your "what to actually drill" map. Companion to [Diskrete-Mathematik.md](Diskrete-Mathematik.md).

> ⚠️ **Solutions gap:** neither the Serien PDFs nor the exam PDFs contain solutions. Your friend's #1 tip was *"understand all the solutions."* → **Get Lösung 1–13 + exam solutions from Moodle.** In the meantime `DM_PVKLösungen.pdf` (+ `DM_PVKSkript.pdf`) is a worked PVK set, and `Ergänzendes Skript … (Flüsse und Schnitte).pdf` covers the flow material.

---

## Part 1 — The 3 real exams (your single best predictor)

**All three exams have an identical skeleton** → you essentially know the exam template already.

### Format (SS25 = 14.08.25, WS25 = 22.01.25, WS26 = 11.02.26)
- **4 problems × 10 points = 40 points · 120 minutes** (~3 min/point).
- **Aids: blue/black pen only.** No pencil/red/green, no devices, **no formula sheet** (matches catalog "Keine"). Lecture results may be used without proof unless asked to prove them. You write directly on the exam.

### Position → topic map (rock-stable across all 3 exams)
| Problem | Block | What it is | Sub-parts |
|---------|-------|-----------|-----------|
| **P1** (10 pts) | All blocks | **10× single-answer MC, 1 pt each, no justification** | mix of A/B/C |
| **P2** (10 pts) | A — Combinatorics | counting | (a) incl-excl / logic deduction · (b) Hasse diagram or pigeonhole · (c) one harder derivation (recursion/multiset) |
| **P3** (10 pts) | B — Graph theory | graphs | (a) structural/proof item (rotates) · **(b) ALWAYS max-flow** |
| **P4** (10 pts) | C — Number theory & Algebra | | **(a) ALWAYS Euclidean gcd** · (b) congruence/RSA/CRC (rotates) · (c) group/symmetry (rotates) |

### 🎯 Guaranteed / high-probability points — drill these FIRST
1. **P4a — Euclidean algorithm gcd**, *every exam*, always `gcd(currentYear, someNumber)` (gcd(2025,1408), gcd(2025,2201), gcd(2026,1102)). ~1–1.5 free pts. → master **extended Euclid** (Bézout coefficients) cold.
2. **P1 MC — the "Rangliste" counting question**, *every exam, same 4 options*: `nᵏ` / `n^(k̲)` (falling factorial) / `C(n,k)` / `C(n+k−1,k)`. → memorize the **4 elementary counting forms** (ordered/unordered × with/without repetition). Guaranteed point.
3. **P1 MC — divisibility-counting** "how many numbers from X to Y divisible by …?", *every exam* → inclusion–exclusion. Guaranteed point.
4. **P1 MC — flow/cut property statement**, *every exam* → know max-flow=min-cut facts.
5. **P3b — max-flow** (residual graph, augmenting path, f_max, min-cut), *every exam* → the **single most reliable big-point graph task**. Drill full Ford–Fulkerson mechanics + the twist ("increase one capacity for most gain" / "redo on the undirected version").
6. **P2 combinatorics**: inclusion–exclusion + pigeonhole + one harder derivation (Fibonacci-type recursion, or multiset/stars-and-bars classes).
7. **P4c — group/symmetry** (5–6 pts, highest-value final): **dihedral group order 2n**, **tetrahedron isometries (12 rotations / 24 with reflections)**, or a **group-axiom proof** (e.g. Fano-plane-style point set). Prepare the whole sub-block.
8. **P4b — rotates**: solve linear congruence `ax≡b (mod n)` / **RSA** encrypt–decrypt / **CRC** polynomial division over GF(2). Prepare all three.
9. **P3a — rotates**: Euler's formula argument / spanning-tree counting / degree-sequence construction. Prepare the whole graph block.

### Time strategy (friends: "it's a speed test")
Bank the easy points fast — **P4a gcd, the ranking MC, the divisibility MC** — then spend the bulk on **P3b max-flow** (figures take time) and the **5–6 pt proof in P2c / P4c**. CRC/congruence arithmetic (P4b) is error-prone → slow down there.

### Per-exam quick reference
| | P1 (MC) | P2 (Combi) | P3 (Graph) | P4 (NT/Algebra) |
|---|---|---|---|---|
| **SS25** | 10 MC (incl-excl, ranking, flow, lcm, (ℤ₁₅,+) subgroups…) | voting-order deduction · Hasse(140) · ≥3-color count | soccer-ball Euler formula · **max-flow** + best edge increase | gcd(2025,1408) · **RSA** decrypt → name · **tetrahedron** isometries |
| **WS25** | 10 MC (∈-relation, cycles permutation, Euler vs Hamilton, inv mod m, #finite-field orders…) | incl-excl enrollment · max overlap · **Fibonacci recursion** | spanning-tree count of K₄-type · **max-flow** + min-cut | gcd(2025,2201) · solve 15x≡10 (mod 25) · **group-axiom proof** (7-point structure) |
| **WS26** | 10 MC (subsets ≤4, binomial in (x+2y²)⁶, LCG period, graph-iso invariants…) | no-prime-digit codes · pigeonhole sum-to-11 · **anagram/multiset classes** | degree-sequence construction · **max-flow** + undirected redo | gcd(2026,1102) · **CRC** g(x)=x⁵+x⁴+x²+1 · **dihedral** groups, cyclic? |

---

## Part 2 — Serien 1–13 index (what each sheet trains)

### Block A — Combinatorics / Sets (Serien 1–4)
- **Serie 1 — Sets, power sets, intro proofs.** Mutilated chessboard (parity/coloring); 6-people monochromatic triangle (Ramsey R(3,3)=6, pigeonhole); set laws (absorption, distributivity, De Morgan, duality); |P(M)|=2^m via bitstrings.
- **Serie 2 — Relations, orders, identities.** Equivalence relation → construction of ℚ; Hasse diagrams (P({1..4})⊆, divisors of 210); C(2n,2)=2C(n,2)+n², **Vandermonde** C(2n,n)=ΣC(n,k)²; Boy/Girl conditional-probability paradox.
- **Serie 3 — Counting principles.** Binary strings with substring "01" k times; numbers 1–300 divisible by 4/6/15 (**incl-excl**); handshake lemma + parity + pigeonhole; prove Σk·C(n,k)=n·2^(n−1) by **double counting**.
- **Serie 4 — Binomial theorem & probabilities.** ΣC(n,k)=2ⁿ, Σ(−1)ᵏC(n,k)=0; Jass card hypergeometric counting; subset-of-subset identity ΣC(n,k)C(n−k,m−k)=2ᵐC(n,m); **hat-guessing puzzle** via Hamming/covering codes.

### Block B — Graph theory (Serien 5–8)
- **Serie 5 — Connectivity, cycles, trees.** Min/max edges for cycle/connectivity; tree with given degrees exists ⇔ **degree sum = 2n−2**; tree with a deg-k vertex has ≥k leaves; bridge-crossing puzzle.
- **Serie 6 — Spanning trees, Euler & Hamilton.** Spanning trees of Kₙ minus an edge (**Cayley**, symmetry); open Euler-trail condition (exactly 2 odd vertices); construct Euler tour; count Hamilton cycles / k-cycles in Kₙ.
- **Serie 7 — Planar graphs, coloring, flows.** Five **Platonic solids** as planar graphs + prove only five exist; triangle-free planar ⇒ vertex deg ≤ 3 (Euler bound); exam-scheduling via **graph coloring**; **Ford–Fulkerson** run (residual graph, augmenting path, γ each step).
- **Serie 8 — Max-flow / min-cut & matching.** Verify a flow is maximal; find min cut; **model assignment problems as bipartite flow** (football positions; workers with capacity 2 jobs); max-flow = min-cut certification.

### Block C — Number theory & Algebra (Serien 9–13)
- **Serie 9 — Divisibility, modular arithmetic, Euclid.** Divisibility-relation proofs; remainder rules for sum/product; divisibility tests 2/3/11 (via 10≡−1 mod 11); consecutive Fibonacci coprime; **extended Euclid** gcd(226,124) as linear combination + lcm.
- **Serie 10 — Congruences, CRT, pseudo-random.** Full-moon period (lcm); **LCG** full-period conditions; modular inverses 57⁻¹, 34⁻¹ mod 128 (34 even → non-invertible **trap**); **CRT** systems + full solution sets.
- **Serie 11 — RSA & group axioms.** RSA p=11,q=13: validate key, find private key, encrypt/decrypt; decide if (ℤ,+),(ℤ,−),(ℤₙ∖{0},·),GL₂(ℝ) are **groups** (axiom checks); Achilles–tortoise geometric series.
- **Serie 12 — Small groups, subgroups, homomorphisms.** Classify groups of order ≤4 (all abelian); subgroups of S₃ and the square's symmetry group; self-inverse elements ⇒ |G| even (**pairing argument**); test homomorphisms + kernel/image.
- **Serie 13 — Fields, CRC & Reed–Solomon.** Prove (ℂ,+,·) is a **field**; **CRC** with g(x)=x⁵+x²+1 (check digits, polynomial division); **Reed–Solomon over 𝔽₄** (α²=α+1 tables, encode/decode); **Nim** winning strategy (XOR nim-sum).

---

## Part 3 — Prioritized drill plan (maps to the W1–W4 schedule)

1. **First, lock the guaranteed points** (P4a gcd, ranking MC, divisibility MC, flow facts) — fast, high-certainty.
2. **Block C (biggest + memorization-heavy, no aids):** Serien 9–13 → extended Euclid, congruences/CRT, RSA, groups/dihedral/symmetry, CRC/fields. Flashcards daily.
3. **Block B graph + the always-present P3b max-flow:** Serien 5–8 → Ford–Fulkerson mechanics until automatic; structural proofs (Euler formula, trees, degree sequences).
4. **Block A combinatorics:** Serien 1–4 → incl-excl, pigeonhole, the 4 counting forms, recursion/multiset derivations.
5. **Then the 3 exams under strict 120-min timing**, twice. After each, redo every missed item from blank and add it to Anki.
