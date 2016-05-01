# -*- coding: utf-8 -*-
import pandas as pd
import datetime
import seaborn as sns
from feature_engineering.duration import between_date, between_datetime
from feature_engineering.most_common import most_common

featured_train = "../../../data/train_final.csv"
user_click = "../../../data/user_click_counts.csv"
total_number_of_clicks = pd.read_csv(user_click)
non_unique_pairs = pd.read_csv(featured_train)



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
unique_pairs = unique_pairs.reset_index()
unique_pairs = unique_pairs.merge(total_number_of_clicks,
                                  left_on="user_id",
                                  right_on="user_id",
                                  how="inner")

n_booking = unique_pairs["is_booking"]
n_clicks = unique_pairs["cnt"]
total_n_clicks = unique_pairs["total_number_of_clicks"]
unique_pairs["appetence"] = (n_clicks + (n_booking*total_n_clicks/2)) / (total_n_clicks*(1+n_booking/2))

sns.distplot(unique_pairs["appetence"], bins=100)
