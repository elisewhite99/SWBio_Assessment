#!/usr/bin/env python

## Script using PyMOL for alignment and RMSD calculation of protein-complex structures from docking experiments. 



# Step 1: Import Pymol python package

import pymol 
from pymol import cmd



# Step 2: Load the .pdb files for all protein structures

import glob #gob module finds pathnames matching a specified pattern according to the rules of the Unix shell, in the below case it uses the special character *

file_path = input('Please copy and paste absolute file path for .pdb protein files e.g. C:/Users/ew17435/OneDrive - University of Bristol/Documents/SWBio PhD/Year 1/Data Science and Machine Learning/Assessment/SWBio_Assessment/Sample Data/') #example pathname

file_list = glob.glob(file_path + '*.pdb') 

for protein in file_list:
    cmd.load(protein) #cmd.load() is the PyMOL command which loads .pdb files into PyMOL

print("(loading .pdb files complete)") #a completion statement is printed to the terminal



# Step 3:  Align actKR of each HADDOCK structure to the actKR of M14

def align_all_to_targetactKR(target,mobile_selection='c. B and n. CA+C+N+O',target_selection='c. B and n. CA+C+N+O'): 
    """
    Align function for the actKR (chain B) backbone atoms of HADDOCK structures onto a target. The mobile and target selections are defined but the target must be specified when using the function.

    It uses cmd.align() which is the PyMOL align command.

    When alignment is completed, a completion statement is printed to the terminal. 
    """   

    object_list = cmd.get_names()
    object_list.remove(target) 

    for object in range(len(object_list)):
        align = cmd.align('%s & %s'%(object_list[object],mobile_selection),'%s & %s'%(target,target_selection)) 
        
align_all_to_targetactKR('M14')

print("(alignment to M14 actKR complete)") 



# Step 4: Calculate RMSD for actACP between HADDOCK structures and M14 (this is the code in which I define my own RMSD function using Numpy arrays, see the Jupyter notebook file for alternative methods, including using the PyMOL RMSD cmd.rmsd_cur command)

from pymol import stored
from pymol import selector

def get_xyz( UserSelection ): 
    """
    get_xyz() obtains a nested list of x, y, z coordinates of atoms. 

    The selection of actACP backbone atoms are defined, but the UserSelection should be specified.
   
    """
    stored.BackboneAtoms = []
    userSelection = UserSelection + ' and c. A and n. CA+C+N+O' #initially had 'and c. A' which didn't work as there wasn't a space before the 'and'
    cmd.iterate_state(1, selector.process(userSelection), "stored.BackboneAtoms.append([x,y,z])")
    return stored.BackboneAtoms


import numpy as np

def calculate_rmsd(target): 
    """
    calculate_rmsd(target) calculates the RMSD for the actACP protein between the target and  the HADDOCK structures. 
    
    Firstly, the xyz coordinates of the target actACP are obtained and the xyz coordinates for the actACP of each HADDOCK structure in the list are obtained.
    
    The RMSD is calculted using the RMSD equation which is written using numpy arrays. Each RMSD value for each HADDOCK structure is added to a list which is then ordered by size and printed to the terminal. This allows the identification of the favourable HADDOCK structures. 
    
    """
    M14_xyz = get_xyz( target ) 

    object_list = cmd.get_names()
    object_list.remove(target)

    rmsd_list = [] 
    for protein in object_list:
            xyz = get_xyz(protein) 
            rmsd = np.sqrt(np.sum((np.array(M14_xyz)-np.array(xyz))**2)/len(xyz)) 
            rmsd_list.append((protein, rmsd)) #add to the empty rmsd_list

    rmsd_list_sorted = sorted(rmsd_list,key=lambda x: x[1]) 
    
    print('RMSD of M14 actACP onto:')
    for x in rmsd_list_sorted:
        print(x[0], 'actACP =', x[1])

calculate_rmsd('M14')


print("Analysis complete")


