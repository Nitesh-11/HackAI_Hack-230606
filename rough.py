from datetime import datetime, timedelta

now = datetime.now()
def convert_datetime_to_hour_minute(datetime_string):
    # Parse the datetime string into a datetime object
    datetime_object = datetime.datetime.strptime(datetime_string, '%Y-%m-%d %H:%M:%S')
    # Extract the hour and minute from the datetime object
    hour = datetime_object.hour
    minute = datetime_object.minute
    # Format the hour and minute into a string with four digits
    hour_minute_string = f'{hour:02}{minute:02}'
    # Return the hour and minute string
    return hour_minute_string

def hour_rounder(t):
    # Rounds to nearest hour by adding a timedelta hour if minute >= 30
    
    return (t.replace(second=0, microsecond=0, minute=0, hour=t.hour)
               +timedelta(hours=t.minute//30))


print(type(now))
print(hour_rounder(now))