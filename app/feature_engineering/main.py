import pandas as pd
import feature_engineering.convert_dtypes as convert_dtypes
from feature_engineering.duration import between_date, between_datetime

## shortcut
data_dir = "../../../data/"
source = data_dir + "train_etienne.csv"
destination = data_dir + "train_final.csv"


## perform operations
data_expedia = pd.read_csv(source, nrows=1000000)
data_expedia = convert_dtypes.pseudo_numerics_to_string(data_expedia)
data_expedia["stay_duration"] = data_expedia.apply(lambda row: between_date(row["srch_ci"], row["srch_co"]), axis=1)
data_expedia["time_to_travel"] = data_expedia.apply(lambda row: between_datetime(row["date_time"], row["srch_ci"]), axis=1)


## write to file
data_expedia.to_csv(destination, index=False)
