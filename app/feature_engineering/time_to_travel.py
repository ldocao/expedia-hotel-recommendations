import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

def duration_between2(begin_time_as_str, end_time_as_str):
	begin_time = datetime.datetime.strptime(begin_time_as_str, "%Y-%m-%d %H:%M:%S")
	end_time = datetime.datetime.strptime(end_time_as_str, "%Y-%m-%d")
	duration = end_time - begin_time
	return duration

data_expedia = pd.read_csv("../../../data_expedia/train_etienne.csv", nrows=100)

data_expedia["time_to_travel"]=data_expedia.apply(lambda row: duration_between2(row["date_time"], row["srch_ci"]), axis=1)

data_expedia.to_csv('train_with_time_to_travel.csv', index=False)


