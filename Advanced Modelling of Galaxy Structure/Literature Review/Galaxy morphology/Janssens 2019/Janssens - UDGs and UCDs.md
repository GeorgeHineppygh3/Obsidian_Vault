---
s:: true
---
---
s:: true
---
---
s:: true
---
UDG - Ultra Diffuse Galaxies
UCD - Ultra Compact Galaxies

## Introduction: ##

UDGs - typically defined in morphological terms as very extended stellar systems with large effective radii - ($R_e > 1.5kpc$), low Sérsic (See: [Sérsic Profiles](./S%C3%A9rsic%20Profiles.md)) indices ($n<1.5$) and characteristic surface brightnesses fainter than $~24\\, mag\\;\\; arcesec^{-2}$ ( roughly Milky way sized).

UDGs appear to be quenched systems and occupy the red sequence in clusters

- Axial ratios of UDGs - mean ~ 0.7 (prolate)
- very few with axial ratios lower than ~0.4
- low $\\frac{V_{rot}}{\\sigma}$ suggests UDGs are dispersion-dominated systems not rotationally supported by thick disks.
- Possibly related to low surface-brightness dwarf spheroidals

It was previously thought that UDGs are dark matter dominated failed $L^*$ galaxies which lost their gas supply in the early times.

#### Formation: ####

Many theories on formation channels.

Failed massive halo scenario:
- extreme feedback from supernovae and young stars
- ram pressure stripping
- feedback from galactic nuclei

Rare UDGs with no DM Halo could be due to collisions of dwarfs in protogroup environments.

Janssens $\\Lambda CDM$ cosmological model assumes: $\\Omega_m = 0.3$, $\\Omega_\\Lambda=0.7$ and $H_0= 70\\, kms^{-1}\\;MPC^{-1}$ and applies galactic extinction corrections from all extinction maps (Schlafly & Finkebeiner).


## Data: ##

Used Hubble Space Telescope Frontier Fields image of six highly lensed clusters.

Cluster information:

![Pasted image 20221115180253.png](../../../../Assets/Pasted%20image%2020221115180253.png)

## Methodology: ##

Source detection:
- run SExtractor
- low exposure time regions removed

Structural Parameters:
- run GALFIT to fit single component Sersic model on objects bighter than $mag\\;=\\;28$ 
- PSFEx to supply Galfit with point spread functions (PSF)
- polynomial maps the variability of the PSF accross the image
- use the RMS map and reduced images to create a total noise map to pass to GALFIT
- Poisson noises from sources are added to the RMS map
- compute absolute magnitudes and sizes from GALFIT model parameters

Mean surface brightness is calculated from the circularised effective radii $R_{e,c}= R_e \\sqrt{b/a}$ .
$$ \\left< \\mu\\right>_{e} = m + 2.5log(2\\pi R_{e,c}^2) $$ and absolute mean surface from:
$$ \\left< \\mu\\right>_{e,abs} = \\left< \\mu\\right>_{e} - 2.5log(1+z^4) - E(z)
 - K(z)$$ where z is the cluster redshift $E(z)$ and $K(z)$ are the evolutionary K-corrections respectively. [K corrections](K%20corrections.md)

UDGs:
similar to previous work in 2017 and Burg 2016.
Transform surface brightness in r-band into a cut.

Cuts:
1. Circularized half-light radius $1.5\\,Kpc\\,<\\,R_{e,c}\\,<10\\,Kpc$ 
2. Sersic index $n<4$ 
3. Absolute mean surface brightness within $R_e$        $\\left< \\mu\\right>_{e,abs}>24.1\\,mag\\,arcsec^{-2}$ 
4. Axis ratio ($q=b/a$)    $q>0.3$ 
5. Photometric redshift  $z_{phot}<1$
6. within WFC3/IR  footprint for uniform photometric accuracy

Matched the catalogue to [ASTRODEEP](ASTRODEEP.md) using nearest neighbour of 5 pixels


![Pasted image 20221115212259.png](Pasted%20image%2020221115212259.png)  
Caption: Locations of UDGs (red points)in the six cluster core fields. The background images are the ACS F814W images and the pink borders are the extent of the  
WFC3/IR coverage. North is up and east is to the left. The bars below the compasses correspond to 200 kpc. Insets show zoom-ins on select UDGs, the sizes of which  
are 15 kpc a side.

UDG's appear to not be distributed very evenly and avoid the centres of the clusters

## Background Correction: ##

Distant high $z$ galaxies appear very similar to UDGs so are removed by assuming all Extreme Deep field galaxies  are $z=0.308-0.545$ lie at the redshift of the target cluster the objects are matched using the UVUDF photo-z catalogue.

## Image simulations: ##
First simulated 2000 object placed at random positions.

Simulated object  parameters using GALFIT:
- Sersic index $n = 1$ 
- circularised effective radius $1.5\\,Kpc\\,< R_{e,c} < 10\\,Kpc$ 
- central surface brightness $17\\,mag\\;arcsec^{-2} < \\mu_0 <0.3\\,mag\\;arcsec^{-2}$ 
- axis ratio $0.3<\\frac{b}{a}<1.0$  
- position angle $0°<\\theta<360°$

## Ultra-compact Dwarf Selection: ##

Applied a medium filter with a kernel size of 15 pixels to remove low frquency power from the image. 
Magnitudes were measured using aperture of 33.3 pixels and PSFEx was employed again as PSF varied across image. 

Point sources were selected based on shape requiring $e=1-\\frac{b}{a}<0.4$ 
and `FLUX_RADIUS`$<10$ pixels and $0.8<C_{3-7}<1.2$ where $C_{3-7}$ represents the difference in magnitude between the 3 and 7 pixel diameter apertures. - Select UCDs from only denses environments.

# Results and Discussion: #

## Radial distributions: ##
![Pasted image 20221116100245.png](Pasted%20image%2020221116100245.png)
Caption:   
Profiles of radial surface number density of UDGs in the six FF clusters. For each cluster, the points in the leftmost panels are the raw observed surface  
densities and the dotted line is the density of background sources estimated from the XDF. The rightmost panels shows the completeness fractions in each bin  
determined from our image simulations (see text for details). The middle panels show the radial profiles after correcting for completeness and subtracting off the  
estimated background contamination. The hatched shaded regions denote radii with no coverage (e.g., between the cluster and parallel fields)



Central depletion or flattening out of radial profile observed on cluster cores most likely from tidal disruption.

## The abundance of UDGs ##


Abundance is calculated from using surface number density (radial profile) and integrating out to $R_{200}$.
Using power law best fit relationship can estimate:
$$N_{UDG}=(19 +- 2)[\\frac{M_{200}}{10^{14}M_o}]^{1.13+-0.06}$$
which shows that there is good agreement to van de burg et al 2017

## Spatial Distributions: ##

![Pasted image 20221116101806.png](Pasted%20image%2020221116101806.png)
Caption:
Top: maps showing the projected spatial distributions of various components of the clusters A2744 and AS1063 within the WFC3 cluster fields (pink border). The black line in the lower right measures 200 kpc in length. Locations of UCDs are marked in black, UDGs in red, and other cluster galaxies (labeled Gs) are marked in blue. The X’s mark different possible adoptions of the cluster center: pink, the BCG center (that listed in Table 1); blue, the mass surface density peak from gravitational lensing; and red, the mean UDG location. The blue–green contours trace the surface mass density of the cluster from gravitational lensing (Merten et al. 2009, 2011; Zitrin et al. 2009, 2013), while the red–yellow contours are Chandra X-ray fluxes. Labels in black correspond to cluster substructures from the literature. In A2744, “Core,”“NW,”and “S1”are the three substructures identified by Jauzac et al. (2016)that are in proximity to the WFC3 field. The single cluster-scale mass component coincident with the BCG found by Richard et al. (2014)is marked “1”in AS1063. UDGs appear deficient in the most dense cluster environments, with UCDs instead being abundant toward the cluster centers. No relationship between UDG locations and the X-ray flux (tracing the hot ICM)is  
observed, as is expected if UDGs are gas-poor systems. Middle: A370 and MACS0416. In A370, 1–4 mark the positions of DM1–DM4, the four “large-scale” mass components identified by Lagattuta et al. (2019). In MACS0416, NE and SW mark the positions of the two main dark matter halos comprising its core, while S1 and  S2 are two additional galaxy group-sized (∼1013 Me) substructures, all from Jauzac et al. (2015). Bottom: MACS 1149 and MACS 0717. In MACS 1149, the  
positions of the three subclusters identified by Golovich et al. (2016)are marked 1, 2, and 3. In MACS 0717, A, B, C, and D mark the NFW fit positions from  
Limousin et al. (2016)of the light peaks found by Ma et al. (2009)in the cluster core.



Lopsidedness has been clearly demonstrated by the histograms below:

![Pasted image 20221116102715.png](Pasted%20image%2020221116102715.png)
Incomplete image taken from full image shows the uneven distribution of UDGs
# Conclusions:#

1. the six clusters observed between 200-1400
2. this is consistent with abundance halo relations
3. slope of relation is weakly non linear  and suggests UDGs are more easily destroyed in low mass halos or UDGs are created in clusters
4. not uniformly distributed
5. only in the most relaxed clusters distributed uniformly
6. location of UDGs and UCDs anticorrelated
7. 3x more abundant in higher mass systems
8. tidal disruption probably produces UCDs
9. the destruction of UDGs