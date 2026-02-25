import datetime
today = datetime.date.today()
exam_day = datetime.date(2026, 6, 1)
difference = exam_day - today
print("Days until exam:", difference.days)


import datetime
now = datetime.datetime.now()
future = datetime.datetime(2026, 2, 26, 18, 30, 0)
diff = future - now
print("Time difference:", diff)
print("Seconds:", diff.total_seconds())