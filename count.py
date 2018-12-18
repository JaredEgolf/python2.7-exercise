count = 0
while count < 10:
    if count % 2 == 0:
        print("Count is even %s" % count)
        count += 1
    print("Counting still %s" % count)
    count += 1
    break
print("End count is %s" % count)

