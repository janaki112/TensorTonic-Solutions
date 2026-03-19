import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.asarray(A)
    m , n = A.shape
    matrix_transpose = np.zeros((n,m))

    for i in range(m):
        for j in range(n):
            matrix_transpose[j][i] = A[i][j]
    return matrix_transpose
    pass
