# Pipeline

The execution order, beginning to end. See `architecture.md` for what each piece is.

1. `params.py` is imported first by everything downstream. It defines every physical constant (`k`, `A`, `H`, `L`, `T`, mesh resolution) and the two mesh factory methods.

2. `run_simulations.py` is the entry point. It defines the sweep: which values of `M` (stream count) and `T` (final time) to run. As currently configured, it sweeps `M = 10, 12`. The wider `M = 2` through `23` convergence sweep, referenced in the thesis, was produced separately, by the older `analysis_clean.py` script (see note below).

3. For each `(M, T)` pair, it calls `run_multistream(M, T)` in `multistream_clean.py`.

4. That function builds a 1D periodic mesh via `params.make_1d_mesh()`.

5. It creates `M` stream functions: `q_1...q_M` on a DG1 space, `u_1...u_M` on a vector CG1 space.

6. Streams are initialized using Gauss-Hermite quadrature (`scipy.special.roots_hermite`), scaled to match a Maxwellian velocity distribution. This quadrature is exact for polynomials up to degree `2M-1`, which is why the multistream moments match the exact analytical moment to machine precision with as few as 3 streams, before any time evolution even begins.

7. A Poisson solver is set up on CG1, with a nullspace correction since periodic boundaries make the system otherwise singular.

8. An advection solver is set up on DG1, using upwind flux at cell facets.

9. A velocity solver is set up on CG1, driven by the negative gradient of the electric potential.

10. The initial state is written to `vtk_ms_init/` and checkpointed to `ms_init/`.

11. The main loop runs SSPRK3 time stepping: three Runge-Kutta stages per step, each stage re-solving Poisson, then advection and velocity for every stream.

12. At the final time, the state is written to `vtk_ms_final/` and checkpointed to `ms_final/`.

13. Separately, `run_simulations.py` calls `run_2d_vlasov(T)` in `vp1d.py`, once per `T` value.

14. That function builds a single 2D extruded mesh (1D base, extended in velocity).

15. It solves the full Vlasov equation directly on that mesh, with no stream approximation, the reference solution.

16. The same SSPRK3 stepping is used, with the Poisson equation coupled through the average density over the domain.

17. Initial and final states are checkpointed to `vlasov_init/` and `vlasov_final/`.

18. Once both sets of checkpoints exist, the `analysis/` package loads them via `data_loader.py`.

19. It computes a chosen velocity moment from each representation, immerses the 1D multistream mesh into 2D phase space via `moment_transfer.py`, and interpolates the 2D moment onto that same line for a like-for-like comparison. This step exists because the two methods don't live on comparable meshes: multistream is a 1D spatial field, the 2D solve is defined over position and velocity together. Without immersion, there's no shared ground to measure an error on.

20. `convergence_study.py` computes the relative L2 error between the two, across every `M` and `T`, and `plotting.py` renders the convergence figures that appear in `plots/`.

## Note

`analysis_clean.py` was an earlier, separate attempt at steps 18-20, using a different weight function and checkpoint layout. It no longer runs (see `architecture.md`, Legacy layer). It is not part of the flow above.
