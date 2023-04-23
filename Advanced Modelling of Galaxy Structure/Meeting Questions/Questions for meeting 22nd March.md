---
s:: true
---

### What have we done:

- Gini coefficient for 8 targets in all bands [Insert Graph]
- Flux fraction for 8 targets in all bands [Insert Graph]
- Created Hough transform function [Hough line scikit image]
- ![Pasted image 20230319181615.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230319181615.png)
- Attempted to create my own accumulator [mixed success]
- ![Pasted image 20230319194743.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230319194743.png)
- 

### Questions:

- [ ] How do we define high frequency components in the smoothness part of CAS? [Post 15th March Meeting to do](../MISC/Post%2015th%20March%20Meeting%20to%20do.md)
- [ ] Where was the information kept for `flux_20` is it in the non atlas files?
- [ ] The running of the ficl on an already extracted image in the hope of extracting the bulge did not work with the error: [INSERT ERROR] - how would we go about resolving this?
- [ ] Can we set $r_{max}$ as half the image diagonal?
- [ ] Do we calculate the log(r) for all pixel indices and then do some rounding for whatever is closest? 
- [ ] If so how does interpolation work here?
- [ ] Have I worked out the way to transform the array indices correctly using the position angle and ellipticity/axis ratios? [Creating Spiral fourier transform](../Code/Code%20description/2Dfft/Creating%20Spiral%20fourier%20transform.md)
- [ ] How do we get from linear eccentricity to axis ratio?
- [ ] What do you think of our bulge masking idea for using the tunning fork to classify the central excluded region?
- [ ] Is there any information for the Hubble classification of the galaxies in any of the data sets or would we have to do this manually?
- [ ] In order to process the image into something that we can pass to the spiral transform what form/shape would the signal be in to be transformed?


![Pasted image 20230321182241.png](../../AA%20%20-%20%20Assets/Pasted%20image%2020230321182241.png)
got an error when running that hasn't happened since a ficl update 

error happened on running `587732050555961424ua` 
