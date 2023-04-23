---
s:: true
---


## Questions:

- What are the meanings of all of the input terms for the functions?

- for main:
	- psf_filename : path of fits file containing psf
	- detection_parameters :
	- sb_threshold :
	- source_flux_limit :
	- learning_rate :
	- large_threshold :
	- large_nsamples :
	- large_scale_nonpar_rate :
	- small_scale_nonpar_rate :
	- psf_oversampling :
	- max_iterations : total number of iterations
	- warmup : how many iterations to try and fit the galaxy before taking away the non param 
	- output_path : path to output the post processed images and iteration updates
	- save_iteration_frequency : the number of iterations between saving new images of progress

- for optimisation step:
	-   orginal_image : image array drawn from fits file
	-   source_param : 
	-   psf : image array of psf drawn from fits file
	-   mask :
	-   learning_rate :
	-   param_norm :
	-   running_gradients :
	-   running_square_gradients :
	-   lower_bounds :
	-   upper_bounds :
	-   large_scale_nonpar_image :
	-   small_scale_nonpar_image :
	-   large_threshold :
	-   large_nsamples :
	-   large_scale_nonpar_rate : set to zero to only worry about one source
	-   small_scale_nonpar_rate :
	-   iteration :
	-   warmup :
	-   output_path : path to output the post processed images and iteration updates
	-   save_iteration_frequency :  the number of iterations between saving new images of progress

## Plan:

get ficl to run on a test image with steven