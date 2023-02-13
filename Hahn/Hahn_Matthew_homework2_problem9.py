# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:45:08 2023

@author: Matthew
"""
import math

print("PART A")
a = float(input("Enter the value for a:"))
b = float(input("Enter the value for b:"))
c = float(input("Enter the value for c:"))

# Creating 2 different equations for the quadratic equation
def x():
    x1 = (0-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    return x1

def y():
    y1 = (0-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    return y1

print("The roots for the quadratice equation are:", x(), y())

