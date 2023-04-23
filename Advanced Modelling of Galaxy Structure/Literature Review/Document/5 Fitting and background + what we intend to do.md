---
s:: true
---
---
s:: true
---
---
s:: true
---
Paragraph from $\\rightarrow$ [Literature review Structure V2](./Literature%20review%20Structure%20V2.md)

## [300 Words]


GAX traces it's origin to GALFIT \\cite{peng2002detailed} which fits two dimensional: Sérsic, Moffat and Nuker profiles to single band images of galaxies using the programming language $C$. The original program minimised the Chi squared between the model and the observed flux to fit the profiles. GALFIT subsequently went through several evolutions where other single band fitting techniques were added \\cite{}[NEED A REFERENCE FOR GALFIT2 and GALFIT3]. The second evolution of GALFIT, GALFITM \\cite{haussler2022galapagos}, incorporated multi band imaging by weighting the bands primarily based on the respective signal to noise ratios. The fitting process was modified such that the structural parameters are weighted by user defined degrees of Chebyshev polynomials to allow for flexibility. The final evolution, GAX, re-writes GALFITM in python employing JAX libraries to execute fitting on GPUs to take advantage of the parallel calculation abilities to reduce run time.

The non parametric fitting uses the same model extraction techniques used in Johnston's bulge-disc decomposition \\cite{johnston2016sdss} by GALFITM. In the proposed work GAX would employ the extraction technique to instead perform arm-disc decomposition. After the model based exclusion of the spiral arms and disc, analysis of the luminosity and colour relationships between each will be performed. The analysis hopes to explore the contribution of the spiral arms to the global luminosity as well as the colour relationships/differences between them.

The code will first be run on a filtered Galaxy Zoo (GZ) dataset \\cite{lintott2011galaxy} consisting of grand design spirals with more easily recognisable spiral arms and low inclination angles. After fine tuning the extraction technique and ensuring low uncertainty measurements for luminosity contribution and colour relationships, the code will then be run on the unfiltered much larger GZ dataset. Further to this the code will then be applied to all viable candidates within the SDSS catalogue. Viable candidates will have sufficient spatial resolution and low enough inclination angles for spiral structure identification. 

As an extension the MATLAB code SPIRALITY \\cite{shields2015spirality}, which uses fits spirals of known winding angles to images to measure the winding angle, may be added to GAX. The code also contains Gen_Spiral which can produce images of spiral galaxies based on user defined parameter inputs. The synthetic images could then be used as tests for GAX by varying the structural parameters to see where the fitting process breaks down and why.