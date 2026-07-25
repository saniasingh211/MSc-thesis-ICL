# Firedrake for report

**Theory for Velocity Solver:**

**Strong form:** $\frac{\partial u}{\partial t} = -\frac{\nabla \phi}{m}$

**Discretization:** $u^{n+1} = u^n + \Delta t \left(-\frac{\nabla \phi}{m}\right)$

**Weak form:** Find $\Delta u$ such that: $$\int v \cdot \Delta u \, dx = \int v \cdot \left(-\frac{\Delta t \nabla \phi}{m}\right) dx$$ for all test functions $v$

**Why this works:**

- Simple explicit update: new velocity = old velocity + acceleration × time
- Mass matrix on left ($\int v \cdot \Delta u$), force on right ($\int v \cdot F$)
- Linear system: $M \Delta u = F$ where $M$ is mass matrix

**Implementation:** LinearVariationalSolver solves this linear system efficiently.
