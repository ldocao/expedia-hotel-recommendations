import datetime
import numpy as np

def between_date(begin_time_as_str, end_time_as_str):
    try:
        begin_time = datetime.datetime.strptime(begin_time_as_str, "%Y-%m-%d")
        end_time = datetime.datetime.strptime(end_time_as_str, "%Y-%m-%d")
        return end_time - begin_time
    except TypeError:
        return np.nan



def between_datetime(begin_time_as_str, end_time_as_str):
    try:
        begin_time = datetime.datetime.strptime(begin_time_as_str, "%Y-%m-%d %H:%M:%S")
        end_time = datetime.datetime.strptime(end_time_as_str, "%Y-%m-%d")
        return end_time - begin_time
    except TypeError:
        return np.nan

