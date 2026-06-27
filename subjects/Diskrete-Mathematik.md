# Diskrete Mathematik (DiskMath) — Study Hub

**Exam:** **Wed 05.08, 16:00–18:00** · HIL G 75 / G 61 · 227-0033-01S · Prof **U. Koch**
**Allowed aids:** 🔴 **KEINE — none.** Blue/black pen only; no formula sheet, no calculator, no devices. **Everything from memory.**
**Format:** **120 min · written · 🔴 keine Hilfsmittel.** Official content split = **four equal 25% blocks**: MC/Kurzfragen · Mengenlehre & Kombinatorik · Graphentheorie · Algebra (elem. Zahlentheorie + Gruppen/Körper/Ringe). Past exams realize this as **4 problems × 10 pts = 40 pts** (one block each, ~3 min/pt); lecture results usable without proof unless asked.
**Textbook:** Boschini, Hansen, Wolf — *Discrete Mathematics*, vdf 2022, ISBN 978-3-7281-4110-1 (= your `4110…OA.pdf`). Prereq: Analysis 1.
**Starting point:** ~from zero
**One-line strategy:** *Memorize the number-theory/algebra machinery cold (flashcards), and grind every Serie + all 3 Koch exams until the patterns are reflex.*

> **✅ Official exam info (course exam-prep slide).** Written · **120 min** · **keine Hilfsmittel**. Content = **four equal 25% blocks**: ① MC / Kurzfragen · ② Mengenlehre & Kombinatorik · ③ Graphentheorie · ④ Algebra (elementary number theory + Gruppen/Körper/Ringe) — exactly the decoded **P1–P4** skeleton below, each worth a quarter. **Resources on Moodle:** book + Skripte + Folien · the **Serien** · the **Quizze** · the **Vorlesungszusammenfassungen** (lecture summaries) · old exams (**reguläre SS25 + Repetitions-WS25**). You already hold SS25/WS25/WS26 + keys.

> **📋 Exam pattern decoded.** All 3 past exams (SS25/WS25/WS26) share an **identical skeleton** → see the full breakdown + Serien index + guaranteed-points drill list in **[DiskMath_Serien-und-Pruefungen.md](DiskMath_Serien-und-Pruefungen.md)**.
> **Skeleton:** P1 = 10× MC (all blocks) · P2 = combinatorics · P3 = graph (**3b is ALWAYS max-flow**) · P4 = number theory/algebra (**4a is ALWAYS Euclidean gcd of `(year, n)`**).
> **Always-present free-ish points:** P4a gcd · the "Rangliste" 4-counting-forms MC · the divisibility-counting MC · flow/cut facts. Lock these first.

> **No aids changes the game.** Unlike EC/SigSys2, you can't lean on a sheet — every identity, property, and algorithm must be in your head. Start the flashcards **early** and keep them warm through the SF trip. Exam is **Aug 5**, only 2 days after EC.

> **Official Koch learning objectives:** use set theory + its axioms as a foundation · apply elementary counting forms/principles · explain graph types & properties · solve classical graph problems · use elementary number theory for information-tech applications · describe algebraic structures & use them for **error-correction**. Topics: Mengenlehre · Kombinatorik · Graphentheorie (incl. **Matchings**, Flüsse & Schnitte) · Algebra (Zahlentheorie, **Kryptographie**, Gruppen/Ringe/Körper).

---

## TL;DR — what actually moves the needle

1. **It's memorization-heavy and there are no aids.** Build **flashcards** for every identity/property/algorithm, especially **number theory & algebra** (the friend: number theory has *~5× more to know by heart* than the other topics).
2. **Do ALL 13 Übungen *and understand all 13 Lösungen.*** The exam is "recht ähnlich zu den Serien und zur alten Prüfung von Ueli Koch." Free points hide in the professor's obscure late-semester topics (e.g. week-13/14 algebra) — only reading the solutions surfaces them.
3. **Do both old Koch exams (SS25, WS25) under time.** Same examiner → same style. This is your best predictor.
4. **Three topic blocks behave very differently** — study each on its own terms (below).

---

## Expert tips (verbatim synthesis)

**Friend A (text):**
> "DiskMath musst du Zeug **auswendig lernen**. Fand die Prüfung echt nicht einfach, hab aber auch nicht viel gelernt — hab DiskMath bisschen für die anderen Prüfungen geopfert. Prüfung war aber **recht ähnlich zur alten von Ueli Koch und zu den Serien** — also schau dir die auf jeden Fall an."

**Friend B (audio, 5.75 w/o bonus in DiskMath, 6.0 in two others):**
> "I took a small notebook and went through all the slides, keeping notes — more for **active recall** than for consulting. Three topics that vary in tricks:"
> **Combinatorics** — "ideas are simple, but they very easily build **confusing scenarios**. Some old-exam combinatorics problems were really tricky." Practice the weird setups.
> **Graph theory** — "almost common sense: coloring, planar graphs, types of graphs, walks. Learn the rules and hope for the best." (Their exam had an unpredictable planar-graph proof — accept that one curveball is possible.)
> **Number theory + algebra** — "the opposite of graph theory: a **bunch of things to know by heart** — many identities, many proofs. But very achievable *if you know everything.* Know the properties of the modular operator / congruences; the **Euclidean (remainder) method** for GCD; **RSA = two formulas to memorize.** Plus Lagrange, subgroups, the divisor stuff, abstract algebra — number theory has ~5× the content of the other two."
> **Biggest regret / best tip:** "**Do all the problem sets and try to understand all the solutions.** There can be free points you'd miss just because you didn't look at the professor's weird week-14 topic. At least read through all the problem sets."
> Recommends **flashcards** + a short **executive cheat sheet** of the most important formulas (to memorize, since no aids in the exam).

---

## Topic map — three blocks, three mindsets

| Block | Topics | Lectures | How to attack it |
|-------|--------|----------|------------------|
| **1. Combinatorics / Counting** | sets, relations (equivalence/order), functions, 4 elementary counting forms, **pigeonhole, inclusion–exclusion**, binomial coefficients, **Stirling numbers** | V1–V4 | *Pattern + care.* Ideas simple; danger is tricky/confusing word-problems. Drill many varied old-exam counting problems. |
| **2. Graph theory + flows** | trees, **Euler/Hamilton**, **planar graphs** (Euler's formula, **Kuratowski**), **coloring**, walks, **network flows & cuts** (Ford–Fulkerson), **matchings/assignment** (bipartite flow) | V4–V8 + Ergänzendes Skript (Flüsse) | *Learn the rules + drill Ford–Fulkerson to reflex* — **exam P3b is always max-flow** (residual graph, augmenting path, min-cut). Accept one possible hard structural proof in P3a. |
| **3. Number theory + Algebra** | divisibility, primes, **Euclidean algorithm/GCD**, **linear congruences (CRT)**, **RSA**, **groups/homomorphisms/cyclic**, **subgroups/rings/fields**, polynomials, **Lagrange**, error-correcting codes (CRC, Reed–Solomon) | V9–V13 | *Memorize cold (no aids!).* Biggest block by content. Flashcard every property/identity/algorithm. RSA = 2 formulas. |

---

## Document inventory (with priority)

### 🔴 Must-use (locations confirmed on disk)
- **Serie 1–13** (`Serie N.pdf`) + ✅ **solutions `your exams folder/DM Serie Lösungen/Lösung 1–13.pdf`** — do every one, then understand every solution (friend's #1 tip). Full per-Serie index in [DiskMath_Serien-und-Pruefungen.md](DiskMath_Serien-und-Pruefungen.md).
- **Prüfung SS25, WS25, WS26** + ✅ **`Lösung SS25/WS25/WS26.pdf`** (all in `your exams folder/`) — Koch's own exams, **3 of them, now with keys.** Do under strict 120 min. Best predictor; analyzed in the playbook.
- **`ZusammenfassungenDerVorlesungsstunden.pdf`** — Koch's own **per-week lecture summaries + Lernziele** (54 pp). Excellent for the active-recall pass your friend recommends. *(= the official "Vorlesungszusammenfassungen" posted to Moodle.)*
- **`DM_PVKSkript.pdf` + `DM_PVKLösungen.pdf`** — PVK script **with worked solutions** (your current best source of solved problems until Moodle Lösungen are pulled).
- **`4110…OA.pdf`** (Boschini/Hansen/Wolf) — primary textbook; reference for theory + proofs.
- **Your flashcard deck** ([`assets/DiskMath_Anki_deck.txt`](../assets/DiskMath_Anki_deck.txt)) — the substitute for the forbidden formula sheet.

### 🟡 Reference
- **Quizze (Moodle)** — the course's own quizzes; ideal **MC/Kurzfragen** drill for the 25% MC block (P1).
- Lecture slides V1–V13 — go through them note-taking style for active recall (friend's method), especially the algebra weeks.
- **`Ergänzendes Skript … (Flüsse und Schnitte).pdf`** — focused source for network flows/cuts (HS25 addition → exam P3b is always max-flow, so **high value**).

### ⚪ Skip
- **`da.pdf`** (Bölcskei diploma thesis, Gabor/frame theory) — unrelated advanced reference. Ignore.

---

## Build this: the memorization layer (since no aids)

Make a **flashcard deck** (Anki recommended for spaced repetition through the SF trip) covering at minimum:
- [ ] Modular arithmetic properties; congruence rules
- [ ] **Euclidean & extended-Euclidean algorithm** (GCD, modular inverse) — be able to execute by hand fast
- [ ] **CRT** (linear congruence systems) — solution recipe
- [ ] **RSA** — key generation + encrypt/decrypt (the two formulas)
- [ ] Group/ring/field axioms; **Lagrange's theorem**; cyclic group facts; subgroup tests
- [ ] Counting: pigeonhole, inclusion–exclusion, binomial identities, Stirling numbers
- [ ] Graph rules: Euler's formula, Kuratowski, planarity/coloring bounds, tree properties
- [ ] **Ford–Fulkerson / max-flow = min-cut**
- [ ] Polynomial/coding facts: CRC, Reed–Solomon basics
- [ ] A short **executive cheat sheet** of the top ~1 page of formulas — to *memorize* (you can't bring it in).

---

## Strategy & sequence (P1, with heavy spaced repetition into Aug 5)

1. **Block 3 (number theory/algebra) first and most** — it's the biggest and most memorization-dependent; start flashcards on day 1 so spacing has time to work before Aug 5.
2. **Block 1 (combinatorics):** do many varied problems; the risk is tricky scenarios, beaten only by volume.
3. **Block 2 (graph theory/flows):** learn the rule-set, do representative problems; don't over-grind (mostly common sense).
4. **Read through all 13 Lösungen** even for Übungen you didn't fully do — harvest the obscure-topic free points.
5. **Both Koch old exams under time**, twice.

**P2 (SF):** **DiskMath flashcards are the #1 SF activity** — exam is Aug 5, no aids, so daily Anki keeps it alive. **P3:** Aug 3 (after EC) → Aug 5 final old-exam + flashcard blitz → **exam Wed Aug 5**.

## Resources to obtain (checklist)
- [ ] Any shared **DiskMath flashcard deck / cheat sheet** from prior years (then verify against Koch's syllabus)
- [ ] Confirm SS25 + WS25 are Koch's (they are — prof matches) and grab any earlier Koch exams

## Time budget
_Provisional P1: ~75 h (top priority — early exam + no aids + memorization runway). Finalized in the master schedule._
