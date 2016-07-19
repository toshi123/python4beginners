#!/usr/bin/env python

def calcBMI(height,weight):
    bmi = weight / height**2
    return bmi

if __name__ == "__main__":
    father_w = 80.0
    father_h = 1.70
    mother_w = 53.0
    mother_h = 1.62
    son_w = 35.0
    son_h = 1.25

    father_bmi = calcBMI(father_h, father_w)
    mother_bmi = calcBMI(mother_h, mother_w)
    son_bmi = calcBMI(son_h, son_w)
    print father_bmi, mother_bmi, son_bmi
