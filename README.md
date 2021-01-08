# SWBio Data Science and Machine Learning Assessment
## Using PyMOL for the alignment and RMSD calculation of protein-complex structures from docking experiments

### Description
This code has been written in Python, utilising features from the python-based protein visualisation programe PyMOL, to process and compare hundreds of enzyme-complex model structures obtained from different protein docking experiments. 

Two different docking programmes (HADDOCK and BUDE) have been used to obtain structures for the complex of actACP (acyl-carrier protein) and actKR (ketoreductase) polyketide synthase enzymes which are involved in the synthesis of the polyketide antibiotic actinorhodin (act). The code is primarily written to compare the hundreds of structures resulting from several HADDOCK docking experiments with the favoured structure from previous work using BUDE, called 'M14'. Comparisons can be made after aligning the actKR protein of each HADDOCK structure with the actKR of M14. The RMSD (root-mean-square deviation - a measure of distance between backbone atoms of superimposed proteins) is then calculated to compare the similarity of the docked orientation of the actACP in HADDOCK structures with its orientation in M14. The closer the RMSD value is to 0, the more similar the orientation of actACP is between the two structures and thus the more evidence that the identified HADDOCK structure shoule be taken forward for further analysis.


### Code components

Step 1: The import of the Pymol python package

Step 2: Loading of pdb files for all protein structures from the 'Sample Data' directory

Step 3: Alignment of actKR of each HADDOCK structure to the actKR of M14

Step 4: Calculation of the RMSD of the HADDOCK actACP onto the M14 actACP


### To run:

1. Download the Python script and the Jupyter Notebook file (for reference) in this repository. Download the 'Sample Data' directory in this repository which contains all the .pdb files. Put these downloaded items into a single directory. 

2. Ensure you have PyMOL v. 2.4.1 installed on your computer. Ensure the PyMOL python package is installed; this can be done in the Anaconda prompt by typing:
```conda install -c schrodinger pymol``` 

3. You might need to edit the .py file to specify the 'target' enzyme complex to which you want to compare the HADDOCK structures to. In this case it is M14, but other model complexes from previous work include M17 and M10. If different to M14 (the default written into the code), ensure you edit the script to specify the 'target' in the align_all_to_targetactKR() function and the calculate_rmsd() function. 

4. Run the .py script (I typed ```python pymol_align_rmsd_script.py``` into the JupyterLab terminal) or alternatively run each step of the code individually in the Jupyter Notebook file. When prompted add the absolute (NOT relative!) file path which leads to the directory in which the .pdb files are saved to - if you downloaded the entire 'Sample data' directory from this repository it should finish with: ```/Sample Data/```

The analysis is completed once a list of RMSD values corresponding to each HADDOCK structure has been produced and the terminal prints out the message: ```Analysis complete```


### Outcome
The resulting ordered list of HADDOCK protein structures and their corresponding RMSD values allows for the rapid identification of favourable structures to take forward for further MD simulations and hence comparable analyses between different methods of favourable conformation identification. Already, the first, second, and third highest ranked HADDOCK protein structures based on these RMSD values have been used in MD simulations.
