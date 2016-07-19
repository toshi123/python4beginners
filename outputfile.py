#! /usr/bin/env python
import sys

filename = sys.argv[1]
inputfile = open(filename,'r')

for line in inputfile:
    print line.rstrip()

inputfile.close()
