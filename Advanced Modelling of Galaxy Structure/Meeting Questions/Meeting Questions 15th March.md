---
s:: true
---

### What has been done:

- Created code that will generate a config file from a filename
- Further created code to then create config files for all bands from a filename/GZ2 ID
- tried to create some code to look at max power radially - don't think it is right 


===============================================================

### Questions for Steven

- What you think about de-projecting galaxies that are more inclined?
	- What uncertainties would be introduced by this? interpolation problems?

A.  suggested don't worry use ellipticity and position angle form fit and incorporate that into the transform on the basis: $r =\\sqrt{x/a +y/b}$ where $a$ and $b$ represent the axis ratios from the ellipticity as: $q =b/a$ 


- What do you think about developing a 2Dfft system that identifies the dominant spatial image modes in polar coordinates to count the number of arms?
	- how would one change the basis function for a 2dfft algorithm?

A. He thought good

- Idea would be use the 2dfft code to estimate the spiral pitch and be able to fit a line through them - the intensity gradients normal to the fitted line could then be measured across different bands 

A. he thought very good

- how can we que the config files up so that we can run batches

A. going to use the running of the main function

- what steps are necessary to run the code on the servers?

A. sorted

===============================================================