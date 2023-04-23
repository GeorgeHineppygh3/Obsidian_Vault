---
s:: true
---
#### Attendance:

- Steven

 - Shivani 
 - George 

## General:

- updated the test which was causing an error 
- need to do a pull request after the meeting
- changes have subtracted the background from the image - taken from header in the fits
- Atlas:
	- pros:
		- only target in image
	- cons:
		- added 1000 counts to everything in order for everything to be positive
		- want to tell the code to ignore 1000 ( could do this with really high value for the uncertainty in the uncertainty image)
		- no background done for compression
		- don't worry now maybe will sort the uncertainty maps afterwards
		- sometimes off centre so possibly cant 
- Ficl tries to estimate uncertainty 
- assumes in electron count
- takes square route to get poison error
- need to look up the gain to get electron counts

## What steven has done:

- looked for strong spirals
- looked at file size to estimate spiral arm quality
- listed by file-size and viewed them
- should install DS9
- tried to run fic on a test image
- got my error
- detection works with the right params
- phot-utils returns different half lights
- it was failing because eveyrhting was the same at the outskirts
- it was failing because eveyrhtireturns the same value at grreater radius

Can specifiy params in a list

if you run python -m ficl -w

it will create a config file which can be edited
then if you run  python -m ficl  -c it will allow you to specify the filename
ignoring psf due to size of image compared to psf at the moment

comment out the psf section of the code to run

background is set to 1000

detect n pixels = minimum size for object to be of interest - this can be larger now due to singke target

deblend contrast = 1% ususally - if you have two lumps next to each other the dip in the middle 

it is now at 1 forcing it to only create one model

worked well with galsim
ran with gax was faster wooo

works better because:

galsim fits in linear units
this is not so good due to assuming normalisation
gax fits in log which makes numbers a lot closer to one and so the decent happens quicker
working image minus residuals is the parametric model
set scales a tiny bit below the background to see noise
set top end to 250 so that you can limit the range to see the image
ficl currently uses photoutils detect threshold to work out the background
possibility to increase smoothness using the small scale components
if we want to get rid of the bulge we need to create a second sersic which is a lot stronger and smaller at the center

#### Topics covered:

- 




#### Suggested work going forward:

1. get the new code to run
	1. use the config file and mess around with it ( have a look )
2. try it on a range of galaxies
3. 

