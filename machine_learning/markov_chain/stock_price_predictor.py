#https://finance.yahoo.com/quote/%5EGSPC/history?p=%5EGSPC - 5Y data from 2017 to 2022
#code reference on https://www.viralml.com/static/code/Predict-Stock-Market-With-Markov-Chains-and-Python.html

import matplotlib
import matplotlib.pyplot as plt
import io, base64, os, json, re
import pandas as pd
import numpy as np
import datetime
from random import randint
import os

relative_path_to_file = '../data/original_files/yahoo/stockdata.csv'
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, relative_path_to_file)

df = pd.read_csv(filename)
print(len(df))
print(df.head())

