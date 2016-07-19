#! /usr/bin/env python
import sys

id = ''
seq = ''
file = open(sys.argv[1])

for line in file:
    line = line.rstrip()
    if line.startswith(">"):
        id = line[1:]
    else:
        seq += line

print id
print seq
