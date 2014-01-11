import os
import pyprot.pdb as ppdb

pdb1 = ppdb.PdbObj("./test/test_data/small_3EIY.pdb")
pdb2 = ppdb.PdbObj("./test/test_data/3EIY.pdb")
pdb3 = ppdb.PdbObj("./test/test_data/small_3EIY_h.pdb")
pdb4 = ppdb.PdbObj("./test/test_data/pdb/short_RIV_1.pdb")


def test_pdb_save():
    dest = "./test/test_data/out/test_pdb_save.pdb"
    os.remove(dest)
    pdb1.save_pdb(dest)
    assert os.path.isfile(dest) == True

def test_grab_radius():
    res = pdb2.grab_radius(5.2, [4.698, 36.387, 11.996])
    out = [ 'ATOM    426  CE1 TYR A  56       5.834  40.653  13.201  1.00 24.86           C',
            'ATOM    428  CZ  TYR A  56       4.585  40.513  12.637  1.00 26.22           C',
            'ATOM    429  OH  TYR A  56       4.338  39.402  11.853  1.00 26.67           O',
            'ATOM    532  CB  ASP A  71       7.284  39.034   9.838  1.00 26.37           C',
            'ATOM    533  CG  ASP A  71       5.942  38.790   9.227  1.00 28.24           C',
            'ATOM    534  OD1 ASP A  71       5.331  39.745   8.677  1.00 30.97           O',
            'ATOM    535  OD2 ASP A  71       5.496  37.624   9.306  1.00 28.38           O',
            'ATOM    719  CE  MET A  96       7.289  33.359  14.839  1.00 33.43           C',
            'ATOM    765  CB  ASP A 103       5.182  31.541  10.962  1.00 39.54           C',
            'ATOM    766  CG  ASP A 103       4.926  33.029  11.126  1.00 40.16           C',
            'ATOM    767  OD1 ASP A 103       5.544  33.843  10.396  1.00 42.27           O',
            'ATOM    768  OD2 ASP A 103       4.081  33.379  11.977  1.00 38.14           O',
            'ATOM    772  O   ALA A 104       9.037  34.959   9.857  1.00 30.17           O',
            'ATOM    778  CB  LYS A 105       9.142  36.750  13.090  1.00 27.30           C',
            'ATOM    779  CG  LYS A 105       7.712  36.235  12.749  1.00 27.03           C',
            'ATOM    780  CD  LYS A 105       6.645  37.016  13.447  1.00 26.83           C',
            'ATOM    781  CE  LYS A 105       5.287  36.300  13.367  1.00 24.94           C',
            'ATOM    782  NZ  LYS A 105       4.698  36.387  11.996  1.00 23.03           N',
            'ATOM   1046  CE1 PHE A 139       4.796  37.021  16.763  1.00 26.81           C',
            'HETATM 1333 NA    NA A 177       1.633  34.181  11.897  1.00 26.73          NA',
            'HETATM 1334 NA    NA A 178       6.489  35.143   8.444  1.00 30.89          NA',
            'HETATM 1335  P1  POP A 179       1.233  37.542  11.212  1.00 32.68           P',
            'HETATM 1336  O1  POP A 179       1.910  38.831  11.612  1.00 32.62           O',
            'HETATM 1337  O2  POP A 179       1.288  37.475   9.712  1.00 33.46           O',
            'HETATM 1338  O3  POP A 179       1.948  36.362  11.841  1.00 30.47           O',
            'HETATM 1388  O   HOH A 200       2.391  38.378  14.597  1.00 23.11           O',
            'HETATM 1389  O   HOH A 201       1.535  33.854  14.371  1.00 27.83           O',
            'HETATM 1409  O   HOH A 221       3.282  37.464   7.811  1.00 36.79           O',
            'HETATM 1419  O   HOH A 231       3.976  32.286  14.525  1.00 31.56           O',
            'HETATM 1445  O   HOH A 257       2.292  33.719   9.368  1.00 44.24           O'
        ]
    assert res == out



def test_calpha():
    atom = [
    'ATOM      2  CA  SER A   2       3.259  54.783  -0.368  1.00 52.54           C',
    'ATOM      8  CA  PHE A   3       4.261  51.413   1.102  1.00 48.73           C', 
    'ATOM     19  CA  SER A   4       4.593  49.745  -2.323  1.00 47.00           C', 
    'ATOM     25  CA  ASN A   5       7.351  52.145  -3.480  1.00 41.42           C', 
    'ATOM     33  CA  VAL A   6       9.636  51.959  -0.457  1.00 32.41           C'
    ]
    assert atom == pdb1.calpha()

def test_main_chain():
    atom = [
    'ATOM      1  N   SER A   2       2.527  54.656  -1.667  1.00 52.73           N',
    'ATOM      2  CA  SER A   2       3.259  54.783  -0.368  1.00 52.54           C',
    'ATOM      3  C   SER A   2       4.127  53.553  -0.105  1.00 52.03           C', 
    'ATOM      4  O   SER A   2       5.274  53.451  -0.594  1.00 52.45           O', 
    'ATOM      7  N   PHE A   3       3.563  52.626   0.674  1.00 50.61           N', 
    'ATOM      8  CA  PHE A   3       4.261  51.413   1.102  1.00 48.73           C', 
    'ATOM      9  C   PHE A   3       4.881  50.670  -0.064  1.00 48.17           C', 
    'ATOM     10  O   PHE A   3       6.035  50.257   0.019  1.00 47.56           O', 
    'ATOM     18  N   SER A   4       4.122  50.518  -1.151  1.00 47.69           N', 
    'ATOM     19  CA  SER A   4       4.593  49.745  -2.323  1.00 47.00           C', 
    'ATOM     20  C   SER A   4       5.896  50.254  -2.977  1.00 45.29           C', 
    'ATOM     21  O   SER A   4       6.627  49.479  -3.592  1.00 45.34           O', 
    'ATOM     24  N   ASN A   5       6.184  51.544  -2.832  1.00 43.32           N', 
    'ATOM     25  CA  ASN A   5       7.351  52.145  -3.480  1.00 41.42           C', 
    'ATOM     26  C   ASN A   5       8.584  52.307  -2.574  1.00 39.00           C', 
    'ATOM     27  O   ASN A   5       9.629  52.802  -3.000  1.00 38.69           O', 
    'ATOM     32  N   VAL A   6       8.466  51.922  -1.312  1.00 35.70           N', 
    'ATOM     33  CA  VAL A   6       9.636  51.959  -0.457  1.00 32.41           C'
    ]
    
    assert atom == pdb1.main_chain()

def test_no_hydro():
    atom = [
    'ATOM      1  N   SER A   2       2.527  54.656  -1.667  1.00 52.73           N',
    'ATOM      2  CA  SER A   2       3.259  54.783  -0.368  1.00 52.54           C',
    'ATOM      3  C   SER A   2       4.127  53.553  -0.105  1.00 52.03           C',
    'ATOM      4  O   SER A   2       5.274  53.451  -0.594  1.00 52.45           O',
    'ATOM      5  CB  SER A   2       2.273  54.944   0.792  1.00 52.69           C',
    'ATOM      6  OG  SER A   2       2.066  56.306   1.121  1.00 54.37           O',
    'ATOM      7  N   PHE A   3       3.563  52.626   0.674  1.00 50.61           N',
    'ATOM      8  CA  PHE A   3       4.261  51.413   1.102  1.00 48.73           C',
    'ATOM      9  C   PHE A   3       4.881  50.670  -0.064  1.00 48.17           C',
    'ATOM     10  O   PHE A   3       6.035  50.257   0.019  1.00 47.56           O',
    'ATOM     11  CB  PHE A   3       3.342  50.479   1.896  1.00 47.95           C',
    'ATOM     12  CG  PHE A   3       2.747  51.112   3.120  1.00 46.23           C',
    'ATOM     13  CD1 PHE A   3       3.425  52.100   3.804  1.00 43.75           C',
    'ATOM     14  CD2 PHE A   3       1.509  50.701   3.594  1.00 45.77           C',
    'ATOM     15  CE1 PHE A   3       2.893  52.679   4.942  1.00 44.62           C',
    'ATOM     16  CE2 PHE A   3       0.955  51.280   4.728  1.00 45.65           C',
    'ATOM     17  CZ  PHE A   3       1.655  52.273   5.409  1.00 45.91           C',
    'ATOM     18  N   SER A   4       4.122  50.518  -1.151  1.00 47.69           N',
    'ATOM     19  CA  SER A   4       4.593  49.745  -2.323  1.00 47.00           C',
    'ATOM     20  C   SER A   4       5.896  50.254  -2.977  1.00 45.29           C',
    'ATOM     21  O   SER A   4       6.627  49.479  -3.592  1.00 45.34           O',
    'ATOM     22  CB  SER A   4       3.489  49.633  -3.387  1.00 47.47           C',
    'ATOM     23  OG  SER A   4       3.169  50.916  -3.908  1.00 49.92           O',
    'ATOM     24  N   ASN A   5       6.184  51.544  -2.832  1.00 43.32           N',
    'ATOM     25  CA  ASN A   5       7.351  52.145  -3.480  1.00 41.42           C',
    'ATOM     26  C   ASN A   5       8.584  52.307  -2.574  1.00 39.00           C',
    'ATOM     27  O   ASN A   5       9.629  52.802  -3.000  1.00 38.69           O',
    'ATOM     28  CB  ASN A   5       6.958  53.491  -4.094  1.00 42.02           C',
    'ATOM     29  CG  ASN A   5       6.108  53.321  -5.366  1.00 45.67           C',
    'ATOM     30  OD1 ASN A   5       4.862  53.286  -5.312  1.00 48.48           O',
    'ATOM     31  ND2 ASN A   5       6.784  53.176  -6.513  1.00 47.35           N',
    'ATOM     32  N   VAL A   6       8.466  51.922  -1.312  1.00 35.70           N',
    'ATOM     33  CA  VAL A   6       9.636  51.959  -0.457  1.00 32.41           C'
    ]
    
    assert atom == pdb3.no_hydro() 



def test_chains():
    h_l = [
    'ATOM      1  N   ASP L   1      11.431   9.546  26.980  1.00 42.84           N',  
    'ATOM      2  CA  ASP L   1      12.768   9.604  27.627  1.00 41.86           C',  
    'ATOM      3  C   ASP L   1      12.634   9.246  29.088  1.00 41.46           C',  
    'ATOM      4  O   ASP L   1      11.654   9.628  29.733  1.00 39.57           O',  
    'ATOM      5  CB  ASP L   1      13.348  11.010  27.535  1.00 38.99           C',  
    'ATOM      6  CG  ASP L   1      13.792  11.368  26.140  1.00 43.09           C',  
    'ATOM      7  OD1 ASP L   1      13.329  10.708  25.180  1.00 41.52           O',  
    'ATOM      8  OD2 ASP L   1      14.594  12.322  26.014  1.00 41.66           O',  
    'ATOM      9  N   ILE L   2      13.612   8.513  29.609  1.00 34.82           N',  
    'ATOM     10  CA  ILE L   2      13.590   8.155  31.016  1.00 29.86           C',  
    'ATOM     11  C   ILE L   2      14.203   9.319  31.777  1.00 30.58           C',  
    'ATOM     12  O   ILE L   2      15.263   9.822  31.415  1.00 32.54           O',  
    'ATOM     13  CB  ILE L   2      14.380   6.874  31.272  1.00 23.91           C',  
    'ATOM     14  CG1 ILE L   2      13.694   5.711  30.546  1.00 25.64           C',  
    'ATOM     15  CG2 ILE L   2      14.456   6.609  32.773  1.00 20.81           C',  
    'ATOM     16  CD1 ILE L   2      14.524   4.451  30.447  1.00 26.02           C',  
    'ATOM     17  N   VAL L   3      13.515   9.759  32.818  1.00 28.51           N',  
    'ATOM     18  CA  VAL L   3      13.974  10.886  33.618  1.00 25.67           C',  
    'ATOM     19  C   VAL L   3      14.696  10.393  34.851  1.00 30.01           C',  
    'ATOM     20  O   VAL L   3      14.147   9.608  35.635  1.00 24.91           O',  
    'ATOM     21  CB  VAL L   3      12.783  11.750  34.073  1.00 30.33           C',  
    'ATOM     22  CG1 VAL L   3      13.268  12.911  34.915  1.00 22.12           C',  
    'ATOM     23  CG2 VAL L   3      12.013  12.237  32.864  1.00 24.01           C',  
    'ATOM     24  N   MET L   4      15.933  10.849  35.017  1.00 30.22           N',  
    'ATOM     25  CA  MET L   4      16.738  10.451  36.159  1.00 27.34           C',  
    'ATOM   3335  CB  LYS H 228      55.744  47.316  42.227  1.00 55.82           C',  
    'ATOM   3336  CG  LYS H 228      54.735  46.929  43.279  1.00 59.26           C',  
    'ATOM   3337  CD  LYS H 228      53.322  47.322  42.862  1.00 62.38           C',  
    'ATOM   3338  CE  LYS H 228      52.879  46.619  41.585  1.00 64.90           C',  
    'ATOM   3339  NZ  LYS H 228      51.517  47.052  41.158  1.00 60.26           N',  
    'ATOM   3340  OXT LYS H 228      57.902  49.285  43.398  1.00 70.44           O',  
    'TER    3341      LYS H 228',  
    'HETATM 3356  C15 OBE H 201      24.725  -3.136  27.406  1.00 27.56           C',  
    'HETATM 3357  C16 OBE H 201      20.533  -2.037  27.441  1.00 16.26           C',  
    'HETATM 3358  N1  OBE H 201      21.820  -2.333  26.716  1.00 21.52           N',  
    'HETATM 3359  O1  OBE H 201      25.350  -3.062  24.488  1.00 23.55           O',  
    'HETATM 3360  O2  OBE H 201      26.881  -1.489  24.963  1.00 21.32           O',  
    'HETATM 3361  O3  OBE H 201      25.782  -3.225  27.941  1.00 19.70           O',  
    'HETATM 3362  O4  OBE H 201      23.810  -4.086  27.519  1.00 23.18           O',  
    'HETATM 3363  O5  OBE H 201      31.267  -3.891  23.783  1.00 37.43           O',  
    'HETATM 3440  O   HOH L 290      39.794  19.138  55.192  1.00 45.73           O',  
    'HETATM 3441  O   HOH L 291      30.165  39.040  46.112  1.00 31.60           O',  
    'HETATM 3442  O   HOH L 292      11.904  -4.213  38.248  1.00 47.47           O',  
    'HETATM 3443  O   HOH H 229      25.710   1.134  24.699  1.00 23.08           O',  
    'HETATM 3444  O   HOH H 230      26.500  -1.587  30.027  1.00 24.76           O',  
    'HETATM 3445  O   HOH H 231      39.649  16.017  31.547  1.00 57.79           O'  
    ]

    h = [  
    'ATOM   3335  CB  LYS H 228      55.744  47.316  42.227  1.00 55.82           C',  
    'ATOM   3336  CG  LYS H 228      54.735  46.929  43.279  1.00 59.26           C',  
    'ATOM   3337  CD  LYS H 228      53.322  47.322  42.862  1.00 62.38           C',  
    'ATOM   3338  CE  LYS H 228      52.879  46.619  41.585  1.00 64.90           C',  
    'ATOM   3339  NZ  LYS H 228      51.517  47.052  41.158  1.00 60.26           N',  
    'ATOM   3340  OXT LYS H 228      57.902  49.285  43.398  1.00 70.44           O',  
    'TER    3341      LYS H 228',  
    'HETATM 3356  C15 OBE H 201      24.725  -3.136  27.406  1.00 27.56           C',  
    'HETATM 3357  C16 OBE H 201      20.533  -2.037  27.441  1.00 16.26           C',  
    'HETATM 3358  N1  OBE H 201      21.820  -2.333  26.716  1.00 21.52           N',  
    'HETATM 3359  O1  OBE H 201      25.350  -3.062  24.488  1.00 23.55           O',  
    'HETATM 3360  O2  OBE H 201      26.881  -1.489  24.963  1.00 21.32           O',  
    'HETATM 3361  O3  OBE H 201      25.782  -3.225  27.941  1.00 19.70           O',  
    'HETATM 3362  O4  OBE H 201      23.810  -4.086  27.519  1.00 23.18           O',  
    'HETATM 3363  O5  OBE H 201      31.267  -3.891  23.783  1.00 37.43           O',  
    'HETATM 3443  O   HOH H 229      25.710   1.134  24.699  1.00 23.08           O',  
    'HETATM 3444  O   HOH H 230      26.500  -1.587  30.027  1.00 24.76           O',  
    'HETATM 3445  O   HOH H 231      39.649  16.017  31.547  1.00 57.79           O'  
    ]

    assert pdb4.chains(['L', 'H']) == h_l
    assert pdb4.chains(['H']) == h

