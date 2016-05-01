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
df=pd.read_csv("train_target.csv").dropna()

#features=df[["srch_adults_cnt"]]

features=df[["orig_destination_distance", #variable to normalize
				"srch_adults_cnt",
				"srch_children_cnt",
				"srch_rm_cnt",
				"time_to_travel",
				"stay_duration",
				"is_mobile",
				"is_package"]]
features_norm = (features-features.mean())/features.std()

target=df["appetence"]

features_train, features_test, target_train, target_test = train_test_split(features_norm, target, test_size=0.2, random_state=1)


reg = linear_model.LinearRegression()
reg.fit(features_train, target_train)

print('Coefficients: \n', reg.coef_)  

target_test_predicted = reg.predict(features_test)

#sns.distplot(np.sqrt((target_test_predicted-target_test)**2),kde=False, bins=100)
# plt.figure(1)
# sns.regplot(features_test,target_test)
# sns.regplot(features_train,target_train)
# plt.show()

plt.figure(2)
sns.distplot(((target_test_predicted-target_test)),kde=False, bins=100)
#plt.yscale("log")
plt.show()
