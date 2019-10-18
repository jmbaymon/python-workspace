from datetime import datetime
from datetime import timedelta


# t = timedelta(days=4, hours=10)

# print(t.days)
# # show only numbers of seconds for the hours ex:10 hrs
# print(t.seconds)

eta = timedelta(hours=6)

today = datetime.today()

print(eta)
print("The ETA is " + str(today + eta))
