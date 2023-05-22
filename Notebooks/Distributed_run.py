# run this file 


import os
import shutil
import jax
import numpy as np
from jax import numpy as jnp
from astropy.table import Table, vstack
from astropy.io import fits
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
import gax_fits as gfits
bands = np.array(['u','g','r','i','z'])
current = os.getcwd()
print(current)
files = np.loadtxt('/home/borge/spiral_arms/George/Folder_list.txt',dtype=str)

name = input("type your name: ")

