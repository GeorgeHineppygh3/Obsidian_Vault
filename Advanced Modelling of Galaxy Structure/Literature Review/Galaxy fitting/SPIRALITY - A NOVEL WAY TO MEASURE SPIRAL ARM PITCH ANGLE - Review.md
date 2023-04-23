---
s:: true
---
---
s:: true
---
---
s:: true
---
### Disclaimers:
- This could be a potential good addition to the GAX code if we are able to get the original MATLAB code and change it to jaxnumpy / python
- Code:
	- https://github.com/DeannaShields/Spirality

## Relations:
- Paper: [SPIRALITY - A NOVEL WAY TO MEASURE SPIRAL ARM PITCH ANGLE - D. W. Shields.pdf](../../../PDFs/SPIRALITY%20-%20A%20NOVEL%20WAY%20TO%20MEASURE%20SPIRAL%20ARM%20PITCH%20ANGLE%20-%20D.%20W.%20Shields.pdf)

### Un-defined Terms:
- 

### Abstract:
- Created a MATLAB code which fits spirals of known winding to images to measure the winding angle
- Computation takes approximately 2 minutes on 8Gb RAM
- Tested code on 117 synthetic spiral galaxies with known pitches varying in both spiral properties and input parameters
- Code had 100% success rate in synthetic images
- The code agreed 26/30 times with a 2DFFT measurement technique - 
- Strong agreement found on:
	- galaxy radius
	- I-band magnitude
- Disagreement on:
	- redshift
- Assumed redshift problems arise from the lack of spirality in the early universe with most spiral structure being fully formed by $z=1-2$ 
- Also produced code Gen Spiral [This will be useful for testing sample produced galaxies for GAX]
- Also produced Spiral arm count which uses 1DFFT to count spiral arm number after pitch angle is established

### Conclusion: [N/A]
- Pitch angle does not vary with radius in current build - but will in future


### General:
- 

