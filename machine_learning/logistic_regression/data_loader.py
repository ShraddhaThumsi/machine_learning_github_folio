

import machine_learning.utils.data_loader as data_loader
from sklearn.model_selection import train_test_split
import numpy as np

def get_features_labels(filename):
    data = data_loader.get_data(filename)

    data[0]=[i.replace('\ufeff','') for i in data[0]]

    X,y = data_loader.splitdata_to_features_labels(data[1:])
    X = np.array(X).astype(np.float)
    y = np.array(y).astype(np.float)
    return X,y


def split_data_to_traintest(X,y,test_size=0.1):
    return train_test_split(X,y,test_size)
