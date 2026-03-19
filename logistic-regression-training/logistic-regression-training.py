import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    X = np.asarray(X)
    y = np.asarray(y)
    w = np.zeros(X.shape[1])
    # Write code here 
    b = 0.0
    N= X.shape[0]
    for step in range(steps):
        Xw = np.dot(X,w )
        p  = 1 / (1 + np.exp(-(Xw + b)))
        dw = np.dot(np.transpose(X) , (p-y)) / N
        db = np.mean(p-y)
        w = w - lr * dw
        b = b - lr * db
    return (w,b)
        
    pass