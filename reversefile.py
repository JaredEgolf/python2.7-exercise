#!/bin/python

# Simplified parameters
# import sys

# print("First argument %s" % sys.argv[1])

# Robust Method
import argparse

parser = argparse.ArgumentParser(description='Read a file in reverse') # Class 'ArgumentParser' with a constructor function
parser.add_argument('filename', help='The helpfile') # Method of the class
parser.add_argument('--limit', '-l', type=int, help='The number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

#print(args.filename)

try:
    f = open(args.filename)
except IOError as err:
    print("Error: file not found")
else:
    with f:
        limit = args.limit
        lines = f.readlines()
        lines.reverse()

        if args.limit:
            lines = lines[:limit]

        for line in lines:
            print(line.strip()[::-1])
finally:
    print("\nEnd of program\n")
