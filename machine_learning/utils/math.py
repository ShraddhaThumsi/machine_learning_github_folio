import numpy as np
def get_regression_parameters(X,y):
    print("in math module, regression params fund")
    xtx = np.matmul(X.T,X)
    print(type(xtx))
    print(xtx.shape)
    print('made it past dot product of xt and x')
    xtx_inverse = np.linalg.inv(xtx)
    xty = np.dot(X.T,y)
    return np.matmul(xtx_inverse,xty)