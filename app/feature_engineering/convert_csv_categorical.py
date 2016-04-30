import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_expedia = pd.read_csv("../../../train_etienne.csv")#, nrows=10)


for i in [1,2,3,4,5,7,8,9,10,16,17,18,20,21,22,23] :
	data_expedia[data_expedia.columns[i]] = data_expedia[data_expedia.columns[i]].apply(str)

data_expedia.to_csv('train_string_data.csv')

