---
s:: true
---
---
s:: true
---
---
s:: true
---


Key:
- [SS] - See Steven
- [CB] - Come Back


Cell by Cell Breakdown
===============================================================

**Testing JAX integration**

This notebook compares approaches to the problem of integrating image pixels.
The conclusion is that adaptive subpixel refinement is essential for correctly rendering Sérsic profiles accurately and quickly.
To make this approach fast with Jax, we need to define a fixed number of pixels to refine at each level of oversampling.

```run-python
import jax

from jax import jit

from jax import numpy as jnp

from jax.tree_util import Partial

from jax.experimental import checkify

import numpy as np

import logging

from scipy.integrate import dblquad

from scipy.special import roots_legendre

from functools import partial

from codetiming import Timer

from gax.integration import roots_clencurt

from gax import sersic, model

from matplotlib import pyplot as plt
```

- Imports cell

```run-python
logging.basicConfig()

logger = logging.getLogger("test")

logger.setLevel(logging.DEBUG)
```

- debugging and utilities cell 

```run-python
jax.config.update("jax_enable_x64", True)
```

- set jax to x64 not sure why [SS]

```run-python
%load_ext memory_profiler
```

- no idea [SS]

```run-python
size = np.array((90, 100))
```

- creates an array called size (90, 100)

```run-python
galpars = dict(mag=-7.5, log_re=0.9, log_n=0.7, x=0.2, y=0.3, q=0.1, theta=0.1)
```

-  creates a dictionary of parameters of galaxies

```run-python
ij = jnp.indices(size)

ij = (ij.T - (size - 1) / 2.0).T

i, j = ij
```

- imagine i and j are array indices for images

```run-python
ij
```

-  prints array indices array

```run-python
@jit

def func(i, j, pars):

    return sersic.sersic_2d(i, j, **pars)
```

- Would imagine this jits the function sersic 2d acting on the galaxy pars dictionary and array indices

```run-python
func(0, 0, galpars)
```

- Runs function on galaxy pars dictionary returns $\\sim$ 39

```run-python
@partial(jax.jit, static_argnames=["f"])

def integrate_pixels(f, i, j, pars, di, dj, w):

    init = jnp.zeros(i.shape)

    int_func = lambda k, x: x + w[k] * f(i + di[k], j + dj[k], pars)

    return jax.lax.fori_loop(0, len(w), int_func, init)

  

@partial(jax.jit, static_argnames=["f"])

def tensor_integrate_pixels(f, i, j, pars, d, w, oversamp=1):

    d = 0.5 * d / oversamp

    di = jnp.repeat(d, len(d))

    dj = jnp.tile(d, len(d))

    w = 0.5 * w / oversamp

    w = jnp.outer(w, w).flatten()

    return integrate_pixels(f, i, j, pars, di, dj, w)
```


This function makes use of the func tools partial function module - don't know hat this is [SS]
-  cell defines two functions:
	- `integrate_pixels`
		- function appears to run integration on given pixel from array indices
		- function returns a vectorised for loop which runs the length of w - assuming w is related to the size of the flattened array for the image
	- `tensor_integrate_pixels`
		- function appears to run tensor integration on given pixels form array indices
		- the function appears to run the integrate pixels and calculate the di and dj inputs from the array indices and the oversampling

```run-python
@partial(jax.jit, static_argnames=["f", "order"])

def gauss_legendre_tensor_integration(f, i, j, pars, order):

    d, w = roots_legendre(order)

    return tensor_integrate_pixels(f, i, j, pars, d, w)
```

- function again makes use of the partial library form functools
- function runs tensor integration function and calculates the inputs d and w usin the gauss legendre roots
- the function then returns the integrated pixels using the gauss legendre roots

```run-python
def clencurt_tensor_integration(f, i, j, pars, order):

    d, w = roots_clencurt(order)

    return tensor_integrate_pixels(f, i, j, pars, d, w)
```

- The  function is the same as above except finds weights d and w from the clencurt method calling the function from [integration.py](../Python%20files/integration.py.md)

```run-python
def oversampled_integration(f, i, j, pars, order):

    d = (2*jnp.arange(order) + 1)/order - 1

    w = 2 * jnp.ones(order)/order

    return tensor_integrate_pixels(f, i, j, pars, d, w)
```

- The cell defines the function which takes the order of the oversampling and calculates the weights d and w to then be input into there tensor integration function

```run-python
G7_nodes = jnp.array([0.000000000000000000000000000000000e+00,

                      -4.058451513773971669066064120769615e-01,

                      4.058451513773971669066064120769615e-01,

                      -7.415311855993944398638647732807884e-01,

                      7.415311855993944398638647732807884e-01,

                      -9.491079123427585245261896840478513e-01,

                      9.491079123427585245261896840478513e-01])

  

G7_weights = jnp.array([4.179591836734693877551020408163265e-01,

                        3.818300505051189449503697754889751e-01,

                        3.818300505051189449503697754889751e-01,

                        2.797053914892766679014677714237796e-01,

                        2.797053914892766679014677714237796e-01,

                        1.294849661688696932706114326790820e-01,

                        1.294849661688696932706114326790820e-01])

  

K15_nonG7_nodes = jnp.array([-2.077849550078984676006894037732449e-01,

                             2.077849550078984676006894037732449e-01,

                             -5.860872354676911302941448382587296e-01,

                             5.860872354676911302941448382587296e-01,

                             -8.648644233597690727897127886409262e-01,

                             8.648644233597690727897127886409262e-01,

                             -9.914553711208126392068546975263285e-01,

                             9.914553711208126392068546975263285e-01])

  

K15_nonG7_weights = jnp.array([2.044329400752988924141619992346491e-01,

                               2.044329400752988924141619992346491e-01,

                               1.690047266392679028265834265985503e-01,

                               1.690047266392679028265834265985503e-01,

                               1.047900103222501838398763225415180e-01,

                               1.047900103222501838398763225415180e-01,

                               2.293532201052922496373200805896959e-02,

                               2.293532201052922496373200805896959e-02])

  

K15_G7_weights = jnp.array([2.094821410847278280129991748917143e-01,

                            1.903505780647854099132564024210137e-01,

                            1.903505780647854099132564024210137e-01,

                            1.406532597155259187451895905102379e-01,

                            1.406532597155259187451895905102379e-01,

                            6.309209262997855329070066318920429e-02,

                            6.309209262997855329070066318920429e-02])

  

K15_nodes = jnp.concatenate((G7_nodes, K15_nonG7_nodes))

K15_weights = jnp.concatenate((K15_G7_weights, K15_nonG7_weights))
```

- Cell defines sets of weights from arrays and then concatenates them into larger parent arrays 

```run-python
G7_2d_nodes = 0.5 * jnp.array((jnp.repeat(G7_nodes, 7), jnp.tile(G7_nodes, 7)))

G7_2d_weights = 0.25 * jnp.outer(G7_weights, G7_weights).flatten()

%time int_G7 = integrate_pixels(func, i, j, galpars, *G7_2d_nodes, G7_2d_weights)
```

- Cell collects and tiles together the nodes and weights (G7) into '2D' arrays 
- [SS] - Need to know what a node and a wight are - how they differ and what they are for
- Cell then times running the integrate pixels using the nodes and weights as inputs di,dj and w to the integrate pixels function


```run-python
K15_2d_nodes = 0.5 * jnp.array((jnp.repeat(K15_nodes, 15), jnp.tile(K15_nodes, 15)))

K15_2d_weights = 0.25 * jnp.outer(K15_weights, K15_weights).flatten()

%time int_K15 = integrate_pixels(func, i, j, galpars, *K15_2d_nodes, K15_2d_weights)
```

- Cell collects and tiles together the nodes and weights (K15) into '2D' arrays 
- [SS] - Need to know what a node and a wight are - how they differ and what they are for
- Cell then times running the integrate pixels using the nodes and weights as inputs di,dj and w to the integrate pixels function

```run-python
K15_new_2d_nodes = 0.5 * jnp.array([[i, j] for i in G7_nodes for j in K15_nonG7_nodes] +

                                   [[i, j] for i in K15_nonG7_nodes for j in G7_nodes] +

                                   [[i, j] for i in K15_nonG7_nodes for j in K15_nonG7_nodes]).T

K15_new_2d_weights = 0.25 * jnp.array([i * j for i in K15_G7_weights for j in K15_nonG7_weights] +

                                      [i * j for i in K15_nonG7_weights for j in K15_G7_weights] +

                                      [i * j for i in K15_nonG7_weights for j in K15_nonG7_weights]).T

K15_G7_2d_weights = 0.25 * jnp.array([i * j for i in K15_G7_weights for j in K15_G7_weights]).T
```

- No idea what is going on here -[SS]
- appears to create new nodes and weights from the previous arrays and then combine them into one 2d array as was done individually above

```run-python
(jnp.concatenate((K15_G7_2d_weights, K15_new_2d_weights)).sort() == K15_2d_weights.sort()).all()
```

- this cell then checks that the result of combining and sorting the new weights is the same as  the K15 2d array ? - no idea idf this is right [SS]

```run-python
(jnp.concatenate((G7_2d_nodes.T, K15_new_2d_nodes.T)).T.sort() == K15_2d_nodes.sort()).all()
```

- The process of above is repeated with the nodes

```run-python
%time a = gauss_legendre_tensor_integration(func, i, j, galpars, 7)
```

- cell runs the gauss_legendre tensor integration using the 7th order assigning it it to the array `a` - 1.66 s
- Repeat run - 32.9 ms

```run-python 
np.max(abs(int_G7 - a))
```

- cell calculates the maximum difference between the integrate pixels method running with the G7 nodes and weights and finds that it is very small $\\sim 10^{-14}$ 

```run-python
np.max(abs(int_K15 - int_G7))
```

- cell calculates the maximum difference between the integrate pixels method running with the K15 nodes and weights and the G7 nodes and weights - finds that it is large $\\sim 34$ 

```run-python
%time b = clencurt_tensor_integration(func, i, j, galpars, 7)
```

- cell times the clencurt integration method using the 7th order and assigns it it to variable `b` - 1.66s
- second run - 171 ms

## Iterative Oversampling

```run-python
def oversample_pixels(i, j, k, oversamp):

    d = ((jnp.arange(oversamp) + 0.5) / oversamp - 0.5) / oversamp**(k-1)

    oi = (i[..., None] + jnp.repeat(d, len(d))).flatten()

    oj = (j[..., None] + jnp.tile(d, len(d))).flatten()

    return oi, oj
``` 

- cell defines function oversample_pixels
- function appears to create a subset of smaller pixels to oversample from

```run-python
def integrate_with_error(func, i, j, pars, k, order, base_oversamp, oversamp):

    int1 = tensor_integrate_pixels(func, i, j, pars, *roots_legendre(order - 1), base_oversamp * oversamp**k)

    int2 = tensor_integrate_pixels(func, i, j, pars, *roots_legendre(order), base_oversamp * oversamp**k)

    int3 = tensor_integrate_pixels(func, i, j, pars, *roots_clencurt(order), base_oversamp * oversamp**k)

    error1 = jnp.abs(int2 - int1)

    error2 = jnp.abs(int2 - int3)

    error = jnp.maximum(error1, error2)

    return 0.5*(int2 + int3), error
```


- cell defines function integrate with error 
- The function appears to run the integration using the tensor integrate function using the the Legendre methods for a given order and the order below it
- The function also runs the integration using the tensor integration function with the Clencurt method
- The function returns the average of the tensor integration method with Clencurt and gauss methods and also returns the error in the value though the largest difference between the two methods or the legendry method and the Legendre at a lower order method

- Very interesting function want to talk to steven about why this is like this [SS

```run-python
def prepare_subpixel_refinements(func, i, j, pars, base_oversamp=1, order=3, oversamp=3, precision=1e-6, frac_refine=0.1, k_max=5):

    jax.debug.print("Preparing subpixel refinements")

    integrated_pixels, idx_to_refine, n_imprecise, n_to_refine = [], [], [], []

    k = 0

    need_refinement = True

    new_i = i.flatten()

    new_j = j.flatten()

    n_to_refine = int(new_i.size * frac_refine)

    jax.debug.print("n_to_refine={}", n_to_refine)

    while need_refinement and k <= k_max:

        if k > 0:

            idx_to_refine.append(error.argsort()[-n_to_refine:])

            i_to_refine = new_i[idx_to_refine[-1]]

            j_to_refine = new_j[idx_to_refine[-1]]

            new_i, new_j = oversample_pixels(i_to_refine, j_to_refine, k, oversamp)

        new_int_pix, error = integrate_with_error(func, new_i, new_j, pars, k, order, base_oversamp, oversamp)

        integrated_pixels.append(new_int_pix)

        n_imprecise.append((error > precision).sum())

        max_error = error.max()

        need_refinement = n_imprecise[-1] > 0

        jax.debug.print("k={}, n_imprecise={}, max_error={}",

                        k, n_imprecise[-1], max_error)

        k += 1

    return idx_to_refine, integrated_pixels, n_imprecise, n_to_refine
```

- 