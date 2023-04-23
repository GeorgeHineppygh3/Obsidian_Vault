---
s:: true
---
## To Do:

### General Utilities
- [x] Get the general fits file and filter and have it read for extracting relevant information
- [x] Publish code to shared repos
- [x] create function for reading fit information from output fits file [positions relative to the center of the image and updates so that only fits one component]
- [x] create a general utility function for directory output access to use in future 

### Continuity
- [x] create a function to measure the Gini coefficient of images
- [ ] create a function to measure the Concentration Asymmetry and Smoothness (CAS)  of the images in each band 
- [ ] http://rb.gy/wne19o
- [ ] http://rb.gy/zawwco
	- [ ] This concentration index is a number, C, defined as the ratio of the 80%–20% curve of growth radii ($r_{80}$, $r_{20}$), within 1.5 times the Petrosian inverted radius at r($\\eta  = 0.2$), normalized by a logarithm; $$C = 5\\,log(r_{80}/ r_{20})$$
	- [ ] ![Pasted image 20230321124855.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230321124855.png)
	- [ ] The asymmetry index is defined as the number computed when a galaxy is rotated 180 degrees from its centre and then subtracted from its pre-rotated image, and the summation of the intensities of the absolute value residuals of this subtraction are compared with the original galaxy flux.	
	 - [ ] ![Pasted image 20230321124607.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230321124607.png)
		
	- [ ] The spatial frequency term 'Smoothness' we define as, the clumpiness index ($S$) as the ratio of the amount of light contained in high-frequency structures to the total amount of light in the galaxy. [How do we define high frequency?]
	- [ ] ![Pasted image 20230321124622.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230321124622.png)
	

'We argue in this paper that the concentration index is a measure of the relative fraction of light in bulge and disk components, i.e., the $B/T$ ratio, and is a measure of the scale of a galaxy, its size, luminosity, and mass. Concentration thus reveals the past formation history of a galaxy. The asymmetry index is shown to be good at identifying galaxies which are currently undergoing major mergers. The clumpiness index is found to correlate very well with the H$\\alpha$ equivalent width of galaxies, and to a lesser degree with the integrated (BV) colour of a galaxy'


### Running
- [x] Run the main function from the notebook singularly
- [x] Run the main function from the notebook in a loop across all bands for one type as a proof of concept
- [x] create a function that will generate folders config and run a list of filenames
- [x] email steven and ask him if there is any reason that this would be truncating strings
- [x] distribute update to repos for everyone else

### Server [ Have to do in Uni ]
- [x] create the Gax library using `pip -e` 
- [x] Get the loop running format in code that can be run on the server
- [x] Run the Server code for `good_spirals.txt` candidates
	- [ ] only got 9 out lol and they are not consistent with each object (red is missing?)
	- [ ] Now have 29 but u band failed [show Steven]

### Easy Objectives
- [x] Create function to remove 1000 count background
- [ ] run ficl on all good spirals in all bands to generate a data set for the flux fraction for proof of concept [ This will take the piss in run time maybe overnight] - [Doing on MLIS1 as a practice run lol] - [Now have to run the remainders?]
	- [ ] If we could split running the remainders over devices it will take less time
- [ ] Create function that calculates magnitude conversions using the flux_20 from the [emailed steven]
- [ ] Create graph showing relationship between the flux's calculated using the conversion to the catalogue values (1:1)
- [ ] Create graphs for flux fraction:
	- [ ] stellar mass
	- [ ] redshift
	- [ ] Look at other parameters
- [ ] Think about ways of classifying error

### Bulge-Disk-Arms
- [x] Attempt running the fitting again on an extracted image to see if it gets rid of the bulge
	- [ ] Did not work need to email steven
- [ ] Re run the graphing on potentially bulge extracted image
- [ ] if Bulge extraction successful:
	- [ ] look at extracted: disk - bulge - arms and compare flux share of each (maybe box plot?)

### 2DFFT
- [x] Create a function to transform an array from ($x,y$) to ($r,\\theta$) and have a look at a plot of result (remember the ellipticity and position angle will skew this and must be accounted for)
	- [ ] Created function for personalised transform using accumulator
	- [ ] Used standard scikit Image `hough_line` transform
	- [ ] attempting to work out the geometry/maths of how transform is affected by position angle and ellipticity
- [x] Create a function to transform to transform an array from ($x,y$) to ($log(r),\\theta$)
	- [ ] This needs to be done by defining the range of $r$ between $r_{min} \\rightarrow r_{max}$ and lin-spacing deciding the number of points for resolution (match the angle resolution for nice square plot?)
	- [x] How do we make a regular sampled grid between $log(r_{min} \\rightarrow r_{max})$ and how do these values correspond to array index for sampling? [Do we calculate the log(r) for all pixel indices and then do some rounding for whatever is closest?] - [If so how does interpolation work here?]
- [ ] Create functions to do best fit and calculate residuals to best fit
- [ ] Look at offset position of arm fit in each band - if unsuccessful wait for more data and try statistically later
- [x] Watch a video on the FFT and make notes on how it works
- [x] Create a FFT algorithm that uses the logarithmic spiral as the basis function
- [x] Plot Fourier coefficient amplitudes to determine $m$ for number of arms
- [x] Manipulate code to find number of arms and the winding angle through optimisation

### Arm-centre to Shock-Front intensity gradients
- [ ] create line plot to overlay on image for spiral arm fit
- [ ] create function to make normal lines to the spiral fit and separate them by a step amount (define in pixels so that you try to minimise overlap)
- [ ] create a function to extract pixel values along normals 
- [ ] graph normal pixel values against (step * radial step distance) - [SEE HAND WRITTEN NOTE BELOW

===============================================================
## Sketch:

Diagram of  what is being measured:
![Pasted image 20230315142801.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230315142801.png)
Resulting figure:
![Pasted image 20230315142854.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230315142854.png)


===============================================================
