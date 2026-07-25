# Firedrake

## LVP and LVSolver

**LinearVariationalProblem** is a Firedrake class.

It represents a linear PDE in weak form: find u such that a(u,v) = L(v) for all test functions v.

**Pattern:**

- a is bilinear form (has both trial and test functions)
- L is in its linear form (has only test function)
- u is the solution function

Then **LinearVariationalSolver** actually solves the problem!

This is the standard way to solve PDEs in firedrake.

**Velocity Solver:**

**Strong form:** ∂u/∂t = -∇φ/m

**Discretization:** u^(n+1) = u^n + Δt(-∇φ/m)

**Weak form:** Find Δu such that: ∫ v · Δu dx = ∫ v · (-Δt∇φ/m) dx for all test functions v

**Why this works:**

- Simple explicit update: new velocity = old velocity + acceleration × time
- Mass matrix on left (∫ v · Δu), force on right (∫ v · F)
- Linear system: M Δu = F where M is mass matrix

**Implementation:** LinearVariationalSolver solves this linear system efficiently.

**Theory for Advection Solver:**

**Strong form:** ∂q/∂t + ∇·(uq) = 0

**Physical meaning:** Charge density q is transported by velocity field u (no sources/sinks)

**DG weak form:** Find q such that: ∫_K (∂q/∂t) v dx - ∫_K uq ∇v dx + ∫_∂K F̂ v ds = 0

for all test functions v, where:

- K = element
- F̂ = **numerical flux** (handles discontinuities between elements)

**Upwind flux:** F̂ = u⁺ q^upwind where q^upwind = q⁺ if u > 0, q⁻ if u < 0

**Why upwind:** Information flows in direction of velocity u.

### Expected behaviour

q: the charge spreads out

u: changes in velocity developing flow patterns

phi: follows charge distribution

$-\nabla^2\phi = q$

Charge creates potential wells

high charge would create a dip in phi
