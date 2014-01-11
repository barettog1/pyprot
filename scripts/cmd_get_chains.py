# sr 01/11/2013
#
# Extracts ATOM and HETATM lines from a PDB file that match a specified chain ID.
#
# usage: 
# [shell]>> python3 cmd_get_chains.py in_file.pdb chain_IDs out.pdb 
#
#   EXAMPLE: python3 cmd_get_chains.py in_file.pdb A,B,D out.pdb 
# 
#

import sys
import pyprot.pdb

try:
    assert len(sys.argv) == 4 
    
    chain_ids = [i.strip() for i in sys.argv[2].split(',')]

    in_pdb = pyprot.pdb.PdbObj(sys.argv[1])      
    in_pdb.cont = in_pdb.chains(chain_ids)
   
    in_pdb.save_pdb(sys.argv[3])   

except IOError:
    print("ERROR\nUSAGE: python3 cmd_get_chains.py in_file.pdb chain_IDs out.pdb")
    print("\nEXAMPLE: python3 cmd_get_chains.py in_file.pdb A,B,D out.pdb\n")
 
