# Sebastian Raschka

import re

def fix2ref_charge(ref_mol2, fix_mol2, ref_col=-1, fix_col=-1):
    """ Applies charges from 1 mol2 file to the other. Assumes that
        both molecules have the same number and order of atoms.

    Keyword Arguments:
        ref_mol2(list): List of mol2 contents for reference molecule.
        fix_mol2(list): List of mol2 contents for mol2 to fix.
        ref_col(int): Column of the charge information in the reference
                      molecule, last column by default.
        fix_col(int): Column of the charge information in the to-be-fixed
                      molecule, last column by default.

    Supports the following formating style by default.
    @<TRIPOS>ATOM entries:
    
    1 CA -0.149 0.299 0.000 C.3 1 ALA1 0.000

    If one of both files are formatted as follows:
    1 CA -0.149 0.299 0.000 C.3
    the parameters ref_col and/or fix_col have to be set to -2

    Returns list of mol2 contents for the fixed molecule.
    
    """
    assert len(ref_mol2) == len(fix_mol2), 'Both Mol2 must be of same length.'
    out_mol2 = []
    atom_section = False
    for r,f in zip(ref_mol2, fix_mol2):
        
        # check if we are in atom coordinate section
        if not atom_section and (r.startswith('@<TRIPOS>ATOM')
                and f.startswith('@<TRIPOS>ATOM')):
            atom_section = True
        elif atom_section and (r.startswith('@<TRIPOS>') or
                f.startswith('@<TRIPOS>')):
            atom_section = False

        # apply fix
        if atom_section:
            f_line = re.split(r'(\s+)', f)
            r_line = re.split(r'(\s+)', r)
            f_line[fix_col] = r_line[ref_col]
            f = "".join(f_line)

        out_mol2.append(f)
    
    return out_mol2 
