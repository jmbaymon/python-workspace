#datetime

from datetime import datetime
from datetime import date
# print whole date and current time
print(datetime.today())

today = datetime.today()

print(type(today))

todaydate = date.today()
# print only the current date
print(todaydate)

print(todaydate.month)
print(todaydate.year)
print(todaydate.day)

christmas = date(2019, 12, 25)

SantaCountdown = christmas - todaydate


if christmas is not todaydate:
    print("It is " + str(SantaCountdown.days) + " days to Christmas")
else: 
    print("It is Xmas")

