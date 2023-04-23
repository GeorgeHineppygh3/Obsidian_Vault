---
s:: true
---
---
s:: true
---
---
s:: true
---
INTRODUCTION 
This function measures a spiral galaxy's best-fit pitch angle. The code  computes spiral coordinate systems, or templates, for every pitch angle  from MINP to MAXP degrees in steps of PSTEP. It then attempts to fit the  galaxy to each template, and outputs a fitting function called Variance  of Means. The galaxy's best-fit pitch corresponds to a peak in the  fitting function.  

COMPUTING THE FITTING FUNCTION: 
For every pitch angle template, the code  computes the mean pixel value along each spiral axis. The variance of  these means is recorded as a point in the fitting function, Variance of  Means vs. Pitch. For a noiseless, logarithmic spiral, the fitting  function shows an absolute maximum at the spiral's true pitch angle. For  a noisy galaxy image, the fitting function shows a local maximum at the  galaxy's best-fit pitch angle.   
ERROR BARS: In order to find the one-sigma confidence interval, the inner  radius of the measurement annulus is varied from MSMT_INNER1 to  MSMT_INNER2 equidistant steps of InnerRadiusSpacing pixels. The mean of  these measurements is considered the best-fit pitch BESTFITPITCH.   The random error is the standard deviation of these measurements. The  random error is scaled in order to penalize small stable measurement  regions and reward large ones. The scale factor is the difference  between the visible inner and outer radii of the galaxy, VIS_OUTER -  VIS_INNER, divided by the difference between the two inner radii,  MSMT_INNER2 - MSMT_INNER1. The scaled result, or the "stretched error"  is added in quadrature with the pitch angle domain spacing PSTEP,  resulting in the total error ERR.  OUTPUTS: PASSED 
VARIABLES   
PITCHvsINNER - A two-column array showing pitch angle in degrees as a  function of inner measurement radius. 
BESTFITPITCH - The mean pitch angle in the PITCHvsINNER array, or the  best-fit pitch angle of the galaxy.   
ERR - The total error in the BESTFITPITCH measurement. It is the  standard deviation of the pitch angles in the PITCHvsINNER array, scaled  by the radial range of the visible spirals divided by the range of inner  measurement radii, then added in quadrature with the spacing between  successive pitch angle templates.  

INPUTS  
FILE - The filename of the galaxy image. The file must be in *.fits  format, and the galaxy must be face-on or deprojected to circular.   X0, Y0 - The center of the galaxy in Cartesian pixel coordinates. Be  sure to use "image" coordinates, not "physical" coordinates. Must be  positive reals.   
VIS_INNER, VIS_OUTER - Visually estimated inner and outer radii, in  pixels, of the galaxy's spirals. These inputs are used to compute the  error bar, not to compute pitch angle itself. Must be positive reals  such that VIS_INNER < VIS_OUTER.   
MSMT_INNER1, MSMT_INNER2, MSMT_OUTER - The code first measures the galaxy  on an annulus with inner radius MSMT_INNER1 and outer radius MSMT_OUTER.  It then repeats the process, increasing the inner radius incrementally.  The final measurement is on an annulus from MSMT_INNER2 to MSMT_OUTER.  The best-fit pitch is the mean of pitch angles measured at all inner  radii from MSMT_INNER1 to MSMT_INNER2. Must be positive reals, such  that MSMT_INNER1 < MSMT_INNER2. All radii are in pixels.   
InnerRadiusSpacing - Spacing, in pixels, between inner radii. If the  user wishes to measure only one inner radius, there are two ways to  accomplish this:   A) Set InnerRadiusSpacing=0. In that case, only the inner radius  MSMT_INNER1 will be measured, while MSMT_INNER2 will be ignoresd.   or   B) Set MSMT_INNER2 = MSMT_INNER1. In that case, only the inner radius  defined by MSMT_INNER2 and MSMT_INNER1 will be measured. The value of  InnerRadiusSpacing will be ignored.   
MSMT_OUTER - The outer radius, in pixels, of all measurement annuli.  Ideally, it should be set just outside the visible outer radius of the  spirals, in empty space. However, it should not include pixel  contamination from foreground stars. Must be a real number greater than  MSMT_INNER2.   NAXIS - Number of spiral axes in each spiral template. 1000 is often  sufficient. Insufficient values of NAXIS will result in high-frequency,  periodic variations in the fitting function, partcularly in the loose  end of pitch angle domain (that is, as |P| approaches 90. In order to  ensure that each pixel is measured at least once, NAXIS should be at  least 2*pi*MSMT_OUTER. Must be a positive integer.   MINP, MAXP - Minimum and maximum pitch angles, in degrees, of the spiral  templates created for fitting. Must be real numbers such that  -90 <= MINP <= MAXP <= 90.   PSTEP - Spacing, in degrees, between pitch angles of successive  templates.   
AxisPointSpacing - The spacing, in pixels, between computation points on  each axis. Must be a positive integer. The code works very well with a  value of 0.1. Lower values will asymptote the pitch angle result toward  the correct value. Computation time varies inversely with this quantity.   SMOOTH - A toggle for applying a 5-point moving average to the Variance  of Means vs. pitch angle fitting function. If SMOOTH is 1, the moving  average is applied; otherwise it is not. This feature be useful in  smoothing high-frequency variations caused by an insufficient value of  NAXIS. However, also affect the location of the peaks, so use with  caution.   Save2D and Save3D - Toggles for saving the output files. If Save2D==1,  a 2-D graph of the fitting function vs. pitch angle will be generated for  each inner radius. If Save3D==1, a 3-D graph of the fitting function vs.  pitch angle and inner radius will be generated. If either variable is  set to 1, then a text file summarizing the results will be generated.   

OUTPUTS: 
FILES GENERATED   If Save2D==1 or if Save3D=1, the following file is generated:   - *.txt: A summary text file showing the passed  variables PITCHvsINNER, BESTFITPITCH, and ERR.   If Save2D==1, the following files is generated:   - 2D*.fig: A MATLAB figure showing the fitting function, Variance  of Means vs. pitch angle. One such file is created for each inner  radius.   - 2D*.eps: Same as *.fig, but an .eps image.   If Save3D==1, the following files is generated:   - 3D*.fig: A MATLAB figure showing the fitting function, Variance  of Means vs. pitch angle. Only one such file is created.   - 3D*.eps: Same as *.fig, but an .eps image.   

OUTSIDE FUNCTIONS NEEDED   
Extract_Filename  
Extract_Extention  [Only necessary for older versions of pitch.m]   
fitsread   
fitsheader   
PeriodToDash  
TROUBLESHOOTING   
This code relies on fitsread.m to read the .fits files. If fitsread.m  reads the wrong pixel values, you might need to tell fitsread.m to  bitswap.   Fitsread.m contains a series of if/else statements that looks for the  endianness of your architecture - that is, to determine whether  bitswapping is necessary. The code isn't familiar with all  architectures. For my Imac64, I had to add the following line to  fitsread.m:   elseif strmatch(friend,'MACI64')  bswap = 'b';  METHOD   The code will record the pixel values along the spiral axes of several  spiral coordinate systems. Then the code will measure the mean of all  pixel values along each coordinate axis. The variance of these means  will be recorded for each coordinate system. The true pitch angle will  yield the maximum variance of means. The true pitch is passed as  PITCHvsINNER.  MATH REVIEW   Let a spiral be given by   R = exp(B*THETA).   Then, using the astronomer's sign convention, the pitch angle is   P = arctan(-B), and   the arclength S from the origin to radius MSMT_OUTER is   S = abs((MSMT_OUTER/B)*sqrt(1+B^2)).   Source: Wolfram (http://mathworld.wolfram.com/LogarithmicSpiral.html)


```
Spirality(FILE,X0,Y0,...

VIS_INNER,VIS_OUTER,MSMT_INNER1,MSMT_INNER2,InnerRadiusSpacing,...

MSMT_OUTER,NAXIS,MINP,MAXP,PSTEP,AxisPointSpacing,SMOOTH,Save2D,Save3D)
```

```
Spirality(588017724937142430ra.fits.gz,116,200,...

10,100,11,21,1,...

105,1100,1,89,1,0.1,1,1,1)
```


## Abandoning this and instead using 2dfft:
