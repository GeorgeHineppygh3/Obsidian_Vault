---
s:: true
---
---
s:: true
---
---
s:: true
---
---
s: true
---

## Function:

```run-python
def fftconv2d(in1, in2, mode="full", calc_fast_len=False):
```

## Comments:

```run-python
"""Convolve two 2-dimensional arrays using FFT.

    Convolve `in1` and `in2` using the fast Fourier transform method, with

    the output size determined by the `mode` argument.

    This is generally much faster than `convolve` for large arrays (n > ~500),

    but can be slower when only a few output values are needed, and can only

    output float arrays (int or object array inputs will be cast to float).

    Parameters

    ----------

    in1 : array_like

        First input.

    in2 : array_like

        Second input.

    mode : str {'full', 'valid', 'same'}, optional

        A string indicating the size of the output:

        ``full``

           The output is the full discrete linear convolution

           of the inputs. (Default)

        ``valid``

           The output consists only of those elements that do not

           rely on the zero-padding. In 'valid' mode, either `in1` or `in2`

           must be at least as large as the other in every dimension.

        ``same``

           The output is the same size as `in1`, centered

           with respect to the 'full' output.

    calc_fast_len : bool, optional

        If `True`, set each value of `shape` to the next fast FFT length.

        Default is `False`, use as-is.

    Returns

    -------

    out : array

        An N-dimensional array containing a subset of the discrete linear

        convolution of `in1` with `in2`.

    """
```

### Description:

- Uses FFT to convolve two 2D arrays much quicker than standard convolve function for arrays of length $n>500$.
- mode is used to determine the size of the output with:
	- full - Default - The output is the full discrete linear convolution of the inputs.
	- valid - The output consists only of those elements that do not rely on the zero-padding. In 'valid' mode, either `in1` or `in2` must be at least as large as the other in every dimension.
	- same - The output is the same size as `in1`, centred with respect to the 'full' output.
- `calc_fast_len` is a boolean set true then the next shape is the FFT length - [ask steven about this]

- Returns N dimensional array of a subset of discrete linear convolution of the two input arrays


===============================================================

## Function:

```run-python
def _apply_conv_mode(ret, s1, s2, mode):
```

## Comments:

```run-python
"""Calculate the convolution result shape based on the `mode` argument.

    Returns the result sliced to the correct size for the given mode.

    Parameters

    ----------

    ret : array

        The result array, with the appropriate shape for the 'full' mode.

    s1 : list of int

        The shape of the first input.

    s2 : list of int

        The shape of the second input.

    mode : str {'full', 'valid', 'same'}

        A string indicating the size of the output.

        See the documentation `fftconvolve` for more information.

    Returns

    -------

    ret : array

        A copy of `res`, sliced to the correct size for the given `mode`.

    """
```

### Description:

- For two arrays to convolve with one another function calculates the output array shape
- Returns the result array sliced to the correct shape
- Takes arguments:
	- ret - the resulting array in shape 'full'
	 - s1 - shape of the first array to be convolved
	- s2 - shape of the second array to be convolved
	- mode is used to determine the size of the output with:
		- full - Default - The output is the full discrete linear convolution of the inputs.
		- valid - The output consists only of those elements that do not rely on the zero-padding. In 'valid' mode, either `in1` or `in2` must be at least as large as the other in every dimension.
		- same - The output is the same size as `in1`, centred with respect to the 'full' output.

- Function appears to be used for resizing the results of `fftconv2d` 

- [Ask steven about the purpose of this it may become clear later]

===============================================================

## Function:
```run-python
def _centered(arr, newshape):
```

## Comments:
```run-python
'''
Return the center newshape portion of the array.
'''
```

## Description:
- Unsure about this function [speak to steven]
- As a guess the function finds the centre of the new array after the convolution

===============================================================