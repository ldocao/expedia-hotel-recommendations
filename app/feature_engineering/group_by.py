# -*- coding: utf-8 -*-
import pandas as pd
import datetime
from feature_engineering.duration import between_date, between_datetime
from feature_engineering.most_common import most_common

featured_train = "../../../data/train_final.csv"
non_unique_pairs = pd.read_csv(featured_train, nrows=1000)



## restore date time
non_unique_pairs["date_time"] = non_unique_pairs["date_time"].apply(lambda date: datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S").date())


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

unique_pairs["date_time"] = group["date_time"].agg(most_common)
unique_pairs["srch_ci"] = group["srch_ci"].agg(most_common)
unique_pairs["hotel_market"] = group["hotel_market"].agg(most_common)
unique_pairs["srch_destination_id"] = group["srch_destination_id"].agg(most_common)
unique_pairs["user_location_city"] = group["user_location_city"].agg(most_common)
unique_pairs["user_location_region"] = group["user_location_region"].agg(most_common)

