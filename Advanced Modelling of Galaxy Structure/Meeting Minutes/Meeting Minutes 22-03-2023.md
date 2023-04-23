---
s:: true
---


#### Attendance:
- Steven

 - Shivani 
 - George 
 - Aden


#### Topics covered:

- Server running - too many at once - remove the & or try some parallel running maybe groups of 5 - speak to steven
- U band failure - either forget the U band or look at re-masking from the previous file (before atlas)
- Nasa Sloan Atlas - potential new data source 
- ManGa - potential new data source
- GZ2 catalogue 'ID' is the Sloan ID so perfect for cross reference
- Could use RA and DEC to match [Think this is probably most likely]
- run rerun camcol field obj - can be used to match using these as they are the same
- brightest sloan galaxies got rerun because they were having background issues - shredded galaxies will be fixed in that one
- the sloan galaxies have psf's as well
- flux fraction currently works out the fraction not in the arms - want one minus that and also need to divide by the total flux of the image
- gini coeff - masking zeros - ignore U - could use zeros in U?
- don't use for loops for the accumulator [see notebook for better method]
- p is the winding angle and so the peak in the distribution is actually over what it thinks is the most likely p value
- cos and sin are the wrong way round in the notebook [SWAP THIS LATER!!!] - fixed now don't worry lol
- divide R by R_e for winding angle at R_e
- data.galaxyzoo.org RAW classifications -  `GZ2_class` 
- bar fraction to3 bar 6 if it is above a certain value then can assume bar etc
- do pitch angle one with isolated one without
- add 1000 to the isolated image
- maybe increase the smoothing for the second run [smooth_sigma = 50-100 pixels] [smooth_size = 2-3x the sigma]
- first try a set value for R_min

#### Suggested work going forward:

- review the coord-transforms notebook that steven has made and look  at how he is doing the calculation to get to the Fourier coefficient amplitude
- 





===============================================================


