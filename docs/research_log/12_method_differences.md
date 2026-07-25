# Differences

## 2D Vlasov Code Recap

### Mesh Construction

```python
base_mesh = PeriodicIntervalMesh(ncells, L)  # 1D spatial mesh
mesh = ExtrudedMesh(base_mesh, layers=nlayers, layer_height=H/nlayers)  # Extrude to 2D
mesh.coordinates.interpolate(as_vector([x, v-H/2]))  # Shift v-coordinate to [-5, 5]
```

- 2D mesh: x ∈ [0, 8π] (spatial), v ∈ [-5, 5] (velocity)
- Resolution: 50×50 cells in (x,v) space

### What It Solves

Single 2D Vlasov equation: `∂f/∂t + v·∂f/∂x - (∂φ/∂x)·∂f/∂v = 0`

Variables:

- `fn(x,v,t)`: Full distribution function in phase space
- `phi(x,t)`: Electric potential (integrated over v)

### Key Differences from 1D Multistream

| Aspect | 1D Multistream | 2D Vlasov |
| --- | --- | --- |
| Unknowns | 4 charge densities `qᵢ(x)` + 4 velocities `uᵢ(x)` | 1 distribution function `f(x,v)` |
| Velocity representation | 4 discrete streams at fixed velocities | Continuous velocity space |
| Computational cost | ~8 scalar fields | 1 field on 2D mesh (2500 points vs ~320) |
| Physics | Approximate velocity discretization | Full kinetic physics |
| Equations | 4 coupled 1D PDEs + Poisson | 1 2D PDE + Poisson |

### Same Initial Condition

Both use: `f₀(x,v) = v²·exp(-v²/2)·(1 + 0.05·cos(0.5x))/√(2π)`

### How to Compare

**1. Moments**

- 2D Vlasov: `moment = ∫∫ v·f(x,v) dx dv`
- 1D Multistream: `moment = Σᵢ vᵢ·∫ qᵢ(x) dx`

**2. Charge Density**

- 2D Vlasov: `ρ(x) = ∫ f(x,v) dv`
- 1D Multistream: `ρ(x) = Σᵢ qᵢ(x)`

**3. Electric Field Evolution**

Both compute `φ` from `ρ(x)`, should evolve similarly

**4. Energy/Conservation**

Both should conserve total energy and particle number

### Comparison Strategy

1. Run both codes with identical parameters
2. Extract 1D projections from 2D: `ρ₂D(x) = ∫ f(x,v) dv`
3. Compare: `ρ₂D(x)` vs `Σᵢ qᵢ(x)`
4. Check moments: Should track similarly over time
5. Verify physics: Landau damping rate, oscillation frequency

Key insight: The 2D code is the "exact" solution; the 1D multistream is an approximation using only 4 velocity points instead of 50.
