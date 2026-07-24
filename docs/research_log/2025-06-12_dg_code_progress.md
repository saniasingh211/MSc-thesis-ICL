# Jun 12: DG code progress

**Summary: Vlasov-Poisson DG Code Progress (Today's Work)**

- **Mesh/Spaces:**

  Set up a 1D periodic mesh and created function spaces:

  - `V` (DG) for q (distribution)
  - `W` (CG) for u (velocity)
  - `Vcg` (CG) for φ (potential)
- **Multiple Streams:**

  Initialized two (m=2) separate q and u functions.

  Set initial conditions with different centers (for q) and frequencies (for u).
- **DG Advection Formulated:**

  Wrote weak form for DG advection (including upwinding and jump terms) for each stream's q.
- **Total Distribution:**

  Summed all q streams to get `q_total` for use in Poisson's equation.
- **Poisson Solver:**

  Set up linear Poisson problem for electric potential φ, using `q_total` as the source.
- **Velocity Update Skeleton:**

  Created placeholder for updating velocities u for each stream based on φ. THIS!!
- **Solvers:**

  Prepared linear solvers for DG advection and Poisson problems.
- **To Do:**
  - Implement time-stepping loop
  - Solve DG advection for each q at each step
  - Complete velocity update for each u
  - Store/visualize results
