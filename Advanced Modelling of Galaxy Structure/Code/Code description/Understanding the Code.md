---
s:: true
---
---
s:: true
---
---
s:: true
---
The code is found through GitHub where you can download the repository and be viewed through Microsoft Visual Studio


## Contents:

### Python Files
- `_init_.py` :  [_init_.py](./Python%20files/_init_.py.md)
- `fftconvolve.py` : [fftconvolve.py](./Python%20files/fftconvolve.py.md) 
- `integration.py` : [integration.py](./Python%20files/integration.py.md)
- `model.py` : [model.py](./Python%20files/model.py.md)
- `sersic.py` : [sersic.py](./Python%20files/sersic.py.md)

### Jupyter Notebooks:
- `gax_multi_sersic.ipynb` : [gax_multi_sersic.pynb](./Juptyer%20Notebooks/gax_multi_sersic.pynb.md)
- `testing_jax_integration.ipynb` : [testing_jax_integration.ipynb](./Juptyer%20Notebooks/testing_jax_integration.ipynb.md)
- `testing_jax_summation.ipynb` : [testing_jax_summation.ipynb](./Juptyer%20Notebooks/testing_jax_summation.ipynb.md) 

## Data:
- GZ2 : Face on Spirals https://s3.amazonaws.com/gz2spirals/index.html


## Notes on the Code

`galpars = dict(mag=-7.5, log_re=0.9, log_n=0.7, x=0.2, y=0.3, q=0.1, theta=0.1)` 

- Above Steven has appeared to have set up a `galpars` dictionary which can be passed to the functions to reduce the number of inputs -this is something which will save a lot of time and could be implemented into our own code

- In order to jit things functions are often called within smaller functions usually called `f(something)` - don't know why [SS]

`jax.lax.fori_loop(0, len(w), int_func, init)`
- When jitting things it appears possible to set up loops as vector sums using Jax architecture


- 


- 


## How the code runs:



## Questions about the code:

1. jaxlib is not available on windows, In order to resolve this what do you recommend?
Linux?
```run-python
py -m pip install jaxlib

======================================================================================
'''
Note: you may need to restart the kernel to use updated packages.
ERROR: Could not find a version that satisfies the requirement jaxlib (from versions: none)
ERROR: No matching distribution found for jaxlib
'''
```
Resolved: Create Linux device which successfully runs the code - See [How to run GAX.pdf](../../../PDF%20exports/How%20to%20run%20GAX.pdf) 

2. In order to use the code to extract spiral arms what needs to be done/ changed?

3. How can we use the code to preliminarily try and fit anything/something to a face on spiral from GZ2?
4. 