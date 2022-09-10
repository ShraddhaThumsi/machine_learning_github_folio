relative_path_to_data = '../data/preprocessed_files/kaggle/loan_sub.csv'
#relative_path_to_data = '../data/original_files/kaggle/accepted_2007_to_2018Q4.csv'
#the loan_sub file has been left out of git because its size exceeds 100mb.
# I have selected the first 20% of the dataset into my subset to allow for speedy processing.
# In case you would like to run the code on the same data as I, please reach out to me at
#thumsishraddhasatish@gmail.com, I will be happy to share the file with you.
# if you would like to download the original data from Kaggle, it can be found at https://www.kaggle.com/datasets/adarshsng/lending-club-loan-data-csv



#this file is the driver code for EDA (Exploratory Data Analysis) on the lending club data, a rich dataset on credit risk and financial parameters of borrowers of Lending Club
# This EDA will be followed by a comparative view of performances of different algorithms to predict whether a borrower will default on his loan.
import os
import pandas as pd
import machine_learning.utils.data_loader as data_loader
#import machine_learning.utils.data_eda_plotter as inhouse_plotter
import pandas as pd

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, relative_path_to_data)

data = data_loader.get_data(filename)
print(len(data))
df = pd.read_csv(filename)
familiar_columns = ['last_credit_pull_d', 'next_pymnt_d', 'issue_d', 'dti', 'num_sats', 'num_tl_30dpd', 'num_tl_90g_dpd_24m', 'num_tl_120dpd_2m']

print(set(list(df.loc[:,'issue_d'])))
print(sum(list(df.loc[:,'num_sats'])))
print(sum(list(df.loc[:,'num_tl_30dpd'])))
print(sum(list(df.loc[:,'num_tl_90g_dpd_24m'])))
print(sum(list(df.loc[:,'num_tl_120dpd_2m'])))




