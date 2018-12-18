#!/bin/python

import argparse

parser = argparse.ArgumentParser(description='Search for words and partial word')
parser.add_argument('snippet', help='partial (or complete) string to search')

args = parser.parse_args()
snippet = args.snippet.lower()

words = open('/usr/share/dict/words').readlines()

numbers = [1,2, 3,4]
print([x * x for x in numbers])

print([word for word in words if snippet in word.lower()])


#matches = []
#
#for word in words:
#    if snippet in word.lower():
#        matches.append(word)
#
#print(matches)

