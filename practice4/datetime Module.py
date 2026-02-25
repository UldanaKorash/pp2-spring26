import datetime
now = datetime.datetime.now()
print("Current date and time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)



import datetime
birthday = datetime.datetime(2005, 7, 15)
print("Birthday:", birthday)


import datetime
now = datetime.datetime.now()
formatted = now.strftime("%d/%m/%Y %H:%M:%S")
print("Formatted:", formatted)