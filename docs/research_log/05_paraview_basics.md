# Jun 18: Understanding Paraview

## VTK Files

> 💡 what do they mean?
>
> - VTK: visualization toolkit for data.
> - **.vtu** store unstructured grid data.
> - **.pvd** is a paraview data file.

1d mesh: Paraview displays mesh as line

plotting the value of $q$, $u$ or $\phi$ along this line.

**X**- Position along the mesh (0 to 1).

**Y**- Value of field selected $q$, $u$, $\phi$

**Scalar warp filter**:

The Scalar Warp filter in ParaView is a visualization tool that helps you "see" how a scalar field like $q$ or $\phi$ or any other scalar quantity) varies by displacing the geometry in the direction of a chosen axis (usually vertically) according to the value of that scalar.

- Eg. if mesh is a line, and `q(x)` is a gaussian bump, then using a scalar warp filter, the line is warped upwards.
- lowers/raises the mesh line in the z-direction according to values of $q$ , $u$ or $\phi$.

## What does it mean for me?

---

**Interpretation of the Simulation Plots**

At the beginning of the simulation, there is a single bump (like a hill) in the center of the plot, representing the initial concentration or quantity. As the simulation progresses, this bump splits into two smaller bumps that move toward opposite ends of the domain. By the end, you see two bumps at both sides of the plot and a dip ("U" shape) in the middle.

This behaviour happens because the simulation uses periodic (looped) boundary conditions, like a racetrack, so anything that moves off one edge re-enters from the other side. The flow (velocity field) in the simulation causes the initial bump to split and transport material toward both sides. The dip in the middle shows the region where the original bump has moved away, leaving it empty.

**In summary:**

The plots show that the initial bump splits and travels to both sides due to the flow and periodic (looped) domain, leaving a dip in the middle. This demonstrates how the quantity is transported and wraps around in the domain.

---

## For Multiple Streams

| Feature | One Stream | Multiple Streams |
| --- | --- | --- |
| Velocity Field | Uniform (same direction/speed everywhere) | Non-uniform (different directions/speeds in regions) |
| Initial Bump Evolution | Bump moves together in one direction | Bump may split and move in several directions |
| Number of Peaks | Usually one peak moving around | Multiple peaks (streams) may form and travel separately |
| Direction of Flow | All material moves the same way | Material can move left in some regions, right in others |
| Plot Appearance Over Time | Single moving bump, possibly wrapping (periodic) | Several bumps/streams, possibly interacting or wrapping |
| Physical Analogy | River flowing in one direction | Braided river or water flowing in different channels |

---

Plot interpretation:

- scales are weird: $6.4e-1$, $7.3e+00$: all positive and $>0$ in case of multiple streams.
- what can we do with the function to tweak this?.
