import pyprot

def test_constructor():
    pdb = pyprot.PdbObj()
    pdb = pyprot.PdbObj("./test/test_data/3EIY.pdb")
    assert len(pdb.cont) == 2147
    assert len(pdb.atom) == 1330
    assert len(pdb.hetatm) == 151
    assert len(pdb.conect) == 54

def test_print():
    pdb = pyprot.PdbObj()
    print(pdb)
    del pdb

def test_calpha():
    pdb = pyprot.PdbObj("./test/test_data/small_3EIY.pdb")
    atom = [
    'ATOM      2  CA  SER A   2       3.259  54.783  -0.368  1.00 52.54           C',
    'ATOM      8  CA  PHE A   3       4.261  51.413   1.102  1.00 48.73           C', 
    'ATOM     19  CA  SER A   4       4.593  49.745  -2.323  1.00 47.00           C', 
    'ATOM     25  CA  ASN A   5       7.351  52.145  -3.480  1.00 41.42           C', 
    'ATOM     33  CA  VAL A   6       9.636  51.959  -0.457  1.00 32.41           C'
    ]
    assert atom == pdb.calpha()

