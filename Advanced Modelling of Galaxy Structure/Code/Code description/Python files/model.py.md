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

import numpy as np

from jax import numpy as jnp

from jax.scipy.signal import convolve

from jax.tree_util import Partial

  

from .fftconvolve import fftconv2d

from .integration import (

    gauss_legendre_tensor_integration,

    get_ij,

    integrate_with_subpixel_refinement,

)

  
  

def rp_from_pix(iy, jx, q, theta):

    # Returns radial coordinates for pixel indices

    ct = jnp.cos(-theta)

    st = jnp.sin(-theta)

    return jnp.sqrt((iy * ct + jx * st) ** 2 / q**2 + (-iy * st + jx * ct) ** 2)

  
  

def asymmetry(i, j, x, y, theta, asym_strength, asym_angle):

    cos_theta, sin_theta = jnp.cos(theta), jnp.sin(theta)

    ix = i - x

    jy = j - y

    x_maj = ix * cos_theta + jy * sin_theta

    x_min = -ix * sin_theta + jy * cos_theta

    eps = 1e-32

    angle = jnp.arctan(x_maj / (x_min + eps))

    angle += jnp.pi * (x_min < 0) - jnp.pi / 2

    angle = jnp.where(jnp.isnan(angle), 0, angle)

    asym = 1 - asym_strength * jnp.cos(asym_angle - angle)

    return asym

  
  

def func_to_pix(

    func, pars, size, order, oversamp=1, keep_oversampling=True, adaptive=True

):

    """Render profiles on a regularly sampled pixel grid.

  

    Compatible with `jax.jit` using

    `static_argnames=("size", "order", "oversamp", "keep_oversampling")`,

    as long as `func` is also `jax.jit` compatible.

  

    Parameters

    ----------

    func : callable

        A python function with signature `(i, j, **pars)`, where `i` and `j` are the

        coordinates at which to evaluate the profile. `i=j=0` is defined as the centre

        of the image. `i` corresponds to the (vertical) y-axis and `j` corresponds to

        the (horizontal) x-axis.

    pars : dict of floats or JAX DeviceArrays (a JAX "pytree")

        Parameters defining one or more profiles. The keys must match the parameter

        argument names of `func`.

    size : tuple of two ints

        The shape of the output image.

    order : int

        The integration order to use.

    oversamp : int

        The oversampling factor to apply to `size`.

    keep_oversampling : bool

        Should the oversampling be kept in the returned image. If `False`, then the

        output image is down-sampled to `size`.

    adaptive: bool

        Should adaptive integration (with subpixel refinement) be used.

  

    Returns

    -------

    JAX DeviceArray

        The rendered image.

    """

    ij = get_ij(size, oversamp)

    pars = jax.tree_util.tree_map(jnp.atleast_1d, pars)

    if adaptive:

        int_func = Partial(

            integrate_with_subpixel_refinement,

            func,

            order=order,

            base_oversamp=oversamp,

        )

    else:

        int_func = Partial(

            gauss_legendre_tensor_integration, func, order=order, oversamp=oversamp

        )

    img = multi_func(int_func, ij, pars)

    if not keep_oversampling and oversamp != 1:

        img = downsample(img, oversamp)

    return img

  
  

def pars_table_to_pytree(pars):

    """Convert an AstroPy Table of parameters to a JAX pytree"""

    return {c: jnp.asarray(pars[c]) for c in pars.columns}

  
  

def multi_func(func, ij, pars):

    """Compute a sum of multiple profiles in a JAX-efficient manner."""

    i, j = ij

    init = jnp.zeros(i.shape)

    n_func = len(next(iter(pars.values())))

  

    def sum_func(k, x):

        pk = {p: pars[p][k] for p in pars}

        return x + func(i=i, j=j, pars=pk)

  

    return jax.lax.fori_loop(0, n_func, sum_func, init)

  
  

def downsample(img, oversamp):

    n1, n2 = img.shape

    img = img.reshape((n1, n2 // oversamp, oversamp)).sum(-1).T

    img = img.reshape((n2 // oversamp, n1 // oversamp, oversamp)).sum(-1).T

    return img

  
  

def convolve_func(func, pars, size, psf, psf_oversamp, order, fft=True):

    # If the psf has even size, then the convolution introduces a shift

    # of half a psf-oversampled pixel. We can move the centres of all

    # sources to counteract this.

    pars = pars.copy()

    pad_y, pad_x = np.floor_divide(psf.shape, 2)

    padding = [pad_y, pad_y](pad_y,%20pad_y.md)

    if psf.shape[0] % 2 == 0:

        pars["y"] = pars["y"] - 0.5 / psf_oversamp

        padding[0][1] -= 1

    if psf.shape[1] % 2 == 0:

        pars["x"] = pars["x"] - 0.5 / psf_oversamp

        padding[1][1] -= 1

    img = func_to_pix(func, pars, size, order, psf_oversamp)

    img = jnp.pad(img, padding, mode="linear_ramp")

    if fft:

        conv = fftconv2d

    else:

        conv = convolve

    img = conv(img, psf, mode="valid")

    img = downsample(img, psf_oversamp)

    return img
```

## General Description: