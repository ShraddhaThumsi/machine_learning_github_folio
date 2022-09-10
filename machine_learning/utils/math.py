import numpy as np



def get_regression_parameters(X,y):

    xtx = np.matmul(X.T,X)
    xtx_inverse = np.linalg.inv(xtx)
    xty = np.matmul(X.T,y)
    return np.matmul(xtx_inverse,xty)


def normalize_data(data):
    for i in range(data.shape[1]):
        data[:,i]=(data[:,i]-np.min(data[:,i]))/(np.max(data[:,i]) - np.min(data[:,i]))
    return data


def F1_score(y,y_hat):
    tp,tn,fp,fn=0,0,0,0
    for i in range(len(y)):
        if y[i]==1 and y_hat[i]==1:
            tp += 1
        if y[i]==0 and y_hat[i]==0:
            tn+=1
        if y[i]==0 and y_hat[i]==1:
            fp += 1
        if y[i] == 1 and y_hat[i] == 0:
            fn += 1
    precision = tp / (tp+fp)
    recall = tp / (tp + fn)
    f1_score = 2*precision*recall/(precision+recall)
    return f1_score
