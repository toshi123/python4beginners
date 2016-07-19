#! /usr/bin/env python

height = 1.76
weight = 100
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
