---
s:: true
---
---
s:: true
---
---
s:: true
---
===============================================================
## Function:
```run-python
def roots_clencurt(order):
```

## Comments:
```run-python

"""Computes the Clenshaw Curtis nodes and weights.

  

    These are useful for adaptive integration, as nodes are repeated

    for higher orders. It is also a useful comparison to alternative

    integration methods (e.g. Gauss-Legendre) for estimating

    uncertainties.

  

    Notes

    -----

    The nodes are on the range [-1, +1].

    Uses the Fast Fourier Transform method presented in:

    Jörg Waldvogel, "Fast Construction of the Fejér and

    Clenshaw-Curtis Quadrature Rules," BIT Numerical Mathematics

    46 (1), p. 195-202 (2006).

    http://www.sam.math.ethz.ch/~waldvoge/Papers/fejer.pdf

  

    Adapted from code found online under MIT license:

    https://github.com/gregvw/orthopoly-quadrature/blob/master/clencurt.pyx

  

    Parameters

    ----------

    order : int

        The order of the integration
    """

```

## Description:
- Computes the Clenshaw Curtis nodes and weights. [Requires further research]
- Takes inputs:
	- order - the order of the intergation
- Returns:
	- Clenshaw Curtis nodes and weights


===============================================================
## Function:
```run-python
def integrate_pixels(func, i, j, pars, di, dj, w):
```

## Comments:
```run-python
'''
Comments
'''
```

## Description:
- function takes inputs:
	- func - function to be integrated
	- i - [array coordinates?]
	- j - [array coordinates?]
	- pars - 
	- di -
	- dj - 
	- w - [order?]
- Function returns:
	- `jax.lax.fori_loop(0, len(w), int_func, init)` - appears to be a vectorised version of looping through the list of the function to compute the integration


- Thoughts:
	- function appears to do 2D integration of some form and takes the input coordinates


===============================================================
## Function:
```run-python
def tensor_integrate_pixels(func, i, j, pars, d, w, oversamp=1):
```

## Comments:
```run-python
'''
Comments
'''
```

## Description:
- function takes inputs:
	- func - function to integrate
	- i - pixel array index
	- j - pixel array index
	- pars -
	- d -
	- w - [order?]
	- oversamp =1 - oversampling amount
- Function returns:
	- returns - [`integrate_pixels` performed on a tensor dimension d from given pixels]

- Thoughts:
	- function performs tensor integration on given pixels calling the `integrate_pixels` from the pixel array index order and tensor dimensions


===============================================================
## Function:
```run-python
def gauss_legendre_tensor_integration(func, i, j, pars, order, oversamp=1):
```

## Comments:
```run-python
'''
Comments
'''
```

## Description:
- function takes inputs:
	- func - function to integrate
	- i - pixel array index
	- j - pixel array index
	- pars -
	- d -
	- w - [order?]
	- oversamp =1 - oversampling amount
- Function returns:
	- returns - function performs gauss Legendre tensor integration on given pixels by calling `tensor_integrate_pixels` 

- Thoughts:
	- function uses the order to calculate the `d, w` for the inputs  for tensor integration


===============================================================
## Function:
```run-python
def integrate_with_error(func, i, j, pars, k, order, base_oversamp, oversamp):
```

## Comments:
```run-python
'''
Comments
'''
```

## Description:
- function takes inputs:
	- - func - function to integrate
	- i - pixel array index
	- j - pixel array index
	- pars
	- k
	- order
	- base_oversamp
	- oversamp
- Function returns:
	- tensor integrated pixels
	- error on the tensor integrated pixels


- Thoughts -
	- function appears to calculate the error of the tensor integration using the `tensor_intergrate_pixels` function
===============================================================
## Function:
```run-python
def oversample_pixels(i, j, k, base_oversamp, oversamp):
```
## Comments:
```run-python
'''
Comments
'''
```

## Description:
- function takes inputs:
	- i
	- j
	- k
	- base_oversamp
	- oversamp
- Function returns:
	- oi - oversampled pixel i [assume this is an array of some type?]
	- oj - oversampled pixel j [assume this is an array of some type?]

===============================================================
## Function:
```run-python
def prepare_subpixel_refinements(

    func,

    i,

    j,

    pars,

    base_oversamp,

    order,

    oversamp,

    precision,

    frac_refine,

    k_max,

    verbose=False,

):
```

## Comments:
```run-python
"""Prepare subpixel refinements for `integrate_with_subpixel_refinement`.

  

    This method operates iteratively to achieve high precision, even for functions

    that are difficult to integrate. At each iteration, pixels with an estimated error

    greater than the desired precision are oversampled and reintegrated.

  

    Parameters

    ----------

    func : callable

        A python function with signature `(i, j, **pars)`, where `i` and `j` are the

        coordinates at which to evaluate the profile. `i=j=0` is defined as the centre

        of the image. `i` corresponds to the (vertical) y-axis and `j` corresponds to

        the (horizontal) x-axis.

    i, j : floats

        The coordinates corresponding to the centre of each pixel in the

        (non-oversampled) image.

    pars : dict of floats or jax arrays (a jax "pytree")

        Parameters defining one or more profiles. The keys must match the parameter

        argument names of `func`.

    base_oversamp : int

        The initial oversampling factor to apply to the image. The returned image will

        be oversampled by this factor.

    order : int

        The initial integration order to use. This may be increased for the refinement

        iterations.

    oversamp : int

        The oversampling factor to apply at each refinement iteration.

        Generally best left at the default value of 2.

    precision : float

        The desired level of precision in the returned pixels.

    frac_refine :

        The fraction of pixels to refine at each iteration.

    k_max : int

        The maximum number of iterations. Probably best left at the default.

    verbose :

        Output details about each iteration.

  

    Returns

    -------

    jax array

        An image formed from the integrated pixels, oversampled by a factor of `base_oversamp`.

    """
```

## Description:
- function takes inputs:
	- func,
	-  i,
	-   j,
	-  pars,
	-  base_oversamp,
	-  order,
	-  oversamp,
	- precision,
	- frac_refine,
	-  k_max,
	 -   verbose=False,
- Function returns:
	- image formed from the integrated pixels, oversampled by a factor of `base_oversamp` 

===============================================================
## Sub-Function:

This is very complex lol

```run-python
def step(k, r):
```

## Comments:
```run-python
'''
Comments
'''
```

## Description:
- function takes inputs:
	- k
	- r
- Function returns:
	- new_int_pix 
	- r

===============================================================
## Function:
```run-python
def shortcut_loop_step(k, r):
```

## Comments:
```run-python
'''
Comments
'''
```

## Description:
- function takes inputs:
	- k
	- r
- Function returns:
	- returns - 

===============================================================
## Function:
```run-python
apply_subpixel_refinements(idx_to_refine,init_int_pix,
ref_int_pix,n_imprecise,oversamp,shape,verbose=False):
```

## Comments:
```run-python
'''
Comments
'''
```

## Description:
- function takes inputs:
	- idx_to_refine - [array index to refine?]
	- init_int_pix - [initial integrated pixel?]
	- ref_int_pix - [reference integrated pixel?]
	- n_imprecise - [not sure]
	- oversamp - [how much to over sample (number of divisions)]
	- shape - [array input or output shape?]
	- verbose=False
- Function returns:
	- sum_pix - [summed pixels?]


===============================================================
## Sub-Function:
```run-python
def function(input):
```

## Comments:
```run-python
'''
Comments
'''
```

## Description:
- function takes inputs:
	- input -
- Function returns:
	- returns - 

===============================================================