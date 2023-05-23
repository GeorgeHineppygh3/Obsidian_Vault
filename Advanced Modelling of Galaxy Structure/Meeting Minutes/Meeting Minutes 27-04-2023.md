---
s:: true
---

#### Attendance:

- Steven

 - Shivani 
 - George 



#### Topics covered:

1. Did Steven get the email with the link to my Obsidian vault on GitHub?
https://github.com/GeorgeHineppygh3/Obsidian_Vault

2. Fixed flux fraction to exclude the bulge by assuming bulge radius of 0.3$R_e$ :
![Pasted image 20230427140624.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230427140624.png)
U band and Z band having issues so excluded - 3 bands is still enough for wavelength dependence right?

Allowing us to select the galaxy with the least spiral arms and the galaxy with the most:
![Pasted image 20230427140653.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230427140653.png)
Proves quantitative way to measure morphological arm prominence


3. Using the normal sampled image created the colour through the difference in flux's:
![Pasted image 20230427140748.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230427140748.png)
![Pasted image 20230427141201.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230427141201.png)
4. Then created the colour through the $-2.5\\,log(band_1/band_2)$ :
 Try a different colourmap with red at the top
![Pasted image 20230427140334.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230427140334.png)
![Pasted image 20230427141208.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230427141208.png)

5. What graphs can we make from our statistical data?
- NSA and GZ2 parameters
- flux fraction of arms
- flux fraction of bulge
- CAS before and after FICL

focus on a few
why is I so high?
how is the extraction affecting the data is the $R_e$ smaller in these bands 
look at 10-20 and compare the FICL extraction
demonstrate what we are measuring

compare findings to the galaxy zoo weighted fractions
strength of arms vs flux fraction ( straight ish line hopefully )
its okay to have a conclusion explaining why it doesnt work for the longer bands - explain why multiband would help this 

gini coeff minus bulge
does gini correlate with flux fraction in the arms

**Do:**
Uncertainties - critically reflect on trends using uncertainty
SDSS electron gain is fixed 
need an error on flux in spiral arms - convert flux to electron count and then assume a poisson distribution of electrons would give error bar on flux frac
colour error - use the standard deviation of radius - assume a larger variation than the uncertainty on each pixel propagated - standard error by dividing by the number of pixels
shaded region showing  hopefully should cover the random fluctuation 

could look at a region where you are pretty sre there is no dust - long shot





6. What else can we explore with our case studies?

#### Current plan:

- add all case studies to the statistical plot as a unique marker
- use SFT inner radius function to find stable region for plotting 
- use plotting to get normal line sampled image
- use normal line sampled image to demonstrate colour gradients away from arm centre
- link in to SFR and subsequent migration away from arm centre  - would be cool to try and plot a stellar maturity gradient - how would we do this?

Stellar population model - Bruzual & Charlot - 2003 'Stellar population modelling at the resolution of 2003'
SSP - form a mass of stars assuming an IMF - gives you zero time parameters and - convolve stellar spectrum with bands to get colours
assume all starts formed at the same time
CSP - instead of all at the same time yoo assume SFR properties

Metalicity changes colour - age-metallicty degeneracy  - would need hig res spectroscopy

Dust reddening (need to get galactic extinction) - this uncertainty would be too high 

**better off:**

- look for evidence that supports the data (dust reddening or metallicity distribution in the arm)
- Enough to have found it


- colour is not real colour right now - photometry is not calibrated - need a zero point (look in the header) - instrumental magnitude if can't find (will only shift the line)

this could be used with simple stellar population models

convince the reader the trend across the arm is real - can we see dust where the red feature is - if instead see groups of blue stuff (SF) 

plot isophotes on top of standard plots use BwR colourmap contours for the intensity 



- may be able to use a table using assumptions

**Ways I have been thinking about:**
- Get the colour magnitude position and then estimate progress along the main sequence
- Would we need to know metallicity? if so how could we estimate this?
- Would this be the same as using the ratio of flux's?

7. For the presentation since there are only 4/5 slides what would you recommend we focus on talking about?

Try and include everything - 1 slide for case studies then
Avoid detail - slides and figures should talk for themselves
defo include a spiral fit
hopefully spur their questions with this
visually interesting things
give the science motivation very broadly


1. What figures would you recommend we use?


3. M101 is failing - consistent error that appears - SHOW IN VSCODE
```
Original exception was:
Traceback (most recent call last):
  File "/home/ppygh3/miniconda3/envs/ficl/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/home/ppygh3/miniconda3/envs/ficl/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/home/ppygh3/ficl/ficl/main.py", line 711, in <module>
    sys.exit(main(**args))
  File "/home/ppygh3/ficl/ficl/main.py", line 54, in main
    sources = estimate_source_param(original_image, detection_parameters)
  File "/home/ppygh3/ficl/ficl/main.py", line 335, in estimate_source_param
    add_half_light_radii(cat, tbl)
  File "/home/ppygh3/ficl/ficl/main.py", line 357, in add_half_light_radii
    interp = interpolate.interp1d(df[i], k_arr, kind="cubic")
  File "/home/ppygh3/miniconda3/envs/ficl/lib/python3.10/site-packages/scipy/interpolate/_interpolate.py", line 616, in __init__
    self._spline = make_interp_spline(xx, yy, k=order,
  File "/home/ppygh3/miniconda3/envs/ficl/lib/python3.10/site-packages/scipy/interpolate/_bsplines.py", line 1293, in make_interp_spline
    raise ValueError("Expect x to not have duplicates")
ValueError: Expect x to not have duplicates
```

#### Suggested work going forward:

- Create flux fraction for the bulge
- Create python files for calculating the stat arrays on the server [Save time]
- Begin write up of the SFT section
- [x] sort out sending the M101 stuff over

- **Tuesday 2nd Meeting - 10:00**