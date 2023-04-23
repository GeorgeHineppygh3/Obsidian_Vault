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
```run-python
import sys

sys.path.append('..')
``` 

- Move system path to the higher directory

```run-python
import os

os.environ['XLA_PYTHON_CLIENT_PREALLOCATE'] = 'false'
```

- Not sure of this one - something to do with the environment [SS]

```run-python
from gax import sersic

from gax.sersic import sersic_2d_linear_pix

from matplotlib import pyplot as plt

import jax

import jax.numpy as jnp

import astropy

import numpy as np

from astropy.table import Table, vstack
```

- Import modules

```run-python
nx, ny = 500, 500
```

- Set number of pixels for image

```run-python
pars = Table(

        names=["x", "y", "flux", "sersic", "ellip", "pa", "re"],

        rows=[

            [30.90, 71.30, 40000.0, 1.1, 0.4, 16.5, 17.0],

            [220.0, 65.20, 7000.00, 4.0, 0.1, 52.0, 7.50],

            [135.3, 173.6, 5000.00, 2.5, 0.2, 63.5, 3.00],

        ],

    )

  

gax_pars = pars['x', 'y', 'flux', 're']('x',%20'y',%20'flux',%20're'.md)

gax_pars['n'] = pars['sersic']

gax_pars['q'] = 1 - pars['ellip']

gax_pars['theta'] = (90 - pars['pa']) * np.pi / 180

gax_pars['x'] = pars['x'] - (nx - 1) / 2.0 + 1

gax_pars['y'] = pars['y'] - (ny - 1) / 2.0 + 1
```

- Assign the parameters to an astropy Table with three data points in it
- Re assign Table to `gax_pars` Table element with different headers 
- New headers change the values based on the operation
	- Sérsic $\\Rightarrow$ n 
	- ellip $\\Rightarrow$ q
	- pa $\\Rightarrow$ theta
	- x $\\Rightarrow$ x (invert and half for array indexing in image)
	- y $\\Rightarrow$ y (invert and half for array indexing in image)

```run-python
size = jnp.array((nx, ny))

ij = jnp.indices(size)

ij = (ij.T - (size - 1) / 2.0).T
```

- assign Jax array with size of the image
- set the indices to variable
- Unsure on last step [SS]

```run-python
for i in range(5):

    gax_pars = vstack((gax_pars, gax_pars))
```

- Stack Table together to make larger repeating table for testing

```run-python
gax_pars = gax_pars['flux', 're', 'n', 'x', 'y', 'q', 'theta']('flux',%20're',%20'n',%20'x',%20'y',%20'q',%20'theta'.md)
```

- Select columns for parameter table

```run-python
gax_pars
```

- show table

```run-python
p = jnp.asarray([list(p) for p in gax_pars])
```

- Convert astropy object to Jax array

### Simple approach

Create a blank image and loop through sersic parameters,
adding image each time

  

* For 12 profiles in 250x250 image:
    * Without `jit`, first run is 930ms, subsequent runs 40ms
    * With `jit`, first run is 7000ms, subsequent runs 1.8ms

* For 12 profiles in 500x500 image:
    * Without `jit`, first run is 1100ms, subsequent runs 55ms
    * With `jit`, first run is 7800ms, subsequent runs 6ms

* For 24 profiles in 250x250 image:
    * Without `jit`, first run is 950ms, subsequent runs 80ms
    * With `jit`, first run is 17000ms, subsequent runs 3.5ms

* On GPU for 24 profiles in 250x250 image:
    * Without `jit`, first run is 3600ms, subsequent runs 95ms
    * With `jit`, first run is 11000ms, subsequent runs 2.2ms

* On GPU for 96 profiles in 500x500 image:
    * Without `jit`, first run is 3900ms, subsequent runs 390ms
    * With `jit`, first run is 50000ms, subsequent runs 10ms

So, fast repeats, but very expensive to create 'jitted' function, and scales badly with number of profiles.

- Analysis of results summarised above

```run-python
def multi_sersic_2d_linear(ij, multipars):    

    image = jnp.zeros(ij.shape[1:])

    for p in multipars:

        image += sersic.sersic_2d_linear(*ij, *p)

    return image
```

- Defines function to create Sérsic profiles in an image from parameter table
- function then draws from `sersic_2d_linear` from [sersic.py](../Python%20files/sersic.py.md) calling all variables except `ij` and `p` [SS][CB]
- function returns the image with the added profiles

```run-python
%time img1 = multi_sersic_2d_linear(ij, p)
```

- Calls the defined function and times how long it takes - first time run so will be slower

```run-python
plt.imshow(img1)
```

-  Shows the image with generate profiles from timed run
![Pasted image 20230206141517.png](../../../../AA%20%20-%20%20Assets/Pasted%20image%2020230206141517.png)

```run-python
%time multi_sersic_2d_linear(ij, p);
```

- Runs for a second time this time only timing the function - 396s ms
- Runs for a second time - 383 ms  (little change without jit)

```run-python
f = jax.jit(multi_sersic_2d_linear)
```

- Sets up the execution to run though `jit`

```run-python
%time f(ij, p);
```

- Runs function though jit timing the function - 58.9s
- Runs function again through jit - 11.1ms (massive change but very costly jit setup)
- Run again down to - 9.81 ms ± 158 µs per loop


### Using `vmap`

Use vmap to create multiple profiles, then sum.
* For 12 profiles in 250x250 image:
    * Without `jit`, first run is 1400ms, subsequent runs 90ms
    * With `jit`, first run is 700ms, subsequent runs 2.2ms
* For 12 profiles in 500x500 image:
    * Without `jit`, first run is 1650ms, subsequent runs 145ms
    * With `jit`, first run is 700ms, subsequent runs 12ms
* For 24 profiles in 250x250 image:
    * Without `jit`, first run is presumably 1500ms, subsequent runs 100ms
    * With `jit`, first run is 700ms, subsequent runs 11ms
* On GPU for 24 profiles in 250x250 image:
    * Without `jit`, first run is 6600ms (if no previous vmap), subsequent runs 100ms
    * With `jit`, first run is similar (if no previous vmap), subsequent runs 0.4ms
* On GPU for 96 profiles in 500x500 image:
    * Without `jit`, first run is 6300ms (if no previous vmap), subsequent runs 100ms
    * With `jit`, first run is similar (if no previous vmap), subsequent runs 2ms

So, much faster to create 'jitted' function, and fast afterwards, but not quite as quick as simple approach. Probably not helping that sum is outside of `jit`. [SS] - how can this be fixed?

```run-python
ijk = ij[:, None] * np.ones((1, p.shape[0], 1, 1))
```

- expand and reshape size array

```run-python
ijk.shape
```

- demonstrate shape

```run-python
%time img2 = jnp.sum(jax.vmap(sersic.sersic_2d_linear)(*ijk, *p.T), axis=0)
```

- Run function instead using `jax.vmap` timing the run - 3.77s

```run-python 
np.allclose(img1, img2)
```

- function returns true 'Returns True if two arrays are element-wise equal within a tolerance.' no tolerance defined so assuming checking both arrays are the same size [SS]

```run-python
%time jnp.sum(jax.vmap(sersic.sersic_2d_linear)(*ijk, *p.T), axis=0);
```

- Run the function again - 199ms (significantly faster with no jit)

```run-python
f = jax.jit(jax.vmap(sersic.sersic_2d_linear))
```

- create the function with jit compiling

```run-python
%time img3 = jnp.sum(f(*ijk, *p.T), axis=0)
```

- Run timed jit function applying to image - 1.39s
- Second run - 1.78ms

```run-python
%timeit jnp.sum(f(*ijk, *p.T), axis=0)
```

-  run timed function without image application - 1.96 ms ± 15.4 µs per loop

### Using `vmap` and `sum` within `jit`ted function

As above, but do everything withing a function, which can then be `jit` compiled.
* For 12 profiles in 250x250 image:
    * Without `jit`, first run is 1500ms (if no previous vmap), subsequent runs 85ms
    * With `jit`, first run is 770ms, subsequent runs 1.7ms
* For 12 profiles in 500x500 image:
    * Without `jit`, first run is 1500ms (if no previous vmap), subsequent runs 140ms
    * With `jit`, first run is 770ms, subsequent runs 7ms
* For 24 profiles in 250x250 image:
    * Without `jit`, first run is presumably 1700ms (if no previous vmap), subsequent runs 100ms
    * With `jit`, first run is 7000ms, subsequent runs 9ms
* On GPU for 24 profiles in 250x250 image:
    * Without `jit`, first run is 6600ms (if no previous vmap), subsequent runs 90ms
    * With `jit`, first run is similar (if no previous vmap), subsequent runs 0.2ms
* On GPU for 96 profiles in 500x500 image:
    * Without `jit`, first run is 6300ms (if no previous vmap), subsequent runs 90ms
    * With `jit`, first run is similar (if no previous vmap), subsequent runs 1ms

So, fast to create 'jitted' function, and as fast as simple approach afterwards.

```run-python
def multi_sersic_2d_linear_vmap(ij, p):

    ijk = ij[:, None] * jnp.ones((1, p.shape[0], 1, 1))

    s2dl = jax.vmap(sersic.sersic_2d_linear)

    return jnp.sum(s2dl(*ijk, *p.T), axis=0)
```

- Define a new function to execute the VMAP method from previous

```run-python
%time img4 = multi_sersic_2d_linear_vmap(ij, p)
```

- apply new defined function to image and time it - 221ms
- second run - 203ms

```run-python
%timeit multi_sersic_2d_linear_vmap(ij, p)
```

- apply new function without image - 91.7 ms ± 3.69 ms per loop

```run-python
f = jax.jit(multi_sersic_2d_linear_vmap)
```

- jit the VMAP function

```run-python
%time f(ij, p);
```

- run jitted function - 665 ms
- second run -  674 µs

```run-python
%timeit f(ij, p)
```

- run again timing loops - 893 µs ± 5.51 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

### Using `vmap` and `sum` within `jit`ted function, taking a parameter dictionary
As above, but take a dictionary of parameters, which is more user friendly.
* For 12 profiles in 250x250 image:
    * Without `jit`, first run is 1500ms (if no previous vmap), subsequent runs 85ms
    * With `jit`, first run is 700ms, subsequent runs 1.6ms
* For 12 profiles in 500x500 image:
    * Without `jit`, first run is 1500ms (if no previous vmap), subsequent runs 140ms
    * With `jit`, first run is 770ms, subsequent runs 7ms
* For 24 profiles in 250x250 image:
    * Without `jit`, first run is 1700ms (if no previous vmap), subsequent runs 100ms
    * With `jit`, first run is 8000ms, subsequent runs 9ms
* On GPU for 24 profiles in 250x250 image:
    * Without `jit`, first run is 6600ms (if no previous vmap), subsequent runs 90ms
    * With `jit`, first run is similar (if no previous vmap), subsequent runs 0.2ms
* On GPU for 96 profiles in 500x500 image:
    * Without `jit`, first run is 6300ms (if no previous vmap), subsequent runs 90ms
    * With `jit`, first run is similar (if no previous vmap), subsequent runs 1ms

So, fast to create 'jitted' function, faster than simple approach afterwards, and friendly interface.

Super fast on GPU: factor ~50 speed-up.

Constant, reasonable overhead for `jit`, then ~100 times faster each operation. Each operation scales ~linearly with number of profiles.


```run-python
pd = {c: jnp.asarray(gax_pars[c]) for c in gax_pars.columns}
```

- create a pandas data-frame with the parameters form the parameter array 

```run-python
%time img5 = multi_sersic_2d_linear_vmap_dict(ij, pd)
```

- run function with parameter dictionary from pandas -196ms

```run-python
%time multi_sersic_2d_linear_vmap_dict(ij, pd);
```

- run function without image action - 187ms
- second run - 87.5 ms ± 2.17 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

```run-python
f = jax.jit(multi_sersic_2d_linear_vmap_dict)
```

- jit the function

```run-python
%time f(ij, pd);
```

- run jitted function - 1.39ms
- second run - 899 µs ± 4.7 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)