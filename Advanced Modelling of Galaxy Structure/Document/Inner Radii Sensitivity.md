---
s:: true
---
Your text to be added
Your text to be added
Your text to be added
Your text to be added
- Interpolated image forms an annulus between the inner radius and the closet edge in the image such that all points in the annulus are inside the image
- The greatest source of error is inaccurate estimation of the 'start' of the spiral arms 
- The Transform is relatively insensitive to outer radii selection but very to the inner radius

Outer Radius
- Underestimation - not all arm measured
- Overestimation - sky is measured at the edge but thankfully since FFT is luminosity biased not too bad
Inner Radius
- Underestimation - bulge and bar measured - worst possible scenario - we overcame this by using the same bulge exclusion conditions in flux fraction
- Overestimation - full spiral not measured

'The inner radius is a numerical artifact which should not affect the measurement of pitch angle.'

- As a result of sensitivity the function is run iteratively for successive inner radii 
- Seek a harmonic mode in which we find the measured angle to be the most stable  - we extended this to plot next to this the effective power which is the fraction of power across the harmonic modes to demonstrate the confidence of the fit

- Uncertainty 2-4 degrees

Stable region criteria
- the stable region must be of the same sign (chirality) as the observed spiral arm windings in the image
- should be of the same harmonic mode as the visually observed number of spiral arms
- there must not be any erratic fluctuation in pitch angle
- the region of stable pitch angles must be contiguous

- even when the correct $m$ value is ambiguous focus on picking a stable pitch angle

- Testing of this stability technique was extensively carried out using simulated low noise artificial logarithmic spirals

- he found that bars have very high pitch angle $\\phi\\sim90$ and so heavily bias the measured angle to higher values

## Error determination:

'The most obvious error is the variance about the mean pitch angle over the selected stable region in inner radii. The error is found by calculating the mean and standard deviation of the sample of pitch angles over the selected stable region. This standard deviation of pitch angle over the selected stable region is then weighted by the length of the stable region compared to the total length from the innermost spiral structure to the edge of the galaxy. Based on our observation from running synthetic logarithmic spirals through our code (see subsequent subsections), reliable pitch angles are not measurable for inner radii selected beyond ≈ 90% of the selected outer radius. At this point, too much information has been ignored for the code to accurately measure a pitch angle.'

#### Two sources of error:
1. Std on stable region $(\\beta\\sigma/\\lambda)^2$
2. Transform resolution $\\epsilon_m^2$

$$E_\\phi = \\sqrt{(\\beta\\sigma/\\lambda)^2+\\epsilon_m^2}$$
'where $E_\\phi$ is the total pitch angle error, $\\epsilon_m$ is the quantized error for the dominant harmonic mode, σ is the standard deviation about the mean pitch angle, $\\beta$ is the distance (e.g., in pixels) from the innermost stable spiral structure (i.e., beyond the influence of a bulge or bar) to 90% of the selected outer radius of the galaxy (0.9$r_{max}$), and $\\lambda$ is the length (in the same units as used for $\\beta$) of the stable range of radii over which the pitch angle is averaged.'

'Equation 7 reflects the fact that in our method, a human researcher rather than a computer makes the final selection of pitch angle. That is, a balance of two main principles governs Equation 7: the fluctuation across and the length of a chosen stable region of pitch angle as a function of inner radius. Our process ensures that the error about the mean pitch angle is appropriate, based on the choices made by the user. For example, an erratic “stable” region or a short stable region will both be punished with appropriately high errors. Thus, a careful selection of stable region is required so as not to produce substantial errors.'

- There is a reason we stop at 90%

Text
===============================================================

Due to the nature of the interpolation into $log(r),\\theta$ format the pixels are sampled from an annulus between the inner radius, $R_{min}$, to the outer radius, $R_{max}$.  The outer radius is set as the distance to the closest image edge, such that the annulus samples positions confined within the image bounds.  The technique, as has been demonstrated and extensively tested in \\cite{Davis}, is sensitive to the inner radius chosen and insensitive to the outer. This human estimation of when spiral structure begins proves to be the dominant source of error in the measurement.  To avoid this the bulge exclusion radius ($0.3R_e$) used in the arm flux fraction calculations was taken as the inner radius. While this seems an appropriate solution it remains rather arbitrary with only  visual estimation confirming it's effectiveness at removing the bulge.  To measure the spiral sensitivity to inner radius selection, the function is run iteratively over successive increments to the effective radius multiple until 90\\% of the extent of the galaxy. Beyond 90% of the galactic radius the measurement is demonstrated to be inaccurate \\cite{Davis}. 

The resulting figures plot pitch angle against inner radius in multiples of the effective radius for all harmonic modes next to the effective power of each harmonic mode against the inner radius. We aim to select a harmonic mode with a consistent stable measured pitch angle over the longest interval of inner radii possible. The effective power, power as a fraction of the summed power across all modes, demonstrates an analogue of the confidence of the fit where a high effective power indicates high fit confidence. 

The criteria for selecting a stable region from the plots selects only regions where:
- the stable region must be of the same sign (chirality) as the observed spiral arm windings in the image
- the stable region should be of the same harmonic mode as the visually observed number of spiral arms
- there must not be any erratic fluctuation in pitch angle over the stable region
- the region of stable pitch angles must be contiguous

To quantize the error across the stable region requires recognition and debiasing as a result of human selection.  The most obvious error contribution comes from fluctuations within the stable region and therefore the standard deviation of the measured value across the stable region. In order to correct for cherry picking the stable region the standard deviation is weighted by the length of the stable region as shown in equation \\ref{eqn:}.

The other hidden source of error stems from the resolution of the transform. The discrete step size of $p$ in the interval $-50<p<50$ across the harmonic modes ($1<m<5$) limits the resolution of $\\phi$ in the conversion of $p\\rightarrow\\phi$. This resolution quantized error is the spiral analogue of the frequency step size used in 1D discrete Fourier Transforms. This error is added in quadrature to the stable region length weighted standard deviation resulting in a final error
$$E_\\phi = \\sqrt{(\\beta\\sigma/\\lambda)^2+\\epsilon_m^2}$$
Where, as in \\cite{Davis},  $E_\\phi$ is the total pitch angle error, $\\epsilon_m$ is the quantized error for the dominant harmonic mode, σ is the standard deviation about the mean pitch angle, $\\beta$ is the distance (e.g., in $R_e$ multiples) from the innermost stable spiral structure (i.e., beyond the influence of a bulge or bar) to 90% of the selected outer radius of the galaxy (0.9$r_{max}$), and $\\lambda$ is the length (in the same units as used for $\\beta$) of the stable range of radii over which the pitch angle is averaged.


#### Fit Overlay:

The resulting fit for the $m=2$ harmonic mode spiral arms is then plotted over the galaxy image with the uncertainty bounds outlined surrounding the fit. The plot in figure \\ref{fig:2857_fit} demonstrates the effectiveness of confining the fit to the stable region and error estimation through equation \\ref{eqn:winding_stability}, where the isolated spiral arms within the bound region are entirely confined between the uncertainty plots. 
