import numpy as np
def get_regression_parameters(X,y):

    xtx = np.matmul(X.T,X)
    xtx_inverse = np.linalg.inv(xtx)
    xty = np.matmul(X.T,y)
    return np.matmul(xtx_inverse,xty)