#!/usr/bin/env python
user = { 'admin': False, 'active': False, 'name': "Jared" }
if user['admin'] and user['active']:
    print("ACTIVE - (ADMIN) %s" % user['name'])
elif user['admin']:
    print("(ADMIN) %s" % user['name'])
elif user['active']:
    print("ACTIVE - %s" % user['name'])
else:
    print(user['name'])


