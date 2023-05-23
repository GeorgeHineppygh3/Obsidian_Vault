---
s:: true
---
Your text to be added
Your text to be added

## Easier Questions

1.  Could you explain how the FICL and GAX programs are more computationally efficient than GALFIT3?

GAX is the modeller that is used for the fitting of the Sérsic profile which makes use of the JAX library developed by google primarily for deep learning. The Library vectorises the arrays for calculation allowing the fitting to be done on a GPU rather than the CPU. This allows for a factor of 50 - 70 times reduction in computation time.

2.  How do the FICL and GAX programs apply progressive Sérsic profile fitting?

GAX applies progressive Sérsic fitting by first creating a list of source parameters in the image. For our fitting the galaxy images are isolated and so the maximum sources is set to one. The Sérsic profile is then fit to the estimated source parameters and the fit is then subtracted leaving a residual image and a working image. The working image is then fit again and the chi squared between the fits is calculated and then the gradient of the chi squared is minimised for the next fit and the residual image is updated. The non parametric image is found from the difference between working image and residual image and after the iteration limit expires or the fit is unable to find a Sérsic distribution in the working image.

3.  Can you explain the non-parametric extraction technique used in your project?


4.  How does the non-parametric extraction help in studying isolated galaxy structure?

By removing the underlying disk photometric distribution the flux from non disk components such as the bulge arms, rings or bar; the photometric contribution from these components can be studied independently of the diffuse more stellar diverse light.

5.  Could you explain how the arm flux removes the bulge using a radial exclusion mask beneath 0.3 effective radii?

The effective radii bulge mask uses the source parameters from the fitting to isolate the bulge as the region within 0.3 effective radii. 0.3 $R_e$ was chosen as a consistent measure as in all bands it was enough to cover the significant central region containing the bulge without containing very much arm. See below.

![Pasted image 20230506105737.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230506105737.png)
![Pasted image 20230506105753.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230506105753.png)

6.  How did you select the data set for your project?

The Data was selected using the criteria:

- Co added magnitude( average across 5 bands) below $m_{avg} < 17$
- Redshift below 0.085
- $f_{spiral} > 0.8$
- $f_{bar} < 0.2$ 

We wanted to select 1000 galaxies that are reasonably local but do not have too large an angular size

We wanted bright galaxies so that there is enough total flux to identify the Sérsic profile for subtraction

We wanted to study the fraction of flux in the arms so only wanted galaxies that the GZ2 classification system was sure was a spiral galaxy.

We did not want barred galaxies as this would mean that the radial exclusion bulge mask would be less accurate as the bars would pertrude beyond the exclusion zone and add to the flux total in the arms.

7.  Can you explain how the extraction allowed identification of arm prominence quantitatively?

By quantifying the amount of flux in the non parametric image after excluding the bulge using the radial mask and dividing by the total flux in the original image the fraction of flux in the arms can be identified. This allows a way to quantitatively estimate how under viewing the galaxy with a 99% scale range the prominence of the arms relative to the general flux from other morphological features. This method requires no human assessment and so is free from bias. 

8.  Why do the U and Z histograms extend beyond 1 and what is the cause of inaccurate background estimation in SDSS?

1.  The U-band is particularly challenging because it is strongly affected by the Earth's atmosphere, which scatters blue light and causes the sky to appear brighter in the U-band than in other bands. This makes it difficult to accurately estimate the true sky background.
    
2.  In the Z-band, the sky background is dominated by thermal emission from the atmosphere and the telescope, which varies with time and can be difficult to model accurately.
    
3.  Both the U and Z bands suffer from scattered light from the Moon and from twilight, which can also affect the accuracy of the sky background estimation.



9.  Could you explain how the Fourier transform with a logarithmic spiral basis function helps identify spiral structure in the image?

The image is first processed into the $log(r),\\theta$ format such that the discretised integral over the spatial domain can be applied through summation of the image elements multiplied by the weight function which is found as the inverse magnitude of the basis function. The weight function applies greater weight to signals that best represent the basis function. The function is run over successive harmonic modes where each harmonic mode represents the number of basis functions represented in the image.  The power spectrum of the resulting complex array demonstrates the magnitude of the spiral represented in the image. From the global maxima of these distributions the most represented spiral of winding angle $\\phi$ and position angle $\\theta$ is found from the argument of the complex component and from operations on the variable $p$ which contains $\\phi$. 

10.  What is the dominant harmonic mode and how does it help in finding the most represented logarithmic spiral in the image?

The dominant harmonic mode is also known as the pattern number and it represents the number of arms in the spiral. The Power spectra are computed over up to 5 arms and the pattern number with the greatest power represents the spiral structure most represented in the image.  

11.  Why does the spiral fit get less accurate at larger radii and how is this issue resolved?

The spiral fit gets less accurate at larger radii as the spiral is not a simple single winding angle spiral but instead is a spiral with a winding angle that varies as a function of radius. The fit stability plot allows estimation of spiral winding angle stability and provides a region over which the winding angle is stable enough to be represented as a single winding angle spiral. 

12.  How did you measure the winding angle stability in your high resolution case study of M51?

The winding angle stability figure plots the inner radius that the $log(r), \\theta$ image is interpolated from before summation into the complex components. The `logspaced` interpolation is performed between the inner radius and maximum radius (the closest edge within the image).  The resulting winding angle value then calculates the spiral that best fits the remainder of the image after the inner radius. By plotting this value against the inner radius the relative change in angle to the previous inner radius can be estimated. 

In the case study the stable region was taken as the region from minimum inner radius (0.3$R_e$) to where the winding angle approximation begins to vary significantly. This point is coincidentally just beyond the Corotation radius where the physical regime responsible for the spiral structure changes.

13.  Could you explain how the normal sampling tool helps in investigating the intensity and colour distribution from the spiral fit towards the shock front of the spiral arm density wave?

The normal sampling tool provides a method for sampling pixels along the spiral fit to view the arm in an unwound state. The normal lines travel perpendicular to the spiral fit out towards the shock front of the leading and trailing edge of the arm. By stacking these pixels into images averages of the ratio to flux's can give information about the colour distributions within the arm. By averaging radially the distance to arm centre-colour distribution can be identified.  This tells us information about the colour change from leading to trailing edge half.


14.  What explanations are there for the observed colour gradient in the isolated arm and how could they be tested?



15.  How could the IFU data be used to create an accurate stellar population model for the arm region?



Harder Questions
===============================================================

1.  How does the non-parametric extraction technique employed in your project differ from other galaxy structure analysis methods? What are its advantages and limitations?

2.  Can you explain how the radial exclusion mask works in the calculation of arm flux? How was the value of 0.3 effective radii chosen as the threshold?

3.  Why do the histograms for the U and Z bands extend beyond 1, and how does this affect the accuracy of the results? Can you suggest any ways to mitigate this issue?

4.  Can you describe the process of interpolating the image into log(R) theta format for the Fourier transform analysis? How does this allow for the identification of spiral structure?

5.  What is the dominant harmonic mode, and how is it related to the number of arms in a spiral galaxy? How was the peak of the power spectrum used to find the most represented logarithmic spiral in the image?

6.  Can you explain how the winding angle stability technique is used to measure the stable region of M51 in bands B, G, and R? How does the measured stable region compare to the corotation radii estimated from literature?

7.  How did you choose the spacing of the normals used to sample pixels along the lines for investigating the intensity and colour distribution along the spiral arm density wave? How does this affect the accuracy of the results?

8.  What is the significance of viewing the arm in an unwound state, and how does this help in studying its properties? How does the non-parametric extracted arm compare to the original arm in terms of colour and intensity?

9.  Can you explain the age-metallicity degeneracy, and how it affects the interpretation of the results obtained from the normal sampling tool? How could the IFU data be used to mitigate this effect?

10.  How do the results obtained from your project contribute to our understanding of the structure and properties of spiral galaxies? What are the implications for future research in this field?

11.  Can you discuss any potential sources of error or bias in your analysis, and how you attempted to address them? How confident are you in the validity of your results?

12.  How do the limitations of the SDSS data affect the accuracy and applicability of the non-parametric extraction technique? How could this be improved in future studies?

13.  What other types of galaxies or structures could be studied using the methods and techniques employed in your project? Are there any particular challenges or limitations that would need to be addressed?

14.  How does your project relate to other research in the field of galaxy structure analysis and morphology? What are some areas of overlap and potential collaboration?
15.  Can you explain the significance of your project in the broader context of astrophysics and cosmology? What are some of the open questions and challenges that remain to be addressed in this field?
