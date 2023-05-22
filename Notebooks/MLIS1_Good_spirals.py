# Imports
import os
import shutil
import jax
import numpy as np
from jax import numpy as jnp
from astropy.table import Table, vstack
from astropy.io import fits
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
#import gax_fits as gfits

bands = np.array(['u','g','r','i','z'])


# Steven recommended doing this
os.environ['XLA_PYTHON_CLIENT_PREALLOCATE'] = 'false'

# First Move to the directory containing the file list
os.chdir('/home/ppygh3/Data')

# Read in file list
files_list = np.loadtxt('Folder_list.txt',dtype=str)

# Move to ficl outer directory
os.chdir('/home/ppygh3/ficl')

# Set the output and input paths according to the server folder structure
data_loc  = '/home/ppygh3/Data/good_spirals'
out_path = '/home/ppygh3/Output'
config_loc = '/home/ppygh3/Data/Config_Files'


# Define the function here to save time:

def command_line_file_list_server_run(file_list,data_location,config_path,output_path):
    """
    Generates and runs FICL commands for a list of FITS files.

    Args:
    - file_list: a list of FITS file names.
    - data_location: the directory where the FITS files are located.
    - output_path: the directory where the ficl outputs will be created

    Returns:
    None
    """    
    # Get directory to return to 
    current = os.getcwd()

    # Create list of filenames without file information
    files = np.empty_like(file_list).astype(str)
    for i in range(0,len(file_list)):
        files[i] = file_list[i].removesuffix('.fits.gz')


    # Generate output folders:
    for i in range(0,len(file_list)):
        create_folder(output_path,files[i])
            
    # Generate the config files:
    config_list = []
    for i in range(0,len(file_list)):
        config_element = Generate_config(file_list[i],data_location,config_path,output_path)
        config_list.append(config_element)

    # first navigate to outer ficl directrory
    os.chdir('/home/ppygh3/ficl/')

    # Initialise list of commands for running
    commands = []

    
    command_structure = 'XLA_PYTHON_CLIENT_PREALLOCATE=false nohup python -m ficl.main -c /home/ppygh3/Data/Config_Files/'
    command_ending = ' &> ficl.out &'

    # Write commands to array
    for i in range(0,len(file_list)):
        command_element = command_structure + config_list[i] + command_ending
        commands.append(command_element)


    # Loop through the list of commands and run each one using os.system
    for i in range(0,len(commands)):
        os.system(commands[i])

    # move back to original cwdir
    os.chdir(current)

# Run the server run specified function

command_line_file_list_server_run(files_list,data_loc,config_loc,out_path)

