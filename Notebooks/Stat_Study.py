import sys
sys.path.append('..')
import os
os.environ['XLA_PYTHON_CLIENT_PREALLOCATE'] = 'false'
os.getcwd()
from gax import sersic
from gax.sersic import sersic_2d_linear_pix
from matplotlib import pyplot as plt
import jax
import jax.numpy as jnp
import astropy
import numpy as np
from astropy.table import Table, vstack
import gax_fits as gfits
from astropy.io import fits
from scipy.interpolate import RegularGridInterpolator

bands = np.array(['U','G','R','I','Z'])
wavs = np.array([354.3e-9, 477.0e-9, 623.1e-9, 762.5e-9, 913.4e-9], dtype=float)

# Functions that need to be defined locally:
#--------------------------------------------

def get_variable_from_name(name):
    # Create a list of all the defined variables
    var_dict = globals() 
    
    # Get the variables from the list
    var_value = var_dict.get(name)
    
    return var_value    

def list_empty_directories(folder_path):
    empty_dirs = []
    for dirpath, dirnames, filenames in os.walk(folder_path):
        if not dirnames and not filenames:
            empty_dirs.append(dirpath)
    return empty_dirs

def flux_fraction(Image,Table,Original_Image,Bulge):
    
    if np.isnan(np.any(Image)):
        print('Found a Nan')
        return np.nan
    else:
        # First apply the bulge mask to the FICL process image
        masked_Image = gfits.R_e_bulge_mask(Image,Table,Bulge=Bulge)
        
        # Set background for SDSS images
        background = 1000
        
        # Calculate fraction of flux in the masked to original image
        flux_fraction  = np.sum(masked_Image)/np.sum(Original_Image-background)
        
        return flux_fraction

#-------------------------------------------------------------------------------------------------

# List of path locations:
candidate_list_path = '/home/borge/Data/MLIS1_Output/01_04_23/Output_01_04_23/directories.txt'
output_parent_dir_path = '/home/borge/Data/MLIS1_Output/01_04_23/Output_01_04_23/' 
original_parent_dir_path = '/home/borge/Data/Brightest_1000/Brightest_1000_Spirals/'

#-------------------------------------------------------------------------------------------------

# Import Data:
#-------------


# Get candidate list and trim band information
candidate_list = np.loadtxt(candidate_list_path,dtype=str)

for i in range(len(candidate_list)):
    candidate_list[i] = candidate_list[i][:-2]

candidate_list = np.unique(candidate_list)

# Get failed directories from emptys and trim band information
failed_dir = list_empty_directories(output_parent_dir_path)

failures = np.empty_like(failed_dir)

for i in range(len(failures)):
    failed_dir[i] = failed_dir[i].removeprefix(output_parent_dir_path)
    failures[i] = failed_dir[i][:-2]

print(failures)

# Remove failed directories from the candidate list
failure_mask = np.isin(candidate_list, failures)
candidate_list = candidate_list[~failure_mask]

# Export Finalised Candidate List
with open('Candidate_list_post_failures.txt', "w") as f:
    for s in candidate_list:
        f.write(s + "\n")

# Create an array of the candidate identifiers (last four digits)
identifiers = np.empty_like(candidate_list)
for i in range(len(candidate_list)):
    x = candidate_list[i]
    identifiers[i] = x[-4:]
    
# Go and get Original and FICL Isolated Images and assign them to variables

for i in range(0,len(candidate_list)):
    exec('tab_{},comp_{} = gfits.Composite_from_directory_raid("{}",output_parent_dir_path)'.format(identifiers[i],identifiers[i],candidate_list[i]),globals())

# Now go and get the originals from the Bright Spiral folder
for i in range(0,len(candidate_list)):
    exec('comp_org_{} = gfits.Read_M_band({},original_parent_dir_path)'.format(identifiers[i],candidate_list[i]),globals())

# Create lists of the variables that have been created
comp_org_arr = np.empty_like(candidate_list)
comp_arr = np.empty_like(candidate_list)
tab_arr = np.empty_like(candidate_list)

for i in range(0,len(identifiers)):
    comp_org_arr[i] = 'comp_org_{}'.format(identifiers[i])
    comp_arr[i] = 'comp_{}'.format(identifiers[i])
    tab_arr[i] = 'tab_{}'.format(identifiers[i])

#-------------------------------------------------------------------------------------------------

# Flux fractions:
#----------------

# Fraction of flux in arm

arm_flux_fractions_all_bands = np.empty((len(candidate_list),len(bands)))

for i in range(0,len(candidate_list)):
    for s in range(0,len(bands)):
        current_tab = get_variable_from_name(tab_arr[i])
        current_comp = get_variable_from_name(comp_arr[i])
        current_comp_org = get_variable_from_name(comp_org_arr[i])
        arm_flux_fractions_all_bands[i,s] = flux_fraction(current_comp[:,:,s],current_tab[s],current_comp_org[:,:,s],False)

# Fraction of flux in bulge

bulge_flux_fractions_all_bands = np.empty((len(candidate_list),len(bands)))

for i in range(0,len(candidate_list)):
    for s in range(0,len(bands)):
        current_tab = get_variable_from_name(tab_arr[i])
        current_comp = get_variable_from_name(comp_arr[i])
        current_comp_org = get_variable_from_name(comp_org_arr[i])
        bulge_flux_fractions_all_bands[i,s] = flux_fraction(current_comp[:,:,s],current_tab[s],current_comp_org[:,:,s],True)
        
# Export Created Data:
#---------------------

np.savetxt('arm_flux_frac_candidates.txt',arm_flux_fractions_all_bands)
np.savetxt('bulge_flux_frac_candidates.txt',bulge_flux_fractions_all_bands)

#--------------------------------------------------------------------------------------------------


# CAS Parameters:
#----------------

# CAS on original:
CAS_of_Originals = np.empty((len(candidate_list),len(bands),3))

for j in range(0,len(bands)):
    for i in range(0,len(candidate_list)):
        current_tab = get_variable_from_name(tab_arr[i])
        current_comp_org = get_variable_from_name(comp_org_arr[i])
        CAS_of_Originals[i,j,:] = gfits.CAS(current_comp_org[:,:,j],current_tab[j])

# CAS on isolated:
CAS_of_Isolated = np.empty((len(candidate_list),len(bands),3))

for j in range(0,len(bands)):
    for i in range(0,len(candidate_list)):
        current_tab = get_variable_from_name(tab_arr[i])
        current_comp = get_variable_from_name(comp_arr[i])
        CAS_of_Isolated[i,j,:] = gfits.CAS(current_comp[:,:,j],current_tab[j])
        
# Export Created Data:
#---------------------

# Originals
np.savetxt('C_Originals_export.txt',CAS_of_Originals[:,:,0])
np.savetxt('A_Originals_export.txt',CAS_of_Originals[:,:,1])
np.savetxt('S_Originals_export.txt',CAS_of_Originals[:,:,2])

# Isolated
np.savetxt('C_Isolated_export.txt',CAS_of_Isolated[:,:,0])
np.savetxt('A_Isolated_export.txt',CAS_of_Isolated[:,:,1])
np.savetxt('S_Isolated_export.txt',CAS_of_Isolated[:,:,2])

#-------------------------------------------------------------------------------------------------
