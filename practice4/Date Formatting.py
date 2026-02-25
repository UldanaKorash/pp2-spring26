import datetime
now = datetime.datetime.now()
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print("Current date and time:", formatted)



import datetime
now = datetime.datetime.now()
formatted = now.strftime("%A, %d %B %Y")
print("Today is:", formatted)


import datetime
now = datetime.datetime.now()
formatted = now.strftime("%I:%M %p")
print("Current time:", formatted)