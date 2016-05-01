# -*- coding: utf-8 -*-
import pandas as pd
import datetime
from feature_engineering.duration import between_date, between_datetime

featured_train = "../../../data/train_final.csv"
non_unique_pairs = pd.read_csv(featured_train, nrows=1000)



## restore date time
non_unique_pairs["date_time"] = non_unique_pairs["date_time"].apply(lambda date: datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S"))


group = non_unique_pairs.groupby(["user_id", "hotel_cluster"])


unique_pairs = group.agg({'orig_destination_distance':'mean',
                          'srch_adults_cnt':'mean',
                          'srch_children_cnt':'mean',
                          'srch_rm_cnt':'mean',
                          'cnt':'sum',
                          'is_mobile':'mean',
                          'is_package':'mean',
                          'is_booking':'sum',
                          'stay_duration':'mean',
                          'time_to_travel':'mean'})


