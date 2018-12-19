#!/bin/python

import glob
import os
import shutil
import json

try:
    os.mkdir("./processed")
except OSError:
    print("'processed' directory already exists")

# Get a list of receipts
receipts = glob.glob('./new/receipt-[0-9]*.json')

subtotal = 0.0

for path in receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    name = path.split('/')[-1]
    destination = "./processed/%s" % name
    shutil.move(path, destination)
    print("moved '%s' to '%s'" % (path, destination))

print("Receipt subtotal: $%.2f" % subtotal)

# Iterate over the receipts
    # read content and tally a subtotal
    # move the file to the processed directory
    # print that we processed the file

# Print the subtotal of all processed receipts
