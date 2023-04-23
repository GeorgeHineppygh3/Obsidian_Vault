---
s:: true
---
Review of the paper [Origin and structure of the galactic discs - Schonrich and Binney.pdf](../../../PDFs/Origin%20and%20structure%20of%20the%20galactic%20discs%20-%20Schonrich%20and%20Binney.pdf). 

## Abstract:

We examine the chemical and dynamical structure in the solar neighbourhood of a model Galaxy that is the endpoint of a simulation of the chemical evolution of the Milky Way in the presence of radial mixing of stars and gas. Although the simulation’s star formation rate declines monotonically from its unique peak and no merger or tidal event ever takes place, the model replicates all known properties of a thick disc, as well as matching special features of the local stellar population such as a metal-poor extension of the thin disc that has high rotational velocity. We divide the disc by chemistry and relate this dissection to observationally more convenient kinematic selection criteria. We conclude that the observed chemistry of the Galactic disc does not provide convincing evidence for a violent origin of the thick disc, as has been widely claimed.

## Introduction:

- [Gilmore & Reid 1983.pdf](../../../PDFs/Gilmore%20&%20Reid%201983.pdf) Split the stellar disk model into two vertical and radial components. Both exponential profiles.
- Thick disk origins are supported by traditional chemical evolution models where there was initial high star formation rates in the early life followed by a cease in star formation rate. During this pause the ISM could be enriched by Iron by Type Ia supernovae (SNeIa) and overall metalicity could be reduced by the accretion of metal-poor gas. See [Chiappini_1997.pdf](../../../PDFs/Chiappini_1997.pdf). 
- [Schonrich & Binney 2009.pdf](../../../PDFs/Schonrich%20&%20Binney%202009.pdf) showed that radial mixing ( an unavoidable consequence f the structure ) causes a two component disc. In this simple model the Star Formation Rate (SFR) is a monotonically declining function of time from its global maximum.

## The Model:

- The [SB09 model](./SB09%20model.md) is the endpoint of a simulation of chemical evolution within a disc in which the SFR is controlled by the density of the ISM. This was sown by [Kennicutt 1998.pdf](../../../PDFs/Kennicutt%201998.pdf).
- The gas disc has an exponential surface density with scale-length 3.5 Kpc
- The stellar disc has an exponential surface density with scale-length 2.5 Kpc
- Model adopts Kennicutt's Initial mass function and stellar lifetimes/yields.
- New feature that the model assumes - radial flow of gas within the disc and radial migration of stars.
- The radial migration of stars occurs due to Churning (change in stars angular momenta) and Blurring (an effect due to stars increasing eccentric and inclined orbits)
- Most models omit blurring
- The model accounts for the extent of the churning using a parameter $k_{ch}$ - The radial dependence of which was taken to be proportional to the product of surface density and radius (based on arguments of disc instability)
- Hot gas assumed to be too far from the disc to take part in churning.
- There is no basis for quantifying impact of velocity dispersion on churning and so the affects are ignored.
- The inflow of gas within discs allows  the surface density of star formation to follow an exponential even where the accreted gas distribution is not exponential.
- Model employs parameters $f_A$ and $f_B$ which model the cosmic in-fall of metal poor gas and the flow of gas.
- $f_B$ is effectively set by the measured oxygen gradient in the ISM and $f_A$ is fitted alongside $k_{ch}$ to the local metallicity of stars
- The random velocities of stars formed at a given radius are assumed to increase with age as $\\tau^{1/3}$  
- The model has been slightly modified by increasing $\\left<v_R\\right>^{1/2}$ from 38 to 45 km $s^{-1}$ 
- It is assumed that the square of the intrinsic velocity dispersion at a given age is assumed to scale with radius as $e^{\\frac{-R}{1.5R_*}}$, where $R_*=2.5\\,Kpc$ is the scale length of the disc such that $\\left<v_R\\right>^{1/2} \\approx \\, 90\\,Km\\,s^{-1}$ at $R=R_*$. Vertically velocity dispersion is steeper (implying constant scale height) proportional to $e^{-R/R_*}$ 

## Model Predictions:

- The principle traces of radial mixing are the large dispersion in the metallicities of stars in the solar neighbourhood and strong increase in the dispersion with age.
- This is caused by the immigration of high metallicity stars inwards and low metallicity stars outwards. SB09 demonstrated that it is impossible to fit the shape of the local metallicity distribution without radial mixing.
- radial migration has a big impact on the interdependence of kinematics and chemistry
- There is a tight relationship between Fe/H and rotational velocity for a given value of $\\alpha$/H. The relationship shows that for high Fe/H => low rotational velocity ( due to stars with high Fe/H being immigrants form smaller radii deficient in angular momentum ) and vice versa
- This correlation is qualitatively consistent with stars being scattered to more eccentric orbits while retaining angular momenta horizontally (Blurring)
- more rapid decline of $\\alpha$/Fe at small radii
-  The velocity dispersion of stars born at any given radius scales with the third power of age
- Velocity dispersion increases inwards
- for any given date of birth more metal-rich stars are born at smaller radii
- the mean metallicity falls with increasing $|z|$ 
- model expected to underestimate the  vertical metallicity gradient on account of  our assumption that a stars velocity dispersion is a result of its birth radius
- A better model would take account of the actual migration paths of stars – how long each star spent with its guiding centre at each radius. ( could this be something?? )
- Model predicts smaller scaleheights for populations of stars born in the inner disc therefore might over predict fraction of high metallicity stars at high altitudes
- The metallicity distribution at high altitudes depends on the weakly constrained early evolution of the disc and on details of mixing
- The model reveals the bimodal structure of metallicities at different hights
- The exact shape of the peaks depends on the assumptions around gas enrichment and  behaviour of [SNeIa](./SNeIa.md)

#### Disk Division:

- It is defined that 'Thick disc' stars are stars which lie above the straight line though figure 8.
- There appears to be no concrete selection criteria which can effectively separate the thick and thin disc star models
- thick discs show larger asymmetric drift than thin discs
- faster enrichment of metallicity is expected in denser inner disc
- essentially all thick disc stars are older than 6 GYr
- most stars in the intermediate population are this old but few are older than 10 Gyr
- a lot of thick disc stars are older than 10 Gyr 'the way the rise follows the decline in intermediate population is very striking'
- older stars formed before SNeIa started to enrich the ISM with iron
- high $\\alpha$ stars modal rotation velocities almost circular
- metal rich portion of the thick disc has mean asymmetric drift 30 km $s^{-1}$ lower than the thin disc
- for any star formed at a given time and place increasing velocity dispersion is demonstrated
- the thin disc is hotter and slower rotating
- The tails in the distribution are due to small numbers of very old stars born at small radii where there is large velocity dispersion
- model uses density profile as sum of two exponentials in $|z|$ 
- model concludes 13% of solar neighbourhood stars belong to the thick disc

#### Kinematic Division of the Disc

- it is much easier to measure the velocity of a star than its metallicity
- samples of local stars are divided into thin and thick disk stars using Distribution Functions (DF's)
- Distribution function:
$$f(U,V,W) = kf_i\\,exp\\biggl[ -\\frac{U^2}{2\\sigma_{U}^2}-\\frac{(V-V_{asym})^2}{2\\sigma_{V}^2}-\\frac{W^2}{2\\sigma_{W}^2}\\biggr]$$
- where $k=(2\\pi)^{-3/2}(\\sigma_U \\sigma_V \\sigma_W)^{-1}$ is the standard normalisation constant and $f_i$ is the relative weight of the population.
- U, V, W are:
- dispersions $\\sigma_i$ are assumed to be lower in thin disc than thick
- dispersion must increase inwards -therefore stars with guiding centres $R<R_0$ are likely to be high velocity stars
- kinematic selection of stars from a chemical component is unclean (cant be done well)
- a large fraction of the thick disc is also excluded from a kinematically selected sample of thick-disc stars, and many of the excluded stars will be assigned to the thin disc because they lie within the region reserved for the thin disc
- The kinematically selected thin disc includes high $\\alpha$ stars in contrast to our chemically selected thin disc
- most stars formed at large radii to be kinematically assigned to the thin disc
- kinematic selection allows for younger stars

## Conclusions:

- 'A very straightforward conclusion is that kinematic selection inevitably misallocates many stars, adding both old stars to the thin disc and young stars to the thick disc'
- Thin-disc stars are all younger than 7 Gyr and are on fairly circular orbits
- The stars of the metal-rich thick disc are nearly all older than 8 Gyr and are on significantly non-circular orbits with guiding centres inside $R_0$ 
- The metal-poor thick disc consists exclusively of stars older than 10 Gyr ( stars are on average higher in angular momenta and smaller velocity than metal-rich thick)
- The metal-rich thick disc can be considered to be a superposition of isothermal components with radial velocity dispersions between 50 and 80 km $s^{−1}$, strongly peaked around 60 km $s^{−1}$.
- rongly  $\\alpha$ enhanced stars, there is an extremely strong negative correlation between $\\alpha$ and V.
- Thick disc has similar properties to the Galactic bulge according to [Meléndez_2008.pdf](../../../PDFs/Mel%C3%A9ndez_2008.pdf) 
- This conclusion is natural in the context of the SB09 model in which the metal-rich disk is made up of stars that have migrated to the sun from the inner disc where rapid star formation enriched the ISM to significant metallicities before SNeIa began to lower $\\alpha$/Fe 
- it is expected that the thick disk stars of the solar neighbourhood are now bulge stars
- there is absolutely no *evidence* that the thick disc has a violent origin