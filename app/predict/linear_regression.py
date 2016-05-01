import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.cross_validation import train_test_split
from math import sqrt
import ipdb
import numpy as np
import random


# Load Database
df = pd.read_csv("../../../data/train_target.csv", nrows=10000)

# features = df[["time_to_travel","stay_duration"]]
# target = df["appetence"]

# features_train = features.iloc[0:1500].values
# target_train = target.iloc[0:1500].values
# features_test = features.iloc[1501:]
# target_test = target.iloc[1501:]

# reg = linear_model.LinearRegression()
# reg.fit(features_train, target_train)

# print('Coefficients: \n', reg.coef_)  

# target_test_predicted = reg.predict(features_test)

