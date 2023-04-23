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
import jax

from jax import numpy as jnp

  
  

def _enable_double_precision():

    jax.config.update("jax_enable_x64", True)

    x = jnp.zeros((1,), dtype=jnp.float64)

    enabled = x.dtype == jnp.float64

    return enabled

  
  

JAX_DOUBLE_PRECISION = _enable_double_precision()
```

## General Description:

- code imports relevant libraries
- code defines function `_enable_double_precision` 
	- function returns `enabled` 
- function with no input is then assigned to variable `JAX_DOUBLE_PRECISION`





