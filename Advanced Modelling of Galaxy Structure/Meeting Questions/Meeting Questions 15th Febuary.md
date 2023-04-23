---
s:: true
---


## Questions:

1. Would you be able to show me (or do you have any existing code working) how to make the code fit profiles to the single band images? If not how do I use the convolve function to fit the profiles to images?

A: 

FICL contains the running of the code! -

Reads in the code -runs algorithm for sources
convert parameters of sources to create the image of the rendered profiles
calculates chi squared and updates
updates non parametric image after each alteration

ficl does large and small scale non param would only want the small

could adapt ficl - or could modify gax to do it on it own

install all software using environment file in ficl (conda environment)

install gax with pip so ficl can see it

speak to Shivani

code sort of already works

see read me in ficl

can specify from the command line which image you want to use also turn of large scale non param component (try on and off)

find any holes in what you want it to do and raise them (joint)



2. How does the convolving work and are the inputs the image arrays?

A: 



3. How does the integration tie into all of this? Is it to do with the error from having to pixel the profiles?

A:



4. Previously I have noticed there were iterations, how many would normally have to run until the model is accurate enough?

A:



5. What are the computing facilities available at Nottingham? How would this be done (forms etc)? is there a spec sheet?

A: Steven has got us accounts on MLIS1 and MLIS2 GPU workstations with the UNI - when it comes to running loads can uses these

just SSH into the server:

open windows shell and 

ssh ppygh3 @ mlis1

will timeout if not on campus - do it on campus - or use VPN - use virtual desktop and it will work from there

nothing online about the specs - two GTX 2080 and lots of cores and memory

6. Shivani has mentioned that you said the main thing is incorporating multiband now - what are the primary steps in going towards this? - is this to do with the SNR weighting and coefficients of Chebyshev polynomials as you mention for GALFITM over GALFIT? If so do you have the code to have a look at to do in JAX?

A:

GALFIT(M) code : https://github.com/MegaMorph


might be best to look for change history to see how the code developed from GALFIT



might be a rabbit hole

what are the primary steps:  

could do something simpler



how does the weighting work:

Chebyshev polynomials allows the size and shape to vary as function of wavelength

make galaxies be the same shape but change brightness in each band

set of params make the model then make the image and then compare with chi squared which describes how well the model fits the data

update parameters to try and decrease chi

fit again

parameters to model image (sersic parameters atm) 

flux in each band become parameters

make to images on in r band one in others 

will have different psf in each band

set of params which are Chebyshev and then convert to parameters for each band

could reproduce this if we have time

call functions from ficl into notebook and run the fitting on an image

### first priorities:

run ficl to fit a spiral and see what it does

try using ficl code in a notebook

could add multiband from here

[need the psf from the SDSS images] - steven is looking for this for us (isn't there on the dataset) - NEEDS DEALING WITH -can do own research

run without psf at the moment or run with a gaussian with fwhm at the scale of a couple pixels





## Possible things to show:

- [x] Jupyter notebook for testing : [Borge_test.ipynb](../../PDF%20exports/Borge_test.ipynb.md) 
- [x] functions for fits handling : [gax_fits.py.pdf](../../PDF%20exports/gax_fits.py.pdf) 


## Notes:

code for running is in ficl

