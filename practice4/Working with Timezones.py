import datetime
import pytz
timezone = pytz.timezone("Asia/Almaty")
now = datetime.datetime.now(timezone)
print("Current time in Almaty:", now)


import datetime
import pytz
tz_tokyo = pytz.timezone("Asia/Tokyo")
tz_ny = pytz.timezone("America/New_York")
tokyo_time = datetime.datetime.now(tz_tokyo)
ny_time = tokyo_time.astimezone(tz_ny)
diff = tokyo_time - ny_time
print("Tokyo time:", tokyo_time)
print("New York time:", ny_time)
print("Time difference:", diff)