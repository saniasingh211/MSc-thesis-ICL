# Block-by-Block summary

First time code.

---

```python
from firedrake import *
import math

ncells = 40
L = 1
mesh = PeriodicIntervalMesh(ncells, L)
```

- Imports Firedrake and math libraries.
- Defines a 1D periodic interval mesh from 0 to 1, consisting of 40 cells.

---

**Block 2: Function Spaces and Initial Conditions**

```python
V = FunctionSpace(mesh, "DG", 1)
W = VectorFunctionSpace(mesh, "CG", 1)

x, = SpatialCoordinate(mesh)

u = Function(W)
q = Function(V).interpolate(exp(-(x-0.5)**2/(0.2**2/2)))
q_init = Function(V).assign(q)
```

- Sets up function spaces: DG for scalar \(q\), CG for vector \(u\).
- Defines spatial coordinate \( x \).
- Initializes velocity \( u \) (zero by default).
- Sets initial condition for \( q \) as a Gaussian centered at \( x=0.5 \).
- Stores the initial \( q \) for future reference.

---

**Block 3: Time-Stepping Parameters**

```python
T = 3
dt = T/500
dtc = Constant(dt)
q_in = Constant(1.0)
mass = Constant(1.0)
```

- Defines total simulation time \( T \).
- Calculates time step size \( dt \).
- Sets constants for time step, input field, and mass.

---

**Block 4: DG Advection Solver Setup**

```python
dq_trial = TrialFunction(V)
psi = TestFunction(V)
a = psi*dq_trial*dx

us = Function(W)
n = FacetNormal(mesh)
un = 0.5*(dot(us, n) + abs(dot(us, n)))

L1 = dtc*(inner(us, grad(psi))*q*dx
          - (psi('+') - psi('-'))*(un('+')*q('+') - un('-')*q('-'))*dS)

q1 = Function(V); q2 = Function(V)
L2 = replace(L1, {q: q1}); L3 = replace(L1, {q: q2})

dq = Function(V)

params = {'ksp_type': 'preonly', 'pc_type': 'bjacobi', 'sub_pc_type': 'ilu'}
prob1 = LinearVariationalProblem(a, L1, dq)
solv1 = LinearVariationalSolver(prob1, solver_parameters=params)
prob2 = LinearVariationalProblem(a, L2, dq)
solv2 = LinearVariationalSolver(prob2, solver_parameters=params)
prob3 = LinearVariationalProblem(a, L3, dq)
solv3 = LinearVariationalSolver(prob3, solver_parameters=params)
```

- Defines trial and test functions for DG advection.
- Sets up upwind flux using facet normals.
- Constructs weak forms for three stages of RK3 time stepping.
- Prepares three solvers (one per RK3 stage) with specified linear solver parameters.

---

**Block 5: Potential (phi) Solver Setup**

```python
Vcg = FunctionSpace(mesh, "CG", 1)
phi_sol = TrialFunction(Vcg)
dphi = TestFunction(Vcg)
phi = Function(Vcg)

nullspace = VectorSpaceBasis(constant=True)

aphi = inner(grad(phi_sol), grad(dphi))*dx
Paphi = phi_sol*dphi*dx + inner(grad(phi_sol), grad(dphi))*dx
F = q*dphi*dx
phi_problem = LinearVariationalProblem(aphi, F, phi, aP=Paphi)
phi_solver = LinearVariationalSolver(phi_problem, nullspace=nullspace,
                                    solver_parameters={
                                        'ksp_type': 'gmres',
                                        'ksp_atol': 1.0e-11,
                                    })
```

- Sets up CG space and variational forms for potential field \( \phi \).
- Handles nullspace for periodic domain.
- Prepares solver for the Poisson-like equation for \( \phi \).

---

**Block 6: Velocity (\( u \)) Solver Setup**

```python
du_trial = TrialFunction(W)
u_test = TestFunction(W)
a = inner(u_test, du_trial)*dx

L1 = -dtc/mass*inner(u_test, grad(phi))*dx
du = Function(W)
u1 = Function(W)
u2 = Function(W)
du_prob = LinearVariationalProblem(a, L1, du)
du_solv = LinearVariationalSolver(du_prob)
```

- Sets up variational form to update velocity \( u \) using the gradient of \( \phi \).
- Prepares solver for velocity update at each RK3 substep.

---

**Block 7: Time-Stepping Loop and Output**

```python
t = 0.0
step = 0
output_freq = 20
outfile = VTKFile("advection_1d.pvd")
outfile.write(q, phi, u)

while t < T - 0.5*dt:
    phi_solver.solve()
    us.assign(u)
    solv1.solve()
    du_solv.solve()
    q1.assign(q + dq)
    u1.assign(u + du)

    phi_solver.solve()
    us.assign(u1)
    solv2.solve()
    du_solv.solve()
    q2.assign(0.75*q + 0.25*(q1 + dq))
    u2.assign(0.75*u + 0.25*(u1 + du))

    phi_solver.solve()
    us.assign(u2)
    solv3.solve()
    du_solv.solve()
    q.assign((1.0/3.0)*q + (2.0/3.0)*(q2 + dq))
    u.assign((1.0/3.0)*u + (2.0/3.0)*(u2 + du))

    step += 1
    t += dt

    if step % output_freq == 0:
        outfile.write(q, phi, u)
        print("t=", t)
```

- Initializes time and output.
- Runs main time-stepping loop using three-stage SSP Runge-Kutta method.
- Solves for \( \phi \), updates velocity and scalar field in each substep.
- Writes simulation output to file every 20 steps for visualization.
