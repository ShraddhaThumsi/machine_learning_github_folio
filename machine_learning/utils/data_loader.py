import csv
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