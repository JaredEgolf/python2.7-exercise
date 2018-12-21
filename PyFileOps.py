#!/bin/python

def get_file_name(reprompt=False):
    if reprompt:
        print("Please enter the filename.")
    file_name = raw_input("Destination file name: ").strip()
    return file_name or get_file_name(True)

filename = get_file_name()

print("Content:  (Empty Line ends input.)")

with open(filename, 'w') as f:
    eof = False
    lines = []

    while not eof:
        line = raw_input()
        if line.strip():
            lines.append("%s\n" %line)
        else:
            eof = True
    f.writelines(lines)
    print("Lines written to %s" % filename)

