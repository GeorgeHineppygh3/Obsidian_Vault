---
s:: true
---

- [x] Create a flux fraction graph - 3 days
- [x] create code that looks at the difference in offset angle (argument of $A(p_{max},m)$) across different bands - 1 
	- [x] added to gen spiral and output of spiral fourier
- [ ] create a python file for the batch running of SFT
	- [ ] adapt the fits table to hold multiband info
	- [ ] include the normal image as an output  - 2 days
	- [ ] work out a good way of finding `R_min_multiple` [THIS NEEDS THOUGHT]
		- [ ] create an augmentation of multi_band_imshow that applys successive anuli for human classification
- [ ]  create a function for calculating winding angle vs colour
	- [ ] not sure on this one I think steven means average the winding angle across the relevant bands and then plot against the overall U-R of the galaxy
- [ ] create a notebook for the reading of the batch SFT data - 4 days
- [x] create a notes document for the normal image process - 1 day
- [ ] review document plan and think about structure - unknown
- [ ] create a function which compares the `R_e` across bands from a comp table to create a mask that separates images that need more attention and less for `R_e_multiple` development
	- [ ] this is not going to work instead we need to make a classifying function that will work off of a candidate list

- [ ] create structure for presentation
	- [ ] create non-param extraction animation
		- [ ] create code for gathering all the images together
		- [ ] make the images into a gif (DS9 ?) - need to try older version
	- [ ] create slides for SFT
	- [ ] create slides for normal
	- [ ] create slides for flux fraction
	- [ ] 

