---
s:: true
---
---
s:: true
---
---
s:: true
---

### Papers:
- [2DFFT Paper - B. L. Davis.pdf](../../../../PDFs/2DFFT%20Paper%20-%20B.%20L.%20Davis.pdf)
- http://rb.gy/lit36t
- http://rb.gy/ouymo2

## Notes:

Logarithmic spirals polar coordinates:
$$r=r_0 e^{\\theta tan(\\phi)}$$
Where $r$ is the radius, $\\theta$ is the central angle, $r_0$ is the initial radius when $\\theta$ = 0◦ , and −90◦ ≤ $\\phi$ ≤ 90◦ is the pitch angle and $tan(\\phi)=-\\frac{m}{p}$ such that:
$$r=r_0 e^{\\theta\\, \\frac{-m}{p}}$$

### Pitch angle definition:

'Pitch angle is defined as the angle between the line tangent to a circle and the line tangent to a logarithmic spiral at a specified radius'


### Fourier transform in polar coordinates with logarithmic spiral as basis function:
===================================================

Amplitude of each Fourier component,
$$A(p,m) = \\frac{1}{D}\\int_{-\\pi}^{\\pi}\\int_{r_{min}}^{r_{max}}I(u,\\theta)e^{i(m\\theta + pu)}\\;dud\\theta$$
where $u ≡ ln \\,r$, $r$ (radius) and $\\theta$ (central angle) are in polar coordinates, $r_{min}$ is the inner radius, $r_{max}$ is the outer radius of the user-defined calculation annulus, and $D$ is a normalization factor written as:
$$D =\\int_{-\\pi}^{\\pi}\\int_{r_{min}}^{r_{max}}I(u,\\theta)\\;dud\\theta$$
$I(u, \\theta)$ is the distribution of light of a given de-projected galaxy, in a $(u, \\theta)$ plane, $m$ represents the number of arms or harmonic modes, and $p$ is the variable associated with the pitch angle $(\\phi)$, defined by;
$$tan(\\phi) = \\frac{-m}{p_{max}}$$

[One of the main measurements in this is knowing the inner and outer radius - could we use bulge arm decomposition to define the beginning of the arm?]

### Making these functions discrete:

Amplitude of each Fourier component,
$$A(p,m) = \\frac{1}{D}\\sum_{-\\pi}^{\\pi}\\sum_{r_{min}}^{r_{max}}I(u,\\theta)e^{i(m\\theta + pu)}\\;dud\\theta$$
Where, $I(u,\\theta)$ represents the image transformed into ($ln(r), \\theta$) representation $D$ becomes the sum of the image:
$$A(p,m) = \\frac{1}{\\sum I(u,\\theta)}\\sum_{-\\pi}^{\\pi}\\sum_{r_{min}}^{r_{max}}I(u,\\theta)e^{i(m\\theta + pu)}\\;dud\\theta$$
$m$ stays fixed for each mode so we require a plot of $A(p)$ for each $m$.

### $r_{min} \\rightarrow r_{max}$ estimations:

Can set $r_{max}$ as `np.max(np.hypot(*Image.shape)/2` as this half the diagonal distance through the image, this should be enough. [Ask Steven if this is okay].
Need an estimate of $r_{min}$ so that we mask out bulge and bar in galaxies where they are present.

| Galaxy Type | $r_{min}$ mask radius ($R_{e}$) |
|-------------|---------------------|
| Sa          | 10%           |
| Sb          | 15%            |
| Sc          | 15%       |
| SBa         | 25%            |
| SBb         | 20%            |
| SBc         | 17.5%         |

Based on the Hubble tuning Fork:
![Pasted image 20230321122623.png](../../../../AA%20%20-%20%20Assets/Pasted%20image%2020230321122623.png)


Trying to work out how PA works
===============================================================

![Pasted image 20230320130238.png](../../../../AA%20%20-%20%20Assets/Pasted%20image%2020230320130238.png)

$\\delta = \\phi - \\theta$ 

===============================================================

### Want to think about the way that $PA$ and $q$ relate to the transformation

Standard transformation finds $R,\\theta$ from $x,y$ :

$$R = \\sqrt{x_{i}^2 + y_{j}^2} $$
$$\\theta = arctan(x_i/y_j)$$
let $PA = \\phi \\therefore$ from above diagram $\\delta = \\phi - \\theta$,
At $\\phi = 0$ the galaxy semi-major axis is aligned to North (vertical in the image) $\\therefore$ $\\phi = \\pi/2$ for aligned along x-axis. 

To find the transformation to $R,\\theta$ incorporating $b/a$ assuming galaxy $\\phi = \\pi/2$  (assuming Steven shows us a way from getting from q to b/a):
$$R = \\sqrt{\\bigg(\\frac{x_{i}}{a}\\bigg)^2 + \\bigg(\\frac{y_{j}}{b}\\bigg)^2}$$
$$\\theta = arctan(x_i/y_j)$$
To find the transformation to $R,\\theta$ incorporating $b/a$ and $\\phi$, the ellipse factors $b$ and $a$ need to swap at $0$ and $\\pi$.
$$R = \\sqrt{sin(\\delta) \\bigg(\\frac{x_{i}}{a}\\bigg)^2 + cos(\\delta) \\bigg(\\frac{y_{j}}{b}\\bigg)^2}$$
or is it:
$$R = \\sqrt{\\bigg(\\frac{sin(\\delta)\\,x_{i}}{a}\\bigg)^2 +  \\bigg(\\frac{ cos(\\delta) \\, y_{j}}{b}\\bigg)^2}$$
Feel like it is probably this one...

Test case of $\\phi = \\pi/4, \\theta = \\pi/2 \\therefore \\delta = \\pi/4$ :
$$R = \\sqrt{\\bigg(\\frac{sin(\\delta)\\,x_{i}}{a}\\bigg)^2 +  \\bigg(\\frac{ cos(\\delta) \\, y_{j}}{b}\\bigg)^2}$$

Want to come up with a polar coordinates 2dfft with a logarithmic spiral basis function instead of sinusoids. 

## Asking AI:
===============================================================
## Question:

Can you do a Discrete Fourier Transform with a logarithmic spiral as a basis function?

## Answer:

Yes, it is possible to perform a discrete Fourier transform using a logarithmic spiral as a basis function. This type of transform is sometimes referred to as the Logarithmic Fourier Transform (LFT) or the Spiral Fourier Transform (SFT).

The basic idea behind the LFT is to use the logarithmic spiral as a basis function instead of the sinusoids used in the standard DFT. The logarithmic spiral is defined by the equation:
$$r = a e^{b\\theta}$$
where r is the radius, θ is the angle, and a and b are constants that control the shape of the spiral.

To perform the LFT, we first define a set of discrete points on the logarithmic spiral by sampling the spiral at regularly spaced angles. Let the number of points be $N$, and let the angles be given by:
$$\\theta_k = 2\\pi \\frac{k}{N}$$
where $k = 0, 1, ..., N-1$. Then, the kth basis function of the LFT is given by:
$$f_k(n) = e^{j\\theta_{kn}}\\; r(n)$$
where $j$ is the imaginary unit, and $r(n)$ is the radius of the spiral at the nth time point.

To compute the LFT coefficients of a signal $x(n)$, we can use the formula:
$$X(k) = \\sum_{n=0}^{N-1} x(n) \\,f_k(n)$$
where $k = 0, 1, ..., N-1$. This formula is similar to the standard DFT formula, but with the logarithmic spiral basis functions substituted in for the sinusoids.

The LFT can be useful in some applications where the signals being analysed have a spiral structure or exhibit rotational symmetry. 

## Translating to discrete code:
=============================================================

`X[k] = np.dot(x, np.conj(np.roll(spiral_basis, k)))` performs the Spiral Fourier Transform (SFT) of the input signal `x` using the logarithmic spiral basis function `spiral_basis`.

To understand how this line works, let's break it down:

-   `np.roll(spiral_basis, k)` shifts the spiral basis function `spiral_basis` by `k` elements. This is equivalent to multiplying the spiral by `e^{ik\\theta}` and rotating it in the complex plane by an angle `k\\theta`.
-   `np.conj` takes the complex conjugate of the rolled spiral basis.
-   `np.dot(x, ...)` performs the dot product of the input signal `x` with the rolled and conjugated spiral basis. This calculates the inner product of the signal with the rotated and scaled basis function at each point in the signal.
-   The result of the dot product is a complex number, which represents the contribution of the `k`-th basis function to the SFT of the input signal.
-   This result is stored in the `X` array, which contains the SFT coefficients for each basis function.

By performing this operation for each value of `k`, we can compute the SFT of the input signal with respect to the logarithmic spiral basis.
