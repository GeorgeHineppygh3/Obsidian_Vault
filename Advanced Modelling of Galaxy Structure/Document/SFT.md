---
s:: true
---
---
s:: true
---
---
s:: true
---
## Links:
- [Creating Spiral fourier transform](../Code/Code%20description/2Dfft/Creating%20Spiral%20fourier%20transform.md)
- [ISFT and SN - working book](../Code/Code%20description/2Dfft/ISFT%20and%20SN%20-%20working%20book.md)
- 

## Sources:
- [2DFFT Paper - B. L. Davis.pdf](../../PDFs/2DFFT%20Paper%20-%20B.%20L.%20Davis.pdf)
- http://rb.gy/lit36t
- http://rb.gy/ouymo2

## Bibtex references:
```
@article{davis2012measurement,
  title={Measurement of galactic logarithmic spiral arm pitch angle using two-dimensional fast Fourier transform decomposition},
  author={Davis, Benjamin L and Berrier, Joel C and Shields, Douglas W and Kennefick, Julia and Kennefick, Daniel and Seigar, Marc S and Lacy, Claud HS and Puerari, Iv{\\^a}nio},
  journal={The Astrophysical Journal Supplement Series},
  volume={199},
  number={2},
  pages={33},
  year={2012},
  publisher={IOP Publishing}
}

@article{puerari1992fourier,
  title={Fourier analysis of structure in spiral galaxies},
  author={Puerari, I and Dottori, HA},
  journal={Astronomy and Astrophysics Supplement Series (ISSN 0365-0138), vol. 93, no. 3, June 1992, p. 469-493. Research supported by CNPq and FINEP.},
  volume={93},
  pages={469--493},
  year={1992}
}

@article{saraiva1994distribution,
  title={The distribution of light in the spiral galaxy NGC 7412.},
  author={Saraiva Schroeder, MF and Pastoriza, MG and Kepler, SO and Puerari, I},
  journal={Astronomy and Astrophysics Supplement Series},
  volume={108},
  pages={41--54},
  year={1994}
}
```

## Figures:
- ![Pasted image 20230401124517.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230401124517.png)
- ![Pasted image 20230401124525.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230401124525.png)
- ![Pasted image 20230401124534.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230401124534.png)
- ![Pasted image 20230401131351.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230401131351.png)



## What has been done?
===============================================================

- Used the system of 2D Fast Fourier Transform originally from the 'FOURN routine from Numerical Recipes in C'  - (Press et al. 1989)
- This method 'does not assume that observed spiral structures are logarithmic. It only decomposes the observed distributions into a superposition of logarithmic spirals of different pitch angles and number of arms, which can be thought of as building blocks.'  -  Considere & Athanassoula (1988)
- The existing methods use older computational techniques and so instead uses the maths from Davis, Puerari and Schroeder to create a python version

## Maths:
===============================================================

Logarithmic spirals polar coordinates:
$$r=r_0 \\,e^{\\theta \\,tan(\\phi)}$$
Where $r$ is the radius, $\\theta$ is the central angle, $r_0$ is the initial radius when $\\theta$ = 0◦ , and −90◦ ≤ $\\phi$ ≤ 90◦ is the pitch angle and $tan(\\phi)=-\\frac{m}{p}$ such that:
$$r=r_0 e^{\\theta\\, \\frac{-m}{p}}$$

### Pitch angle definition:

'Pitch angle is defined as the angle between the line tangent to a circle and the line tangent to a logarithmic spiral at a specified radius'

#### Spiral Power spectrum

Amplitude of each Fourier component,
$$A(p,m) = \\frac{1}{D}\\int_{-\\pi}^{\\pi}\\int_{r_{min}}^{r_{max}}I(u,\\theta)e^{i(m\\theta + pu)}\\;dud\\theta$$
where $u ≡ ln \\,r$, $r$ (radius) and $\\theta$ (central angle) are in polar coordinates, $r_{min}$ is the inner radius, $r_{max}$ is the outer radius of the user-defined calculation annulus, and $D$ is a normalization factor written as:
$$D =\\int_{-\\pi}^{\\pi}\\int_{r_{min}}^{r_{max}}I(u,\\theta)\\;dud\\theta$$
$I(u, \\theta)$ is the distribution of light of a given de-projected galaxy, in a $(u, \\theta)$ plane, $m$ represents the number of arms or harmonic modes, and $p$ is the variable associated with the pitch angle $(\\phi)$, defined by;
$$tan(\\phi) = \\frac{-m}{p_{max}}$$
Where $p_{max}$ is the value with the highest amplitude ($|A(p,m)|$) for a given harmonic mode, $m$,  the argument of the complex component $A(p_{max},m)$ defines the phase angle, $\\Phi$, of the orientation of the spiral pattern. 

## Python SFT:
===============================================================


### Deprojection:
[does this need the matrices for deprojection?]

In order to process the image array into \\ref{eqn:Fourier} in $I(u,\\theta)$ form; the galaxy must first be de-projected and processed to $I(r, \\theta)$ form and then sampled logarithmically. The deprojection follows a series of three affine transformations: rotation by position angle, stretch according to axis ratio and rotation and conversion to polar coordinates. 

The transformations are applied to a set of image of $ln(r),\\, \\theta$ indices defined between the inner radius and closest image edge to the centre to ensure no pixels are sampled from outside the image bounds. The inner radius is taken as a multiple of the effective radius with criteria that the locus must fully contain the bulge and bar when present/necessary [come back to this when sure].

#### Regular Grid interpolation:

After applying the transformations to the image indices regular grid interpolation is applied to a masked set of co-ordinates where $0<x,y<$`img.shape[:2]`, which sample the original image to create an image array in the form $u,\\theta$. 

![Pasted image 20230401121238.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230401121238.png)
Caption:


#### Fourier Transform:

With the image array in the log polar format the Fourier transform can be applied by summing across the image indices multiplied by the complex spiral weight function for each $p$ value for a given $m$. The spiral weight function takes the form:
$$w_{i,j} = e^{i(m\\theta \\,+ \\,ln(r)\\, p)}$$
Creating a discrete form of \\ref{eqn:Fourier} in terms of the image indices $i,j$ 
$$|A(p,m)| = \\frac{1}{D} \\left| \\sum_{i,j} I(u,\\theta)_{i,j} \\,w_{i,j} \\right|$$

[come back to this not sure on the discretisation]

Where $p_{max}$ can be identified from the maximum of the power spectrum $|A(p,m)|$ ultimately leading to the winding angle, $\\psi$, using equation \\ref{eqn:winding_p}.

![Pasted image 20230401124415.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230401124415.png)
Caption:

The code also calculates the dominant harmonic mode $m$ by calculating $|A(p_{max},m)|$  for $0<m<6$ and selecting  the largest amplitude.  

![Pasted image 20230401131339.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230401131339.png)
Caption:

The $S/N$, for each spectrum, is given by the expression:
$$\\frac{S}{N} = (|A(p,m)|_{max} - L)/\\sigma$$

where $A(p, m) _{max}$ is the maximum amplitude of the Fourier coefficients, $L$ is the mean level out of the main peak and $\\sigma$ is an rms estimate of the spectrum given by:
$$\\sigma^2 = \\langle(|A(p,m)|-L)^2\\rangle$$ 

===============================================================