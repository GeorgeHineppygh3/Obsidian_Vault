---
s:: true
---
Sérsic Profiles:
$$ln[I(R)] = ln[I_0 - kR^{1/R}]$$ 
Where $I_0$ represents the intensity at $R=0$.
More commonly written:
$$ I(R) = I_e [ - b_n (\\frac{R}{R_e}^\\frac{1}{n}-1) \\big]$$
Where $b_n$ is approximately $2n-\\frac{1}{3}$, $\\gamma(2n;b_n)$, $\\frac{1}{2}\\Gamma(2n)$  (there are many approximations) and $I_e$ represents the intensity at the half light radius $R_e$.

## Sérsic.py functions: 

`EQ1 _bn_approx_high(n):` Approximation taken from [Ciotti and Bertin.pdf](../../../../PDFs/Ciotti%20and%20Bertin.pdf) 

`EQ2 _bn_approx_low(n):` Approximation from Steven's own fit to 0.01 < n < 0.5

`EQ3 _bn_approx(n):` function selects either high or low n approximation given n input

`EQ4 _f(n):` function returns $b_n$ approximation using incomplete gamma function $\\gamma(2n;b_n)$ 
Following this first, second and third order derivatives are taken for following [Halley's method](./Halley's%20method.md) Approximation.

`EQ5  _bn_halley(n):` function employs [Halley's method](./Halley's%20method.md) using previously generated derivatives (average error of $1e^{-5}$ for $n>0.1$ and with jax only takes $\\approx 100 \\mu s$ )

`EQ6  bn(n):`   '`jax.lax.cond`'   applies conditional true false statement for $n>2.5$ on high low combination function and Halley's approximation. Returns $b_n$.

`EQ7  sersic_1d_linear(r, flux, re, n):` Calculates Sérsic intensity from radius

`EQ8 sersic_pars_log_to_linear(mag, log_re, log_n):` Converts parameters for 1D Sérsic function from logarithmic equivalents to linear quantities. 

`EQ9 sersic_1d(r, mag, log_re, log_n):` Calculates Sérsic intensity at radius from logarithmic parameters.

`EQ10 sersic_Ie_from_lum(flux, re, n):` Calculates Intensity at circularised effective radius from flux/luminosity.

`EQ11 sersic_lum(mu_e, log_re, log_n):` Calculates intensity at circularised effective radius from logarithmic quantities.      (I think $\\mu_e$ is logarithmic form of radius)

`EQ12 sersic_enc_lum_linear(r, Ie, re, n):` Calculates `sersic_lum` multiplied by the incomplete gamma function approximation for $b_n$.

`EQ 13 sersic_enc_lum(r, mu_e, log_re, log_n):` Calculates `sersic_enc_lum` from logarithmic quantities.

`EQ 14 rp_from_pix(iy, jx, q, theta):` Calculates radial co-ordinates for pixel indices

`EQ 15 serseic_2d_linear(i, j, flux, re, n, x, y, q, theta):` Calculates Sérsic intensity at 2d position ($x,y$) on image. Position is calculated from an offset of the centre of the shape ($i,j$).

`EQ 16 sersic_2d(i, j, mag, log_re, log_n, x, y, q, theta):` Calculates 2d Sérsic intensity from logarithmic quantities.

`EQ 17 asymmetry(i, j, x, y, theta, asym_strength, asym_angle):` NOT SURE SPEAK TO STEVEN

`EQ 18 sersic_2d_asym_linear(i, j, flux, re, n, x, y, q, theta, asym_strength, asym_angle):` 
Calculates (from linear quantities) based on the asymmetry the flux at a given 2d position on the Sérsic fit.

`EQ 18 sersic_2d_asym(i, j, mag, log_re, log_n, x, y, q, theta, asym_strength, asym_angle):` 
Calculates (from logarithmic quantities) based on the asymmetry the flux at a given 2d position on the Sérsic fit.

`EQ 19 func_to_pix(func, pars, size, oversamp=1, keep_oversampling=True):` Renders profiles on a regularly sampled pixel grid.


FROM HERE ONWARDS I HAVE NO IDEA WHAT IS GOING ON