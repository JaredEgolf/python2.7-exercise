#!/bin/python

import os

stage = os.environ["STAGE"].upper()

output = "We're running in %s" % stage

if stage.startswith("PROD"):
    output = "DANGER?? - " + output

print(output)
