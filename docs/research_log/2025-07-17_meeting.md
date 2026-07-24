# July 17 Meeting

---

What i've done:

- used initial q(x,0): gaussian with 3 bumps, they all travel
- what would happen if they were to clash/overlap
- cosine function is useless

---

Questions:

> 💡
> - Ask about "moments"
> - Discuss "projection" method
> - show paraview simulations for "projected" method, push commits for "projected" method on the vp1d file
> - visualise SOMETHING
> - the "H" stuff

---

**TASKS:**

- AT the end of both scripts, run both scripts going to the same time
- write to checkpoint files
- check context manager with 'w'

Checkpointing after time loop (just once):

- save the mesh
- name the mesh
- load the mesh

Analysis script (3rd script):

Import this:
`from firedrake.__future__ import interpolate`

- open 2 files
1. read mesh, soln from 2d
2. read mesh, soln from 1d
- Do the moments stuff
- make the 1d mesh immersed in 2d
- interpolate 2d moments to the 1d immersed mesh

> 💡 Note for next time: do it for multiple times

Websites:

Interpolation: Firedrake

[https://www.firedrakeproject.org/interpolation.html](https://www.firedrakeproject.org/interpolation.html)

Checkpointing:

https://www.firedrakeproject.org/checkpointing.html

changing mesh coordinates:

[https://www.firedrakeproject.org/checkpointing.html](https://www.firedrakeproject.org/checkpointing.html)

---

- plots 2d vs 1d (the moments stuff)
