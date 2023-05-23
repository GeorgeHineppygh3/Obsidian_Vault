---
s:: true
---
Your text to be added
Your text to be added
1
===============================================================
This project makes use of the programs FICL and GAX developed by my supervisor, Steven Bamford, as a more computationally efficient replacement for GALFIT3. The programs apply progressive Sérsic profile fitting and extracts non-parametric components to create a disk subtracted image of a galaxy using the Jax  NumPy libraries.

The aim of this project is to explore how the extraction technique can be used to study isolated galaxy structure  and quantitatively identify prominence of morphological components from images.  

Our project focuses on spiral galaxies and specifically spiral arms. On the left is an RGB image of NGC 2857, in the centre we see the red band image taken from Galaxy Zoo 2 . On the right a demonstration of the non parametric extraction of the inhomogeneities to the Sérsic profile with labelled iteration number.


2
===============================================================
By selecting a data set of the 1000 brightest local face on blue spirals from galaxy zoo 2 and applying the non parametric extraction. The fraction of flux from spiral arms can be calculated. The arm flux removes the bulge using a radial exclusion mask beneath 0.3 effective radii.  

By taking the R band for example (click) the extraction has allowed identification of arm prominence quantitatively (click) which is in agreement with the GZ2 arm prominence weighted fractions. [ add these to the image somehow]

This method is successful in the G R and I bands however (click) you may have noticed the U and Z histograms extend beyond 1. 

This is a result of inaccurate background estimation in SDSS where negative flux is summed and contributes to a smaller total for original image than the extracted one. (click)

This is especially evident when examining a candidate with flux fraction above 1in the affected bands and azimuthally averaging the intensity (click). It is demonstrated that almost a fifth of the pixels are below the background and that the average intensity at larger radii goes negative.

3
===============================================================


- Galaxy spirals are logarithmic
- In order to identify spiral structure in the image we apply Fourier transform with a logarithmic spiral basis function 
- In order to perform the summation required the image must first be interpolated into log(R) theta format (top right)
- Spirals can have any number of arms so the power spectrum runs over up to 5 arm spirals
- By selecting the dominant harmonic mode (click)
- and measuring the peak of the spectrum the logarithmic spiral that is most represented in the image can be found
- By plotting this spiral on the image an approximate fit for the arms can be found (click)
- This spiral fit is good as you can see but gets less accurate at larger radii
- To fix this we can look at the spiral winding angle stability by varying the inner radius in the log(R) theta image (click)
- By doing so we are able to see that the fit is stable up to approximately 2.1 effective radii after which the effective power begins to drop and the measured angle varies


4
===============================================================

- Using these winding angle stability techniques (shown on the right) we can measure the stable region for our high resolution case study M51 in bands B G and R
- We can see the winding angle is stable until between 0.6 and 0.7 effective radii just beyond estimates of the corotation radii from the literature where the physical regime for the structure changes (click)
- By sampling pixels along equally spaced  normals to the fit the intensity and colour distribution can be investigated from the spiral fit out towards the shock front of the spiral arm density wave
- Stacking these pixels into images (click) allows the arm to be viewed in an unwound state
- On the left we see the non parametric image extracted arm and on the right the original image arm where dust lanes and arm spurs can be identified


5
===============================================================
- Averaging radially the normal sampling tool allows us to explore the relationship between the distance to the spiral fit and the colour in our original and arm isolated image
- The plots demonstrate a gradient of colour across the spiral fit with the trailing arm front being redder than the leading front which agrees with the literature regarding star formation and migration out of the arm as the pattern sweeps through 
- The isolated arm demonstrates the same colour gradient at zero  except with significantly more noise and the intensity remains approximately the same but lower due to the subtraction of the underlying disk distribution
- The intensity plot indicates that most of this colour gradient can be explained by dust reddening from dust lanes in the arm
- Other explanations could include a gradient of stellar maturity
- however without IFU data to quantify the Balmer decrement to estimate the dust extinction the colour contribution from this hypothesis cannot be tested
- In order to test this the IFU data could estimate the local metallicity to quantify the contribution from the age-metallicity degeneracy to create an accurate stellar population model for the arm region

6
===============================================================

- Thank you for listening