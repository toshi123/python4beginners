#!/usr/bin/env python

import sys

height = sys.argv[1]
weight = sys.argv[2]
height = float(height)
weight = float(weight)

bmi = weight / height**2

if bmi > 25:
    print "BMI is " + str(bmi)
    print "Overweight"
elif bmi >= 18.5:
    print "BMI is " + str(bmi)
    print "Normal weight"
else:
    print "BMI is " + str(bmi)
    print "Underweight"
