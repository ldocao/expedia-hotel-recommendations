# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


data_dir = "../../../data/" 
source = data_dir + "train_etienne.csv"
destination = data_dir + "user_click_counts.csv"
df = pd.read_csv(data)


sum_counts_per_user = df.groupby("user_id")["cnt"].sum()
sum_counts_per_user = sum_counts_per_user.reset_index()
sum_counts_per_user.columns = ["user_id", "total_number_of_clicks"]
sum_counts_per_user.to_csv(destination, index=False, header=True)
