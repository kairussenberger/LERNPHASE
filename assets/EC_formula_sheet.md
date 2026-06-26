# Electronic Circuits — Formelsammlung (STARTER)

> **Exam aid:** 5×A4 double-sided = **10 pages, machine-printed OK** + calculator. This is the content backbone — typeset it (LaTeX/Word) into a navigable PDF with **schematic thumbnails per row** and **edge tabs** so you can find any circuit in seconds.
> ⚠️ **STARTER from standard analog content — verify every formula's sign/convention against the course (esp. whether r_o / channel-length modulation is included, and the prof's notation).** Convention below: small-signal, low frequency.
> 💡 **You already have a fuller, course-exact version:** `ec pvk main doc complete.pdf` (the "EC Masterclass") has these R_in/R_out/A_v tables for every config on pp. 30–34, 42–43, 49–55, 57–64. **Use this typed sheet as a cross-check/index; build your 10-page exam sheet primarily by curating the Masterclass pages.** See [EC playbook](../subjects/EC_Uebungen-und-Playbook.md).

## Small-signal parameters
| Param | MOSFET (saturation) | BJT (active) |
|-------|--------------------|--------------|
| Transconductance gₘ | gₘ = 2I_D/V_ov = √(2·μCₒₓW/L·I_D) | gₘ = I_C/V_T (V_T≈26 mV) |
| Output resistance r_o | r_o = 1/(λI_D) ≈ V_A/I_D | r_o = V_A/I_C |
| Input (base) resistance | gate: ∞ (r_gs→∞) | r_π = β/gₘ = V_T·β/I_C |
| Current gain | — | β = I_C/I_B, α = β/(β+1) |
| Useful identity | gₘr_o = intrinsic gain (a₀) | gₘr_π = β |

## Master amplifier table — R_in, R_out, A_v
**R_S** = source/emitter degeneration resistor; **R_sig** = driving source resistance; loads **R_D/R_C** at drain/collector, **R_L** at output node. `∥` = parallel. Approximations assume r_o large unless noted.

### MOSFET stages
| Stage | A_v (gain) | R_in | R_out (looking into output) |
|-------|-----------|------|------------------------------|
| **Common-Source** (no degen) | −gₘ(R_D ∥ r_o) | ∞ | R_D ∥ r_o |
| **CS with source degen R_S** | −gₘ(R_D∥r_o)/(1+gₘR_S) ≈ −R_D/(R_S+1/gₘ) | ∞ | R_D ∥ [r_o(1+gₘR_S)+R_S] |
| **Common-Gate** | +gₘ(R_D ∥ r_o) | ≈ 1/gₘ (exactly (r_o+R_D)/(1+gₘr_o)) | R_D ∥ [r_o + R_S + gₘr_oR_S] |
| **Common-Drain / Source Follower** | gₘ(r_o∥R_S)/(1+gₘ(r_o∥R_S)) ≈ <1 | ∞ | (1/gₘ) ∥ r_o ∥ R_S ≈ 1/gₘ |

### BJT stages
| Stage | A_v (gain) | R_in | R_out |
|-------|-----------|------|-------|
| **Common-Emitter** (no degen) | −gₘ(R_C ∥ r_o) | r_π (∥ R_B) | R_C ∥ r_o |
| **CE with emitter degen R_E** | −gₘR_C/(1+gₘR_E) ≈ −R_C/(R_E+1/gₘ) | r_π + (β+1)R_E (∥R_B) | R_C ∥ [r_o(1+gₘ(R_E∥r_π))] |
| **Common-Base** | +gₘ(R_C ∥ r_o) | r_π ∥ (1/gₘ) ≈ 1/gₘ (=r_e=α/gₘ) | R_C ∥ [r_o(1+gₘ(R_E∥r_π))] |
| **Common-Collector / Emitter Follower** | (R_E∥r_o)/((R_E∥r_o)+1/gₘ) ≈ <1 | r_π + (β+1)(R_E∥r_o) | R_E ∥ [1/gₘ + R_sig/(β+1)] |

**Quick mental model:** CS/CE = high inverting gain. CG/CB = low R_in (1/gₘ), non-inverting, current buffer. CD/CC = ~unity gain, high R_in, low R_out (voltage buffer).

## Multi-transistor blocks
| Block | Key result |
|-------|-----------|
| **Cascode** (CS+CG / CE+CB) | R_out ≈ gₘ₂r_o₂·r_o₁ (boosted); A_v ≈ −gₘ₁·(R_out ∥ R_L). High gain, high R_out. |
| **Current mirror (MOS)** | I_out = I_ref·(W/L)₂/(W/L)₁; R_out = r_o₂. Cascode mirror: R_out ≈ gₘr_o². |
| **Current mirror (BJT)** | I_out ≈ I_ref·(1/(1+2/β)) (base-current error); R_out = r_o. |
| **gₘR_out method** | For a stage, |A_v| = gₘ·R_out(total at output node). Build complex amps by composing. |

## DC bias recipe (do this FIRST in every problem)
1. **Kill small signals** (AC sources→0): DC only. Capacitors→open, inductors→short.
2. Assume a region (MOS: saturation; BJT: active). Write the loop: V_GS / V_BE drop, then the current law.
3. **MOSFET:** I_D = ½μCₒₓ(W/L)(V_GS−V_th)²(1+λV_DS). **BJT:** I_C = I_S e^(V_BE/V_T), I_B=I_C/β.
4. Solve for I_D / I_C and node voltages. **Check region:** MOS sat needs V_DS≥V_ov; BJT active needs V_BE≈0.7, V_BC<0.5 (B-C reverse).
5. Compute gₘ, r_o, r_π from the bias point → proceed to small-signal.

## Region conditions
| Device | Cutoff | Triode/Saturation (MOS) · Active (BJT) |
|--------|--------|----------------------------------------|
| **NMOS** | V_GS<V_th | Triode: V_DS<V_ov · Saturation: V_DS≥V_ov=(V_GS−V_th) |
| **NPN BJT** | V_BE<0.5 | Active: V_BE≈0.7, B-C reverse-biased · Saturation: both junctions forward |

## Diodes & rectifiers
| Item | Formula |
|------|---------|
| Diode I/V | I = I_S(e^(V_D/V_T) − 1); constant-voltage-drop model V_D≈0.7 V |
| Small-signal diode resistance | r_d = V_T/I_D |
| Half-wave rectifier (peak) | V_out,peak = V_in,peak − V_D |
| Full-wave (bridge) | V_out,peak = V_in,peak − 2V_D |
| Ripple voltage (cap filter) | V_ripple ≈ I_load/(f·C) (half-wave); /(2fC) for full-wave |
| Peak detector / voltage doubler | output ≈ 2·V_in,peak (minus drops) |

## Bode plot rules (review strip)
- Pole at ω_p: gain slope −20 dB/dec above ω_p; phase −45° at ω_p, −90° a decade above.
- Zero: +20 dB/dec, +45°/+90°.
- Magnitude (dB) = 20·log₁₀|H|. Cascade poles/zeros add slopes.
- Dominant-pole approx: bandwidth set by lowest-frequency pole.

## Worked pattern — copy this in the exam
**Task:** find A_v of a CE stage with R_C, biased by I_C.
1. DC: from bias, I_C ⇒ gₘ=I_C/V_T, r_π=β/gₘ, r_o=V_A/I_C.
2. Small-signal: replace BJT with gₘv_π, r_π, r_o. Input sees r_π; output node has R_C∥r_o.
3. A_v = −gₘ(R_C∥r_o); R_in=r_π; R_out=R_C∥r_o. → write numbers.

---
**To-do before printing:** add thumbnails per row · verify against both midterms · confirm whether r_o is expected in answers · hunt a classmate's last-year sheet as a cross-check.
