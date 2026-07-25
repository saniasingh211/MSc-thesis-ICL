# Error Plots

What I gotta do:

Predefined: ncells, L, A, k, mesh

```python
q_list = []
u_list = []

with CheckpointFile("multistream_checkpoint.h5", 'r') as afile:
    mesh_1d = afile.load_mesh("1d_mesh")
    for i in range(M):
        q_list.append(afile.load_function(mesh_1d, f"q_{i+1}"))
        u_list.append(afile.load_function(mesh_1d, f"u_{i+1}"))
    phi_1d = afile.load_function(mesh_1d, "phi")
```
