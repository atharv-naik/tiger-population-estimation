'''
get_features.py
    This script finds new and useful features from the dataset
Usage:
    python get_features.py'''


import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from scipy import stats
stats.chisqprob = lambda chisq, df: stats.chi2.sf(chisq, df)

raw_data = pd.read_csv('Train.csv') # Load the dataset
raw_data = raw_data.drop('Trail', axis = 1)
print(raw_data)

# We make sure to create a copy of the data before we start altering it. Note that we don't change the original data we loaded.
data = raw_data.copy()
print(data.describe())

y = data ['Distinct']
x1 = data.drop ('Distinct', axis = 1) # Selecting the independent and dependent variables

x = sm.add_constant(x1) # Trying to find useful features with logistic distribution
x = x
reg_log = sm.Logit(y,x)
results_log = reg_log.fit()
# Get the regression summary
print(results_log.summary())
