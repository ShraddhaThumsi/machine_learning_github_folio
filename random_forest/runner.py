import os


import machine_learning.utils.data_loader

relative_path_to_file = '../machine_learning/data/preprocessed_files/rbi/banks_posatm_summary.csv'
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, relative_path_to_file)
headers,X,y = machine_learning.utils.data_loader.get_features_labels(filename)
print(X.shape)
print(y.shape)
print(headers)