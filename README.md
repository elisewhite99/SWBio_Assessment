# A guide to using PyMOL for the alignment and RMSD calculation of protein-complex structures from docking experiments

The RMSD (root-mean-square deviation) is a measure of the average distance between backbone atoms of superimposed proteins.

<EQUATION>

In this case, it is used to calculate the simlarity of the orientation of one protein docked onto another.  




Therefore, it can help quantify how similar the docked orientation of actACP onto actKR is between the HADDOCK docked structures and the BUDE docked structure from previous work – the closer the RMSD is to 0, the more similar the orientation of two proteins. PyMOL (a python-based protein visualisation programme) can be used to achieve this analysis as it  can be used to align the actKR of each HADDOCK docked structure to the actKR of M14 and subsequently calculate the RMSD of the actACP between that of the HADDOCK docked structures and M14. Scripts which define the ‘align’ and ‘rmsd’ commands in PyMOL already exist (reference) so these were used to inform how each function actually does this. As there are many protein structures (~250) which resulted from the multiple HADDOCK runs, scripting this in python to then run in PyMOL is much more efficient than doing each individually. Initially, this was tried in CPPTRAJ from Amber but there were issues with atom names, so PyMOL was used instead.

Aim of the Code
PyMOL v. 2.4.1 and Anaconda were installed. The PyMOL python package was installed to Anaconda by typing ‘conda install -c schrodinger pymol’ into the Anaconda Prompt (Anaconda 3).
A python script was written using Jupyter Notebook. Step 1 of the code installed the PyMOL python package and opened PyMOL in a separate window (based on code from the CompBioMed e-seminar which I attended: “Molecular Visualisation using PyMOL”, found at  https://www.comp biomed.eu/compbiomed-e-seminar-14/).
Step 2 of the code loaded all ~250 .pdb files from the specified folder into PyMOL, using the glob module and the special character *. A for-loop iteratively loads each file. An input function allowed the user to input the absolute path to their directory containing the files. An example of my path is included for the ease of copying and pasting.
To align all the structures against the actKR of M14, the function ‘align_all_to_M14actKR’ was defined in step 3. The target was defined as ‘M14’ and the target selection as ‘c. B and n. CA+C+N+O’ which are the backbone atoms of chain B (actKR). The mobile selection (i.e. the atoms to move to align against M14 actKR) were defined as ‘c. B and n. CA+C+N+O’. All HADDOCK structures were added to ‘object list’ using the PyMOL command ‘cmd.get_names()’, except for M14. A for-loop iteratively aligned the HADDOCK structures against the M14 actKR using the PyMOL command ‘cmd.align()’.
To calculate the RMSD, in step 4, initially code was written which used the ‘cmd.rms_cur()’ command in PyMOL. However, as a simple equation is used to calculate RMSD (equation 1), a function was created to calculate it manually, using the output from the previous approach with ‘cmd.rms_cur()’ to identify when the new function worked. A ‘get_xyz()’ function was defined which obtained the xyz coordinates of the backbone atoms in chain A (actACP). A nested list of [x, y, z] coordinates of M14 was obtained using this ‘get_xyz()’ function. A for-loop was set up for each HADDOCK structure and a nested list of [x, y, z] coordinates of each was obtained, again using the ‘get_xyz()’ function. Two different functions were then written to calculate the RMSD, one more concise than the other.
For the original code, a for-loop was created to loop over the indexes of atoms: ‘for idx in range(len(xyz))’. The indexes from the two nested lists and the ‘np.squared’ function were used to calculate the sum component of the equation and add it to ‘sum = 0’. The RMSD was then calculated by directly encoding equation 1 using the ‘np.sqrt’ function. The resulting calculated RMSD was appended to an empty list with the protein name as x[0] and the calculated RMSD as x[1]. A sorted list based on size of RMSD values was printed.
The final simplified code harnessed the power of numpy arrays, rather than working with nested lists. Instead of looping over indexes in nested lists, the calculation was done directly using numpy arrays. This meant the calculation of RMSD could be encoded on one line, thus being more efficient. Again, the resulting RMSD values were appended to a ‘rmsd_list’ including the protein name, and the list ordered according to RMSD size.    

Equation 1: 
In the above steps, functions were defined and then recalled. One improvement could be to create a module specific to this and then import the functions from the module. If this was done, the functions would need to be more generalised.

Outcome of Analysis
The resulting ordered list of HADDOCK protein structures and their corresponding RMSD values allows for the rapid identification of favourable structures to take forward for further MD simulations and hence comparable analyses between different methods of favourable conformation identification. Already, the first, second, and third highest ranked HADDOCK protein structures based on these RMSD values have been used in MD simulations.

