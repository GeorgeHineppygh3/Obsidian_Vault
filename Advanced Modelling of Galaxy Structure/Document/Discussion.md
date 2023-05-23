---
s:: true
---
Your text to be added
Your text to be added
Your text to be added
Your text to be added

### Flux Fraction:

**References**
```
@INPROCEEDINGS{SDSS_Background,
  author={Qin, Lili and Liu, Fengshan and Tu, Ya and Yu, Guiying and Yu, Hongfeng},
  booktitle={2010 3rd International Congress on Image and Signal Processing}, 
  title={A more precise method of sky subtraction in SDSS astronomical image processing}, 
  year={2010},
  volume={5},
  number={},
  pages={2458-2460},
  doi={10.1109/CISP.2010.5648062}}

Demonstrations:

@article{Bernardi_2007,
	doi = {10.1086/511783},
	url = {https://doi.org/10.1086%2F511783},
	year = 2007,
	month = {mar},
	publisher = {American Astronomical Society},
	volume = {133},
	number = {4},
	pages = {1741--1755},
	author = {Mariangela Bernardi and Joseph B. Hyde and Ravi K. Sheth and Chris J. Miller and Robert C. Nichol},
	title = {The Luminosities, Sizes, and Velocity Dispersions of Brightest Cluster Galaxies: Implications for Formation History},
	journal = {The Astronomical Journal}
}

@article{Lauer_2007,
	doi = {10.1086/518223},
	url = {https://doi.org/10.1086%2F518223},
	year = 2007,
	month = {jun},
	publisher = {American Astronomical Society},
	volume = {662},
	number = {2},
	pages = {808--834},
	author = {Tod R. Lauer and S. M. Faber and Douglas Richstone and Karl Gebhardt and Scott Tremaine and Marc Postman and Alan Dressler and M. C. Aller and Alexei V. Filippenko and Richard Green and Luis C. Ho and John Kormendy and John Magorrian and Jason Pinkney},
	title = {The Masses of Nuclear Black Holes in Luminous Elliptical Galaxies and Implications for the Space Density of the Most Massive Black Holes},
	journal = {The Astrophysical Journal}
}

@article{Lisker_2007,
	doi = {10.1086/513090},
	url = {https://doi.org/10.1086%2F513090},
	year = 2007,
	month = {may},
	publisher = {American Astronomical Society},
	volume = {660},
	number = {2},
	pages = {1186--1197},
	author = {Thorsten Lisker and Eva K. Grebel and Bruno Binggeli and Katharina Glatt},
	title = {Virgo Cluster Early-Type Dwarf Galaxies with the Sloan Digital Sky Survey. {III}. Subpopulations: Distributions, Shapes, Origins},
	journal = {The Astrophysical Journal}
}

@article{U_band_ISSUES,
doi = {10.1088/0004-6256/150/4/104},
url = {https://dx.doi.org/10.1088/0004-6256/150/4/104},
year = {2015},
month = {sep},
publisher = {The American Astronomical Society},
volume = {150},
number = {4},
pages = {104},
author = {Hu Zou and Zhaoji Jiang and Xu Zhou and Zhenyu Wu and Jun Ma and Xiaohui Fan and Zhou Fan and Boliang He and Yipeng Jing and Michael Lesser and Cheng Li and Jundan Nie and Shiyin Shen and Jiali Wang and Tianmeng Zhang and Zhimin Zhou},
title = {SOUTH GALACTIC CAP u-BAND SKY SURVEY (SCUSS): DATA REDUCTION},
journal = {The Astronomical Journal},
abstract = {The South Galactic Cap u-band Sky Survey (SCUSS) is a deep u-band imaging survey in the Southern Galactic Cap, using the 90Prime wide-field imager on the 2.3 Bok telescope at Kitt Peak. The survey observations started in 2010 and ended in 2013. The final survey area is about 5000 deg2 with a median 5σ point source limiting magnitude of ∼23.2. This paper describes the survey data reduction process, which includes basic imaging processing, astrometric and photometric calibrations, image stacking, and photometric measurements. Survey photometry is performed on objects detected both on SCUSS u-band images and in the SDSS database. Automatic, aperture, point-spread function (PSF), and model magnitudes are measured on stacked images. Co-added aperture, PSF, and model magnitudes are derived from measurements on single-epoch images. We also present comparisons of the SCUSS photometric catalog with those of the SDSS and Canada–France–Hawaii Telescope Legacy surveys.}
}

```

- Inaccurate background estimation

How SDSS estimate background:

'PHOTO then performs two levels of sky subtraction; when first processing each frame image it estimates a global sky level, and then, while searching for and measuring faint objects, it re-estimates the sky level locally.'

'The initial sky estimate is taken from the median value of every pixel in the image (more precisely, every fourth pixel in the image), clipped at 2.3 sigma. This estimate of sky is corrected for the bias introduced by using a median, and a clipped one at that. The statistical error in this value is then estimated from the values of sky determined separately from the four quadrants of the image.'

'Using this initial sky estimation, PHOTO proceeds to find all the bright objects (typically those with more than 60 sigma detections). Among these are any saturated stars present on the frame, and PHOTO is designed to remove the scattering wings from at least the brighter of these — this should include the scattering due to the atmosphere, and also that due to scattering within the CCD membrane.'

'PHOTO then proceeds with a more local sky estimate. This is carried out by finding the same clipped median, but now in 256x256 pixel boxes, centered every 128 pixels. These values are again debiased.'

'It is understandable if a large fraction of the pixels in a 256x256 pixels is part of an object rather than blank sky, this procedure casues the local sky to be an overestimate of the true sky background. This may happen for galaxies with large size and/or in crowded fields.'

### Text:

The background estimation performed by \\texttt{PHOTO} systematically under estimates the luminosities and effective radii of bright local large angular size galaxies \\cite{SDSS_Background}. Due to our filtering criteria this feature is strongly evident in the statistical study sample. 

\\texttt{PHOTO} performs global and local sky subtraction via a sigma clipping process $2.3\\,\\sigma$ beyond the median pixel value. The global clipping is first applied to the entire $2048\\times1498$ frame whereafter the same process is repeated on 256 pixel boxes across a 128 pixel spaced grid. The grid is then interpolated using a Bresenham algorithm variant to create a background map for all large frame images.  Galaxies that occupy significant portions of these 256 pixel skew the local background estimates to be larger than the true background level.

- Why it is worse in U and Z

The U and Z bands have the lowest signal to noise across the images in our sample and are strongly affected by the \\texttt{PHOTO} system. The U band's short wavelength ($3590 \\AA$) leaves it especially vulnerable to atmospheric scattering increasing the uncertainty in the in the low signal to noise extremities of large angular size galaxies. The U band scattering issues are exacerbated by a downward bias in the background estimation of nearly 0.1 DN per pixel resulting in errors on the order of 10% for U band Petrosian fluxes of large galaxies \\cite{U_band_ISSUES}.
The Z band's position within the near infra-red ($7900\\AA$) leaves the flux vulnerable to atmospheric and thermal variations. Atmospheric conditions such as aerosol concentration significantly affect the transparency and emission properties of the NIR sky. Recombination and excitation of of atmospheric constituents releases diffuse NIR (Airglow) contributing to temporal and spatial variations in the background increasing the uncertainty in estimating the noise level.

- Demonstration of negative flux

To demonstrate the background estimation inaccuracy, candidates with non physical flux fractions ($f_{\\text{Arm}}>1$) in the affected bands can be demonstrated to have significant flux beneath the background. Figure \\ref{fig:bad_cand} demonstrates the galaxy \\textbf{NGCXXXX} in the U band where $16.9\\%$ of the flux is negative. The inaccurate background estimation is most prominent when examining the azimuthally averaged intensity of the affected candidate (figure \\ref{fig:azimuth}) where it is demonstrated at large radii that the average intensity becomes negative resulting in a dark ring surrounding the galaxy.

- Discussion of fixes from the literature

Background correction provided by \\cite{SDSS_Background} resolves the high brightness systematic error using Legendre polynomials. The technique calculates the background by first creating a background only image, removing sources by masking objects $1\\,\\sigma$ above the whole frame noise. The frame is then smoothed using a gaussian kernel convolution ($\\sigma = 3$ pixels) before being convolved with a 51 pixel square median filter. The resulting image rows and columns are then fit with second order Legendre polynomials which are in turn smoothed with a larger gaussian kernel ($\\sigma = 9$ pixels). This background model proves accurate to $\\sim2\\times10^{-2}\\,DN$  and therefore provides potential for the prominence estimation technique to be applied to the unsuccessful bands.


- problem with prominence and arm fraction not containing continuity

### Case study:

- arm not logarithmic
	- companion
- talk about the general inside out blue disk thing
	- create a smoothed colour distribution?
- talk about how the disk subtraction may have under/over corrected for this with regards to the bulge

- How the information provided leads to questions that can be resolved using IFU data 


Due to the large gravitational influence from M51's companion galaxy the arms are only logarithmic over a small radial interval limiting the fit to be acceptably accurate over the inner region. As can be seen from figure \\ref{fig:M51BV} 

![Pasted image 20230520222820.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230520222820.png)

## Graph Observations

- Systematically bluer in $B/R$ and $V/R$ but bluer in $B/V$ 
	- 
- Isolated arms are smoother than the non isolated
	- 
- Spread and uncertainty is $\\approx$ the same in both
	- 
- All demonstrate colour gradient across the arm
	- 
- dust lane hump present in both isolated and original (all)
	- 
- 

We calculated colour in our images by zero point calibrating the flux according to the run time information in the headers and then taking the ratio of the flux's inside a logarithm to calculate the change in magnitudes according to
$$\\Delta m = -2.5 \\log(B/V) \\equiv -2.5\\big(\\log(B) - \\log(V)\\big) \\equiv m_B - m_V$$

The spiral arm structure in M51 is heavily influenced by the gravitational influence of its companion galaxy and as a result is only well described by a static winding angle logarithmic spiral over the limited radial interval $0.3\\leq R_e\\leq 0.9$. This region is confined close to the centre of the spiral where the colour distribution, as shown in figure \\ref{fig:}, is more red due to the presence of a very red bulge. To observe this we created bulge subtracted smoothed ($\\sigma=25$ pixels) colour image for each flux ratio. The images demonstrated the trailing edge inter arm region of the fit to be noticeably redder than the outer.  This trend is also noticeable in the unwound arm colour images in figure \\ref{fig:} and may have an overall affect on skewing the original average colour gradient across the arm (figure \\ref{fig:}).

The colour gradient across the arms in both the original and isolated images follow the general trend of red to blue from trailing to leading edge however the average gradient across the arm in the isolated images is greater. The interior edge in the colours $B/R$ and $V/R$  is redder than the original images but the leading edge is approximately the same colour suggesting the subtraction of a Sérsic of greater index, $n$, in the $R$ band. This assumption is backed up by examining the final model parameters for each image where: $n_B=0.32$, $n_V=0.34$ and $n_B=0.52$ demonstrating the increased arm gradient to be due to the presence of light within the arm and not the underlying disk trend. The $B/V$ gradient however is systematically bluer than the original image with a bluer overall average colour. Due to the Sérsic indices being approximately the same this demonstrates the arm to be a dominantly blue feature. Interestingly the gradient across the isolated image is less than the original demonstrating the affect of the similar fit subtraction.

The Isolated arm plots are smoother over all but have approximately the same amount of uncertainty associated with each point. This is most likely due to the subtraction of the disk increasing the number of zeros in each radially averaged column lowering the random variation present. Despite the smoother distributions extra disk features presented as bumps along the distribution are still visible and trace the approximate distribution in the original image. This is most likely a result of successful extraction of the spiral arms by \\texttt{GAX} demonstrating the studied region to be entirely describe by inhomogeneities to the Sérsic.

We estimate the bump between $-100$ to $0$ pixels in all colours to be due to the presence of extincting dust from dust lanes present within the same interval in the unwound colour images (figure \\ref{fig:}). The extinction hypothesis  is further backed by the feature being less pronounced at colours of ratios of longer wavelengths, where absorption and scattering would be lower reducing the extinction (as seen in $V/R$ compared to $B/V$ in figure \\ref{fig:}).

While the observations agree with the red to blue trend the stellar maturity gradient remains a suitable hypothesis that could be further studied. While this study qualitatively identifies the affect of dust extinction the tools used to do so could be quantitatively exercised using IFU data. The IFU data would be able to calculate extinction values for each pixel from the ratio of observed to intrinsic Balmer decrement ($H_\\alpha/H_\\beta$) from measures of the local gas density. By ruling out the contribution from extinction the metallicity of the local region could be measured from a variety of emission lines. From the metallicity estimates of each pixel an accurate stellar population model could be generated. This model could be used to quantify the age-metallicity colour degeneracy to plot the stellar maturity gradient against distance from the fit.

## Tool effectiveness:

- Is the tool successful at morphological classification?
- How can it be improved?
- Does the arm isolation help studying the arm? how?
- How does the tool affect SFT fitting?
- what improvements to the tool could be made?

FICL and GAX provide an automatic spiral prominence measure with several caveats: 
\\begin{itemize}
	\\item The isolated flux summation is not guaranteed to resemble spiral arms but instead inhomogeneities to the Sérsic profile.
	\\item The measurement is sensitive to background estimation.
	\\item The measurement is limited to non barred spiral galaxies.
	\\item The measurement requires single nucleated galaxies.
\\end{itemize}

When identifying prominence in Galaxy Zoo subtle factors such as the continuity and spatial distribution of the arms are assessed subconsciously by the reviewer to give an estimate of spiral prominence. Through the summation of non disk flux using FICL and GAX any inhomogeneity contributes to a larger arm flux fraction without consideration of the spatial distribution of the summed intensity. To counteract this, arm isolated images that had a Gini coefficient greater than $2\\,\\sigma$  from the sample mean were human reviewed to ensure the heavily concentrated arm images resembled arms. This human review resulted in the exclusion of two galaxies from the sample. This counter-measure however directly contradicts the benefits of an automatic system. To improve this the average SFT power spectrum value could be used as an estimate of the spatial distribution of the flux resembling spiral structure.

The background estimation issue being only present in the two lowest signal to noise bands is not a massive issue as morphological estimation is consistent across the spectrum. The estimates from each band weighted by the signal to noise of the image provide a suitable classification system with consistent results to GZ2. GAX takes input the background level and is set as standard for SDSS images as 1000 counts, however to counteract the background issue the minimum of the smoothed fit to the azimuthal average of the image could be set as background value to remove the possibility of summation of large amounts of negative flux. By increasing the number of bands the average weighted classification is calculated over this would in turn increase the accuracy of the classification.

Both the bulge and bars of galaxies are well described by small circular high Sérsic index and larger heavily elliptical lower Sérsic index profiles NEED REFERENCE. Due to the functionality of GAX being a Sérsic profile fitter both the bulge and bars could in future be non parametrically removed from the resulting arm extracted image, removing the need for bulge radial exclusion and increasing the arm flux total. GAX also has the ability to fit multiple sources within an image simultaneously due to its primary functionality to fit low surface brightness galaxies in wide field galaxy cluster images to study intra-cluster light. The fitting could potentially be applied to the bulge and disk simultaneously however multiple iterative fitting over the same confined spatial distribution may end up counteracting each other and requires testing. By extraction of the bar through successive fitting the tool would become effective for all morphologies and could create a system for classifying the flux contribution from each component.

For the purpose of this analysis all the galaxies in the sample are single nucleated however this method would definitely not work for a dual nucleus galaxy as the tool assumes the galaxies are well fit by a single Sérsic profile. The tool as a result is should only be applied to regular galaxy morphologies.