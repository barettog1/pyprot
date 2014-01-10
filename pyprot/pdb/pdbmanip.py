# Class with methods specialized for PDB file content manipulation
# Imported into PdbObj class.
# Sebastian Raschka 11/18/2013

class PdbManip(object):
    def __init__():
        pass
    
    def save_pdb(self, dest):
        """
        Writes out the contents of the PDB object (pdb.cont) as .pdb file

        Arguments:
            dest = path+filename of the pdb file (e.g., /home/.../Desktop/my_pdb.pdb)

        """
        with open(dest, 'w') as out:
            for line in self.cont:
                out.write(line)


    def grab_radius(self, radius, coordinates):
        """ Grabs those atoms that are within a specified 
            radius of a provided 3D-coordinate.

        Arguments:
            radius: radius in Angstrom (float or integer)
            coordinates: a list of x, y, z coordinates , e.g., [1.0, 2.4, 4.0]

        Returns:
            list that contains the PDB contents that are within the specified
            radius.

        """
        in_radius = []
        for line in self.cont:
            if line.startswith("ATOM") or line.startswith("HETATM"):
                xyz_coords = [float(line[30:38]),\
                             float(line[38:46]),\
                              float(line[46:54])]
                distance = (sum([(coordinates[i]-xyz_coords[i])**2 for i in range(3)]))**0.5
                if distance <= radius:
                    in_radius.append(line)
        return in_radius
    

