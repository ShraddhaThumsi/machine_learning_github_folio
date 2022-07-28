# data credits to: UCI Machine Learning Repository [http://archive.ics.uci.edu/ml].
import os
import numpy as np
import machine_learning.utils.data_loader as data_loader
#relative_path_to_data = '../data/preprocessed_files/uci_archives/data_banknote_authentication.txt'
relative_path_to_data = 'test_logistic_regression.csv'
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, relative_path_to_data)

# def data_loader(file_n):
#     file = open(file_n, 'r')
#     lines = file.readlines()
#     file.close()
#     return lines

# def data_cleaner(lines):
#     lines = [l.replace('\n','') for l in lines]
#     lines= [l.split(',') for l in lines]
#     data = []
#     label = []
#     [data.append(l[0:-1]) for l in lines]
#     [label.append(l[-1]) for l in lines]
#     X,y = (data,label)
#     print(len(lines))
#     print(lines[0])
#     return X,y

lines = data_loader.get_data(filename)
print(lines)
X,y = data_loader.splitdata_to_features_labels(lines)
X = np.array(X).astype(np.float)
y = np.array(y).astype(np.float)
print('shape of features')
print(X.shape)
print('shape of labels')
print(y.shape)
