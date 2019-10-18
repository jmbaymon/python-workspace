from datetime import datetime
from datetime import timedelta
from datetime import time


# User selects time option 

timeselection = input("Enter the amount of minutes: ")

def timer(timeselection):
    tmins = timedelta(minutes=timeselection)
    while tmins != timedelta( minutes=0 , seconds=0):
        print(tmins)
        time.
        tmins = tmins - timedelta(seconds=1)

timer(timeselection)