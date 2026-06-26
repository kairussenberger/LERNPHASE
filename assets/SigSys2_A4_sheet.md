# Signals & Systems II — A4 Sheet (STARTER)

> **Exam aid:** ONE A4 sheet, **two-sided, HANDWRITTEN** (Aug 15, Prof Dörfler). So this is the *content plan* to copy by hand — distill, don't transcribe. Add your own worked problem-2/4 templates from old exams.
> ⚠️ STARTER from standard linear-systems/control content — **verify scope + notation against Dörfler's chapters 0–7 and the PVK.**

## State-space model
- Continuous LTI: **ẋ = Ax + Bu, y = Cx + Du** (x∈ℝⁿ state, u input, y output).
- Solution: **x(t) = e^(At)x(0) + ∫₀ᵗ e^(A(t−τ))Bu(τ)dτ**.
- Matrix exponential **3 ways**: ① diagonalizable A=VΛV⁻¹ → e^(At)=V·diag(e^(λᵢt))·V⁻¹; ② nilpotent (Aᵏ=0) → finite sum Σ(At)ⁱ/i!; ③ A=D+N (D diag, N nilpotent, DN=ND) → e^(At)=e^(Dt)·Σ(Nt)ⁱ/i!. Handy: [[λ,1],[0,λ]]→e^(λt)[[1,t],[0,1]]; [[σ,ω],[−ω,σ]]→e^(σt)[[cos ωt, sin ωt],[−sin ωt, cos ωt]].

## ① Stability (time domain)
- **Asymptotically stable ⇔ all eig(A) have Re(λ)<0.** Marginally stable: Re(λ)≤0 with simple eigenvalues on jω-axis. Unstable: any Re(λ)>0 (or repeated jω-axis).
- Zero-input response governed by eigenvalues; modes e^(λᵢt).
- **Hurwitz quick tests** (avoid solving the char. poly): degree-2 `αλ²+βλ+γ` asymp stable ⇔ α,β,γ all same sign; degree-3 `λ³+αλ²+βλ+γ` asymp stable ⇔ α,β,γ>0 **and** αβ>γ.
- **Routh–Hurwitz** (general): all poles in LHP ⇔ first column of Routh array has no sign changes (count = # RHP poles).
- **Lyapunov (linear):** Re λ<0 ∀λ ⇔ for any R=Rᵀ≻0, ∃! Q=Qᵀ≻0 with AᵀQ+QA=−R.
- **Non-diagonalizable + eigenvalue on jω-axis** → eigenvalues alone are inconclusive; inspect e^(At) directly.
- **Discrete-time stability uses |λ|:** asymp ⇔ |λᵢ|<1 ∀i; marginally ⇔ |λᵢ|≤1 (simple on |λ|=1); unstable ⇔ ∃|λᵢ|>1.

## ② Controllability & Observability
- **Controllability matrix** 𝒞 = [B AB A²B … Aⁿ⁻¹B]. Controllable ⇔ rank 𝒞 = n.
- **Observability matrix** 𝒪 = [C; CA; CA²; …; CAⁿ⁻¹]. Observable ⇔ rank 𝒪 = n.
- **Min-energy control** (to reach x_f at T): u*(t)=Bᵀe^(Aᵀ(T−t)) W_c⁻¹ x_f, with controllability Gramian W_c=∫₀ᵀ e^(Aτ)BBᵀe^(Aᵀτ)dτ; energy = x_fᵀW_c⁻¹x_f.
- **Kalman decomposition:** transform splits system into (controllable/uncontrollable)×(observable/unobservable) subsystems; transfer function sees only the controllable+observable part.
- PBH test: controllable ⇔ rank[A−λI, B]=n ∀λ; observable ⇔ rank[A−λI; C]=n ∀λ.

## ③ Frequency domain
- **Transfer function:** H(s) = C(sI−A)⁻¹B + D. Poles = eig(A) (of minimal realization).
- **Laplace:** ℒ{f}=∫₀^∞ f(t)e^(−st)dt. Pairs: 1→1/s; e^(at)→1/(s−a); sin ωt→ω/(s²+ω²); cos ωt→s/(s²+ω²); tⁿ→n!/s^(n+1). Properties: ℒ{f'}=sF−f(0); ℒ{∫f}=F/s; shift e^(at)f→F(s−a).
- **Nyquist (principle of the argument):** # encirclements N of −1 by L(jω) = P − Z (P=open-loop RHP poles, Z=closed-loop RHP poles). Closed-loop stable ⇔ Z=0 ⇔ N=−P (CCW encirclements = P).
- **Bode rules:** pole −20 dB/dec & −90°; zero +20 dB/dec & +90°; magnitude(dB)=20log₁₀|H|; phase −45° at a pole frequency.
- **2nd-order:** H=ω_n²/(s²+2ζω_n s+ω_n²). Poles −ζω_n ± jω_n√(1−ζ²). Overshoot M_p=e^(−ζπ/√(1−ζ²)); ζ=1 critically damped; ζ<1 underdamped.

## Discrete-time systems
- **z-transform:** X(z)=Σ x[k]z⁻ᵏ. Discrete LTI stable ⇔ all poles inside unit circle (|z|<1).
- **Sampling / quantization:** value + time quantization; sampled-data systems.
- **Discretization (Euler):** Forward Euler x[k+1]=(I+hA)x[k]+hBu[k] — stable region: eig(I+hA) inside unit circle ⇒ |1+hλ|<1 (conditionally stable). Backward Euler implicitly more stable.
- Mapping: continuous pole s ↔ discrete pole z=e^(sh) (exact); LHP ↔ unit disk.

## Nonlinear systems (lighter)
- **Local linearization** around equilibrium x*: A=∂f/∂x|_{x*}; stable if linearization is (Hartman–Grobman, hyperbolic).
- **Lyapunov direct method:** V(x)>0, V(x*)=0; if V̇(x)≤0 ⇒ stable; V̇(x)<0 ⇒ asymptotically stable.
- **LaSalle's invariance principle:** trajectories converge to the largest invariant set where V̇=0 (lets you conclude asymptotic stability when V̇≤0 only).

## Linear algebra refresh
- Eigen: Av=λv; det(A−λI)=0. Diagonalizable if n independent eigenvectors.
- SVD: A=UΣVᵀ. Rank = # nonzero singular values.

---
**Add by hand before exam:** your distilled **problem-2 & problem-4 step templates** from old exams (these repeat most) · any course-specific formula Dörfler emphasizes · a tiny Laplace/z table.
