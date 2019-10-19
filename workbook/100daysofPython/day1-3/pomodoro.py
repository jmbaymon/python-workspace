from datetime import datetime
from datetime import timedelta
import time


# User selects time option 

timeselection = input("Enter the minutes: ")

def timer(timeselection):
    tmins = timedelta(minutes=timeselection)
    while tmins != timedelta( minutes=0 , seconds=0):
        print(tmins)
        time.sleep(1)
        tmins = tmins - timedelta(seconds=1)
    print("Take a break.")

timer(timeselection)
