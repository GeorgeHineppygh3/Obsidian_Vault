---
s:: true
---
---
s:: true
---
---
s:: true
---
K correction converts measurements of astronomical objects into their respective rest frames. The correction acts on that object's observed magnitude (or equivalently, its flux). Because astronomical observations often measure through a single filter or bandpass, observers only measure a fraction of the total spectrum, redshifted into the frame of the observer. For example, to compare measurements of stars at different redshifts viewed through a red filter, one must estimate K corrections to these measurements in order to make comparisons. If one could measure all wavelengths of light from an object (a bolometric flux), a K correction would not be required, nor would it be required if one could measure the light emitted in an emission line.

Carl Wilhelm Wirtz (1918), who referred to the correction as a Konstanten k (German for "constant") - correction dealing with the effects of redshift of in his work on Nebula. English-speaking claim for the origin of the term "K correction" is Edwin Hubble, who supposedly arbitrarily chose $K$ to represent the reduction factor in magnitude due to this same effect and who may not have been aware / given credit to the earlier work.

The K-correction can be defined as follows:
$$
M = m - 5(log_{10}D_L - 1) - K_{Corr}
$$
I.E. the adjustment to the standard relationship between absolute and apparent magnitude required to correct for the redshift effect. Here, DL is the luminosity distance measured in parsecs.

The exact nature of the calculation that needs to be applied in order to perform a K correction depends upon the type of filter used to make the observation and the shape of the object's spectrum. If multi-colour photometric measurements are available for a given object thus defining its spectral energy distribution (SED), K corrections then can be computed by fitting it against a theoretical or empirical SED template. It has been shown that K corrections in many frequently used broad-band filters for low-redshift galaxies can be precisely approximated using two-dimensional polynomials as functions of a redshift and one observed colour. This approach is implemented in the K corrections calculator web-service.