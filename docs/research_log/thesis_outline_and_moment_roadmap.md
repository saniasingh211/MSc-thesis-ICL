# MSc Thesis

Report structure

- Project title: VP Plasma FE firedrake
- Abstract, with some other ways to solve vlasov.

---

### Chapter 1

- Introduce the Vlasov Poisson system for plasma.
- Perhaps some plots about fluids/velocity/plasma simulation (etc)
- Talk about plasma.

### Chapter 2: FE appx and the problem setup

- Finite element approximation to the VP method, and what it does.
- Some stuff about the DG method, function spaces, and where our variables will be living.
- Upwind, cells, etc etc.
- The problem setup- explain particle in cell method.

### Chapter 3: Solving In firedrake

- Techniques in Firedrake- meshes
- Trial functions used with perturbations.
- A plot (perhaps)
- Mesh immersion and interpolation
- Transferring functions to cells
- Introduce the firedrake demos.

### Chapter 4: Moments, and physical meaning

- Gauss Hermite quadrature, and why we use it in our code
- How it can be used to approximate the moments (and quadrature points)
- How we tie together the firedrake demos.
- Comparison in the analysis script.

### Chapter 5: Results

- my plots: one by one.
- what does the error in moment mean, what it corresponds to.
- more plots- more methods to say how the streams approximation is accurate

### Future Plans

References.

---

- Pseudocode
- Appendix
- References

I am solving for phi at each stage. Great.

---

See also: [firedrake_velocity_solver_notes.md](firedrake_velocity_solver_notes.md)

---

# Moment Computing for Vlasov Solvers

## Current Implementation Status

- ✅ Basic first moment (momentum) computation working
- ✅ Conservation monitoring in place
- ✅ Integration between multistream and 2D Vlasov methods
- 🔄 **Needs improvement**: Limited to single moment type, hardcoded weight functions

---

## 1. Generalized Moment Framework

### Moment Hierarchy

Instead of hardcoding `w(u) = u[0]`, implement flexible moment system:

**Standard Statistical Moments:**

- **Zeroth moment**: `∫ f dv` → **Density/Charge**
- **First moment**: `∫ v f dv` → **Momentum/Current**
- **Second moment**: `∫ v² f dv` → **Energy/Temperature**
- **Third moment**: `∫ v³ f dv` → **Heat flux/Skewness**
- **Fourth moment**: `∫ v⁴ f dv` → **Pressure tensor/Kurtosis**

### Derived Quantities

- **Temperature**: `T = (⟨v²⟩ - ⟨v⟩²)/m`
- **Thermal velocity**: `v_th = √(T/m)`
- **Heat flux**: `q = ⟨v³⟩ - 3⟨v²⟩⟨v⟩ + 2⟨v⟩³`

---

## 2. Conservation Properties

### Key Theoretical Points

- **Moment evolution**: Each moment follows its own evolution equation
- **Hierarchy coupling**: Higher moments couple to lower ones through Vlasov equation
- **Invariant preservation**: Discretization should preserve correct moment dynamics

### Implementation Checks

- **Consistency verification**: Multistream moments → continuous Vlasov as M → ∞
- **Conservation monitoring**: Track how well moments are preserved over time
- **Physical bounds**: Ensure moments remain physically reasonable

---

## 3. Numerical Stability Considerations

### Weight Function Design

- **Hermite polynomial weights**: Natural choice since using Hermite quadrature
    - Exact for polynomials up to degree 2M-1
    - Orthogonal → better numerical properties
- **Moment boundedness**: Implement checks for unphysical growth
- **Adaptive strategies**: Higher moments may need refined quadrature

### Error Sources

- **Truncation effects**: How finite M affects moment accuracy
- **Quadrature errors**: Limited by Hermite rule degree
- **Time discretization**: SSP-RK3 impact on conservation
- **Spatial discretization**: DG vs CG effects on moment computation

---

## 4. Computational Efficiency

### Optimization Strategies

- **Precompute weights**: Calculate moment weight functions at initialization
- **Vectorized moments**: Compute multiple moments simultaneously
- **Selective evaluation**: Only compute moments when needed (output times)
- **Memory management**: Reuse temporary functions between moment calculations

### Current Bottlenecks

- Separate loops for each stream
- Repeated function interpolation calls
- Individual moment calculations instead of batch processing

---

## 5. Physical Interpretation & Applications

### Plasma Physics Context

- **Plasma frequency**: `ωp = √(ne²/ε₀m)` from zeroth moment
- **Landau damping**: Extractable from moment evolution rates
- **Instability analysis**: Growth rates visible in higher moments
- **Phase mixing**: Higher moments show velocity space structure

### Diagnostic Capabilities

- **Energy conservation**: Monitor kinetic energy moment
- **Entropy production**: Track through moment spreads
- **Phase space evolution**: Higher moments reveal filamentation
- **Convergence studies**: Compare multistream vs continuous solutions

---

## 6. Implementation Roadmap

### Immediate Improvements

1. **Flexible weight functions**: Replace hardcoded `w(u) = u[0]`
2. **Multiple moment types**: Implement zeroth through fourth moments
3. **Batch computation**: Calculate all moments in single pass
4. **Better diagnostics**: Enhanced conservation monitoring

### Advanced Features

1. **Adaptive quadrature**: For high-order moments
2. **Moment hierarchy solver**: Couple moment evolution equations
3. **Error estimation**: Quantify truncation and discretization errors
4. **Visualization tools**: Plot moment evolution over time

### Research Questions

- How does moment accuracy scale with M?
- What's the optimal moment hierarchy for different physics?
- Can moment-based error indicators guide adaptive refinement?
- How do boundary conditions affect moment conservation?

---

## Code Integration Notes

### Current Structure

- `compute_moment()` in both `1d1v_multistream.py` and `analysis.py`
- Hard-coded first moment calculation
- Manual integration of moment values

### Suggested Refactor

- Create unified `MomentComputer` class
- Support multiple moment types
- Consistent interface between multistream and 2D methods
- Built-in conservation checking and diagnostics

---

## References & Further Reading

- Moment methods for kinetic equations
- Hermite spectral methods for Vlasov equations
- Conservation properties of plasma simulation methods
- Landau damping and moment hierarchy truncation
