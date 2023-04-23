---
s:: true
---

### Continuity

- [ ] create a function to measure the Concentration Asymmetry and Smoothness (CAS)  of the images in each band 
- [ ] http://rb.gy/wne19o
- [ ] http://rb.gy/zawwco
	- [ ] This concentration index is a number, C, defined as the ratio of the 80%–20% curve of growth radii ($r_{80}$, $r_{20}$), within 1.5 times the Petrosian inverted radius at r($\\eta  = 0.2$), normalized by a logarithm; $$C = 5\\,log(r_{80}/ r_{20})$$
	- [ ] ![Pasted image 20230321124855.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230321124855.png)
	- [ ] The asymmetry index is defined as the number computed when a galaxy is rotated 180 degrees from its centre and then subtracted from its pre-rotated image, and the summation of the intensities of the absolute value residuals of this subtraction are compared with the original galaxy flux.	
	 - [ ] ![Pasted image 20230321124607.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230321124607.png)
		
	- [ ] The spatial frequency term 'Smoothness' we define as, the clumpiness index ($S$) as the ratio of the amount of light contained in high-frequency structures to the total amount of light in the galaxy. [How do we define high frequency?] -  [ could we do this better using the spiral frequency components?]
	- [ ] ![Pasted image 20230321124622.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230321124622.png)
	

'We argue in this paper that the concentration index is a measure of the relative fraction of light in bulge and disk components, i.e., the $B/T$ ratio, and is a measure of the scale of a galaxy, its size, luminosity, and mass. Concentration thus reveals the past formation history of a galaxy. The asymmetry index is shown to be good at identifying galaxies which are currently undergoing major mergers. The clumpiness index is found to correlate very well with the H$\\alpha$ equivalent width of galaxies, and to a lesser degree with the integrated (BV) colour of a galaxy'

### Server [ Have to do in Uni ]

- [ ] Create a catalogue using the magnitude locality and inclination as desirable qualities [100 galaxies?]
- [ ] Use catalogue to go and get the SDSS Sloan images [in the hope that the U band is less shredded]
- [ ] Run ficl on all 500 fits for a suitable basis data set 
- [ ] create graphs for:
	- [ ] flux fraction
		- [ ] opportunities for using colourmap and size etc to add in loads of relevant info
	- [x] Gini coefficient
	- [x] Spiral Fourier transform coefficient amplitude graph
	- [x] $ln(r),\\theta$ images

### Arm-centre to Shock-Front intensity gradients

- [x] create line plot to overlay on image for spiral arm fit
- [x] create function to make normal lines to the spiral fit and separate them by a step amount (define in pixels so that you try to minimise overlap)
- [x] create a function to extract pixel values along normals 
- [x] graph normal pixel values against (step * radial step distance) - [SEE HAND WRITTEN NOTE BELOW

### 2DFFT

- [x] Create function to measure signal to noise in the Fourier coefficients and add to main function legend (maybe text box)
	- [x] use the S/N to weight the plots so that only statistically significant maxima are selected - [possibly]
- [x] classifying error: 'The most obvious error is the variance about the mean pitch angle over the selected stable region in inner radii. The error is found by calculating the mean and standard deviation of the sample of pitch angles over the selected stable region.'
- [x] Create document explaining the process in detail (maybe separate code into separate file and make documentation?)
- [x] Create functions to do best fit and calculate residuals to best fit
- [ ] Look at offset position of arm fit in each band - if unsuccessful wait for more data and try statistically later
- [ ] Read the existing papers and look at how they plot the arm centre line 
- [ ] Think about ways to create the continuous arm using the top 20 spiral frequencies
	- [ ] Here is a paper using the components to plot in the image:
	- [ ] ![Pasted image 20230325104630.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230325104630.png)
	- [ ] found it 'overlaid with the contours of the' Inverse FFT' for the m = 3 harmonic mode (in red)' <--- need to take top 20 components (by S/N) and then ISFT 
	- [ ] need to use this as a reference for creating the reverse function: ![Pasted image 20230325110428.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230325110428.png)
	- [ ] ![Pasted image 20230325110213.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230325110213.png)
	- [ ] Once we can plot these on top we need to centroid them and then plot the resulting line on top of the image!!!
- [ ] create a planning page for this
- [ ] think of appropriate scaling factor $r_0$ for plotting spiral in image
- [ ] plot resulting superposition on top of graph
- [ ] Would be interesting to look how pitch angle changes before and after co rotation in radial annuli? [might be able to say something about density wave to invariant manifold regime changes] - [how would we measure co-rotation?]  
	- [ ] [1.4x the bar?] - http://rb.gy/nueml8
	- [ ] unreal paper doing this using spirality - http://rb.gy/0pitxz
- [ ] Think it might be a good idea to plot $p_{max}$ against $r_{min}$ to demonstrate dependence and then give good reasons as to why $r_{min}$ is chosen by the classification scheme (unless bulge removal works lol)

### Bulge-Disk-Arms
- [ ] Attempt running the fitting again on an extracted image to see if it gets rid of the bulge
	- [ ] need to add background (1000 counts)
- [ ] Re run the graphing on potentially bulge extracted image
- [ ] if Bulge extraction successful:
	- [ ] look at extracted image

===============================================================


## Sketch:

Diagram of  what is being measured:
![Pasted image 20230315142801.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230315142801.png)
Resulting figure:
![Pasted image 20230315142854.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230315142854.png)


===============================================================
