#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
#
# Author:   toshi123
# URL:      http://github.com/toshi123/
# License:  MIT License
# Created:  2016-07-19
#

import sys
filename = sys.argv[1]
s = 0
c = 0
inputfile = open(filename,'r')
for line in inputfile:
    s = s + float(line)
    c = c + 1
avr = s / c
inputfile.close()
print avr
