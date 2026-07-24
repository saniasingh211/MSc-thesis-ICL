# Research Log

A working notebook kept during the project (June-September 2025), lightly cleaned up from the original Notion pages: filenames de-junked, broken internal links fixed, and anything that was my supervisor's words rather than mine removed. Everything else is unedited, including the rough edges.

## Dated entries

- [2025-06-12](2025-06-12_dg_code_progress.md) : first working DG advection code, single stream
- [2025-06-18](2025-06-18_understanding_paraview.md) : learning to read ParaView output
- [2025-07-17](2025-07-17_meeting.md) : meeting notes, checkpointing and mesh immersion tasks
- [2025-07-22](2025-07-22_updates.md) : progress update, questions for Colin
- [2025-07-25](2025-07-25_edits_and_questions.md) : matching initial conditions between the two methods
- [2025-07-31](2025-07-31_hermite_quadrature.md) : discovering `scipy.special.roots_hermite`
- [2025-09-03](2025-09-03_convergence_and_checkpointing.md) : supervisor feedback on convergence and checkpointing

## Topical notes

- [multiple_streams_first_run.md](multiple_streams_first_run.md) : first working multi-stream code, task list
- [code_walkthrough_single_stream.md](code_walkthrough_single_stream.md) : block-by-block breakdown of the early single-stream code
- [single_vs_multistream_differences.md](single_vs_multistream_differences.md) : what changes going from 1 to M streams
- [output_interpretation.md](output_interpretation.md) : what q, u, phi mean physically, reading the output
- [code_cleanup_suggestions.md](code_cleanup_suggestions.md) : refactor notes for the early advection code
- [2d_vs_1d_differences.md](2d_vs_1d_differences.md) : comparing the two methods' meshes, equations, moments
- [firedrake_solver_theory.md](firedrake_solver_theory.md) : `LinearVariationalProblem`/`Solver`, weak forms, upwind flux
- [firedrake_velocity_solver_notes.md](firedrake_velocity_solver_notes.md) : the velocity solver's weak form, written up for the report
- [dg_cg_theory_notes.md](dg_cg_theory_notes.md) : why DG for advection, why CG for Poisson
- [vlasov_vs_multistream_comparison.md](vlasov_vs_multistream_comparison.md) : full comparison table, meshes/ICs/equations/function spaces
- [plasma_paper_notes.md](plasma_paper_notes.md) : reading notes, kinetic instabilities
- [error_plots_notes.md](error_plots_notes.md) : early checkpoint-loading code for error plots
- [final_suggestions.md](final_suggestions.md) : open questions near the end, higher moments, regridding
- [folder_structure_planning.md](folder_structure_planning.md) : planning the M/T sweep and checkpoint layout
- [thesis_outline_and_moment_roadmap.md](thesis_outline_and_moment_roadmap.md) : original chapter outline, plus a moment-computation roadmap
