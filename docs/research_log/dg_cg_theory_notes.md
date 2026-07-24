# Theory

- continuity equation is hyperbolic
- DG naturally handles **upwinding** - information flows in the direction of velocity u
- Allows **discontinuities** which can develop in hyperbolic equations

**CG for potential φ:**

- Poisson equation ∇²φ = q is **elliptic**
- CG is standard for elliptic PDEs
- Needs **continuity** across elements for second derivatives

**Periodic mesh:**

- Models plasma in a periodic domain (common in plasma physics)
- charge that exits one side automatically enters the other
- It's easier to deal with than walls or boundaries

---

### Purposes of Solvers

**1. Poisson solver** (for φ): -∇²φ = q

- **Purpose**: Given charge density q, find electric potential φ
- **Why**: Need φ to compute electric field E = -∇φ for particle forces

**2. Momentum solver** (for u): ∂u/∂t = -∇φ

- **Purpose**: Update fluid velocity based on electric field
- **Why**: Particles accelerate due to electric force F = qE

**3. Advection solver** (for q): ∂q/∂t + ∇·(uq) = 0

- **Purpose**: Transport charge density with the fluid velocity
- **Why**: Charge moves with the particles (continuity equation)

This is the **operator splitting** approach: solve each physics piece separately, then combine.

---

## The plan:

**Summary - What we've planned:**

**Goal**: Rewrite the advection code in your own style, same math/solvers

**Setup (looks good):**

- Periodic mesh, DG for q, CG for u and φ
- Initial conditions and time parameters

**Three solvers to implement:**

1. **Poisson**: -∇²φ = q → get electric potential
2. **Momentum**: ∂u/∂t = -∇φ → update velocity
3. **Advection**: ∂q/∂t + ∇·(uq) = 0 → transport charge

**Time stepping**: SSP-RK3 (3 stages like original)

**Next session**: Code the three solvers, then put together the time loop.

Sleep well!
