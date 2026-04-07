def f_to_txt(flow_file_name):
    import numpy as np
    from scipy.io import FortranFile

    f = FortranFile(flow_file_name, "r")            # READING FILE FROM FORTRAN
    f.read_ints(np.int32)                           # READING NBLOCKS
    ni, nj, nk, var = f.read_ints(np.int32)         # READING CELLS AND VARIABLES
    q = f.read_reals(np.float64)                    # READING DATA IN THE ORDER OF FORTRAN EXPORT SETTINGS

    n = ni * nj* nk                                 # TOTAL CELLS EXPORTED
    Q = q.reshape(5, n).T                           # SORTING DATA, ROWS: CONTAINS DATA ON ALL 'n' cells, COLUMNS: VARIABLES

    address = "flow_txt/"
    np.savetxt(address + flow_file_name.rsplit(".", 1)[0] + ".txt", Q, header="rho u v w p", comments="")
    return