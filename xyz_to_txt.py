def xyz_to_txt(mesh_file_name):
    import numpy as np
    from scipy.io import FortranFile

    g = FortranFile(mesh_file_name, "r")
    g.read_ints(np.int32)
    ni, nj, nk = g.read_ints(np.int32)
    xyz = g.read_reals(np.float64)

    n = ni * nk
    x = xyz[:n]
    y = xyz[n:2*n]
    z = xyz[2*n:3*n]

    data = np.column_stack((x, y, z))

    address = "flow_txt/"

    np.savetxt(address + mesh_file_name.rsplit(".", 1)[0] + ".txt", data, header="x y z", comments="")
    return