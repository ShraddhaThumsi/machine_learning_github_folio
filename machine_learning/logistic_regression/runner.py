#data credits to https://www.npci.org.in/statistics
#code credits to https://www.analyticsvidhya.com/blog/2022/02/implementing-logistic-regression-from-scratch-using-python/
# Files used for analysis - (Bank-wise ATM/POS/Card statistics - March, April, May 2022)
# (Unanswered) Questions about data:
# 1. If payments through online modals for credit card counts as e-commerce, what is the column "other" representing? does it represent fees to the merchant or any other third party?
# 2. How can we have more volume of "other" credit card swipes than the value incurred from it? unless we are able to charge a credit card half rupee in a transaction, this wouldn't make sense



"""Problem statement - You are given the credit card/debit transaction yield per bank for the months March, April and May 2022.
Over all the banks which is likely to yield higher value, credit card, or debit card?
(predict 1 for debit card and 0 for credit card)"""


#Month bucketing - 44621 - March 2022, 44652 - April 2022, 44682 - May 2022


import os
import data_loader
import regression
import machine_learning.utils.plotter as inhouse_plotter
relative_path_to_file = '../data/preprocessed_files/rbi/banks_posatm_summary.csv'
learning_rate = 0.001
iterations_for_learning = 175
number_of_simulations = 75
test_set_proportion = 0.4
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, relative_path_to_file)
X,y = data_loader.get_features_labels(filename)
print(X.shape)
print(y.shape)


training_f1_score = []
testing_f1_score = []


for i in range(number_of_simulations):
    X_train, X_test, y_train, y_test = data_loader.split_data_to_traintest(X, y,test_size=test_set_proportion)

    X_train = data_loader.normalize_data(X_train)
    X_test = data_loader.normalize_data(X_test)
    reg_obj = regression.LogisticRegression()
    num_iter,cost_list = reg_obj.fit(X_train, y_train, alpha=learning_rate, iter=iterations_for_learning)
    y_test_pred = reg_obj.predict(X_test)
    y_train_pred = reg_obj.predict(X_train)

    f1_score_train = regression.F1_score(y_train,y_train_pred)
    f1_score_test = regression.F1_score(y_test,y_test_pred)
    training_f1_score.append(f1_score_train)
    testing_f1_score.append(f1_score_test)


inhouse_plotter.plot_curve(range(1, num_iter + 1), cost_list)
inhouse_plotter.plot_curve(range(1,number_of_simulations+1),testing_f1_score,include_bar_graph=True)


