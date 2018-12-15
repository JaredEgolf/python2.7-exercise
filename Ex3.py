#!/usr/bin/env python
users = [{ 'admin': False, 'active': False, 'name': "Jared" }, { 'admin': False, 'active': True, 'name': "John" }, { 'admin': True, 'active': False, 'name': "Jill" }, { 'admin': True, 'active': True, 'name': "ADMIN" }]
count = 1
for user in range(len(users)):
    user = users.pop()
    if user['admin'] and user['active']:
        print("%s ACTIVE - (ADMIN) %s" % (count, user['name']))
        count += 1
    elif user['admin']:
        print("%s (ADMIN) %s" % (count, user['name']))
        count += 1
    elif user['active']:
        print("%s ACTIVE - %s" % (count, user['name']))
        count += 1
    else:
        print("%s %s" % (count, user['name']))
        count += 1

