---
s:: true
---

## General:

- [x] Create overleaf document
- [x] Create document plan
- [x] create a function that runs flux fraction given a list of variables
- [x] plot flux fraction against each band flux fraction
- [x] Create a list of simple figures that can be made with 8 candidates
- [x] Create a list of figures for the document
- [x] Add rotation by argument of spiral Fourier component
- [x] Add spiral overlay line to figure plot function
- [x] Add a best fit line to flux frac plot weighted by the std of each band
	- [x] add bands as ticks for x axis
- [x] add plotting functionality to number of arms

## Document:

- [x] gather equations for SFT section
- [x] gather plots for SFT section
- [x] create plan document for SFT

## Spiral Overlay:

- [x] Add the other spiral arm (i.e. using number of arms)
	- [x] need a way of sampling p in a much more coarse way to select the second maxima rather than frequencies surrounding the primary maximum
	- [x] `argsort(A)` and select `p` that produces the highest `A` but furthest from `p_max` 
	- [x] I THINK the current method works but unfortunately is selecting the wrong second p
	- [x] if we need to look at the other arms use the derivative method to remove the global peak
		- [x] then look at the peak from the remaining distribution
- [ ]  Come to the realisation that we don't actually need the second arm we can still analyse shock front distributions in terms of just the one arm


## Server:

- [x] Download data
- [x] filter data for top 1000 spirals
- [x] run subset of 100

- [ ] create a python file for running sft and processing its outputs to a folder
- [ ] create code in a notebook for the easy reading of SFT information
- [ ] run SFT on each band of a candidate and collect in meaningful table format
- [ ] run sft on top 100 and return an image for each candidate

## Shock front intensity gradients:

- [x] Create a function for calculating the tangent at points along the spiral plot
- [x] Apply the Bresenham function along a tangent and sample the pixel values at each index returned
- [x] Loop the Bresenham sampling into an image/ data set
- [x] Plot the scatter of the intensity distributions as a function of radius (before and after corotation)
- [ ] Plot the intensity distribution at the co-rotation radius and at the bar? - test the manifolds?
- [x] Sort out the line starting from the other end problem
- [x] sort out y axis in image use scale as multiples of $R_e$
![Screenshot 2023-04-01 215735.jpg](../../AA%20%20-%20%20Assets/Screenshot%202023-04-01%20215735.jpg)

Need to decide what range of $r,\\theta$ want to sample over:
- Coarse sampling across extent of spiral after count subtraction
- Fine sampling around the resonance zones and co-rotation?

By sampling $n$ tangents for $m$ pixels along normal (arm thickness might be something we have to think about) we will end up creating an image $(n,m)$ where each row represents the intensity along the $\\hat{n}$ - normal plane with the centre of the row being the intersect of the normal and the spiral fit.

**Using this we can measure:**

- The Gini coefficient along these lines?
- the intensity distributions towards the shock front
- the position of the 1D centroid of the line and then plot on the image (mean moment)
- the intensity peak position and plot on image

- could we look at a description of the distribution of intensity in the normal plane as a function of radius and do a statistical analysis on that - [What would this tell us?] 

- Flipping it on its head we could also look along the tangent direction?

## Data sets and potential science:

#### GZ2
- https://data.galaxyzoo.org/

- Red Spirals 
- Mergers