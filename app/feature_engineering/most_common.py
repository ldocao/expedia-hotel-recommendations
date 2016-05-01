import numpy as np

def most_common(pandas_series):
    if len(pandas_series) > 1:
        try:
            return pandas_series.value_counts().index[0]
        except IndexError:
            return np.nan
    else:
        return pandas_series


