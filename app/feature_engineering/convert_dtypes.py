def pseudo_numerics_to_string(data):
    column_to_convert = ['site_name',
                         'posa_continent',
                         'user_location_country',
                         'user_location_region',
                         'user_location_city',
                         'user_id',
                         'channel',
                         'srch_destination_id',
                         'srch_destination_type_id',
                         'hotel_continent',
                         'hotel_country',
                         'hotel_market',
                         'hotel_cluster']
    
    for col in column_to_convert :
        data[col] = data[col].apply(str)

    return data
