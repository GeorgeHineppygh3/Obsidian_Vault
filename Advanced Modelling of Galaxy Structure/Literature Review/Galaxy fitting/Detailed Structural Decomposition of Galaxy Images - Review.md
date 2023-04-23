---
s:: true
---
---
s:: true
---
---
s:: true
---
### Disclaimers:
NONE

## Relations:
- Paper: [Detailed Structural Decomposition of Galaxy Images - Peng et. al - GALFIT origin.pdf](../../../PDFs/Detailed%20Structural%20Decomposition%20of%20Galaxy%20Images%20-%20Peng%20et.%20al%20-%20GALFIT%20origin.pdf)

### Un-defined Terms:
- NONE

### Abstract:

- 2D fitting algorithm designed to extract structural components from galaxy images
- specifically works well for modelling light profiles of spatially well-resolved, nearby galaxies
- algorithm improves ion previous techniques by:
	- being able to simultaneously fit a galaxy with an arbitrary number of components and with optimization in computation speed
- Uses 2d model using: [Nuker Profile](./Nuker%20Profile.md)s, [Sérsic Profiles](../Janssens%202019/S%C3%A9rsic%20Profiles.md), exponential discs, and Gaussian or [Moffat](./Moffat.md) distribution
- The azimuthal shapes are generalized ellipses that can fit discy and boxy components
- Uses for the program:
	- standard modelling of global galaxy profiles
	- extracting bars
	- stellar discs
	- double nuclei
	- compact nuclear sources
	- measuring absolute dust extinction
	- measuring surface brightness fluctuations after removing the galaxy model
- found that even simple looking galaxies generally require at least three components to be modelled accurately
- found that galaxies with:
	- complex isophotes
	- ellipticity changes
	- position angle twists
- can be modelled accurately in 2D
- Work was demonstrated on a sample of 11 galaxies including: spirals, bars highly discy lenticular galaxies and elliptical galaxies of various complexities
- Extension for the algorithm - extract nuclear point sources in galaxies

### Conclusion:

- can model the central regions of galaxies accurately
- After the major components are removed, in a number of systems discovered evidence of galaxy substructures too subtle to be seen in the original image - like: nuclear point sources, low-level dust patterns, stellar disks and stellar bars
- number of components can reveal information about its evolutionary history
- Substructure may also signal triaxiality in the bulge potential
- future research would be to compare the structural decomposition of real galaxies with a similar analysis applied to high-resolution N-body simulations of galaxy formation - couple the two dimensional structural analysis with integral-field kinematic maps
