# Learning

Before writing any original code for this project, I worked through Firedrake's own tutorial demos, to learn the finite element framework itself.

- `helmholtz.py`: solving a Helmholtz equation, the simplest possible finite element problem in Firedrake.
- `DG_advection.py`: the classic cosine-bell / cone / slotted-cylinder advection test case, introducing discontinuous Galerkin elements and upwind flux, the same ingredients the multistream method later depends on.

Both are Firedrake's official demos, included here unmodified, as a record of the starting point. The original work begins in `../02_prototypes/`.
