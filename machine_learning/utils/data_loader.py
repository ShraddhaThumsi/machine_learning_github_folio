import csv

import numpy as np
from sklearn.model_selection import train_test_split


def get_data(filename):
    file = open(filename)
    csvreader = csv.reader(file)
    data = []
    for row in csvreader:
        data.append(row)

    file.close()
    return data


def splitdata_to_features_labels(data):
    features = []
    labels = []
    for d in data:
        f = d[:-1]
        features.append(f)
        l = d[-1]
        labels.append(l)
    if len(features) != len(labels):
        raise ValueError('no of features is not same as number of labels')
    return features,labels


def split_data_to_traintest(X,y,test_size=0.3,shuffle=True):
    return train_test_split(X,y,test_size=test_size,shuffle=shuffle)


def get_features_labels(filename):
    data = get_data(filename)

    data[0]=[i.replace('\ufeff','') for i in data[0]]
    headers = data[0]
    X,y = splitdata_to_features_labels(data[1:])
    X = np.array(X).astype(np.float)
    y = np.array(y).astype(np.float)
    return headers,X,y
