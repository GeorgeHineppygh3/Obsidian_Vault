---
s:: true
---
---
s:: true
---
---
s:: true
---
---
s::  true
---
Supporting python file to [Borge_test.ipynb](../../../../PDF%20exports/Borge_test.ipynb.md) 

File contains functions for the easy manipulation and formatting of data from fits files.

## Code Breakdown:
===============================================================
## Function:
```run-python
def Read(fits_path):
    hdulist = fits.open(fits_path) # Open the FITS file

    data = hdulist[0].data # Get the data from the first HDU (header/data unit)

	return jnp.asarray(data) # Return JAX array of image
```

- Function reads an image into a Jax array format from the Primary HDU in a fits file

- Function Takes arguments:
	- `fits_path` : the path to find the fits file
- Function Returns:
	- `jnp.asarray(data)` : Jax NumPy array of image

## Function:
```run-python
def Read_M_band(file_name):

    initial_fits_path = np.array(['/home/borge/gax/{}ua.fits.gz'.format(file_name)])

    initial_image = Read(initial_fits_path[0])

    bands = np.array(['ua','ga','ra','ia','za'])
    Composite = np.empty((initial_image.shape[0],initial_image.shape[1],len(bands)))

    for i in range(0,len(bands)):

        fits_path = np.array(['/home/borge/gax/{}{}.fits.gz'.format(file_name,bands[i])])

        print(fits_path)
        image = Read(fits_path[0])
        Composite[:,:,i] = image


    return jnp.asarray(Composite)
``` 

- Function reads images from file name into a 5 image stacked JAX NumPy array

- Function takes arguments:
	- `file_name` : The name of the file with multiple bands - input must be a string
- Function returns:
	- `Composite` : A JAX NumPy array of stacked images

## Function:
```run-python
def norm(X):
    return(X/np.max(X)) #normalise array
```

- Function normalises an array

- Function takes arguments:
	- `X` : array to be normalised
- Function returns:
	- `X/np.max(X)` : normalised array

## Function:
```run-python
def multi_band_imshow(Composite_image):

    R = norm(Composite_image[:,:,2]-np.average(Composite_image[0:20,0:20,2])) #Assign longest wavelength band to Red

    G = norm(Composite_image[:,:,1]-np.average(Composite_image[0:20,0:20,1])) #Assign middle wavelength band to Green

    B = norm(Composite_image[:,:,0]-np.average(Composite_image[0:20,0:20,0])) #Assign shortest wavelength band to Blue

    RGB = np.array([R,G,B]).T #Concatenate and transpose

    plt.imshow(RGB) #Show image
```

- Function plots a cleaned RGB image from `Composite` array 
- Function cleans the data by subtracting the average pixel value in each channel over an empty region and normalising for RGB output

- Function takes arguments:
	- `Composite_image` : array of images in each band
- Function returns:
	- `RGB` : array of three images in

## Update:

Changed `Read_M_band` to include a file location parameter

```run-python
def Read_M_band(file_name,location):

    """Function reads multiple bands from a specified file location
    into stacked composite Jax NumPy array
    Args:
        file_name (string): string of file name
        location (string): string of path location
    Returns:
        Composite: Composite array of all bands stacked vertically
    """
    # Find dimensions of image for creating empty composite array
    initial_fits_path = np.array(['{}{}ua.fits.gz'.format(location,file_name)])
    initial_image = Read(initial_fits_path[0])
 
    # Initialise composite array with dimensions of image and number of bands
    bands = np.array(['ua','ga','ra','ia','za'])
    Composite = np.empty((initial_image.shape[0],initial_image.shape[1],len(bands)))
    # Read images from folder into Composite array
    for i in range(0,len(bands)):
        fits_path = np.array(['{}{}{}.fits.gz'.format(location,file_name,bands[i])])
        print(fits_path)
        image = Read(fits_path[0])
        Composite[:,:,i] = image

	 # Return Composite JAX NumPy array
    return np.asarray(Composite)
```

- Function plots a cleaned RGB image from `Composite` array 
- Function cleans the data by subtracting the average pixel value in each channel over an empty region and normalising for RGB output

- Function takes arguments:
	- `file_name` : The name of the file with multiple bands - input must be a string
	-  `location` : Path of folder housing files
 
- Function returns:
	- `Composite_image` : array of images in each band

## Function:

```run-python
def gaussian_psf(image,stddev,size,smooth):

    """Function creates a guassian psf for an image
    Args:
        image (2D array): image that psf is being generated for
        stddev (float): standard deviation fo gaussian kernel
        size (int): size fo kernel central intensity in pixels
        smooth (Bool): Boolean for whether psf is smoothed or not before returning
    Returns:
        psf: Gaussian psf same size as input function with specified size and std dev
    """
    # Create the 2D Gaussian kernel
    x, y = np.meshgrid(np.linspace(-size/2, size/2, size),
     np.linspace(-size/2, size/2, size))

    kernel = np.exp(-(x**2 + y**2) / (2*stddev**2))

    # Normalise kernel
    kernel /= np.sum(kernel)

    # Create array size of imageS
    psf = np.zeros(image.shape)

    # Place kernel at the center of array
    center = (np.array(image.shape) - 1) / 2

    xmin = int(center[0] - (size - 1) / 2)
    xmax = int(center[0] + (size - 1) / 2) + 1
    ymin = int(center[1] - (size - 1) / 2)
    ymax = int(center[1] + (size - 1) / 2) + 1

    psf[xmin:xmax, ymin:ymax] = kernel

    if smooth == True:
        psf = gaussian_filter(psf,sigma=stddev)
        return psf
    else:
        return psf
```
**gaussian_psf(image,stddev,size,smooth):**

-   Inputs:
    -   image: a 2D NumPy array representing an image
    -   stddev: a float value representing the standard deviation of the Gaussian kernel
    -   size: an integer representing the size of the kernel's central intensity in pixels
    -   smooth: a Boolean value representing whether or not the Gaussian PSF should be smoothed before being returned
-   Outputs:
    -   A Gaussian PSF, represented as a 2D NumPy array the same size as the input image and with the specified size and standard deviation. If the "smooth" parameter is set to True, the PSF is smoothed using a Gaussian filter before being returned.

## Function:
```run-python
def threshold_image(image,value):
    for i in range(0,image.shape[0]):
        for j in range(0,image.shape[1]):
            if image[i,j] > value:
                image[i,j] = 1
            else:
                0
    return image
```
**threshold_image(image,value):**

-   Inputs:
    -   image: a 2D NumPy array representing an image
    -   value: a threshold value for the image
-   Outputs:
    -   The input image, with pixel values greater than the threshold set to 1 and all other pixel values set to 0

## Function:
```run-python
def sum_background(image):
    count = 0

    for i in range(0,image.shape[0]):
        for j in range(0,image.shape[1]):
            if image[i,j] == image[20,20]:
                count =+ 1
            else:
                continue
    return count*image[20,20]
```
**sum_background(image):**

-   Inputs:
    -   image: a 2D NumPy array representing an image
-   Outputs:
    -   A count of the number of pixels in the image with the same value as the pixel at position (20,20), multiplied by the value of that pixel

## Function:
```run-python
def source_flux(Composite_image,band):

"""Function calculates the summed pixel values of the source within an image by removing     the background which is characterised as the minimum flux value - subject to change

	Args:
        Composite_image (array): stacked array of bands
        band (int): 0 - 5 for  u g r i z
    Returns:
        float: value of summed pixels
    """
    image = Composite_image[:,:,band] # Select band from composite image
    image = image - np.min(image) # Remove background flux
    return np.sum(image)
```
**source_flux(Composite_image,band):**

-   Inputs:
    -   Composite_image: a stacked array of bands
    -   band: an integer representing the band (0-5) for the input composite image
-   Outputs:
    -   A float value representing the summed pixel values of the source within the image after removing the background

## Function:
```run-python
def source_flux_minus_background(Composite_image,band):

    """Function calculates the summed pixel values of the source within an image by removing the background
        which is characterised as the minimum flux value - subject to change
    Args:
        Composite_image (array): stacked array of bands
        band (int): 0 - 5 for  u g r i z
    Returns:
        float: value of summed pixels
    """
    image = Composite_image[:,:,band] # Select band from composite image
    image = image - np.min(image) # Remove background flux
    return np.sum(image) - sum_background(image)
```
**source_flux_minus_background(Composite_image,band):**

-   Inputs:
    -   Composite_image: a stacked array of bands
    -   band: an integer representing the band (0-5) for the input composite image
-   Outputs:
    -   A float value representing the summed pixel values of the source within the image after removing the background, as calculated by subtracting the background sum from the output of the source_flux function

### These Functions still very provisional was just bored, thought I should start making these
===============================================================

## Function:
```run-python
def arm_flux(image):
    """Calculate flux of arm from separated arm image
    Args:
        image ("2D NumPy array"): Image array

    Returns:
        float: summed image value
    """
    return np.sum(image)
```
**arm_flux(image):**

-   Inputs:
    -   image: a 2D NumPy array representing an image of an arm
-   Outputs:
    -   A float value representing the summed pixel values of the input image


## Function:
```run-python
def flux_frac(Composite_image,band,isolated_image):

    """Calculate flux fraction for source to seperated arms
    Args:
        Composite_image (Stacked NumPy image arrays): composite image array for stacking        2D images
        band (int): integer 0 - 5 representing u g r i z
        isolated_image (2D NumPy array): image after non_parametric extraction
    Returns:
        float: fraction of flux coming from the arms inside the source
    """
    source = source_flux(Composite_image,band)
    arm = arm_flux(isolated_image)
    return arm/source
```
**flux_frac(Composite_image,band,isolated_image):**

-   Inputs:
    -   Composite_image: a stacked array of bands
    -   band: an integer representing the band (0-5) for the input composite image
    -   isolated_image: a 2D NumPy array representing an image after non-parametric extraction
-   Outputs:
    -   A float value representing the fraction of flux coming from the arms inside the source, calculated as the arm flux divided by the source flux

===============================================================

## Update:

Changing `multi_band_imshow` to specify what bands you want.

```run-python
def multi_band_imshow(Composite_image,R_band,G_band,B_band):
    """Function creates an RGB image from a composite image array where
    bands can be specified for each channel but if not then
    R = bands[2] = r
    G = bands[1] = g
    B = bands[0] = u

    Args:
        Composite_image (array)): Composite array of all bands stacked vertically
        R_band (int): bands index for specified band
        G_band (int): bands index for specified band
        B_band (int): bands index for specified band
    """
    if R_band is None and G_band is None and B_band is None:
        R_band = 2
        G_band = 1
        B_band = 0

    R = norm(Composite_image[:,:,R_band]-np.average(Composite_image[0:20,0:20,R_band])) 
    #Assign longest wavelength band to Red
    G = norm(Composite_image[:,:,G_band]-np.average(Composite_image[0:20,0:20,G_band])) 
    #Assign middle wavelength band to Green
    B = norm(Composite_image[:,:,B_band]-np.average(Composite_image[0:20,0:20,B_band])) 
    #Assign shortest wavelength band to Blue
    RGB = np.array([R,G,B]).T #Concatenate and transpose
    plt.figure()
    plt.axis('off')
    plt.imshow(RGB) #Show image

```
Inputs:

-   `Composite_image`: A 3D array representing the composite image, where bands are stacked vertically.
-   `R_band`: An integer representing the index of the band to be used for the Red channel.
-   `G_band`: An integer representing the index of the band to be used for the Green channel.
-   `B_band`: An integer representing the index of the band to be used for the Blue channel.

Outputs:

-   Displays an RGB image created from the composite image array using the specified or default bands for each channel.


## Function:
```run-python
def Generate_config(filename,location,output_path):
    """Generate a config file from a given filename and location, and write it to a .yml file.
    Parameters:
        filename (str): The name of the file to generate the config file for.
        location (str): The location of the file to generate the config file for.
        output_path (str): The directory to write the output file to.
    Returns:
        None
    """
    # Remove file information from filename
    file = filename.removesuffix('.fits.gz')

    # Create a basic string of the config file
    document = """image_filename = loc_filename_
    #psf_filename = None
    output_path = /home/borge/Data/Output_Data/file_
    psf_oversampling = 1
    sb_threshold = 0
    source_flux_limit = 0
    learning-rate = 0.05
    large_threshold = 50
    large_nsamples = 25
    large_scale_nonpar_rate = 0
    small_scale_nonpar_rate = 0.05
    max_iterations = 204
    warmup = 3
    modeller = gax
    gax_integration_order = 3
    save_iteration_frequency = 100
    loglevel = DEBUG
    nsigma = 1.0
    background = 1000.0
    smooth_sigma = 3.0
    smooth_size = 25.0
    detect_npixels = 1000
    deblend_npixels = 1000
    deblend_nlevels = 1
    deblend_contrast = 1
    """
    # Replace basic componenents with specified variables
    doc1 = document.replace('loc_',str(location),1)
    doc2 = doc1.replace('filename_',str(filename),1)
    doc3 = doc2.replace('file_',str(file),1)

	# specify the name of your output file
    output_file = 'file__config.txt'
    output_file = output_file.replace('file_',file,1)

	# specify the string you want to write to the file
    doc3

    # open the file for writing and write the string to the file
    with open(output_file, 'w') as file:
        file.write(doc3)

	# specify the name of the file you want to rename
    old_filename = output_file

    # get the filename without the extension
    base = os.path.splitext(old_filename)[0]

    # specify the new filename with the .yml extension
    new_filename = base + '.yml'

    # rename the file
    os.rename(old_filename, new_filename)

    # specify the name of the directory you want to move the files to
    destination_dir = output_path

	# get a list of files in the current working directory
    files = os.listdir()

    # loop through each file and move it to the destination directory
    for file in files:
        if os.path.isfile(output_file):
            shutil.move(file, os.path.join(destination_dir, file))

    print('config_file_created')
```

**Inputs:**

-   `filename` (str): The name of the file to generate the config file for.
-   `location` (str): The location of the file to generate the config file for.
-   `output_path` (str): The directory to write the output file to.

**Outputs:**

-   None

The function takes in a `filename`, `location`, and `output_path` as inputs. It generates a config file from the `filename` and `location`, and writes it to a `.yml` file in the `output_path`. The function does not return anything, but prints "config_file_created" to the console when it has finished running.

## Update:
```run-python
def Generate_config(filename,location,output_path):
    """Generate a config file from a given filename and location, and write it to a .yml file.
    Parameters:
        filename (str): The name of the file to generate the config file for.
        location (str): The location of the file to generate the config file for.
        output_path (str): The directory to write the output file to.
    Returns:
        None
    """
    # Remove file information from filename
    file = filename.removesuffix('.fits.gz')

    # Create a basic string of the config file
    document = """image_filename = loc_filename_
    #psf_filename = None
    output_path = /home/borge/Data/Output_Data/file_
    psf_oversampling = 1
    sb_threshold = 0
    source_flux_limit = 0
    learning-rate = 0.05
    large_threshold = 50
    large_nsamples = 25
    large_scale_nonpar_rate = 0
    small_scale_nonpar_rate = 0.05
    max_iterations = 204
    warmup = 3
    modeller = gax
    gax_integration_order = 3
    save_iteration_frequency = 100
    loglevel = DEBUG
    nsigma = 1.0
    background = 1000.0
    smooth_sigma = 3.0
    smooth_size = 25.0
    detect_npixels = 1000
    deblend_npixels = 1000
    deblend_nlevels = 1
    deblend_contrast = 1
    """
    # Replace basic componenents with specified variables
    doc1 = document.replace('loc_',str(location),1)
    doc2 = doc1.replace('filename_',str(filename),1)
    doc3 = doc2.replace('file_',str(file),1)

	# specify the name of your output file
    output_file = 'file__config.txt'
    output_file = output_file.replace('file_',file,1)

	# specify the string you want to write to the file
    doc3

    # open the file for writing and write the string to the file
    with open(output_file, 'w') as file:
        file.write(doc3)

	# specify the name of the file you want to rename
    old_filename = output_file

    # get the filename without the extension
    base = os.path.splitext(old_filename)[0]

    # specify the new filename with the .yml extension
    new_filename = base + '.yml'

    # rename the file
    os.rename(old_filename, new_filename)

    # specify the name of the directory you want to move the files to
    destination_dir = output_path

	# get a list of files in the current working directory
    files = os.listdir()

    # loop through each file and move it to the destination directory
    for file in files:
        if os.path.isfile(output_file):
            shutil.move(file, os.path.join(destination_dir, file))

    print('config_file_created')
```


## Function:
```run-python
def Composite_imshow(Composite):
    """Plots each band of composite with title corresponding to band
    Args:
        Composite (NumPy array): Composite array of Images
    """

    fig, ax = plt.subplots(1,5)

    for i in range(0,len(bands)):

        ax[i].imshow(Composite[:,:,i])
        ax[i].set_title('{}'.format(bands[i]))
        ax[i].axis('off')
```

This function is designed to plot each band of a composite image using matplotlib's `imshow` function. The input `Composite` is a NumPy array that contains the composite image.

The function creates a figure object and a set of subplots using the `subplots` function from the `matplotlib.pyplot` module. The `fig` object represents the entire figure, while `ax` is an array of axes objects that correspond to each subplot.

The function then uses a loop to iterate through each band of the composite image. It uses the `imshow` function to plot the band in the corresponding subplot, and sets the title of the subplot to the name of the band using the `set_title` function. Finally, it sets the axis off for each subplot to remove any unnecessary axis labels or tick marks.

Note that the `bands` variable used in the loop is not defined in the function itself, so it must be defined elsewhere in the code.

## Update:

Changed centroid to specify if it wants cartesian output or array index output.

```run-python
def centroid(img,cartesian):

    """First moment of the flux distribution.

    Parameters
    ----------
    img : numpy or jax array

    Returns
    -------
    x, y : floats
        The calculated centroid position.
    """
    x_cen = (np.arange(img.shape[0]) * img.sum(1) / img.sum()).sum()
    y_cen = (np.arange(img.shape[1]) * img.sum(0) / img.sum()).sum()

	if cartesian == True:
        return x_cen, y_cen
    else:
        return y_cen, x_cen # array indices are swapped
```

-   The first function does not have a `cartesian` parameter, and always returns the centroid position as `(x, y)`.
-   The second function has an optional `cartesian` parameter that defaults to `True`. If `cartesian` is `True`, the function returns the centroid position as `(x, y)` like the first function. If `cartesian` is `False`, the function returns the centroid position as `(y, x)`, which swaps the array indices.


## Update:

changed generate config so that it doesn't move everything and is a bit simpler.

```run-python
def Generate_config(filename,location,output_path):
    """Generate a config file from a given filename and location, and write it to a .yml file.

    Parameters:
        filename (str): The name of the file to generate the config file for.
        location (str): The location of the file to generate the config file for.
        output_path (str): The directory to write the output ficl files to.

    Returns:
        None
    """
    # First get current working so we can return to after
    current = os.getcwd()

    # specify the name of the directory you want to move the config files to
    destination_dir = '/home/borge/Data/Config_files'

    # Move to output directory
    os.chdir(destination_dir)

    # Remove file information from filename
    file = filename.removesuffix('.fits.gz')

    # Create a basic string of the config file
    document = """image_filename = loc_/filename_
    #psf_filename = None
    output_path = /home/borge/Data/Output_Data/file_
    psf_oversampling = 1
    sb_threshold = 0
    source_flux_limit = 0
    learning-rate = 0.05
    large_threshold = 50
    large_nsamples = 25
    large_scale_nonpar_rate = 0
    small_scale_nonpar_rate = 0.05
    max_iterations = 204
    warmup = 3
    modeller = gax
    gax_integration_order = 3
    save_iteration_frequency = 100
    loglevel = DEBUG
    nsigma = 1.0
    background = 1000.0
    smooth_sigma = 3.0
    smooth_size = 25.0
    detect_npixels = 1000
    deblend_npixels = 1000
    deblend_nlevels = 1
    deblend_contrast = 1
    """
    # Replace basic componenents with specified variables
    doc1 = document.replace('loc_',str(location),1)
    doc2 = doc1.replace('filename_',str(filename),1)
    doc3 = doc2.replace('file_',str(file),1)

	# specify the name of your output file
    output_file = 'file__config.txt'
    output_file = output_file.replace('file_',file,1)
 
    # specify the string you want to write to the file
    doc3
    
    # open the file for writing and write the string to the file
    with open(output_file, 'w') as file:
        file.write(doc3)
    # specify the name of the file you want to rename
    old_filename = output_file


    # get the filename without the extension
    base = os.path.splitext(old_filename)[0]

 
    # specify the new filename with the .yml extension
    new_filename = base + '.yml'
  
    # rename the file
    os.rename(old_filename, new_filename)

    # move back to original chdir
    os.chdir(current)

    print('config_file_created: {} in {}'.format(new_filename,destination_dir))
```

- no more using `shutil` in a loop just change directory then change back


## Function:
```run-python
def command_line_file_list_run(file_list,data_location):

    """
    Generates and runs FICL commands for a list of FITS files.

    Args:
    - file_list: a list of FITS file names.
    - data_location: the directory where the FITS files are located.

    Returns:
    None
    """    

    # Get directory to return to
    current = os.getcwd()

    # define config directory path
    config_path = '/home/borge/Data/Output_Data/Test_Folder/'

    # Create list of filenames without file information
    files = np.empty_like(file_list).astype(str)
    for i in range(0,len(file_list)):
        files[i] = file_list[i].removesuffix('.fits.gz')

    # Generate output folders:
    for i in range(0,len(file_list)):
        gfits.create_folder(config_path,files[i])

    # Generate the config files:
    config_list = []

    for i in range(0,len(file_list)):
        config_element = gfits.Generate_config(file_list[i],data_location,config_path)
        config_list.append(config_element)

    # first navigate to outer ficl directrory
    os.chdir('/home/borge/ficl/')

    # Initialise list of commands for running
    commands = []

    command_structure = 'python -m ficl.main -c /home/borge/Data/Config_files/'

    # Write commands to array
    for i in range(0,len(file_list)):
        command_element = command_structure + config_list[i]
        commands.append(command_element)
  

    # Move to ficl outer directory
    os.chdir('/home/borge/ficl')

  
    # Loop through the list of commands and run each one using os.system
    for i in range(0,len(commands)):
        os.system(commands[i])
  

    # move back to original cwdir
    os.chdir(current)
```
### Description:

This function takes in a list of FITS file names and a data location directory, and then generates and runs FICL commands for each FITS file. Here are the steps that the function performs:

-   Gets the current working directory and stores it in a variable.
-   Defines a path to the configuration directory.
-   Creates a list of filenames without file information.
-   Generates output folders for each filename in the list.
-   Generates a list of configuration files for each FITS file.
-   Navigates to the outer FICL directory.
-   Writes a list of commands to an array for running FICL.
-   Moves to the FICL outer directory.
-   Loops through the list of commands and runs each one using the `os.system()` method.
-   Moves back to the original current working directory.


### For Shivani & Aden:

To modify the paths to fit your own workspace, you need to update the following paths in the code:

-   `config_path`: This variable defines the path to the output directory where the generated configuration files will be stored. You should update this path to match the desired location in your own workspace.
    
-   `command_structure`: This variable defines the command structure that will be used to run FICL. You should update this path to match the location of the configuration files generated in the previous step.
    
-   `os.chdir()`: This method is used to navigate to specific directories in the code. You should update the directory paths passed to this method to match the directory structure in your own workspace.
    
-   `data_location`: This variable specifies the directory where the FITS files are located. You should update this path to match the location of the FITS files in your own workspace.
    

After updating these paths, you can call the function with your own list of FITS file names and the function will generate and run FICL commands using the updated paths.

## Replace:

- Old flux frac was not good and a bit of position holder - the new one is better

```run-python
def flux_frac(Composite,Composite_isolated):
     """
    Calculates the flux fraction between a composite image and an isolated composite image for each band.

    Args:
    - Composite (np.ndarray): A 3D numpy array of the composite image.
    - Composite_isolated (np.ndarray): A 3D numpy array of the isolated composite image.

	Returns:
    - np.ndarray: A 1D numpy array containing the flux fraction for each band.
    """
    background = 1000
    flux_frac = np.empty_like(bands)
    for i in range(0,len(bands)-1):
        flux_frac[i] = np.sum(Composite[:,:,i]-background)-np.sum(Composite_isolated[:,:,i])
    return flux_frac
```
### Description:

-   The `flux_frac()` function calculates the flux fraction between a composite image and an isolated composite image for each band.
    
-   The input arguments for the function are:
    
    -   `Composite`: A 3D NumPy array of the composite image.
    -   `Composite_isolated`: A 3D NumPy array of the isolated composite image.
-   The output of the function is a 1D NumPy array containing the flux fraction for each band.
    
-   The function subtracts a fixed background value of 1000 from each band in the composite image before calculating the flux fraction.
    
-   The function uses a for loop to calculate the flux fraction for each band and stores the result in the `flux_frac` NumPy array.


### Function:
```run-python
def raid_directory(directory_path):
    """
    Navigates to the most recent subdirectory within a given directory path and reads in two FITS files.

    Parameters:
    -----------
    directory_path : str
        A string representing the path of the directory to search for subdirectories.
    Returns:
    --------
    Tuple
        A tuple of two FITS file objects, `source_params_table` and `small_non_par_image`.

    Raises:
    -------
    FileNotFoundError:
        If no subdirectories are found within the given directory.
    TypeError:
        If the directory path provided is not a string.
    Note:
    -----
    This function assumes that the subdirectories within the given directory have integer names and that the most recent subdirectory has the highest integer value name. Additionally, it assumes that the FITS files `source_params.fits` and `small_nonpar.fits` exist within the most recent subdirectory.
    """
    # get current working directory to return to at the end
    current = os.getcwd()

	# Move to folder
    os.chdir(directory_path)

    # List directory contents
    contents = os.listdir()

    # convert to an array
    arr = np.asarray(contents).astype(int)

    # Find contents largest output value
    latest = np.max(arr)

    # Convert back to string     (we assume no iterations over 1000)
    latest = '0' + str(latest)

    # Move to most recent output directory
    os.chdir(latest)
  
    # Read files in
    source_params_table = gfits.Read_Table('source_params.fits')
    small_non_par_image = gfits.Read('small_nonpar.fits')

	# Return to original directory
    os.chdir(current)

    return(source_params_table,small_non_par_image)
```

Arguments:

-   directory_path: path to the directory that needs to be raided

Return:

-   A tuple containing two objects:
    -   source_params_table: contents of the 'source_params.fits' file in the most recent sub-directory in the given directory path
    -   small_non_par_image: contents of the 'small_nonpar.fits' file in the most recent sub-directory in the given directory path

Functionality:

-   Changes the current working directory to the given directory path
-   Lists the contents of the directory
-   Finds the largest numeric value in the names of the directory contents
-   Changes the working directory to the sub-directory with the highest numeric value in the name
-   Reads the contents of `source_params.fits` and `small_nonpar.fits` files in the selected sub-directory
-   Returns the contents of these two files in a tuple
-   Changes the working directory back to the original directory path.

### Function:
```run-python
def Composite_from_directory_raid(OBJID,Parent_directory):
    """
    Create a composite image and source parameter table by raiding multiple directories.

    Parameters
    ----------
    OBJID : str
        The object ID used to create directory names.
    Parent_directory : str
        The parent directory where the OBJID subdirectories are located.

    Returns
    -------
    Composite_Source_Table : astropy.table.Table
        A table containing the composite source parameters.
    Isolated_Composite : numpy.ndarray
        A 3D array containing the isolated composite image data.

	Notes
    -----
    The function expects the OBJID subdirectories to have the following suffixes:
    'ua', 'ga', 'ra', 'ia', 'za', corresponding to the five filter bands used in the imaging survey.

    The function first raids the directory for the first filter band to get the image     dimensions, and then reads in the non-parametric images from the other bands to create the isolated composite.

    The source parameter tables from all bands are stacked together to create the composite source parameter table.
    Finally, the composite source parameter table is augmented with additional columns indicating the filter band and the corresponding effective wavelength.
    """
    # Create suffix array for raiding
    bands_suffix = np.array(['ua','ga','ra','ia','za'])

    # Initialise list of directories to raid
    directrories_to_raid = []

    # creates a list of directories based on the OBJID    
    directrories_to_raid
    for i in range(0,len(bands)):
        directory = Parent_directory + OBJID + bands_suffix[i]
        directrories_to_raid.append(directory)

	# First raid directory to get image dimensions for Composite
    source0, nonpar0 = raid_directory(directrories_to_raid[0])
    Composite_Source_array = source0[0]
    Isolated_Composite = np.empty((nonpar0.shape[0],nonpar0.shape[1],len(bands)))
    Isolated_Composite[:,:,0] = nonpar0

    # Raid the rest of the directories
    for i in range(1,len(bands)):
        source_table, non_par = raid_directory(directrories_to_raid[i])
        Isolated_Composite[:,:,i] = non_par
        Composite_Source_array = np.vstack([Composite_Source_array,source_table[0]])

	# Convert array to astropy table
    Composite_Source_Table = Table(Composite_Source_array)

    # Now want to add a column detailing band and corresponding central wavelength
    Composite_Source_Table.add_column(bands, name='Band')
    Composite_Source_Table.add_column(wavs,name='Effective Wavelength')

    return Composite_Source_Table, Isolated_Composite
```
#### Description:

-   Creates a suffix array `bands_suffix` for raiding.
-   Initializes an empty list `directories_to_raid`.
-   Creates a list of directories to raid by appending the suffixes to the `Parent_directory` using the `OBJID` and the `bands_suffix`.
-   Raids the first directory to get the image dimensions of the composite source and the isolated composite.
-   Initializes the `Composite_Source_array` and `Isolated_Composite` array with the data from the first directory.
-   Loops over the rest of the directories and raids them to create the isolated composite for each band.
-   Appends the source parameter table from each band to the `Composite_Source_array`.
-   Converts the `Composite_Source_array` to an `astropy.table.Table` object named `Composite_Source_Table`.
-   Adds two additional columns to `Composite_Source_Table`: `Band` and `Effective Wavelength`, indicating the filter band and the corresponding effective wavelength.
-   Returns `Composite_Source_Table` and `Isolated_Composite` as output.

#### Input parameters:

-   `OBJID`: A string that represents the object ID used to create directory names.
-   `Parent_directory`: A string that represents the parent directory where the `OBJID` subdirectories are located.

#### Output values:

-   `Composite_Source_Table`: An `astropy.table.Table` object that contains the composite source parameters.
-   `Isolated_Composite`: A 3D numpy array that contains the isolated composite image data.

Note that the returned `Composite_Source_Table` is augmented with two additional columns: `Band` and `Effective Wavelength`, indicating the filter band and the corresponding effective wavelength.


## Function
```run-python
def hough_transform(image):
    """
    Apply the Hough transform to an image to detect lines.

    Parameters
    ----------
    image : ndarray
        Input image.

    theta_range : tuple or None, optional
        Range of theta values to use, specified as a tuple (min_theta, max_theta).
        If not specified, the range (-pi/2, pi/2) is used.
    Returns
    -------
    rhos : ndarray
        Distance values for each row in the Hough transform accumulator.
    thetas : ndarray
        Angle values for each column in the Hough transform accumulator.
    accumulator : ndarray
        Hough transform accumulator array.
    """
    h, w = image.shape
    diag_len = np.sqrt((h-1)**2 + (w-1)**2)
    num_rhos = int(2 * diag_len)
    rhos = np.linspace(-diag_len, diag_len, num=num_rhos)
    hough, thetas, rhos = hough_line(image)
    return rhos, np.rad2deg(thetas), hough
```
### Description

The `hough_transform` function takes an image as input and applies the Hough transform to detect lines in the image. The output of the function is a Hough transform accumulator array, which can be used to detect the lines in the image.

Here's a description of the inputs and outputs:

Inputs:

-   `image`: A NumPy array representing the input image.
-   `theta_range`: A tuple specifying the range of theta values to use in the Hough transform. If not specified, the default range (-pi/2, pi/2) is used.

Outputs:

-   `rhos`: A NumPy array representing the distance values for each row in the Hough transform accumulator.
-   `thetas`: A NumPy array representing the angle values for each column in the Hough transform accumulator.
-   `accumulator`: A NumPy array representing the Hough transform accumulator array.


### Function:
```run-python
def Spiral_Fourier_Transform(Image,Table,R_min_multiple,m,plot,save):
    """A function to calculate the Spiral Fourier Transform and the winding angle of a given image.

    Args:
    Image (numpy.ndarray): A 2D numpy array representing the input image.
    Table (astropy.Table): A table containing the coordinates and parameters of the object to be analyzed.
    R_min_multiple (float): The multiple of the effective radius at which the minimum radius is set.
    m (int): The order of the Fourier mode.
    plot (bool): A boolean indicating whether or not to plot the results.
    save (bool): A boolean indicating whether or not to save the plot.

    Returns:
    phi (float): The winding angle in degrees.
    """
    img = Image
    Tab = Table

    # First collect image info from Table
    x0 = np.array([img.shape[1]/2 + np.asarray(Tab['x'])]).astype(int) # x offset
    y0 = np.array([img.shape[0]/2 + np.asarray(Tab['y'])]).astype(int) # y offset
    R_e = 10**(np.asarray(Tab['log_re'])) # effective radius in pix
    log_R_e = np.asarray(Tab['log_re']) # log effective radius
    log_R_e_05 = np.log(10**np.asarray(Tab['log_re'])*R_min_multiple) # log half effective radius
    pa = np.asarray(Tab['theta']) # position angle
    q = np.asarray(Tab['q']) # axis ratio

    # Get the dimensions of the Image
    height, width = img.shape[:2]  

    # Calculate the maximum possible radius
    max_radius = min(x0, y0, width-x0, height-y0)
    max_R = max_radius -1

    # Create x and y index arrays
    y, x = np.indices(img.shape)

    # Center index arrays
    x -= x0
    y -= y0

    # Deprojecting x,y by a series of affine transformations

    # Rotate by minus position angle
    ct = np.cos(-pa)
    st = np.sin(-pa)

    # Stretch according to axis ratio and rotation
    xp = (y * ct + x * st) / q
    yp = (-y * st + x * ct)

    # Convert to Polar
    rp2 = xp ** 2 +  yp ** 2
    rp = np.sqrt(rp2)
    tp = np.arctan2(yp, xp)

    # Define ln(r),theta image dimensions
    n_lnr = 150
    n_theta = 150

    # Create index arrays
    lnr, theta = np.indices((n_lnr, n_theta))

    # Define bounds for image dimensions
    lnr_min = float(log_R_e_05)
    lnr_max = float(np.log(int(max_R) -1))
    theta_max = 360
    lnr = (lnr / n_lnr) * (lnr_max - lnr_min) + lnr_min
    theta = theta * theta_max / n_theta

	# Define xp and yp in terms of new coord system
    xp = np.exp(lnr) * np.sin(np.radians(theta))
    yp = np.exp(lnr) * np.cos(np.radians(theta))

	# this is an attempt at using the above deprojection code
    # to do the inverse by pa -> -pa and q -> 1/q  
    ct = np.cos(pa)
    st = np.sin(pa)
    x = (yp * ct + xp * st) * q
    y = (-yp * st + xp * ct)
    x += y0
    y += x0
    # Create a Regular grid from interpolation
    img_interp = RegularGridInterpolator((np.arange(img.shape[0]),
                                          np.arange(img.shape[1])), img)

    # Define allowed indices
    ok = (x >= 0) & (x < img.shape[0] - 1)
    ok &= (y >= 0) & (y < img.shape[1] - 1)

    # Create image from interpolation
    img_lnr_theta = img_interp((x, y))

	# Use broadcasting to do multiple p at once
    p = np.arange(-25, 25, 0.1).reshape((-1, 1, 1))
    weight = np.exp(1j*(m * np.radians(theta) + lnr * p))
    D = img_lnr_theta.sum()
    A = 1/D * abs((img_lnr_theta * weight).sum((-1, -2)))

    # Calculate winding angle from maximum of Spiral Power spectrum
    p_max = p.ravel()[A.argmax()]
    phi = np.degrees(np.arctan(-m/p_max))
    print('Winding angle \\u03C6 =', phi)

    if plot == True:
        # Spiral Power Spectrum
        plt.figure()
        plt.plot(p.ravel(), A,'k')
        plt.vlines(p_max,0,np.max(A),'k','dashed','$p_(max)$')
        plt.legend(['Spiral Power Spectrum ','$p_{max}$'],loc='upper left')
        plt.title('Spiral Fourier Transform (m = {})'.format(m))
        plt.xlabel('p')
        plt.xticks([-20,-10,p_max,0,10,20],['-20','-10','{}'.format(np.around(p_max,1)),'0','10','20'])
        plt.ylabel('|A(p,m)|');
        if save == True:
            plt.savefig('Power Spectrum.png')

		# ln(r) theta image
        plt.figure()
        plt.imshow(img_lnr_theta.T, vmin=1000, vmax=1200,
           extent=(lnr_min, lnr_max, 0, theta_max),
           origin='lower', aspect='auto');
        plt.xlabel('\\u03B8 (radians)')
        plt.ylabel('log(R)')
        if save == True:
            plt.savefig('log(R) Theta image.png')

		# Labeled galaxy Image
        fig, ax = plt.subplots()
        ax.imshow(img,vmin=1000,vmax=1200)

  

        # Define circle
        R_e_1 = Circle((x0,y0),R_e,edgecolor='black', facecolor=None, fill=False)
        R_e_05 = Circle((x0,y0),R_min_multiple*R_e,edgecolor='red', facecolor=None, fill=False)
        ax.plot(x0,y0,'xk')
        ax.add_patch(R_e_1)
        ax.add_patch(R_e_05)
        ax.legend(['center','$R_e$','${}\\, R_e$'.format(R_min_multiple)])
        ax.axis('off')
        if save == True:
            plt.savefig('Labelled R_e image.png')
        return phi
    else:
        return phi
```

The function performs the following operations:

-   Collects image information from the Table.
-   Calculates the maximum possible radius of the image.
-   De-projects the image by rotating it by minus position angle, stretching it according to axis ratio and rotation, and converting it to polar coordinates.
-   Defines the dimensions of the new coordinate system.
-   Interpolates the image onto a regular grid.
-   Calculates the Spiral Fourier Transform using the interpolated image.
-   Calculates the winding angle from the maximum of the Spiral Power spectrum.
-   Plots the Spiral Power Spectrum and the ln(r) theta image if plot is True.
-   Saves the plot if save is True.

### Function:
```run-python
def Spiral_power_spec(Image,Table,R_min_multiple,m):
    """
    This function calculates the Spiral Power Spectrum of an input image based on a given table of galaxy properties.

    Parameters:
    Image (numpy array): Input image to be analyzed
    Table (astropy Table): Table containing galaxy properties including x, y, log_re, theta, and q
    R_min_multiple (float): Multiplicative factor for the effective radius to set the minimum radius for the Spiral Power Spectrum
    m (int): Integer value for the number of spiral arms to analyze

    Returns:
    A (numpy array): Spiral Power Spectrum values
    p (numpy array): Fourier mode values
    p_max (float): Fourier mode corresponding to the maximum Spiral Power Spectrum value
    phi (float): Winding angle of the spiral arms in degrees
    """
    img = Image
    Tab = Table

    # First collect image info from Table
    x0 = np.array([img.shape[1]/2 + np.asarray(Tab['x'])]).astype(int) # x offset
    y0 = np.array([img.shape[0]/2 + np.asarray(Tab['y'])]).astype(int) # y offset
    R_e = 10**(np.asarray(Tab['log_re'])) # effective radius in pix
    log_R_e = np.asarray(Tab['log_re']) # log effective radius
    log_R_e_05 = np.log(10**np.asarray(Tab['log_re'])*R_min_multiple) # log half effective radius
    pa = np.asarray(Tab['theta']) # position angle
    q = np.asarray(Tab['q']) # axis ratio

    # Get the dimensions of the Image
    height, width = img.shape[:2]  

    # Calculate the maximum possible radius
    max_radius = min(x0, y0, width-x0, height-y0)
    max_R = max_radius -1

    # Create x and y index arrays
    y, x = np.indices(img.shape)

    # Center index arrays
    x -= x0
    y -= y0

    # Deprojecting x,y by a series of affine transformations

    # Rotate by minus position angle
    ct = np.cos(-pa)
    st = np.sin(-pa)

    # Stretch according to axis ratio and rotation
    xp = (y * ct + x * st) / q
    yp = (-y * st + x * ct)

    # Convert to Polar
    rp2 = xp ** 2 +  yp ** 2
    rp = np.sqrt(rp2)
    tp = np.arctan2(yp, xp)

    # Define ln(r),theta image dimensions
    n_lnr = 150
    n_theta = 150

    # Create index arrays
    lnr, theta = np.indices((n_lnr, n_theta))

    # Define bounds for image dimensions
    lnr_min = float(log_R_e_05)
    lnr_max = float(np.log(int(max_R) -1))
    theta_max = 360
    lnr = (lnr / n_lnr) * (lnr_max - lnr_min) + lnr_min
    theta = theta * theta_max / n_theta

    # Define xp and yp in terms of new coord system
    xp = np.exp(lnr) * np.sin(np.radians(theta))
    yp = np.exp(lnr) * np.cos(np.radians(theta))

    # this is an attempt at using the above deprojection code
    # to do the inverse by pa -> -pa and q -> 1/q  
    ct = np.cos(pa)
    st = np.sin(pa)
    x = (yp * ct + xp * st) * q
    y = (-yp * st + xp * ct)
    x += y0
    y += x0

	# Create a Regular grid from interpolation
    img_interp = RegularGridInterpolator((np.arange(img.shape[0]),
                                          np.arange(img.shape[1])), img)

    # Define allowed indices
    ok = (x >= 0) & (x < img.shape[0] - 1)
    ok &= (y >= 0) & (y < img.shape[1] - 1)

    # Create image from interpolation
    img_lnr_theta = img_interp((x, y))

    # Use broadcasting to do multiple p at once
    p = np.arange(-25, 25, 0.1).reshape((-1, 1, 1))
    weight = np.exp(1j*(m * np.radians(theta) + lnr * p))
    D = img_lnr_theta.sum()
    A = 1/D * abs((img_lnr_theta * weight).sum((-1, -2)))

	# Calculate winding angle from maximum of Spiral Power spectrum
    p_max = p.ravel()[A.argmax()]
    phi = np.degrees(np.arctan(-m/p_max))
    #print('Winding angle \\u03C6 =', phi)
    return A, p, p_max, phi
```
#### Function description: 
This function calculates the Spiral Power Spectrum of an input image based on a given table of galaxy properties. It first extracts necessary information from the table, such as the x and y offsets, effective radius, position angle, and axis ratio. Then, it centers and deprojects the image by rotating, stretching, and converting to polar coordinates. It creates a new coordinate system with defined dimensions for ln(r) and theta and interpolates the image onto a regular grid. It uses broadcasting to analyze multiple values of p at once and calculates the Spiral Power Spectrum by taking the absolute value of the sum of the image multiplied by the weight (a complex exponential based on m, theta, lnr, and p) and dividing by the sum of the image. Finally, it calculates the winding angle of the spiral arms based on the maximum Spiral Power Spectrum value.

#### Inputs:

-   `Image` (numpy array): Input image to be analysed
-   `Table` (astropy Table): Table containing galaxy properties including `x`, `y`, `log_re`, `theta`, and `q`
-   `R_min_multiple` (float): Multiplicative factor for the effective radius to set the minimum radius for the Spiral Power Spectrum
-   `m` (int): Integer value for the number of spiral arms to analyse

#### Outputs:

-   `A` (numpy array): Spiral Power Spectrum values
-   `p` (numpy array): Fourier mode values
-   `p_max` (float): Fourier mode corresponding to the maximum Spiral Power Spectrum value
-   `phi` (float): Winding angle of the spiral arms in degrees

### Function:
```run-python
def Number_of_arms(Image,Table,R_e_multiple):
		""" This function calculates the number of spiral arms in an image by analysing its power spectrum.
	
	Parameters:
		-   Image: a 2D numpy array representing the image.
	-   Table: a dictionary containing the logarithmic spiral model parameters (see Spiral_power_spec function).
	-   R_e_multiple: the value of the effective radius to be used for the logarithmic spiral model.
	
	Returns:
	-   An integer representing the estimated number of spiral arms in the image.
    """
    # Initialise empty arrays
    m_arr = np.empty_like(m).astype(float)

    # Create Loop
    for i in range(0,len(m)):
        A, p, p_max, phi = Spiral_power_spec(Image,Table,R_e_multiple,m[i])
        m_arr[i] = np.max(A)
        A_arr[:,i] = A
    print('Number of arms: ',m[np.argmax(m_arr)])
    #print(m_arr)
    return m[np.argmax(m_arr)]
```
#### Function description:

This function takes an image and a table of parameters for spiral galaxies and calculates the number of spiral arms present in the image using the `Spiral_power_spec` function. The number of arms is determined by finding the value of "m" that maximizes the Spiral Power spectrum of the image.

#### Inputs:

-   Image: a numpy array representing an image of a spiral galaxy
-   Table: a table of parameters for spiral galaxies containing the following columns:
    -   `x`: x coordinate of center of galaxy
    -   `y`: y coordinate of center of galaxy
    -   `log_re`: log10 of the effective radius of galaxy in pixels
    -   `theta`: position angle of galaxy in degrees
    -   `q`: axis ratio of galaxy
-   R_e_multiple: a float representing a multiple of the effective radius used to set the minimum radius for calculating the Spiral Power spectrum

#### Outputs:

-   An integer representing the estimated number of spiral arms present in the image.


## Function:
```run-python 
def SN(A):
    """This function calculates the signal to noise for the global maxima as well as a weighting list for each component

    Args:
        A (numpy array): A complex array representing the spiral fourier transform of an image

    Returns:
        SN_max (float): Signal to noise on the global maxima
        SN_weightings (numpy array): Signal to noise for each p
    """
    # get average of power spectrum
    L = np.average(np.abs(A))

	# Calculate rms estimate of the spectrum
    sigma = np.sqrt(np.average((np.abs(A)-L)**2))

    # Calculate signal to noise of global maxima using sigma and L
    SN_max = (np.abs(A[np.argmax(np.abs(A))])-L)/sigma

    # Calculate signal to noise of all values to provide a weighting list
    SN_weightings = (np.abs(A)-L)/sigma

    return SN_max, SN_weightings
```
### Function: SN(A)

#### Inputs:

-   A: numpy array, input signal or power spectrum

#### Outputs:

-   SN_max: float, signal to noise ratio of the global maxima of the input signal/power spectrum
-   SN_weightings: numpy array, signal to noise ratios of all values of the input signal/power spectrum, used as a weighting list

Functionality:

-   Calculates the average power spectrum of the input signal/power spectrum
-   Calculates the root mean square estimate of the input signal/power spectrum
-   Calculates the signal to noise ratio of the global maxima using the average and root mean square estimate
-   Calculates the signal to noise ratio of all values of the input signal/power spectrum using the average and root mean square estimate as a weighting list
-   Returns the signal to noise ratio of the global maxima and the signal to noise ratios of all values

## Update:

- Adding the signal to noise functionality to spiral power spectrum

```run-python
def Spiral_power_spec(Image,Table,R_min_multiple,m):
    """
    This function calculates the Spiral Power Spectrum of an input image based on a given table of galaxy properties.

    Parameters:
    Image (numpy array): Input image to be analyzed
    Table (astropy Table): Table containing galaxy properties including x, y, log_re, theta, and q
    R_min_multiple (float): Multiplicative factor for the effective radius to set the minimum radius for the Spiral Power Spectrum
    m (int): Integer value for the number of spiral arms to analyze

    Returns:
    A (numpy array): Spiral Power Spectrum values
    p (numpy array): Fourier mode values
    SN_w (numpy array): the signal to noise wights for each A(p,m)
    p_max (float): Fourier mode corresponding to the maximum Spiral Power Spectrum value
    SN_m (float): Signal to noise of the global maxima
    phi (float): Winding angle of the spiral arms in degrees
    """

    img = Image
    Tab = Table

	# First collect image info from Table
    x0 = np.array([img.shape[1]/2 + np.asarray(Tab['x'])]).astype(int) # x offset
    y0 = np.array([img.shape[0]/2 + np.asarray(Tab['y'])]).astype(int) # y offset
    R_e = 10**(np.asarray(Tab['log_re'])) # effective radius in pix
    log_R_e = np.asarray(Tab['log_re']) # log effective radius
    log_R_e_05 = np.log(10**np.asarray(Tab['log_re'])*R_min_multiple) # log half effective radius
    pa = np.asarray(Tab['theta']) # position angle
    q = np.asarray(Tab['q']) # axis ratio

	# Get the dimensions of the Image
    height, width = img.shape[:2]  

    # Calculate the maximum possible radius
    max_radius = min(x0, y0, width-x0, height-y0)
    max_R = max_radius -1

	# Create x and y index arrays
    y, x = np.indices(img.shape)

    # Center index arrays
    x -= x0
    y -= y0

    # Deprojecting x,y by a series of affine transformations
    # Rotate by minus position angle
    ct = np.cos(-pa)
    st = np.sin(-pa)

    # Stretch according to axis ratio and rotation
    xp = (y * ct + x * st) / q
    yp = (-y * st + x * ct)

	# Convert to Polar
    rp2 = xp ** 2 +  yp ** 2
    rp = np.sqrt(rp2)
    tp = np.arctan2(yp, xp)

	# Define ln(r),theta image dimensions
    n_lnr = 150
    n_theta = 150

    # Create index arrays
    lnr, theta = np.indices((n_lnr, n_theta))

	# Define bounds for image dimensions
    lnr_min = float(log_R_e_05)
    lnr_max = float(np.log(int(max_R) -1))
    theta_max = 360
    lnr = (lnr / n_lnr) * (lnr_max - lnr_min) + lnr_min
    theta = theta * theta_max / n_theta

	# Define xp and yp in terms of new coord system
    xp = np.exp(lnr) * np.sin(np.radians(theta))
    yp = np.exp(lnr) * np.cos(np.radians(theta))
    
    # this is an attempt at using the above deprojection code
    # to do the inverse by pa -> -pa and q -> 1/q  
    ct = np.cos(pa)
    st = np.sin(pa)
    x = (yp * ct + xp * st) * q
    y = (-yp * st + xp * ct)
    x += y0
    y += x0

    # Create a Regular grid from interpolation
    img_interp = RegularGridInterpolator((np.arange(img.shape[0]),

                                          np.arange(img.shape[1])), img)

    # Define allowed indices
    ok = (x >= 0) & (x < img.shape[0] - 1)
    ok &= (y >= 0) & (y < img.shape[1] - 1)

    # Create image from interpolation
    img_lnr_theta = img_interp((x, y))

    # Use broadcasting to do multiple p at once
    p = np.arange(-25, 25, 0.1).reshape((-1, 1, 1))
    weight = np.exp(1j*(m * np.radians(theta) + lnr * p))
    D = img_lnr_theta.sum()
    A = 1/D * abs((img_lnr_theta * weight).sum((-1, -2)))

    # Calculate winding angle from maximum of Spiral Power spectrum
    p_max = p.ravel()[A.argmax()]
    phi = np.degrees(np.arctan(-m/p_max))
    #print('Winding angle \\u03C6 =', phi)

	# Calculate signal to noise
    SN_m, SN_w = SN(A)

    return A, p, SN_w, p_max, SN_m, phi
``` 
### Function Description

The `Spiral_power_spec` function calculates the Spiral Power Spectrum of an input image based on a given table of galaxy properties.

### Inputs

The function takes the following inputs:

-   `Image` (numpy array): Input image to be analyzed
-   `Table` (astropy Table): Table containing galaxy properties including x, y, log_re, theta, and q
-   `R_min_multiple` (float): Multiplicative factor for the effective radius to set the minimum radius for the Spiral Power Spectrum
-   `m` (int): Integer value for the number of spiral arms to analyze

### Outputs

The function returns the following outputs:

-   `A` (numpy array): Spiral Power Spectrum values
-   `p` (numpy array): Fourier mode values
-   `SN_w` (numpy array): the signal to noise wights for each A(p,m)
-   `p_max` (float): Fourier mode corresponding to the maximum Spiral Power Spectrum value
-   `SN_m` (float): Signal to noise of the global maxima
-   `phi` (float): Winding angle of the spiral arms in degrees

### Function Steps

The function performs the following steps:

1.  Collects image information from the input table.
2.  Calculates the maximum possible radius for the input image.
3.  Creates x and y index arrays for the input image.
4.  Deprojects x and y by a series of affine transformations.
5.  Converts to polar coordinates.
6.  Defines the dimensions of the ln(r),theta image.
7.  Defines index arrays for ln(r) and theta.
8.  Defines bounds for image dimensions.
9.  Defines xp and yp in terms of new coordinate system.
10.  Does the inverse transformation using pa -> -pa and q -> 1/q.
11.  Creates a regular grid from interpolation.
12.  Defines allowed indices.
13.  Creates an image from interpolation.
14.  Calculates the Spiral Power Spectrum using Fourier modes.
15.  Calculates the winding angle from the maximum Spiral Power Spectrum value.
16.  Calculates signal to noise for both individual weights and the global maximum.

## Function
```run-python
def gen_spiral(p_max,A_p_m,m,R_e,R_min_multiple):
    """
    Generates a polar spiral with the given parameters and returns its x and y coordinates.

    Args:
        p_max (float): The maximum power density of the spiral.
        A_p_m (numpy.ndarray): Array of complex amplitudes of the spiral.
        m (float): Constant that determines the rate of increase in pitch of the spiral.
        R_e (float): The radius of the spiral.
        R_min_multiple (float): Multiple of R_e that represents the minimum radius at which the spiral can be sampled.

    Returns:
        tuple: A tuple of two numpy arrays representing the x and y coordinates of the polar spiral.
    """

    # Create Polar Spiral
    A_p_max = A_p_m[np.argmax(A_p_m)]
    argument = np.angle(A_p_max)
    r_0 = 1                                     # Scale 1:1 pix
    theta = np.linspace(2*np.pi,8*(np.pi),3600)
    phi = np.degrees(np.arctan(-m/p_max))
    r = r_0 *np.exp(theta*np.abs(np.tan(np.radians(phi))))
    
    # Convert to Cartesian
    x = r*np.cos(theta)
    y = r*np.sin(theta)

    rot_mat = np.array([[np.cos(argument),-np.sin(argument)],
                    [np.sin(argument), np.cos(argument)]])

    rotated_vector = rot_mat @ vector

    x_ = rotated_vector[0]
    y_ = rotated_vector[1]

    # Trim line plot so that it doesn't enter the unsampled area
    count = 0
    for i in range(0,len(x_)):
        if np.sqrt(x_[i]**2 + (y_[i]**2)) <= R_min_multiple*R_e:
            count = count +  1
        else:
            continue
    x_ = x_[count:len(x_)]
    y_ = y_[count:len(y_)]

	return x_,y_
```
**Function: gen_spiral**

Generates a polar spiral with the given parameters and returns its x and y coordinates.

**Inputs:**

-   `p_max` (float): The maximum power density of the spiral.
-   `A_p_m` (numpy.ndarray): Array of complex amplitudes of the spiral.
-   `m` (float): Constant that determines the rate of increase in pitch of the spiral.
-   `R_e` (float): The radius of the spiral.
-   `R_min_multiple` (float): Multiple of R_e that represents the minimum radius at which the spiral can be sampled.

**Outputs:**

-   tuple: A tuple of two numpy arrays representing the x and y coordinates of the polar spiral.

## Function:
```run-python
def SFM(spectrum):
    """
    Calculates the spectral flatness measure (SFM) of a given spectrum.

    The SFM is defined as the ratio of the geometric mean to the arithmetic mean of the spectrum.

    Args:
    - spectrum (ndarray): 1-D array containing the power spectrum of a signal.

    Returns:
    - SFM (float): the spectral flatness measure of the input spectrum.
    """
    arithmetic_mean = np.mean(spectrum)
    geometric_mean = gmean(spectrum)
    SFM = arithmetic_mean/geometric_mean
    return SFM

```
#### SFM Function:
The `SFM` function takes in a one-dimensional numpy array representing the power spectrum of a signal as its input, and calculates the spectral flatness measure (SFM) of the spectrum. The SFM is defined as the ratio of the geometric mean to the arithmetic mean of the spectrum. The function then returns the calculated SFM as a float value.

**Inputs**

-   `spectrum` (ndarray): 1-D array containing the power spectrum of a signal.

**Outputs**

-   `SFM` (float): the spectral flatness measure of the input spectrum.


## Function:
```run-python
def save_spiral_power_spec(OBJID, band, band_index,
							A, A_p_m, p, SN_w, p_max, SN_m, phi):

    """This function assembles the outputs of Spiral_power_spec() function into a FITS table and saves it to disk
 

    Args:
        OBJID (str): ID of the object
        band (str): Name of the band
        band_index (int): Index of the band
        A (numpy array): Complex array representing the spiral Fourier transform of an image
        p (numpy array): Array of radial frequencies
        SN_w (numpy array): Signal-to-noise ratio for each radial frequency
        p_max (float): Radial frequency of the global maximum
        SN_m (float): Signal-to-noise ratio at the global maximum
        phi (float): Phase of the complex value at the global maximum

    Returns:
        (str): Filename of the saved FITS file
    """
    # Create FITS table
    hdu = fits.BinTableHDU.from_columns([
        fits.Column(name='abs(A)', format='D', array=A.real),
        fits.Column(name='A_real', format='D', array=A_p_m.real),
        fits.Column(name='A_imag', format='D', array=A_p_m.imag),
        fits.Column(name='p', format='D', array=p),
        fits.Column(name='SN_w', format='D', array=SN_w),
        fits.Column(name='p_max', format='D', array=[p_max]),
        fits.Column(name='SN_m', format='D', array=[SN_m]),
        fits.Column(name='phi', format='D', array=[phi])
    ])

    # Add header information
    hdu.header['OBJID'] = OBJID
    hdu.header['BAND'] = band
    hdu.header['BANDINDX'] = band_index

    # Save FITS file
    filename = f'{OBJID}_{band}_{band_index}.fits'
    hdu.writeto(filename, overwrite=True)

    return filename, hdu
```


**Function: save_spiral_power_spec**

The `save_spiral_power_spec` function takes the outputs of the `Spiral_power_spec` function and assembles them into a FITS table which is saved to disk. The function takes the following input parameters:

**Inputs**

-   `OBJID` (str): ID of the object.
-   `band` (str): Name of the band.
-   `band_index` (int): Index of the band.
-   `A` (numpy array): Complex array representing the spiral Fourier transform of an image.
-   `A_p_m` (numpy array): Complex array representing the spiral Fourier transform of an image, after projection onto the principal modes.
-   `p` (numpy array): Array of radial frequencies.
-   `SN_w` (numpy array): Signal-to-noise ratio for each radial frequency.
-   `p_max` (float): Radial frequency of the global maximum.
-   `SN_m` (float): Signal-to-noise ratio at the global maximum.
-   `phi` (float): Phase of the complex value at the global maximum.

The function returns a tuple with two elements: **Outputs**

-   `filename` (str): Filename of the saved FITS file.
-   `hdu` (fits.BinTableHDU): FITS table containing the spiral

## Function:
```run-python
def collect_candidate_info(candidate_list, catalogue):
    """
    Collects information from a catalogue for a list of candidates.
    
    Args:
    candidate_list (array-like): A list of candidate objects to search for in the catalogue.
    catalogue (astropy.table.Table): A table object containing the catalogue data.
    
    Returns:
    tuple: A tuple containing the following arrays:
        U_mags (numpy.ndarray): Array of U magnitudes for each candidate.
        R_mags (numpy.ndarray): Array of R magnitudes for each candidate.
        U_mag_errs (numpy.ndarray): Array of U magnitude errors for each candidate.
        R_mag_errs (numpy.ndarray): Array of R magnitude errors for each candidate.
        dists (numpy.ndarray): Array of comoving distances for each candidate.
        zs (numpy.ndarray): Array of redshifts for each candidate.
        zerrs (numpy.ndarray): Array of redshift errors for each candidate.
        colours (numpy.ndarray): Array of U-R colours for each candidate.
        colour_errs (numpy.ndarray): Array of errors in U-R colour for each candidate.
    """
    U_mags = np.empty_like(candidate_list, dtype=float)
    R_mags = np.empty_like(candidate_list, dtype=float)
    U_mag_errs = np.empty_like(candidate_list, dtype=float)
    R_mag_errs = np.empty_like(candidate_list, dtype=float)
    dists = np.empty_like(candidate_list, dtype=float)
    zs = np.empty_like(candidate_list, dtype=float)
    zerrs = np.empty_like(candidate_list, dtype=float)
    colours = np.empty_like(candidate_list, dtype=float)
    colour_errs = np.empty_like(candidate_list, dtype=float)
    
    for i in range(len(candidate_list)):
        tab = cat_search(catalogue, candidate_list[i])
        U_mags[i] = float(tab['U'])
        R_mags[i] = float(tab['R'])
        U_mag_errs[i] = float(tab['UERR'])
        R_mag_errs[i] = float(tab['UERR'])
        dists[i] = float(tab['COMOVING_DISTANCE'])
        zs[i] = float(tab['REDSHIFT'])
        zerrs[i] = float(tab['REDSHIFTERR'])
        colours[i] = float(U_mags[i] - R_mags[i])
        colour_errs[i] = float(np.sqrt(U_mag_errs[i]**2 + R_mag_errs[i]**2))
        
    return U_mags, R_mags, U_mag_errs, R_mag_errs,
	     dists, zs, zerrs, colours, colour_errs

```
**Function: collect_candidate_info**

The `collect_candidate_info` function collects information on astronomical objects in a given catalogue based on a list of object IDs. It searches the catalogue for each object ID, retrieves relevant information such as magnitudes, redshifts, and distances, and stores the information in numpy arrays.

## Inputs:

-   `candidate_list`: A list of object IDs (str)
-   `catalogue`: A catalogue containing information on astronomical objects (pandas DataFrame)

## Outputs:

-   `U_mags`: Numpy array of U-band magnitudes for each object in `candidate_list`
-   `R_mags`: Numpy array of R-band magnitudes for each object in `candidate_list`
-   `U_mag_errs`: Numpy array of U-band magnitude errors for each object in `candidate_list`
-   `R_mag_errs`: Numpy array of R-band magnitude errors for each object in `candidate_list`
-   `dists`: Numpy array of comoving distances for each object in `candidate_list`
-   `zs`: Numpy array of redshifts for each object in `candidate_list`
-   `zerrs`: Numpy array of redshift errors for each object in `candidate_list`
-   `colours`: Numpy array of U-R colors for each object in `candidate_list`
-   `colour_errs`: Numpy array of U-R colour errors for each object in `candidate_list`

## Function:
```run-python
def var_from_dir_raid(candidates,parent_dir):
    # Create array of identifiers:
    identifiers = np.asarray([s[-4:] for s in candidates])
    identifiers.astype(str)

    comp_ = 'comp_'
    tab_ = 'tab_'

    # Assign all the candidates information from the directory raid to variables
    for i in range(0,len(identifiers)):
        exec('{}{}, {}{} = gfits.Composite_from_directory_raid("{}","{}")'
             .format(tab_,identifiers[i],comp_,identifiers[i],candidates[i],parent_dir))

    # Create a list of variable names created
    comps_array = np.empty_like(candidates)
    tabs_array = np.empty_like(candidates)
 

    for i in range(0,len(candidates)):
        comps_array[i] = '{}{}'.format(comp_,identifiers[i])
        tabs_array[i] = '{}{}'.format(tab_,identifiers[i])

    return comps_array, tabs_array
```
**Function: var_from_dir_raid**

The `var_from_dir_raid` function creates two arrays of variable names based on candidate list and parent directory provided. It iterates over the candidate list and reads the contents of the parent directory, creating composite fits files and tables for each candidate in the directory. Finally, it returns arrays of the composite fits file and table variable names created for each candidate.

## Inputs

The function `var_from_dir_raid` takes two arguments as inputs:

-   `candidate_list`: A list of candidate names.
-   `parent_dir`: A string representing the parent directory path where composite fits files for each candidate are stored.

## Outputs

The `var_from_dir_raid` function returns two arrays of variable names, which correspond to the composite fits files and tables created for each candidate in the directory. The arrays returned are:

-   `comps_array`: An array of variable names for the composite fits files created.
-   `tabs_array`: An array of variable names for the tables created.

## Function
```run-python
def get_variable_from_name(name):

    # Create a list of all the defined variables

    var_dict = globals()

    # Get the variables from the list

    var_value = var_dict.get(name)

    return var_value
```
**Function: get_variable_from_name**

The `get_variable_from_name` function retrieves the value of a variable by passing its name as a string. It first creates a dictionary of all the currently defined variables in the global scope using the `globals()` function. It then retrieves the value of the variable with the given name from the dictionary using the `get()` method.

## Inputs

The function takes a single input argument:

-   `name` (str): The name of the variable to get the value of.

## Outputs

The function returns the value of the variable with the given name. If the variable doesn't exist, it returns `None`.

## Function:
```run-python
def line_equation(point1, point2):
    """
    Given two points, return the equation of the line that passes through them
    in slope-intercept form: y = mx + b
    """
    x1, y1 = point1
    x2, y2 = point2

    # Calculate the slope (m)
    m = (y2 - y1) / (x2 - x1)

    # Calculate the y-intercept (b)
    c = y1 - m * x1

    # Return the equation of the line in slope-intercept form
    return m, c
```
**Function: line_equation**

This function takes two points (point1 and point2) in a 2D Cartesian plane and returns the equation of the line that passes through them in slope-intercept form: y = mx + b.

### Inputs:

-   `point1` : A tuple of two elements `(x1, y1)` representing the coordinates of the first point.
-   `point2` : A tuple of two elements `(x2, y2)` representing the coordinates of the second point.

### Outputs:

-   A tuple `(m, c)` representing the slope and y-intercept of the line respectively, where `m` is the slope and `c` is the y-intercept.

Note: `m` and `c` are floats, which can be used to form a linear equation of the form; $y = mx + c$

## Function:
```run-python
def normal_to_line(m, c, point):
    """
    Given the slope (m), y-intercept (c), and a point a line passes through,
    return the slope and y-intercept of the line that is normal (perpendicular) to it and passes through the point.
    """
    # Calculate the negative reciprocal of the slope to get the slope of the normal line
    m_normal = -1 / m
  
    # Calculate the y-intercept of the normal line using the point it passes through
    x, y = point
    b_normal = y - m_normal * x


    # Return the slope and y-intercept of the normal line
    return m_normal, b_normal
```
**Function: normal_to_line**
This function takes the slope `m`, y-intercept `c`, and a point `point` that the line passes through as inputs, and returns the slope and y-intercept of the line that is normal (perpendicular) to the original line and passes through the given point.

### Inputs:

-   `m` : A float representing the slope of the original line.
-   `c` : A float representing the y-intercept of the original line.
-   `point` : A tuple of two elements `(x, y)` representing the coordinates of the point that the normal line passes through.

### Outputs:

-   A tuple `(m_normal, b_normal)` representing the slope and y-intercept of the normal line respectively, where `m_normal` is the slope and `b_normal` is the y-intercept.

Note: `m_normal` and `b_normal` are floats, which can be used to form a linear equation of the form $y = m_{normal} * x + b_{normal}$.

## Function:
```run-python
def normal_from_points(x0,y0,x1,y1):
     """
    Calculates the normal vector of a line passing through two points.
  
    Args:
        x0 (float): The x-coordinate of the first point.
        y0 (float): The y-coordinate of the first point.
        x1 (float): The x-coordinate of the second point.
        y1 (float): The y-coordinate of the second point.

    Returns:
        Tuple[float, float]: A tuple containing the slope and y-intercept of the normal line
        to the line passing through (x0, y0) and (x1, y1). The normal line passes through the
        midpoint of the line segment connecting (x0, y0) and (x1, y1).

    Raises:
        ZeroDivisionError: If the line passing through (x0, y0) and (x1, y1) is vertical.
    """
    middle = (x0+((x1-x0)/2),y0+((y1-y0)/2))
    m,c= line_equation((x0,y0),(x1,y1))
    m_n, m_c = normal_to_line(m,c,middle)
    return m_n, m_c
```
**Function: normal_from_points**
This function calculates the slope and y-intercept of a line that is perpendicular to the line passing through two given points, and passes through the midpoint of these two points.

### Inputs:

-   `x0` : A float or an integer representing the x-coordinate of the first point.
-   `y0` : A float or an integer representing the y-coordinate of the first point.
-   `x1` : A float or an integer representing the x-coordinate of the second point.
-   `y1` : A float or an integer representing the y-coordinate of the second point.

### Outputs:

-   A tuple `(m_n, m_c)` representing the slope and y-intercept of the line that is normal (perpendicular) to the original line and passes through the midpoint of the two points respectively, where `m_n` is the slope and `m_c` is the y-intercept.

Note: `m_n` and `m_c` are floats, which can be used to form a linear equation of the form $y = m_n * x + m_c$.

## Function:
```run-python
def get_pixels_on_line(normal_intersect, m, c,pixels): 
#passed in the coordinates of the spiral-lin-line intercept
    """
    Computes an array of pixel coordinates that lie on a line passing through a given point
    and having a specified slope and y-intercept.

    Args:
        normal_intersect (Tuple[int, int]): A tuple containing the x and y coordinates of
            the point where the line intersects a normal line passing through the center of a spiral.

        m (float): The slope of the line.
        c (float): The y-intercept of the line.
        pixels (int): The number of pixels on either side of the intersection point to compute.

    Returns:
        numpy.ndarray: A 2D numpy array of shape (2*pixels, 2) containing the (x, y) pixel
        coordinates that lie on the line, in order from left to right or from top to bottom depending on the steepness of the line.
    """
    #returns 'result' which is an array of pixel co-ordinates
    resulf=np.empty((2*pixels,2))
    if (abs(m)<1): #count along the X-axis as it's not steep
        n=0
        for my_x in range(normal_intersect[0]-pixels,normal_intersect[0]+pixels):
            resulf[n]=(my_x,m*my_x+c)
            n=n+1
        resulf = np.flip(resulf,axis=0)

    else: #this is steep,so work in the y dimension
        n=0
        for my_y in range (normal_intersect[1]-pixels,normal_intersect[1]+pixels):
            resulf[n]=(((my_y-c)/m),my_y)
            n=n+1
    result=resulf.astype(int)
    return result
```
**Function: get_pixels_on_line**
This function computes an array of pixel coordinates that lie on a line passing through a given point and having a specified slope and y-intercept. The function first checks whether the line is steep or not, and then iterates over the pixels on the line to calculate their coordinates.

### Inputs:

-   `normal_intersect` (Tuple[int, int]): A tuple containing the x and y coordinates of the point where the line intersects a normal line passing through the center of a spiral.
-   `m` (float): The slope of the line.
-   `c` (float): The y-intercept of the line.
-   `pixels` (int): The number of pixels on either side of the intersection point to compute.

### Output:

-   `numpy.ndarray`: A 2D numpy array of shape (2 * pixels, 2) containing the (x, y) pixel coordinates that lie on the line, in order from left to right or from top to bottom depending on the steepness of the line.

## Function:
```run-python
def get_normals(spiral_points,num_samples):
    """
    Computes the normal lines to a spiral at specified sample points.

    Args:
        spiral_points (numpy.ndarray): A 2D numpy array containing the (x, y) coordinates of points along the spiral curve.
        num_samples (int): The number of sample points to use for computing the normal lines.

    Returns:
        Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]: A tuple containing three numpy arrays: the slope and y-intercept of the normal lines at each sample point, and the (x, y) coordinates of the sample points.
    """

    samples = np.linspace(0,len(points)-1,num_samples,dtype=int)
    tangent_points = spiral_points[samples]
 
    bigger_r  = samples+1
    smaller_r = samples-1

    for i in range(0,len(bigger_r)):
        if bigger_r[i] >= len(points):
            bigger_r[i] = len(points)-1
        else:
            continue

    big_point   = points[bigger_r]
    small_point = points[smaller_r]
 
    m_array = np.zeros(len(big_point))
    c_array = np.zeros(len(big_point))

    for i in range(0,len(big_point)):
        m_array[i], c_array[i] = normal_from_points(small_point[i,0],small_point[i,1],big_point[i,0],big_point[i,1])
    return m_array, c_array, tangent_points
```
**Function: get_normals**
This function computes the slope and y-intercept of the normal lines passing through a set of points on a spiral curve.

### Inputs:

-  ` spiral_points` (numpy.ndarray): A 2D numpy array containing the (x, y) coordinates of the points on the spiral curve.
-   `num_samples` (int): The number of points to sample from the spiral curve.

### Output:

-   `m_array` (numpy.ndarray): A 1D numpy array containing the slopes of the normal lines passing through the spiral points.
-   `c_array` (numpy.ndarray): A 1D numpy array containing the y-intercepts of the normal lines passing through the spiral points.
-   `tangent_points` (numpy.ndarray): A 2D numpy array containing the (x, y) coordinates of the sampled points on the spiral curve.

Note: The output arrays have the same length as the number of sampled points on the spiral curve.

## Function:
```run-python
def spiral_normal_distributions(image,table,
spiral_points,num_samples,half_line_width,plot,analysis):
    """
    Computes normal distributions along a spiral arm in an astronomical image.

    Parameters:
    -----------
    image : numpy.ndarray
        The input astronomical image.
    table : astropy.table.table.Table
        A table containing galaxy properties.
    spiral_points : numpy.ndarray
        An array of points on the spiral arm.
    num_samples : int
        Number of samples to be taken along the spiral arm.
    half_line_width : int
        Half-width of the line in pixels.
    plot : bool
        Whether or not to plot the output.
    analysis : bool
        Whether or not to perform an analysis on the plotted output.

    Returns:
    --------
    numpy.ndarray
        A transposed array of stacked pixel values representing the normal distributions.
    """
    # Get equations of normal lines using above function
    m_array, c_array, tangent_points = get_normals(spiral_points,num_samples)

	# Calculate distance of each tangent point in terms of R_e
    # First collect centers and R_e from table
    x0 = table['x'] + image.shape[1]/2
    y0 = table['y'] + image.shape[0]/2
    R_e = 10**(table['log_re'])

    # Loop through tangent points and calculate radius at each point
    radii_in_pixels = np.empty(len(tangent_points))

    for i in range(0,len(tangent_points)):
        radii_in_pixels[i] =  np.sqrt((x0-tangent_points[i,0])**2+(y0-tangent_points[i,1])**2)

    # Get tangent_points in terms of R_e
    radii_in_R_e = radii_in_pixels/R_e

	# Sample radii array to get y_ticks
    y_tick_samples = np.linspace(0,len(radii_in_R_e)-1,5).astype(int)
    y_ticks = radii_in_R_e[y_tick_samples]
    y_tick_labels = np.array(['{}'.format(np.around(y_ticks[0],1)),
                              '{}'.format(np.around(y_ticks[1],1)),
                              '{}'.format(np.around(y_ticks[2],1)),
                              '{}'.format(np.around(y_ticks[3],1)),
                              '{}'.format(np.around(y_ticks[4],1))])

    # Set up Params for x_ticks
    quarter_line_width = half_line_width/2
    line_width = half_line_width*2

    # Stack sampled pixels into image
    stacked_line_pixels = np.zeros((line_width,len(tangent_points)))

    for j in range(1,len(tangent_points)):
        array = get_pixels_on_line(tangent_points[j].astype(int),
        m_array[j],c_array[j],half_line_width)

		line_pixel_values = np.empty(len(array))
        for i in range(0,array.shape[0]):
            line_pixel_values[i] = iso_im[array[i,0],array[i,1]]
	        stacked_line_pixels[:,j] = line_pixel_values
		
		stacked_line_pixels = stacked_line_pixels.T

    # Plotting section
    if plot == True:
        colours =  plt.cm.plasma(np.linspace(0,1,len(tangent_points)))
        plt.figure()
        plt.imshow(image,vmin=1000,vmax=1200)
        plt.plot(spiral_points[:,0],spiral_points[:,1],'r')
        plt.xlim(0,image.shape[1])
        plt.ylim(0,image.shape[0])
        plt.axis('off')

        for i in range(1,len(tangent_points)):
            arr = get_pixels_on_line(tangent_points[i].astype(int),
            m_array[i],c_array[i],20)
            arr = np.asarray(arr).astype(int)
            if analysis == True:
                if i%10 == 0:
                    plt.plot(arr[:,0],arr[:,1],c='k')
                else:
                    continue
            else:
                plt.plot(arr[:,0],arr[:,1],c=colours[i])

        plt.figure()
     plt.imshow(stacked_line_pixels,vmin=1000,
     vmax=1100,aspect='auto',origin='lower') # This is quite amazing!
        plt.xticks([0,half_line_width/2,
        half_line_width,half_line_width*1.5,line_width-1],
                   ['-{}'.format(half_line_width),
                    '-{}'.format(int(quarter_line_width)),
                    '0',
                    '{}'.format(int(quarter_line_width)),
                    '{}'.format(half_line_width)])

        plt.yticks(y_tick_samples,y_tick_labels)
        plt.xlabel('Distance from Spiral fit (pixels)')
        plt.ylabel('Radial Distance/$R_e$')
        if analysis == True:
          plt.hlines(np.arange(0,len(tangent_points),10),
          0,stacked_line_pixels.shape[1]-1,colors='k')

    return stacked_line_pixels.T
```
**Function: Spiral_normal_distributions**
The `Spiral_normal_distributions` function takes an astronomical image, a table containing galaxy properties, an array of points on a spiral arm, the number of samples to be taken along the spiral arm, half-width of the line in pixels, a boolean indicating whether or not to plot the output, and a boolean indicating whether or not to perform an analysis on the plotted output. It then computes normal distributions along the spiral arm, and returns a transposed array of stacked pixel values representing the normal distributions.

## Inputs

-   `image`: A numpy ndarray, the input astronomical image.
-   `table`: An astropy.table.table.Table, a table containing galaxy properties.
-   `spiral_points`: A numpy ndarray, an array of points on the spiral arm.
-   `num_samples`: An integer, the number of samples to be taken along the spiral arm.
-   `half_line_width`: An integer, half-width of the line in pixels.
-   `plot`: A boolean, whether or not to plot the output.
-   `analysis`: A boolean, whether or not to perform an analysis on the plotted output.

## Output

-   `stacked_line_pixels`: A numpy ndarray, a transposed array of stacked pixel values representing the normal distributions.

## Function:
```run-python
def R_e_bulge_mask(image,table):
    """
    Generates a mask for a given image based on a table of parameters related to a bulge.
    The mask is generated by calculating the Euclidean distance between each pixel in the image and the position
    of the brightest pixel (assumed to be the center of the bulge) in the image. Pixels within a certain distance
    (determined by a factor of the effective radius, Re) from the bulge center are set to zero in the mask, while
    pixels outside this distance are set to one. The resulting masked image is obtained by element-wise multiplication
    of the original image with the generated mask.

    Args:
        image (numpy.ndarray): A 2D numpy array representing the input image.
        table (dict or structured array): A dictionary or structured array containing the parameters related to the bulge, including the effective radius (Re), which is used to determine the size of the mask.
  
    Returns:
        numpy.ndarray: A masked version of the input image, where pixels within a certain distance from the center of
                       the bulge are set to zero and pixels outside this distance are preserved. The resulting masked
                       image has the same shape as the input image.
    """
    bulge_intensity = np.max(image)
    bulge_pos = np.asarray(np.argwhere(image == bulge_intensity))
    Re = 10**table['log_re']
    multiple = 0.3
    Re_mask = np.empty((image.shape[0],image.shape[1]))
    for i in range(0,image.shape[0]):
        for j in range(0,image.shape[1]):
            if np.sqrt((j-bulge_pos[0,1])**2 + (i-bulge_pos[0,0])**2) < multiple*Re:
                Re_mask[i,j] = 0
            else:
                Re_mask[i,j] = 1
    return image*Re_mask
```
**Function: R_e_bulge_mask**
This function generates a mask for a given image based on a table of parameters related to a bulge in the image. The mask is generated by calculating the Euclidean distance between each pixel in the image and the position of the brightest pixel (assumed to be the centre of the bulge) in the image. Pixels within a certain distance (determined by a factor of the effective radius, Re) from the bulge centre are set to zero in the mask, while pixels outside this distance are set to one. The resulting masked image is obtained by element-wise multiplication of the original image with the generated mask.

### Inputs

-   `image`: A 2D NumPy array representing the input image.
-   `table`: A dictionary or structured array containing the parameters related to the bulge, including the effective radius (Re), which is used to determine the size of the mask.

### Outputs

-   `image*Re_mask`: A masked version of the input image, where pixels within a certain distance from the centre of the bulge are set to zero and pixels outside this distance are preserved. The resulting masked image has the same shape as the input image.

## Update:

- Update the flux fraction function to use the `R_e_mask` to exclude the bulge

```run-python

```

## Function:
```run-python
def deproject_galaxy_image(image, center, position_angle, axis_ratio):
    """
    Deprojects a galaxy image based on position angle, axis ratio, and center coordinates.

    Args:
        image (ndarray): Input galaxy image.
        center (tuple): Center coordinates (x, y) of the galaxy in the image.
        position_angle (float): Position angle (in degrees) of the galaxy.
        axis_ratio (float): Axis ratio of the galaxy.

    Returns:
        ndarray: Deprojected galaxy image.
    """
    # Convert position angle to radians
    theta = np.deg2rad(position_angle)

    # Shift the galaxy center to the origin
    x, y = center
    image_centered = np.roll(np.roll(image, -y+image.shape[0]//2, axis=0), -x+image.shape[1]//2, axis=1)

    # Create a grid of coordinates centered at the origin
    xx, yy = np.meshgrid(np.arange(-image.shape[1]//2, image.shape[1]//2), np.arange(-image.shape[0]//2, image.shape[0]//2))

    # Rotate the grid by the position angle
    xx_rot = xx * np.cos(theta) + yy * np.sin(theta)
    yy_rot = -xx * np.sin(theta) + yy * np.cos(theta)

    # Scale the rotated grid by the axis ratio
    xx_scaled = xx_rot / axis_ratio
    yy_scaled = yy_rot * axis_ratio

    # Interpolate the deprojected image from the scaled grid to the original grid
    deprojected_image = RectBivariateSpline(yy_scaled[:, 0], xx_scaled[0, :], image_centered)(yy[:, 0], xx[0, :])

	return deprojected_image
```
**Function: Deproject_galaxy_image**

This function deprojects a galaxy image based on the given position angle, axis ratio, and center coordinates. The input is a 2D numpy array representing the galaxy image, a tuple of two integers representing the x and y coordinates of the galaxy center in the image, a float value representing the position angle of the galaxy in degrees, and a float value representing the axis ratio of the galaxy. The function performs the following steps:

1.  Converts the position angle from degrees to radians.
2.  Shifts the galaxy center to the origin of the image.
3.  Creates a grid of coordinates centered at the origin.
4.  Rotates the grid by the position angle.
5.  Scales the rotated grid by the axis ratio.
6.  Interpolates the deprojected image from the scaled grid to the original grid.
7.  Returns the deprojected galaxy image as a 2D numpy array.

Inputs:

-   `image` (ndarray): A 2D numpy array representing the galaxy image.
-   `center` (tuple): A tuple of two integers representing the x and y coordinates of the galaxy center in the image.
-   `position_angle` (float): A float value representing the position angle of the galaxy in degrees.
-   `axis_ratio` (float): A float value representing the axis ratio of the galaxy.

Outputs:

-   `deprojected_image` (ndarray): A 2D numpy array representing the deprojected galaxy image.

## Function:
```run-python
def CAS(image,table):
    """
    Calculates Concentration (C), Asymmetry (A), and Smoothness (S) parameters for a galaxy image.
 
    The CAS parameters are commonly used in astronomy to quantify the morphological properties of galaxies.
    This function takes an input galaxy image and a table of parameters containing information about the galaxy,
    such as center coordinates, position angle, axis ratio, and effective radius. It then calculates the Concentration,
    Asymmetry, and Smoothness parameters based on the provided algorithm.
  
    Args:
        image (ndarray): Galaxy image for which the CAS parameters need to be calculated.
        table (Table): Table of parameters containing information about the galaxy.
 
    Returns:
        tuple: A tuple containing the calculated Concentration (C), Asymmetry (A), and Smoothness (S) parameters.
  
    Note:
        This function assumes that the deproject_galaxy_image() function is available to deproject the galaxy image.
        The deproject_galaxy_image() function should be called before calling this function to deproject the galaxy image.
 
    References:
        - Conselice, C. J. 2003, ApJS, 147, 1
        - Lotz, J. M., et al. 2004, ApJ, 613, 262
        - Bershady, M. A., et al. 2000, AJ, 119, 2645
    """
    # Gather Information
    img = image
    Tab = table
    centre = (int(img.shape[1]/2 + np.asarray(Tab['x'])),int(img.shape[0]/2 + np.asarray(Tab['y'])))
    pa = float(Tab['theta'])
    q = float(Tab['q'])

    # 'approximations commonly used in astronomy' - estimating R20 and R80 form R50

    Re = 10**Tab['log_re']
    R20 = 0.4*Re
    R80 = 1.4*Re

    # Deproject image
    dep_im = deproject_galaxy_image(img,centre,pa,q)

	# Create Concentration masks
    R20_mask = np.empty_like(img)
    R80_mask = np.empty_like(img)

	for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            if np.sqrt((i-centre[1])**2+(j-centre[0])**2) < R20:
                R20_mask[i,j] = 1
            else:
                R20_mask[i,j] = 0
            if np.sqrt((i-centre[1])**2+(j-centre[0])**2) < R80:
                R80_mask[i,j] = 1
            else:
                R80_mask[i,j] = 0
  
    R20_img = dep_im*R20_mask
    R80_img = dep_im*R80_mask

    # Rotate image 180 for Asymmetry
    rotated_im = np.rot90(dep_im,2)

	# Normalise dep_im for shannon_entropy for

    norm_dep_im = dep_im/np.max(dep_im)
    high_freq_structures = shannon_entropy(norm_dep_im)
    total_flux = np.sum(norm_dep_im)

    # Calculate CAS parameters

	C = 5*np.log10(np.sum(R80_img)/np.sum(R20_img))
    A = np.sum(np.abs(dep_im-rotated_im))/np.sum(dep_im)
    S = high_freq_structures/total_flux

    return C,A,S
```
**Function: CAS**
The `CAS` function appears to calculate the Concentration (C), Asymmetry (A), and Smoothness (S) parameters for a given galaxy image, based on information provided in a table. Here's a breakdown of the steps performed by the function:

1.  Gather Information: The function takes an input galaxy image (`image`) and a table of parameters (`table`) as inputs. It extracts the center coordinates (`centre`), position angle (`pa`), and axis ratio (`q`) from the table.
    
2.  Estimate R20 and R80: The function calculates the values of R20 and R80, which are approximations of the radii at 20% and 80% of the light profile of the galaxy, respectively, based on the value of the effective radius (`Re`) obtained from the table.
    
3.  Deproject Image: The `deproject_galaxy_image` function is called to deproject the input galaxy image based on the center coordinates, position angle, and axis ratio.
    
4.  Create Concentration Masks: Two masks (`R20_mask` and `R80_mask`) are created based on the calculated R20 and R80 values. These masks are used to extract the regions within R20 and R80 from the deprojected image.
    
5.  Calculate Concentration Parameters: The concentration (C) parameter is calculated as 5 times the logarithm (base 10) of the ratio of the total flux within R80 (`np.sum(R80_img)`) to the total flux within R20 (`np.sum(R20_img)`).
    
6.  Rotate Image for Asymmetry: The deprojected image is rotated by 180 degrees (`np.rot90(dep_im,2)`) to calculate the asymmetry (A) parameter. Asymmetry is calculated as the sum of absolute differences between the deprojected image and the rotated image, divided by the total flux within the deprojected image.
    
7.  Normalize Image for Smoothness: The deprojected image is normalized by dividing it by the maximum value of the deprojected image (`np.max(dep_im)`) to obtain `norm_dep_im`, which is used to calculate the smoothness (S) parameter.
    
8.  Calculate Smoothness Parameter: The smoothness (S) parameter is calculated as the Shannon entropy (`shannon_entropy()`) of the normalized deprojected image (`norm_dep_im`), divided by the total flux within the deprojected image (`total_flux`).
    
9.  Return Results: The calculated values of C, A, and S are returned as the output of the function.
Inputs:

1.  `image`: The galaxy image for which the Concentration, Asymmetry, and Smoothness parameters need to be calculated.
2.  `table`: A table of parameters containing information about the galaxy, such as center coordinates, position angle, axis ratio, effective radius, etc.

Outputs:

1.  `C`: The Concentration parameter calculated based on the input galaxy image and table.
2.  `A`: The Asymmetry parameter calculated based on the input galaxy image and table.
3.  `S`: The Smoothness parameter calculated based on the input galaxy image and table.

The function takes the galaxy image and table as inputs, performs calculations based on the provided algorithm, and returns the calculated Concentration, Asymmetry, and Smoothness parameters as outputs.

## Function:
```run-python
def pitch_angle_against_radius(Image,Table):
    """
    Calculates pitch angles against inner radii for a given image and table data.

    Parameters:
        Image (array): The input image for which pitch angles need to be calculated.
        Table (array): The input table data associated with the image.

	Returns:
        Inner_radii_multiples (array): An array of inner radii multiples ranging from 0.3 to 1 with 70 equally spaced values.
        phi_array (array): An array of pitch angles, where each element represents the pitch angle at a specific combination of inner radii multiple and dominant harmonic mode. The shape of phi_array is (len(Inner_radii_multiples), len(m_array)).
    """
    # Need to create an array of inner radii
    Inner_radii_multiples = np.linspace(0.3,1,70)

	# Create array of dominant harmonic modes
    m_array = np.arange(0,6,1)+1

    # Create an empty array of pitch angles
    phi_array = np.empty((len(Inner_radii_multiples),len(m_array)))

    for j in range(0,phi_array.shape[1]):
        for i in range(0,phi_array.shape[0]):
            A, A_p_m, p, SN_w, p_max, SN_m, phi_array[i,j] = gfits.Spiral_power_spec(Image,Table,
            Inner_radii_multiples[i],
            m_array[j],byte_order=True)
            
    return Inner_radii_multiples, phi_array
```
**Function: pitch_angle_against_radius**

This function calculates the pitch angles against inner radii for a given image and table data. It uses the `Spiral_power_spec` function from the `gfits` module to compute the pitch angles for different inner radii and dominant harmonic modes.

### Inputs

-   Image: The input image for which the pitch angles need to be calculated.
-   Table: The input table data associated with the image.

### Outputs

-   Inner_radii_multiples: An array of inner radii multiples ranging from 0.3 to 1 with 70 equally spaced values.
-   phi_array: An array of pitch angles, where each element represents the pitch angle at a specific combination of inner radii multiple and dominant harmonic mode. The shape of `phi_array` is `(len(Inner_radii_multiples), len(m_array))`.

Note: The function assumes that the `gfits` module, which contains the `Spiral_power_spec` function, is imported and available for use.


## Function:
```run-python
def plot_radial_pitch_angle_dependance(Candidate,phi_array,Inner_radii_multiples):
    """
    Plots the radial dependence of pitch angles for a given candidate.

    Parameters:
        Candidate (str): The name or identifier of the candidate for which the plot is being generated.
        phi_array (array): An array of pitch angles, where each element represents the pitch angle at a specific combination of inner radii multiple and dominant harmonic mode. The shape of phi_array is (len(Inner_radii_multiples), len(m_array)).
        Inner_radii_multiples (array): An array of inner radii multiples ranging from 0.3 to 1 with 70 equally spaced values.

    Returns:
        Plot: A plot showing the radial dependence of pitch angles for different harmonic modes, with the average winding angle for m=2 harmonic mode indicated in the plot title. The plot has pitch angle values on the y-axis, inner radii multiples on the x-axis, and different harmonic modes represented by different line styles/colors. The plot also includes a legend with labels for each harmonic mode. The y-axis is limited to a range of -90 to 90 degrees.
    """    
    M_str_arr = np.array(['m = 1','m = 2','m = 3','m = 4','m = 5','m = 6'])
    plt.figure()
    avg_pitch = np.around(np.mean(phi_array[:,1]),1)
    plt.title('{} Average winding angle (m=2): {}\\u00B0'.format(Candidate,avg_pitch))
    plt.ylabel('Pitch angle (deg)')
    plt.xlabel('Inner Radius / $R_e$')
    for i in range(0,len(m_array)):
        if i == 1:
            plt.plot(Inner_radii_multiples,phi_array[:,i],c='k')
        else:
            plt.plot(Inner_radii_multiples,phi_array[:,i],linestyle='--')
    plt.ylim(-90,90)    
    plt.legend(M_str_arr)
```
**Function: plot_radial_pitch_angle_dependence**
This function plots the radial dependence of pitch angles for a given candidate using the input arrays of pitch angles (`phi_array`) and inner radii multiples (`Inner_radii_multiples`). The plot shows the average winding angle for `m=2` harmonic mode and pitch angles for other harmonic modes.

### Inputs

-   Candidate: The name or identifier of the candidate for which the plot is being generated.
-   phi_array: An array of pitch angles, where each element represents the pitch angle at a specific combination of inner radii multiple and dominant harmonic mode. The shape of `phi_array` is `(len(Inner_radii_multiples), len(m_array))`.
-   Inner_radii_multiples: An array of inner radii multiples ranging from 0.3 to 1 with 70 equally spaced values.

### Outputs

-   Plot: A plot showing the radial dependence of pitch angles for different harmonic modes, with the average winding angle for `m=2` harmonic mode indicated in the plot title. The plot has pitch angle values on the y-axis, inner radii multiples on the x-axis, and different harmonic modes represented by different line styles/colors. The plot also includes a legend with labels for each harmonic mode. The y-axis is limited to a range of -90 to 90 degrees.

## Function:
```run-python
def R_e_in_KPC(fits_path,R_e_in_pixels,Distance_to_object):
    """
    Calculate the effective radius (R_e) of a galaxy in kiloparsecs (Kpc) based on its pixel size
    in a FITS file, given the distance to the object in kiloparsecs.

    Parameters
    ----------
    fits_path : str
        File path to the FITS file.

    R_e_in_pixels : float or int
        Effective radius of the galaxy in pixels.

    Distance_to_object : float or int
        Distance to the galaxy in kiloparsecs.

    Returns
    -------
    R_e_kpc : float
        Effective radius of the galaxy in kiloparsecs.

    Notes
    -----
    - Distance_to_object must be in kiloparsecs.
    - The function opens the FITS file, retrieves header information, and calculates the
      pixel-to-kiloparsec conversion factors based on the CD1_1 and CD2_2 header keywords.
    - The function then calculates the effective radius of the galaxy in kiloparsecs by multiplying
      the pixel size (R_e_in_pixels) with the pixel-to-kiloparsec conversion factors
      (kpc_per_pixel_x and kpc_per_pixel_y) and taking the square root of the sum of the
      squares of these values.
    """

    # Distance to Object must be in Kpc!
    # Open Fits File
    hdul = fits.open(fits_path)
    fits_info = {}  # Create dictionary for header info
    for key, value in hdul[0].header.items():
        fits_info[key] = value
    # Retreive Pixel conversion factors
    CD1_1 = fits_info['CD1_1'] *3600 # Convert to arcseconds
    CD2_2 = fits_info['CD2_2'] *3600
    kpc_per_pixel_x = angular_arcsec_to_real(CD1_1,Distance_to_object) # Convert to real distance
    kpc_per_pixel_y = angular_arcsec_to_real(CD2_2,Distance_to_object)
    # Convert Pixel conversion to Re factors
    R_e_kpc_x = R_e_in_pixels*kpc_per_pixel_x
    R_e_kpc_y = R_e_in_pixels*kpc_per_pixel_y

    R_e_kpc = np.sqrt((R_e_kpc_x**2) + (R_e_kpc_y**2)) # Find radial Kpc value

	return R_e_kpc
```
**Function R_e_in_KPC**
The `R_e_in_KPC()` function calculates the effective radius (R_e) of a galaxy in kiloparsecs (Kpc) based on its pixel size in a FITS file, given the distance to the object in kiloparsecs. It uses the pixel-to-kiloparsec conversion factors from the FITS file header to convert the pixel size to kiloparsecs, and then calculates the effective radius by taking the square root of the sum of the squares of the converted pixel size in x and y directions.

#### Inputs

-   `fits_path` (str): File path to the FITS file.
-   `R_e_in_pixels` (float or int): Effective radius of the galaxy in pixels.
-   `Distance_to_object` (float or int): Distance to the galaxy in kiloparsecs.

#### Outputs

-   `R_e_kpc` (float): Effective radius of the galaxy in kiloparsecs.

#### Notes

-   `Distance_to_object` must be in kiloparsecs.
-   The function opens the FITS file using `fits.open()` from the Astropy library, retrieves the necessary header information, and calculates the pixel-to-kiloparsec conversion factors based on the `CD1_1` and `CD2_2` header keywords.
-   The function then calculates the effective radius of the galaxy in kiloparsecs by multiplying the pixel size (`R_e_in_pixels`) with the pixel-to-kiloparsec conversion factors (`kpc_per_pixel_x` and `kpc_per_pixel_y`) in x and y directions, respectively, and taking the square root of the sum of the squares of these values.