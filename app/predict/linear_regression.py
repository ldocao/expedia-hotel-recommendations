import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
import ipdb


# Load Database
train_df=pd.read_csv("train_target.csv").dropna()


features=train_df[["orig_destination_distance", #variable to normalize
				"srch_adults_cnt",
				"srch_children_cnt",
				"srch_rm_cnt",
				"time_to_travel",
				"stay_duration",
				"is_mobile",
				"is_package"]]


target=train_df["appetence"]

reg = linear_model.LinearRegression()
reg.fit(features, target)
print('Coefficients: \n', reg.coef_)  