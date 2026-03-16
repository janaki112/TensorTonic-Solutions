import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X = np.asarray(X)
    print(X.shape , X.ndim)
    if X.ndim < 2 or not np.issubdtype(X.dtype, np.number) or X.shape[0] < 2:
        return None

    X = X.astype(float)

    X_mean = np.mean(X, axis =0)
    X_centered = X - X_mean
    co_variance =  np.matmul(np.transpose(X_centered), X_centered)  / (X.shape [0] - 1)
    return co_variance
    
    pass