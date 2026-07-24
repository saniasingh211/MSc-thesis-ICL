# Vlasov VS multistream Code comparison

## Fundamental Approach

| Aspect | 2D Vlasov | 1D Multistream |
| --- | --- | --- |
| **Method** | Eulerian grid in phase space (x,v) | Lagrangian particles with discrete velocities |
| **Variables** | Distribution function f(x,v,t) | Charge densities q_i(x,t) and velocities u_i(x,t) |
| **Dimensions** | 2D phase space | 1D physical space + discrete velocity streams |
| **Discretization** | Finite elements on (x,v) mesh | M streams with fixed velocity points |

## Mesh & Domain

| Property | 2D Vlasov | 1D Multistream |
| --- | --- | --- |
| **Spatial domain** | x ∈ [0, 8π] | x ∈ [0, 1] |
| **Velocity domain** | v ∈ [-5, 5] (continuous) | 4 discrete points from Hermite quadrature |
| **Spatial resolution** | 50 cells | 40 cells |
| **Velocity resolution** | 50 layers | 4 streams |
| **Mesh type** | ExtrudedMesh (2D) | PeriodicIntervalMesh (1D) |

## Initial Conditions

| Component | 2D Vlasov | 1D Multistream |
| --- | --- | --- |
| **Density** | `v²·exp(-v²/2)·(1 + 0.05·cos(0.5x))/√(2π)` | `exp(-(x-center_i)²/0.05²)` for each stream |
| **Velocity** | Continuous v-distribution | All streams: u_i = 0.1 |
| **Physics** | Landau damping test case | Gaussian blobs with uniform velocity |
| **Spatial structure** | Sinusoidal modulation | Multiple Gaussian packets |

## Time Integration

| Aspect | 2D Vlasov | 1D Multistream |
| --- | --- | --- |
| **Method** | SSP-RK3 | SSP-RK3 |
| **Total time** | T = 8.0 | T = 8.0 |
| **Time steps** | 1000 steps (dt = 0.008) | 500 steps (dt = 0.016) |
| **Stability** | Upwind flux for advection | Upwind flux for advection |

## Equations Solved

### 2D Vlasov

- **Vlasov equation**: ∂f/∂t + v·∂f/∂x - E·∂f/∂v = 0
- **Poisson equation**: -∂²φ/∂x² = ∫(f - f̄)dv

### 1D Multistream

- **Continuity**: ∂q_i/∂t + ∇·(u_i·q_i) = 0
- **Momentum**: ∂u_i/∂t = -∇φ/m
- **Poisson**: -∇²φ = Σq_i

## Function Spaces

| Variable | 2D Vlasov | 1D Multistream |
| --- | --- | --- |
| **Density/Distribution** | DG(1) on 2D mesh | DG(1) on 1D mesh |
| **Potential** | CG(1) with R(0) in v-direction | CG(1) on 1D mesh |
| **Velocity** | Implicit in phase space | VectorFunctionSpace CG(1) |

## Moment Calculation

| Property | 2D Vlasov | 1D Multistream |
| --- | --- | --- |
| **Formula** | ∫∫ v·f(x,v) dv dx | Σ w(u_i)·q_i where w(u) = u² |
| **Meaning** | First velocity moment | Weighted sum over streams |
| **Conservation** | Should conserve momentum | Should conserve moment |

---

## Key Differences Summary

1. **Completely different test cases**: Vlasov uses Landau damping, multistream uses Gaussian blobs
2. **Different domains**: Vlasov uses [0,8π] vs multistream [0,1]
3. **Different physics**: Vlasov captures velocity distribution evolution, multistream tracks discrete particle groups
4. **Different moment definitions**: Vlasov computes ∫v·f dv, multistream computes Σu²·q

---

## Recommendations for Direct Comparison

### Option 1: Match the Landau Damping Test Case

**Modify multistream to match Vlasov initial conditions:**

```python
# In multistream code, replace initial conditions with:
for i in range(M):
    # Use Hermite quadrature points as velocities
    v_i = v_scaled[i]  # Already computed from Hermite roots

    # Initialize density to match Landau damping case
    landau_density = v_i**2 * exp(-v_i**2/2) * (1 + A*cos(k*x)) / sqrt(2*pi)
    q_list[i].interpolate(landau_density)

    # Set velocity to the quadrature point
    u_list[i].interpolate(as_vector([v_i]))

# Update domain size
L = 8*pi  # Match Vlasov domain
mesh = PeriodicIntervalMesh(ncells, L, name="1d_mesh")

# Update constants
A = Constant(0.05)
k = Constant(0.5)
```

### Option 2: Modify Vlasov to Match Multistream

**Change Vlasov initial conditions to Gaussian blobs:**

```python
# Replace Landau damping with superposition of Gaussians
def multistream_initial_condition(x, v):
    result = 0
    centers = [0.3, 0.7, 1.1, 1.5]  # Adjust for 8π domain
    for center in centers:
        result += exp(-(x-center)**2/0.05**2) * exp(-v**2/2) / sqrt(2*pi)
    return result

fn.interpolate(multistream_initial_condition(x, v))
```

### Option 3: Create Common Benchmark

**Both codes solve the same problem:**

1. **Domain**: Both use x ∈ [0, 2π]
2. **Initial condition**: Two-stream instability

    ```python
    # Vlasov
    fn.interpolate((exp(-(v-1)**2/0.1) + exp(-(v+1)**2/0.1)) * (1 + 0.01*cos(x)))

    # Multistream (2 streams at v = ±1)
    q_list[0].interpolate((1 + 0.01*cos(x)) * 0.5)
    q_list[1].interpolate((1 + 0.01*cos(x)) * 0.5)
    u_list[0].interpolate(as_vector([1.0]))
    u_list[1].interpolate(as_vector([-1.0]))
    ```

3. **Consistent moment**: Both compute ∫ρ(x)dx and ∫v·ρ(x,v)dxdv

**Recommendation**: Start with Option 1 (modify multistream to Landau damping) as it's the standard plasma physics benchmark.
