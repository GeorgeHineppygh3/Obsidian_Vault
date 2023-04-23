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


## Relations:
- Paper: [MegaMorph – multiwavelength measurement of galaxy structure - complete Sersic profile information from modern surveys - B. Haussler et. al.pdf](../../../PDFs/MegaMorph%20%E2%80%93%20multiwavelength%20measurement%20of%20galaxy%20structure%20-%20complete%20Sersic%20profile%20information%20from%20modern%20surveys%20-%20B.%20Haussler%20et.%20al.pdf)

### Un-defined Terms:
- GAMA: Galaxy And Mass Assembly - survey
- S/N : Signal to Noise

### Abstract:

- demonstrate a new method for fitting galaxy profiles which makes use of the full multiwavelength data
- new version of GALAPAGOS which utilizes GALFITm
- tested on data from GAMA and simulated data made to the same spec
- find that fitting galaxy light profiles with multiwavelength data increases the stability and accuracy of the measured parameters - produces more complete and meaningful multiwavelength photometry
- improvement is particularly significant for magnitudes in low-S/N bands
- improvement also significant for structural parameters like half-light radius $r_e$ and Sérsic index $n$ 
- allows fit to go to higher magnitudes for fainter galaxies
- technique uses a smooth transition of galaxy parameters with wavelength - allows accurate interpolation between passbands, good for derivation of rest-frame values


### Conclusion:

- real data selected nine-band (ugrizYJHK) data from the GAMA survey
- Simulations were created following H07
- Multiband fitting significantly improves the recovery of galaxy magnitudes, at least in the lower S/N bands
- The multiband approach returns more accurate results than treating the bands independently
- multiband fitting is able to derive reliable values for ∼75 times more galaxies in SDSS u-band data than the single-band approach
- single-band fits occasionally return results which are affected by the constraints that are provided by GALAPAGOS and used by GALFITm during the fitting process -Multi bands do not have this issue and so are more stable and less likely to return no fit
- Multi band fitting produces better interpolation
- single-band fits return more or less equivalent results for bright galaxies, multiband fitting provides a more homogenous data set
- multiband code can be run on fainter objects
- number of scientifically useful galaxies as a result increase by factor of 16 for (griYHK) (6 band)
- number of scientifically useful galaxies as a result increase by factor of 180 for (ugrizYJHK) (9 band)
- multiband fitting instead of single-band fitting improves both quality and quantity of galaxy fits on survey data
