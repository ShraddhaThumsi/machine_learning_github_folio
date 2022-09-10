import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt
import hvplot
import hvplot.pandas
import machine_learning.algo_comparison_lendingclubdata.loandefaulters_eda as eda

df = eda.get_data_frame()
print(df.shape)

#plt.figure(figsize=(12, 8))
#sns.heatmap(df.corr(), annot=True, cmap='viridis')

