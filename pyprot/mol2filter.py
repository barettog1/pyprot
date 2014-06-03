import os

def mol2_to_coords(line):
    """ Extracts XYZ coordinates from mol2 atom entry line. """
    line = line.strip().split()
    return [float(i) for i in line[2:5]]


def _filter_atoms(mol2_cont, chargetype_list):
    """
    Searches for atom types in a mol2 file.
    Returns the mol2 lines that contains matches as a list.

    Keyword arguments:
        mol2_cont (list): mol2 file content as where each list item represents
                     a line
        chargetype_list (list): List of sublists that consists of atom types as
                first sublist item, and the allowed charge range is given
                as 2nd and 3rd sublist items.
                Example: [['O.2', -1.12, -0.792], ['O.2', -0.595, -0.315]]

    Returns:
         The mol2 lines that contains matches as a list.

    """
    matched_lines = []
    for line in mol2_cont:
        fields = line.split()
        for atom in chargetype_list:
            if atom[0] in fields:
                if len(atom) == 3: # optional: requires user defined charge range
                    try:
                        charge = float(fields[-1])
                    except ValueError:
                        print("Error: cannot get charge")
                        continue
                    if charge >= atom[1] \
                            and charge <= atom[2]:
                        matched_lines.append(line)
                else:
                    matched_lines.append(line)
        if '@<TRIPOS>BOND' in fields:
            break
    return matched_lines


def contains_atom(mol2_cont, chargetype_list, cnt=False):
    """
    Searches for atom types in a mol2 file in specified charge ranges.

    Keyword arguments:
       mol2_cont (list): mol2 file content as where each list item represents
                     a line
        chargetype_list (list): List of sublists that consists of atom types as
                first sublist item, and the allowed charge range is given
                as 2nd and 3rd sublist items.
                Example: [['O.2', -1.12, -0.792], ['O.2', -0.595, -0.315]]
        cnt (bool): If True, absolut number of matched atoms is returned.
                    Else reports if >= 1 match occurred as True or False

    Returns:
        Bool if `cnt` is set to False: reports if match occurred or not
        Int if `cnt` is set to True: number of matched atoms]

    """
    matches = len(_filter_atoms(mol2_cont, chargetype_list))
    if cnt:
        val = matches
    else:
        val = matches >= 1
    return val


def distance_match(mol2_cont, chargetype_list, distance, mol2_cont2=None):
    """
    Searches for atom types in mol2 file(s). Returns True if
    2 atoms of the defined types are within a certain distance range.

    Keyword arguments:
       mol2_cont (list): mol2 file content as where each list item represents
                     a single line in the mol2 file.
        chargetype_list (list): List of sublists that consists of atom types as
                first sublist item, and the allowed charge range is given
                as 2nd and 3rd sublist items.
                Example: [['O.2', -1.12, -0.792], ['O.2', -0.595, -0.315]]
                Max number of sublists is 2!
        distance (list): List of 2 numbers that specify the allowed distance
                between the 2 atoms in Angstrom. E.g., [4, 12.5]
        mol2_cont2 (list): Calculates intermolecular instead of
            intramolecular atomic distance if contents for a second mol2 file are provided.

    Returns bool:
        True if 2 atoms (each of one specified type) are within a
        specified distance.

    """
    assert len(chargetype_list) == 2   # can only compare 2 atoms
    atom_lines1 = _filter_atoms(mol2_cont, [chargetype_list[0]])
    if not mol2_cont2:
        mol2_cont2 = mol2_cont
    atom_lines2 = _filter_atoms(mol2_cont2, [chargetype_list[1]])
    coords_1 = []
    coords_2 = []
    for line in atom_lines1:
        line = line.strip().split()
        coords_1.append([float(i) for i in line[2:5]])
        # expected format of a 'line':
        # ['11', 'O1', '0.0847', '-6.3706', '-0.6593', 'O.2', '1', '<0>', '-0.0409']
    for line in atom_lines2:
        line = line.strip().split()
        coords_2.append([float(i) for i in line[2:5]])

    dist_match = False
    for xyz_1 in coords_1:
        for xyz_2 in coords_2:
            dist = sum([(j-i)**2 for i,j in zip(xyz_1,xyz_2)])**0.5
            if dist >= distance[0] and dist <= distance[1]:
                dist_match = True
                break

    return dist_match