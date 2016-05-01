def most_common(pandas_series):
    if len(pandas_series) > 1:
        return pandas_series.value_counts().index[0]
    else:
        return pandas_series


