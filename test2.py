# Import the datetime module
from datetime import datetime

# Use the datetime.now() function to get the current date and time as a datetime object
dt = datetime.now()

# Use the strftime() method to format the date and time as a string
# Use '%H%M' as the format string to get only the hour data in the format '0700'
hour_data = dt.strftime('%H%M')

# Print or use the formatted string as you wish
print(type(hour_data)) # This will print the current hour data in the format '0700'
