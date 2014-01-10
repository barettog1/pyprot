# sr 11/26/2013
# RMSD Calculation
#
# usage: 
# [shell]>> python3 cmd_rmsd.py file1.pdb file2.pdb [lig/ca]
#
# If no optional third parameter [lig/ca] is provided, the RMSD (in Angstrom)
# between two provided protein structures in PDB format is calculated, including
# all atoms but hydrogen.
# If the optional 3rd argument is 'lig', the RMSD between 2 ligand molecules is 
# calculated, also excluding hydrogens.
# If the If the optional 3rd argument is 'ca,' only C-alpha atoms of the two
# proteins are considered for the RMSD calculation.
#
#

import sys
import pyprot.pdb

if len(sys.argv) < 5 or len(sys.argv) > 5:
    print("USAGE: python3 cmd_rmsd.py file1.pdb file2.pdb [lig/ca]")

else:
    pdb_in = pyprot.pdb.PdbObj(sys.argv[1])
    radius =
    coordinates = 
    pdb_out
    pdb2 = pyprot.pdb.PdbObj(sys.argv[2])

    if len(sys.argv) == 4: 
        if sys.argv[3] == "lig":
            print(pdb1.rmsd(pdb2, ligand = True))
        elif sys.argv[3] == "ca":
             print(pdb1.rmsd(pdb2, atoms = "ca"))
        else:
           print("USAGE: python3 cmd_rmsd.py file1.pdb file2.pdb [lig/ca]")
    else:
         print(pdb1.rmsd(pdb2))
