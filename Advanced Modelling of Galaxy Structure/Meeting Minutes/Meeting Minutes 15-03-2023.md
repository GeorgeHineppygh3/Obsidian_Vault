---
s:: true
---


#### Attendance:

 - Shivani 
 - George 

## Remember to take off the background

#### Topics covered:

-  Converting pixel intensity to magnitudes and needing a zero point
	- Found in the header of the non atlas version of the images - `flux_20` - how many counts would be in a 20th magnitude object
	- AB magnitude scale - compare to catalogue values
	- different due to within an aperture - plot a line against each should be y = x [DO THIS]
	- then do arms separate and after then plot a fraction and maybe compare how distance affects it
	- look at wavelength vs magnitude plots - plot in linear
	- could measure the disk contribution as well

Getting rid of the bulge/bar:

- Masking - less precise -could use a fraction of $R_e$ 
- fitting the bulge - could run it a second time to remove the bulge- classical bulge created by mergers with very high sersic index 

Continuity:

- Gini coefficient - would tell you how concentrated the light is along the arms - Possibly in AstroPy
- CAS - Concentration Asymmetry and Smoothness - tell you many things
- could measure many things - stellar mass - colour - environment

2DFFT:

- Hough transform to get new (numpy.indicese)
- get ellipticity and position angle from fitting
- theta becomes theta-PA
- $r =\\sqrt{x/a +y/b}$
- maybe make the Hough plot anyway
- could measure the offset between Hough plots to demonstrate shock front migration and the leaving behind of older stars
- could use the fwhm of the m peak to measure the uncertainty

Running Batches:

- When running can give all the inputs to the main function running in a loop
- could use os sys to run strings in a shell (this could run it through the command line)
- subprocesses - does os sys but with ability to remove outputs immediately

Servers

- SSH into the server 
- Get the data with R sync
- needs to be on campus or on the remote desktop - Nottingham remote desktop
- If want to sync data back from the server do the rsync method in reverse
- Could possibly get VPN access now
- Need to install anaconda and set up the ficl environment
- Save the server for running big things
-

#### Suggested work going forward:

Aden:
- get the gpu running
- run on a fits file

Shivani:
- sort out logger error
- run on a fits file


George:
- 2dfft sort it out
- Running Hough transform
- Filter galaxies by brightness
- install anaconda on the server
- remember to pip install -e in gax or it won't work
- `$ <command> &`  the ampersand allows you to carry on doing other things 'gives you back your terminal'
- `$ nohup <command> & `  allows you to run with closed terminal and nohup.out will contain all the prints
-  `$ nohup <command> &> outout_path &` specifying the output
- use `ps -u` to check if there is anything going
- if there is something you don't want running the run `kill PID` process ID from `ps -u` bit
===============================================================

## To Do:

### General Utilities
- Get the general fits file and filter and have it read for extracting relevant information
- 

### Continuity
- create a function to measure the Gini coefficient of images
- create a function to measure the Concentration Asymmetry and Smoothness (CAS)  of the images in each band

### Running
- Run the main function from the notebook singularly
- Run the main function from the notebook in a loop across all bands for one type as a proof of concept

### Server
- create the Gax library using `pip -e` 
- Get the loop running format in code that can be run on the server
- Run the Server code for `good_spirals.txt` candidates
- Create function to remove 1000 count background
- Create function that calculates magnitude conversions using the flux_20 from the 
- Create graph showing relationship between the flux's calculated using the conversion to the catalogue values (1:1)
- Create graphs for flux fraction:
	- stellar mass
	- redshift
	- Look at other parameters
- Think about ways of classifying error

### Bulge-Disk-Arms
- Attempt running the fitting again on an extracted image to see if it gets rid of the bulge
- Re run the graphing on potentially bulge extracted image
- if Bulge extraction successful:
	- look at extracted: disk - bulge - arms and compare flux share of each (maybe box plot?)

### 2DFFT
- Create a function to transform an array from ($x,y$) to ($r,\\theta$) and have a look at a plot of result (remember the ellipticity and position angle will skew this and must be accounted for)
- Create a function to transform to transform an array from ($x,y$) to ($log(r),\\theta$)
- Create functions to do best fit and calculate residuals to best fit
- Look at offset position of arm fit in each band - if unsuccessful wait for more data and try statistically later
- Watch a video on the FFT and make notes on how it works
- Create a FFT algorithm that uses the logarithmic spiral as the basis function
- Plot Fourier coefficient amplitudes to determine $m$ for number of arms
- Manipulate code to find the winding angle through optimisation

### Arm-centre to Shock-Front intensity gradients
- create line plot to overlay on image for spiral arm fit
- create function to make normal lines to the spiral fit and separate them by a step amount (define in pixels so that you try to minimise overlap)
- create a function to extract pixel values along normals 
- graph normal pixel values against (step * radial step distance) - [SEE HAND WRITTEN NOTE]

===============================================================
## Sketch:

Diagram of  what is being measured:
![Pasted image 20230315142801.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230315142801.png)
Resulting figure:
![Pasted image 20230315142854.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230315142854.png)
