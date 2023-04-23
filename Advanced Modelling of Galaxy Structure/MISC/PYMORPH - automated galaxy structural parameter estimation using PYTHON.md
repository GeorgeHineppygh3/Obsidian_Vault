---
s:: true
---

## Paper:
- [PYMORPH - automated galaxy structural parameter estimation using PYTHON](PYMORPH%20-%20automated%20galaxy%20structural%20parameter%20estimation%20using%20PYTHON.md)


## Documentation:

- https://statmorph.readthedocs.io/en/latest/notebooks/tutorial.html
Using pymorph?

```run-python
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
from astropy.visualization import simple_norm
from astropy.modeling import models
from astropy.convolution import convolve
import photutils
import time
import statmorph
%matplotlib inline

print('Gini =', morph.gini)

```

**Measuring morphological parameters**

Now that we have all the required data, we are ready to measure the morphology of the source just created. Note that we include the PSF as a keyword argument. In principle, this results in more correct Sersic profile fits, although it can also make the code run slower, depending on the size of the PSF.

[10]:

start = time.time()
source_morphs = statmorph.source_morphology(
    image, segmap, gain=gain, psf=psf)
print('Time: %g s.' % (time.time() - start))

Time: 2.41027 s.

In general, `source_morphs` is a list of objects, each corresponding to a labeled source in the image. Here we focus on the first (and only) labeled source.

[11]:

morph = source_morphs[0]

Now we print some of the morphological properties just calculated:

[12]:

```run-python
print('xc_centroid =', morph.xc_centroid)
print('yc_centroid =', morph.yc_centroid)
print('ellipticity_centroid =', morph.ellipticity_centroid)
print('elongation_centroid =', morph.elongation_centroid)
print('orientation_centroid =', morph.orientation_centroid)
print('xc_asymmetry =', morph.xc_asymmetry)
print('yc_asymmetry =', morph.yc_asymmetry)
print('ellipticity_asymmetry =', morph.ellipticity_asymmetry)
print('elongation_asymmetry =', morph.elongation_asymmetry)
print('orientation_asymmetry =', morph.orientation_asymmetry)
print('rpetro_circ =', morph.rpetro_circ)
print('rpetro_ellip =', morph.rpetro_ellip)
print('rhalf_circ =', morph.rhalf_circ)
print('rhalf_ellip =', morph.rhalf_ellip)
print('r20 =', morph.r20)
print('r80 =', morph.r80)
print('Gini =', morph.gini)
print('M20 =', morph.m20)
print('F(G, M20) =', morph.gini_m20_bulge)
print('S(G, M20) =', morph.gini_m20_merger)
print('sn_per_pixel =', morph.sn_per_pixel)
print('C =', morph.concentration)
print('A =', morph.asymmetry)
print('S =', morph.smoothness)
print('sersic_amplitude =', morph.sersic_amplitude)
print('sersic_rhalf =', morph.sersic_rhalf)
print('sersic_n =', morph.sersic_n)
print('sersic_xc =', morph.sersic_xc)
print('sersic_yc =', morph.sersic_yc)
print('sersic_ellip =', morph.sersic_ellip)
print('sersic_theta =', morph.sersic_theta)
print('sky_mean =', morph.sky_mean)
print('sky_median =', morph.sky_median)
print('sky_sigma =', morph.sky_sigma)
print('flag =', morph.flag)
print('flag_sersic =', morph.flag_sersic)
```
 
xc_centroid = 120.57974325587848
yc_centroid = 96.54876631751854
ellipticity_centroid = 0.49504651780554065
elongation_centroid = 1.980380441489651
orientation_centroid = -0.5025297323963465
xc_asymmetry = 120.49795192600573
yc_asymmetry = 96.5041141987735
ellipticity_asymmetry = 0.49503516784340607
elongation_asymmetry = 1.9803359289977076
orientation_asymmetry = -0.5025187596927418
rpetro_circ = 32.10584845059099
rpetro_ellip = 43.15534219578999
rhalf_circ = 14.607365607744995
rhalf_ellip = 19.197894171055044
r20 = 5.072220422468954
r80 = 26.11103164489153
Gini = 0.5674867473634592
M20 = -2.073215859383315
F(G, M20) = 0.2857979900017602
S(G, M20) = -0.05336512456445619
sn_per_pixel = 55.04891460404779
C = 3.5581295638595445
A = -0.0003891696891799785
S = 0.010867687703064226
sersic_amplitude = 1.0017449025553842
sersic_rhalf = 19.980728153552768
sersic_n = 2.496959225794045
sersic_xc = 120.50130875759518
sersic_yc = 96.50065293649406
sersic_ellip = 0.49994266664181736
sersic_theta = 2.6415533250460546
sky_mean = 0.00021039195094124476
sky_median = -1.9658131250737553e-06
sky_sigma = 0.010284385196536397
flag = 0
flag_sersic = 0

Note that the fitted Sersic profile is in pretty good agreement with the “true” Sersic profile that we originally defined (n=2.5, r_eff=20, etc.). However, such agreement tends to deteriorate somewhat at higher noise levels and larger Sersic indices (not to mention that real galaxies are not always well described by Sersic profiles).

Other morphological measurements that are more general and more robust to noise, which are also calculated by statmorph, include the Gini-M20 (Lotz et al. 2004), CAS (Conselice 2003) and MID (Freeman et al. 2013) statistics, as well as the outer asymmetry (Wen et al. 2014) and shape asymmetry (Pawlik et al. 2016).

Also note that statmorph returns two quality flags:

1.  `flag` : indicates the quality the basic morphological measurements, taking one of the following values: 0 (good), 1 (suspect), 2 (bad), or 4 (catastrophic). More details can be found [here](https://statmorph.readthedocs.io/en/latest/description.html#output).
2.  `flag_sersic` : indicates if there was a problem/warning during the Sersic profile fitting: values of 0 and 1 indicate good and bad fits, respectively.

In general, `flag <= 1` should always be enforced, while `flag_sersic == 0` should only be used when one is interested in Sersic fits (which might fail for merging galaxies and other “irregular” objects).