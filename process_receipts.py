#!/bin/python

import glob
import os
import shutil
import json
import re # Regular Expression Package
import math

try:
    os.mkdir("./processed")
except OSError:
    print("'processed' directory already exists")

# Get a list of receipts
# receipts = glob.glob('./new/receipt-[0-9]*.json')

# Get only even number receipts
receipts = [f for f in glob.iglob('./new/receipt-[0-9]*.json')
        if re.match('./new/receipt-[0-9]*[02468].json', f)]

subtotal = 0.0

for path in receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    destination = path.replace('new', 'processed')
    shutil.move(path, destination)
    print("moved '%s' to '%s'" % (path, destination))

print("Receipt subtotal: $%s" % round(subtotal,2))

# Iterate over the receipts
    # read content and tally a subtotal
    # move the file to the processed directory
    # print that we processed the file

# Print the subtotal of all processed receipts
