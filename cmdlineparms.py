#!/bin/python

# Simplified parameters
# import sys

# print("First argument %s" % sys.argv[1])

# Robust Method
import argparse

parser = argparse.ArgumentParser() # Class 'ArgumentParser' with a constructor function
parser.add_argument('filename', help='The helpfile') # Method of the class
args = parser.parse_args()

