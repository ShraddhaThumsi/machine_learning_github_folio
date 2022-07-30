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
relative_path_to_file = '../data/preprocessed_files/rbi/banks_posatm_summary.csv'
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, relative_path_to_file)
X,y = data_loader.get_features_labels(filename)
print(X.shape)
print(y.shape)

X_train,X_test,y_train,y_test = data_loader.train_test_split(X,y)
print('shape of training data:')
print(X_train.shape)
print('shape of training labels')
print(y_train.shape)


print('shape of testing data:')
print(X_test.shape)
print('shape of testing labels')
print(y_test.shape)