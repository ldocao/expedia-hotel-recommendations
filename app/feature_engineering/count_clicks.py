# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

data = "../../../data/train_etienne.csv"
df = pd.read_csv(data)


sum_counts_per_user = df.groupby("user_id")["cnt"].sum()
sum_counts_per_user = sum_counts_per_user.reset_index()
sum_counts_per_user.columns = ["user_id", "total_number_of_clicks"]
sum_counts_per_user.to_csv("../../../data/user_click_counts.csv", index=False, header=True)
