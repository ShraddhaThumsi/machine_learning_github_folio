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
#type bucketing - 1 - Public sector banks, 2 - private sector banks,
#                 3 - foreign banks, 4- payment banks, 5 - small finance banks


import os
import data_loader
import machine_learning.logistic_regression.data_loader as logreg_dataloader
import machine_learning.utils.data_loader as generic_data_loader

import regression
import machine_learning.utils.algorithm_results_plotter as inhouse_plotter
import machine_learning.utils.math as inhouse_math
relative_path_to_file = '../data/preprocessed_files/rbi/banks_posatm_summary.csv'
learning_rate = 0.0009
iterations_for_learning = 275
number_of_simulations = 100
test_set_proportion = 0.4
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, relative_path_to_file)
headers,X,y = data_loader.get_features_labels(filename)
print(X.shape)
print(y.shape)
print(headers)



training_f1_score = []
testing_f1_score = []


for i in range(number_of_simulations):
    X_train, X_test, y_train, y_test = generic_data_loader.split_data_to_traintest(X, y, test_size=test_set_proportion)

    X_train = inhouse_math.normalize_data(X_train)
    X_test = inhouse_math.normalize_data(X_test)
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


month_sum_dict = logreg_dataloader.get_sum_given_feature(X, headers, 'Timeline', 'total debit card value')
banktype_sum_dict = logreg_dataloader.get_sum_given_feature(X, headers, 'type of bank', 'total debit card value')
month_correction_map = {'44621':'March 2022', '44652':'April 2022', '44682':'May 2022','44713':'June 2022','44743':'July 2022'}
banktype_correction_map = {'1':'Public Sector Bank', '2': 'Private Sector Bank', '3':'Foreign Bank', '4':'Payment Bank', '5':'Small Finance Bank'}
month_sums = data_loader.sumdict_with_corrected_labelnames(month_sum_dict, month_correction_map)
banktype_sums = data_loader.sumdict_with_corrected_labelnames(banktype_sum_dict, banktype_correction_map)
inhouse_plotter.plot_sums_as_pie(list(month_sums.keys()), list(month_sums.values()),'Value of debit card transactions per month (in Rs \'000)',convert_sums_to_int=False)
inhouse_plotter.plot_sums_as_pie(list(banktype_sums.keys()), list(banktype_sums.values()),'Value of debit card transactions per bank type over March-July 2022 (in Rs \'000)',convert_sums_to_int=False)
print(month_sums)
print(banktype_sums)