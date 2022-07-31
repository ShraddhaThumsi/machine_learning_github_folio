import csv

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
