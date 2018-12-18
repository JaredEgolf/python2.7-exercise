#!/bin/python

import random
import os
import json

#random.choice(1,2,3,4,5,6)
#random.uniform(1,1000)

count = os.getenv("FILE_COUNT") or 100
words = [word.strip() for word in open('/usr/share/dict/words').readlines()]

for id in range(1, count + 1):
    amount = random.uniform(1,1000)
    content = {
        'topic': random.choice(words),
        'value': "%.2f" % amount
    }
    with open('./new/receipt-%s.json' % id, 'w') as f:
        json.dump(content, f)
