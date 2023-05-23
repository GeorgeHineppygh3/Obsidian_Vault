---
s:: true
---
Your text to be added
Your text to be added

To get the flux density from a flux value in an astronomy image array, you need to take into account the pixel scale and the wavelength of the observation.

The flux density is defined as the flux per unit area per unit wavelength. In astronomy, the flux is usually measured in units of counts or electrons, which need to be converted to physical units such as ergs or watts.


### Converting from counts to physical flux

B band: Central wavelength = 4350 Å, Bandwidth = 1030 Å

-   Gain: 1.97 e-/ADU
-   F435W: 4250 Å (QE = 0.62), 4700 Å (QE = 0.82), 5000 Å (QE = 0.84)

G band: Central wavelength = 4750 Å, Bandwidth = 1400 Å

-   Gain: 1.73 e-/ADU
-   F555W: 4918 Å (QE = 0.61), 5022 Å (QE = 0.73), 5150 Å (QE = 0.78)

R band: Central wavelength = 6250 Å, Bandwidth = 1700 Å

-   Gain: 1.74 e-/ADU
-   F814W: 7800 Å (QE = 0.68), 8200 Å (QE = 0.79), 8600 Å (QE = 0.78)

Collecting area of HST:
 - 4.0 $m^2$ 


Assuming you have converted the flux values to physical units, you can calculate the flux density using the following formula:

$$f_\\nu = \\frac{f}{((D_{pix})^2 \\Delta \\lambda)}$$

where $D_{pix}$ is the size of a pixel in arcseconds, and $\\Delta\\lambda$ is the width of the wavelength bandpass in angstroms. The resulting flux density will be in units of ergs/s/$cm^2$/angstrom. Since 1 Jansky ($Jy$) = $10^{-23}$ ergs/s/$cm^2$/Hz - convert the wavelength to a frequency and divide by $10^{-23}$.

To then get calibrated flux you divide the flux density by the zero point flux density of the equipment, $f_0$:
$$f_c = \\frac{f_\\nu}{f_0}$$

- The Hubble images have a zero points:
	- $4270\\,Jy$ - B band
	- $3610\\,Jy$ - G band
	- $2840\\,Jy$ - R band

This gives real flux and so from this you can get real colour.

