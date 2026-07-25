# Research Log

A working notebook kept during the project (June-September 2025), lightly cleaned up from the original Notion pages: filenames de-junked and numbered into a single chronological sequence, broken internal links fixed, and anything that was my supervisor's words rather than mine removed. Everything else is unedited, including the rough edges.

1. [01_dg_progress.md](01_dg_progress.md) : first working DG advection code, single stream (Jun 12)
2. [02_single_stream_code.md](02_single_stream_code.md) : block-by-block breakdown of that code
3. [03_dg_cg_theory.md](03_dg_cg_theory.md) : why DG for advection, why CG for Poisson
4. [04_solver_theory.md](04_solver_theory.md) : `LinearVariationalProblem`/`Solver`, weak forms, upwind flux
5. [05_paraview_basics.md](05_paraview_basics.md) : learning to read ParaView output (Jun 18)
6. [06_output_meaning.md](06_output_meaning.md) : what q, u, phi mean physically
7. [07_stream_differences.md](07_stream_differences.md) : what changes going from 1 to M streams
8. [08_multistream_first_run.md](08_multistream_first_run.md) : first working multi-stream code, task list
9. [09_cleanup_suggestions.md](09_cleanup_suggestions.md) : refactor notes for the early advection code
10. [10_july_meeting.md](10_july_meeting.md) : meeting notes, checkpointing and mesh immersion tasks (Jul 17)
11. [11_july_updates.md](11_july_updates.md) : progress update, questions for Colin (Jul 22)
12. [12_method_differences.md](12_method_differences.md) : comparing the two methods' meshes, equations, moments
13. [13_method_comparison.md](13_method_comparison.md) : full comparison table, ICs/equations/function spaces
14. [14_matching_conditions.md](14_matching_conditions.md) : matching initial conditions between the two methods (Jul 25)
15. [15_hermite_quadrature.md](15_hermite_quadrature.md) : discovering `scipy.special.roots_hermite` (Jul 31)
16. [16_velocity_solver.md](16_velocity_solver.md) : the velocity solver's weak form, written up for the report
17. [17_thesis_outline.md](17_thesis_outline.md) : original chapter outline, plus a moment-computation roadmap
18. [18_error_plots.md](18_error_plots.md) : early checkpoint-loading code for error plots
19. [19_folder_planning.md](19_folder_planning.md) : planning the M/T sweep and checkpoint layout
20. [20_convergence_checkpoints.md](20_convergence_checkpoints.md) : supervisor feedback on convergence and checkpointing (Sep 3)
21. [21_final_suggestions.md](21_final_suggestions.md) : open questions near the end, higher moments, regridding
22. [22_plasma_paper.md](22_plasma_paper.md) : reading notes, kinetic instabilities
