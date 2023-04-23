---
s:: true
---
---
s:: true
---
---
s:: true
---
```run-python
from functools import partial

  

import jax

from jax import numpy as jnp

from jax.scipy.special import gammainc, gammaln

  

import gax

from gax.model import asymmetry, convolve_func, func_to_pix, rp_from_pix

  

# Should the centre of the Sérsic profile be softened?

soft = False

# Radius for softening, in units of the (non-oversampled) pixel size

soft_r_min = 0.1

  
  

def _bn_approx_high(n):

    """Calculate an approximate value of bn valid for `n` > 0.5.

  

    Uses the approximation from Ciotti and Bertin (1999A&A...352..447C).

  

    Compatible with `jax.jit`.

    """

    x = (

        2 * n

        - 1 / 3

        + 4 / (405 * n)

        + 46 / (25515 * n**2)

        + 131 / (1148175 * n**3)

        - 2194697 / (30690717750.0 * n**4)

    )

    return x

  
  

def _bn_approx_low(n):

    """Calculate an approximate value of bn valid for 0.01 < `n` < 0.5.

  

    Uses an polynomial approximation fit to accurate values of bn for 0.01 < n < 0.5.

  

    Compatible with `jax.jit`.

    """

    coeffs = jnp.array(

        [

            1.15205926e03,

            -2.24625160e03,

            1.75367589e03,

            -6.86264989e02,

            1.31394847e02,

            -6.28463389e00,

            5.28056265e-02,

            5.93745234e-04,

        ]

    )

    m = len(coeffs)

    p = 0

    for i in range(m):

        p += coeffs[i] * n ** (m - 1 - i)

    return jnp.clip(p, a_min=1e-4)

  
  

def _bn_approx(n):

    """Calculate an approximate value of bn valid for `n` > 0.01.

  

    Uses `_bn_approx_high` for n > 0.5 and `_bn_approx_low` otherwise.

  

    Compatible with `jax.jit`.

    """

    return jnp.where(n > 0.5, _bn_approx_high(n), _bn_approx_low(n))

  
  

def _f(x, n):

    """This function is zero where x = bn for a given n."""

    return (gammainc(2.0 * n, x) - 0.5) ** 2

  
  

_df = jax.grad(_f)

_d2f = jax.grad(_df)

_d3f = jax.grad(_d2f)

  
  

def _bn_halley(n):

    """Calculate an accurate value of bn.

  

    Initial approximation refined by Halley's method.

    Accurate to absolute error better than 1e-5 for n >= 0.1.

  

    Compatible with `jax.jit`.

    """

    x = _bn_approx(n)

    d = _df(x, n)

    d2 = _d2f(x, n)

    d3 = _d3f(x, n)

    return x - 2 * d * d2 / (2 * d2**2 - d * d3)

  
  

def bn(n):

    """Calculate the bn constant for the Sérsic profile function.

  

    The returned value is accurate to an absolute error < 1e-4 for `n` > 0.01.

  

    Compatible with `jax.jit`. For an input array of 1000 n values, takes only ~100 µs.

  

    Parameters

    ----------

    n : array like of floats

        Sérsic indexes.

  

    Returns

    -------

    float

        The corresponding values of bn.

    """

    b = jax.lax.cond(n > 2.5, _bn_approx, _bn_halley, n)

    return jnp.where(n < 0.1, jnp.nan, b)

  
  

def sersic_1d_linear_hard_centre(r, flux, re, n):

    Ie = sersic_Ie_from_lum(flux, re, n)

    return Ie * jnp.exp(-bn(n) * ((r / re) ** (1 / n) - 1))

  
  

def sersic_1d_linear_soft_centre(r, flux, re, n):

    # remove peak

    r_clip = jnp.clip(r, a_min=soft_r_min)

    clipped_flux = sersic_1d_linear_hard_centre(r_clip, flux, re, n)

    # calculate missing flux

    flux_min = sersic_1d_linear_hard_centre(soft_r_min, flux, re, n)

    Ie = sersic_Ie_from_lum(flux, re, n)

    missing_lum = (

        sersic_enc_lum_linear(soft_r_min, Ie, re, n)

        - flux_min * jnp.pi * soft_r_min**2

    )

    norm = missing_lum * 2.0 / (jnp.pi * soft_r_min**2)

    # spread missing flux out over central region

    missing_flux = jnp.where(r <= soft_r_min, norm * (1 - (r / soft_r_min) ** 2), 0)

    return clipped_flux + missing_flux

  
  

def sersic_1d_linear(r, flux, re, n):

    return jax.lax.cond(

        soft, sersic_1d_linear_soft_centre, sersic_1d_linear_hard_centre, r, flux, re, n

    )

  
  

def sersic_pars_log_to_linear(mag, log_re, log_n):

    flux = 10 ** (-0.4 * mag)

    re = 10**log_re

    n = 10**log_n

    return flux, re, n

  
  

def sersic_1d(r, mag, log_re, log_n):

    pars = sersic_pars_log_to_linear(mag, log_re, log_n)

    return sersic_1d_linear(r, *pars)

  
  

def sersic_Ie_from_lum(flux, re, n):

    return flux / sersic_lum_linear(1, re, n)

  
  

def sersic_lum_linear(Ie, re, n):

    b = bn(n)

    g2n = jnp.exp(gammaln(2 * n))

    return Ie * re**2 * 2 * jnp.pi * n * jnp.exp(b) / (b ** (2 * n)) * g2n

  
  

def sersic_lum(mu_e, log_re, log_n):

    pars = sersic_pars_log_to_linear(mu_e, log_re, log_n)

    return sersic_lum_linear(*pars)

  
  

def sersic_enc_lum_linear(r, Ie, re, n):

    x = bn(n) * (r / re) ** (1 / n)

    return sersic_lum_linear(Ie, re, n) * gammainc(2 * n, x)

  
  

def sersic_enc_lum(r, mu_e, log_re, log_n):

    pars = sersic_pars_log_to_linear(mu_e, log_re, log_n)

    return sersic_enc_lum_linear(r, *pars)

  
  

def sersic_2d_linear(i, j, flux, re, n, x, y, q, theta):

    flux = flux / q

    iy = i - y

    jx = j - x

    rp = rp_from_pix(iy, jx, q, theta)

    return sersic_1d_linear(rp, flux, re, n)

  
  

def sersic_2d(i, j, mag, log_re, log_n, x, y, q, theta):

    pars = sersic_pars_log_to_linear(mag, log_re, log_n)

    pars = pars + (x, y, q, theta)

    return sersic_2d_linear(i, j, *pars)

  
  

def sersic_2d_asym_linear(i, j, flux, re, n, x, y, q, theta, asym_strength, asym_angle):

    flux = sersic_2d_linear(i, j, flux, re, n, x, y, q, theta)

    asym = asymmetry(i, j, x, y, theta, asym_strength, asym_angle)

    return flux * asym

  
  

def sersic_2d_asym(i, j, mag, log_re, log_n, x, y, q, theta, asym_strength, asym_angle):

    flux = sersic_2d(i, j, mag, log_re, log_n, x, y, q, theta)

    asym = asymmetry(i, j, x, y, theta, asym_strength, asym_angle)

    return flux * asym

  
  

def sersic_2d_pix(pars, size, order, oversamp=1, keep_oversampling=True):

    return func_to_pix(sersic_2d, pars, size, order, oversamp, keep_oversampling)

  
  

def sersic_2d_linear_pix(pars, size, order, oversamp=1, keep_oversampling=True):

    return func_to_pix(sersic_2d_linear, pars, size, order, oversamp, keep_oversampling)

  
  

def sersic_2d_asym_pix(pars, size, order, oversamp=1, keep_oversampling=True):

    return func_to_pix(sersic_2d_asym, pars, size, order, oversamp, keep_oversampling)

  
  

convolved_sersic_2d = jax.jit(

    partial(convolve_func, sersic_2d),

    static_argnames=["size", "psf_oversamp", "order", "fft"],

)
```

## General Description: