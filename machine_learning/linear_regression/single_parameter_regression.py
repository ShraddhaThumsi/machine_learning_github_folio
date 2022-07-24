#credits to https://www.geeksforgeeks.org/linear-regression-python-implementation/
# for skeleton of code
import csv
import numpy as np
from sklearn import linear_model
import os
import machine_learning.utils.plotter as inhouse_plotter
import machine_learning.utils.math as inhouse_math
dirname = os.path.dirname(__file__)
data_pairs_path = '../data/preprocessed_files/rbi/crop_data_pairs.csv'
filename = os.path.join(dirname, data_pairs_path)
file = open(filename)
csvreader = csv.reader(file)
x_axis_vals = []
y_axis_vals = []
rows = []
# here, you can choose which crop you want to use to perform linear regression upon.
# The aim is to predict the value of the column "Total Cereals" as appears in the data set.
# Consider the data-point for 2020-2021: Rice - 1223,Wheat - 1095,Course Cereals- 512,Total Cereals - 2829
# Simple observation concludes that
# Rice + wheat + course cereal = total cereal,
# i.e. we want to attach a coefficient of 1 to each to get closer to the "truth"

list_of_possible_crops = ['Rice','Wheat','Coarse Cereals']
crop_for_analysis = 'Wheat'
index_to_search = list_of_possible_crops.index(crop_for_analysis)
for row in csvreader:
    rows.append(row)
    x_axis_vals.append(row[index_to_search])
    y_axis_vals.append(row[-1])
file.close()
X = np.array(x_axis_vals).astype(np.float)
y = np.array(y_axis_vals).astype(np.float)

def find_deviations(axis_1, axis_2):
    n = len(axis_1)

    axis_1 = np.array(axis_1).astype(np.float)
    axis_2 = np.array(axis_2).astype(np.float)
    mean_1 = np.mean(axis_1)


    mean_2 = np.mean(axis_2)

    running_sum = 0
    for i in range(0,n):
        v1 = axis_1[i]
        v2 = axis_2[i]

        running_sum += (v1*v2)

    return running_sum - (n * mean_1 * mean_2)

deviation_xx = find_deviations(axis_1=X, axis_2=X)
deviation_xy = find_deviations(axis_1= X, axis_2 = y)

# in the equation y=b_0 + b_1x, we are writing the code to find values for beta manually.
# below this, there is also a version where I fit a LinearRegression model and invoke the .coef_ property
b_1 = deviation_xy/deviation_xx
b_0 = np.mean(y) - (b_1 * np.mean(X))

from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test = train_test_split(X.reshape(-1,1), y, test_size=0.4,
													random_state=1)

print(X_train.shape)
# create linear regression object
reg = linear_model.LinearRegression()

# train the model using the training sets
reg.fit(X_train, y_train)

print('Coefficients: ', reg.coef_)


# closeness score: 1 means perfect prediction
# We want to find how close we are to the truth, so closer to the value of 1, better our prediction is.
# We can change the crop we use for analysis and see how our performance changes.
# In a summary, it was found that Rice as about 99% closeness score, wheat about 98% and course cereal about 80%
# This is interesting because examining the values in
#    2020-2021: Rice - 1223,Wheat - 1095,Course Cereals- 512,Total Cereals - 2829
#    we can say that Rice and Wheat are clearly cultivated in larger quantities compared to total cereals,
#    so the differences in performance make intuitive sense
print('Closeness score: {}'.format(reg.score(X_test, y_test)))


# In the following graph, we will plot the values of predictions and the closeness score line
# The code to auto-save the image to disc has been omitted but rather stored manually.
# Please refer to the image univariate_linearregression.png.
inhouse_plotter.plot_variance(X_train, y_train,X_test,y_test,reg)

# In the next graph, we will plot the data itself and the regression line to see how well we fit the data.
# Again, based on the crop we choose, we can see different graphs here.
# Refer to univariate_regressionline.png
inhouse_plotter.plot_regression_line(X, y, b_0,b_1,crop_for_analysis)