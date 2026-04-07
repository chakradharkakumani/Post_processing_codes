def TDMA_function(Coeffiecient_A, Coeffiecient_B, Coeffiecient_C, Coeffiecient_D):
    # THOMAS ALGORITHM
    import numpy as np
    import matplotlib as plt

    # DEFINING VARIABLES
    A   = np.loadtxt((Coeffiecient_A), dtype=np.float64)
    B   = np.loadtxt((Coeffiecient_B), dtype=np.float64)
    C   = np.loadtxt((Coeffiecient_C), dtype=np.float64)
    D   = np.loadtxt((Coeffiecient_D), dtype=np.float64)
    n   = len(C)
    C2  = np.zeros(n, dtype=np.float64)
    D2  = np.zeros(n, dtype=np.float64)
    X   = np.zeros(n, dtype=np.float64)

    # FORWARD SWEEPING
    for i in range(n):
        if i == 0:
            C2[i] = C[i] / B[i]
            D2[i] = D[i] / B[i]
        elif i < n-1:
            C2[i] = C[i] / (B[i] - A[i]*C2[i-1])
            D2[i] = (D[i] - A[i]*D2[i-1]) / (B[i] - A[i]*C2[i-1])
        else:
            D2[i] = (D[i] - A[i]*D2[i-1]) / (B[i] - A[i]*C2[i-1])

    # BACKWARD SWEEPING
    for i in range(n-1, -1, -1):
        if i == n-1:
            X[i] = D2[i]
        else:
            X[i] = D2[i] - C2[i]*X[i+1]
    np.savetxt("X.txt", X)
    return