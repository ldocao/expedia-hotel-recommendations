def pseudo_numerics_to_string(data):
    for i in [1,2,3,4,5,7,8,9,10,16,17,18,20,21,22,23] :
        data[data.columns[i]] = data[data.columns[i]].apply(str)

    return data
