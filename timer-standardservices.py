#!/bin/python

# import time
from time import localtime, strftime, mktime

start_time = localtime()
print("Timer started at %s" % strftime("%X", start_time))

# Wait for user input
raw_input("Please press Enter to continue...")

stop_time = localtime()
difftime = mktime(stop_time) - mktime(start_time)

print("Timer stopped at %s" % strftime("%X", stop_time))
print("Total time: %s seconds" % difftime)

