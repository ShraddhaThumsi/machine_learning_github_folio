#credits to https://www.geeksforgeeks.org/linear-regression-python-implementation/
# for skeleton of code

import numpy as np
from sklearn import linear_model
import os
import csv
import machine_learning.plotter as inhouse_plotter
dirname = os.path.dirname(__file__)

relative_path_to_file = '../data/preprocessed_files/rbi/crop_data_pairs.csv'
filename = os.path.join(dirname, relative_path_to_file)
file = open(filename)
csvreader = csv.reader(file)
x_axis_vals = []
y_axis_vals = []

for row in csvreader:

    x_axis_vals.append(row[0:-1])
    y_axis_vals.append(row[-1])
file.close()
X = np.array(x_axis_vals).astype(np.float)
y = np.array(y_axis_vals).astype(np.float)


# splitting X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4,
													random_state=1)


# create linear regression object
reg = linear_model.LinearRegression()

# train the model using the training sets
reg.fit(X_train, y_train)

# regression coefficients
print('Coefficients: ', reg.coef_)

# variance score: 1 means perfect prediction
print('Variance score: {}'.format(reg.score(X_test, y_test)))




inhouse_plotter.plot_variance(X_train,y_train,X_test,y_test,reg)

#inhouse_plotter.plot_regression_line(X, y, b_0,b_1,is_singlevariate=False)