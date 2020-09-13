from datetime import datetime
import time
import pytz

def parse_datetime_str(datetime_value, datetime_format, timezone):
  return datetime.strptime(
    datetime_value + " " + timezone, datetime_format + " %z"
  )

def datetime_to_timestamp(dt):
  return int(time.mktime(dt.timetuple()))

def convert_datetime_timezone(dt, target_timezone):
  return dt.astimezone(pytz.timezone(target_timezone))