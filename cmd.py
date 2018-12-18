#!/bin/python

import subprocess

#code = subprocess.call(['ls', '-l'])
code = subprocess.check_output(['ls', '-z'])
#if code == 0:
#    print("command finished successfully")
#else:
#    print("failed with code: %i" % code)
print(code)

