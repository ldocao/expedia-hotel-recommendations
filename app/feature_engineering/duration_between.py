import datetime

def duration_between(begin_time_as_str, end_time_as_str):
	begin_time = datetime.datetime.strptime(begin_time_as_str, "%Y-%m-%d")
	end_time = datetime.datetime.strptime(end_time_as_str, "%Y-%m-%d")
	duration = end_time - begin_time
	return duration