#!/bin/python

import os

xmen_file = open('xmen.txt', 'r+')

xmen_file.seek(-1, os.SEEK_END)

xmen_file.write("\nBeast\n")
xmen_file.write("Phoenix\n")

xmen_file.seek(0, 0)

print(xmen_file.read())
# for line in xmen_file:
#    print(line)

xmen_file.close()

with open('xmen.txt', 'a') as xmen_file:
    xmen_file.write("professor xavier\n")

# read, write, readplus and append are the four file modes.
