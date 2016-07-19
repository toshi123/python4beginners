#!/usr/bin/env python

class Person:
    def __init__(self,nm,h,w):
        self.name = nm
        self.height = h
        self.weight = w
        self.bmi = w / h**2
    def say(self):
        print self.name,self.bmi
    def getBMI(self):
        return self.bmi
