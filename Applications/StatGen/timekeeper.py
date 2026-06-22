import pytz
from datetime import date, datetime
import time

time_zones = pytz.all_timezones

def time_table_generator():
    increment = 15
    hour_max = 24
    current_minutes = 0
    current_hour = 0
    time_table = []
    while current_hour < hour_max:
        time_string = f"{current_hour:02}:{current_minutes:02}:00"
        time_table.append(time_string)
        current_minutes += increment
        if current_minutes == 60:
            current_minutes = 0
            current_hour += 1
    return time_table

def time_name():
    name_ = int(time.time())
    return name_

def convert_time(start_time, end_time, time_zone):
    today_ = date.today().strftime("%Y-%m-%d")
    start_ = f"{today_} {start_time}"
    end_ = f"{today_} {end_time}"
    gmt_start = pytz.timezone(time_zone).localize(datetime.strptime(start_, '%Y-%m-%d %H:%M:%S')).astimezone(pytz.utc)
    gmt_end = pytz.timezone(time_zone).localize(datetime.strptime(end_, '%Y-%m-%d %H:%M:%S')).astimezone(pytz.utc)
    start_date = gmt_start.strftime("%Y-%m-%d")
    end_date = gmt_end.strftime("%Y-%m-%d")
    start_time = gmt_start.strftime("%H:%M:%S")
    end_time = gmt_end.strftime("%H:%M:%S")
    return start_date, end_date, start_time, end_time
