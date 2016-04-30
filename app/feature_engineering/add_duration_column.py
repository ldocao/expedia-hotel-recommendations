import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os 

os.sys.path.append("C:\\Users\\shan\\Desktop\\Hackathon\\expedia-hotel-recommendations\\app")

import feature_engineering.duration_between as db


df=pd.read_csv("train_string_data.csv")

try:
	df["stay_duration"]=df.apply(lambda row: db.duration_between(row["srch_ci"], row["srch_co"]), axis=1)
except TypeError:
	pass

df.to_csv("train_with_stay_duration.csv")
