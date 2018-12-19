#!bin/python

message = raw_input("What is your message? ")
count = raw_input("How many times should we repeat it? ").strip()

if count:
    count = int(count)
else:
    count = 1

def message_output(message, count):
    while count > 0:
        print(message)
        count -= 1

message_output(message,count)
