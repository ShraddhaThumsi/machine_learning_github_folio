#credits to https://www.geeksforgeeks.org/linear-regression-python-implementation/
# for skeleton of code

import numpy as np
from sklearn import linear_model
import os
import csv
import machine_learning.utils.algorithm_results_plotter as inhouse_plotter
import machine_learning.utils.math as inhouse_math
dirname = os.path.dirname(__file__)

relative_path_to_file = '../data/preprocessed_files/rbi/crop_data_pairs.csv'
filename = os.path.join(dirname, relative_path_to_file)
file = open(filename)
csvreader = csv.reader(file)
x_axis_vals = []
y_axis_vals = []

for row in csvreader:
    # loading up all columns for features, i.e. we will use Rice, Wheat and Cereal production values to predict the value of Total Cereal
    # example data point: 2020-2021: Rice - 1223,Wheat - 1095,Course Cereals- 512,Total Cereals - 2829
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
print('Closeness score: {}'.format(reg.score(X_test, y_test)))



# We plot the variances from the truth and also the closeness score line.
# Worth noting is that single parameter regression had much greater variation,
# i.e. the (truth - predicted) values varied greatly,
# but we were still able to arrive at the desired coefficient i.e. 1.

# Here, the multi-parameter regression is growing more steadily,
# and most of the variances are bound in a tighter range between -1 and 1.
# Refer to the image multivariate_linearregression.png in the graphs/ directory
inhouse_plotter.plot_variance(X_train,y_train,X_test,y_test,reg)

# invoking the manual calculation of the coefficients using the formula
# Theta = (XT*X)^-1*(XT)*y
# Theta is the array of values where each value is the respective coefficient of the feature.
params = inhouse_math.get_regression_parameters(X,y)
print(params)

# Plotting the data itself along with the regression line
# Note that we had to plot all three crop productions here, so I have added the values for the y-axis.
# In other words, you will see the x axis value for the production of each crop,
# but the y value is the sum of the three individual crops.
# There will be three squiggly lines for each of the three crops,
# where the corresponding y value is the same for each, denoting the sum
# Refer to multivariate_regressionline.png
inhouse_plotter.plot_regression_line(X, y, 0,params,is_singlevariate=False)