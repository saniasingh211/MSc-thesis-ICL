# July 25- edits+ questions

- initial parameters
- velocity distribution for 2d and 1d files- look at them, understand it for the 2d file
- 2d file uses a continuum approach
- translate this to my "streams" code
- Draw comparisons

---

my job: make sure the initial parameters are the same for both codes, especially after I interpolate it onto the mesh.

Think about the velocity profile: before and after interpolation

The PDF colin talked about, and how the distribution function should change after that.

---

To compare the moments meaningfully, both codes need to represent the same initial velocity distribution.

- First code has discrete velocity: 4 bins
- Second code: continuous distribution

My job: to make sure these both use the same initial velocity distribution. Idea- choosing one reference distribution, and letting both codes approximate that.

next: think about getting time derivative of moments.

if the moment is conserved, this means $\frac{d}{dt}M(x,t) = 0.$

- check this and see if it works!

$\delta(v-v_i) \approx (1/\sqrt{2\pi\sigma^2}) \exp(-(v-v_i)^2/(2\sigma^2))$

$\delta(v-v_i) \approx 1/\Delta v$ if $|v-v_i| < \Delta v/2$, else 0

- replace dirac delta with gaussian maybe to run tests?
