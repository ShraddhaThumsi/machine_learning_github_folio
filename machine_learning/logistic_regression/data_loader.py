

import machine_learning.utils.data_loader as data_loader
import numpy as np

def get_features_labels(filename):
    data = data_loader.get_data(filename)

    data[0]=[i.replace('\ufeff','') for i in data[0]]
    headers = data[0]
    X,y = data_loader.splitdata_to_features_labels(data[1:])
    X = np.array(X).astype(np.float)
    y = np.array(y).astype(np.float)
    return headers,X,y


def get_sum_given_feature(data,all_features,xaxis_metric,yxis_metric):
    x_axis_index = all_features.index(xaxis_metric)
    y_axis_index = all_features.index(yxis_metric)
    x_axis_values = []
    y_axis_values = []
    for d in data:
        x_axis_values.append(str(int(d[x_axis_index])))
        y_axis_values.append(float(d[y_axis_index]))
    dict_of_vals = {}
    for index,xval in enumerate(x_axis_values):
        yval = y_axis_values[index]
        if xval in dict_of_vals:
            exist = dict_of_vals[xval]
            exist.append(float(yval))
            dict_of_vals[xval] = exist
        else:
            dict_of_vals[xval] = [yval]

    dict_of_sums = {}
    for key,list_of_vals in dict_of_vals.items():
        dict_of_sums[key] = np.sum(list_of_vals)

    return dict_of_sums
