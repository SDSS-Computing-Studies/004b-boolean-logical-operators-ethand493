#! python3
# Task2.py

"""
Ask the user to enter a number.
Tell them if the number is both a perfect square and a perfect cube.

Note:  Many languages have a problem when dealing with floating point
decimals, and python is no exception.
Sometimes, when finding the cube root of large numbers, like 729,
you may get 8.9999999999999999999998 instead of 9
To get around this, we can use the round() command
round() accepts 2 parameters, the number to be rounded, and how many decimals
a = round(3.999999999999998, 8) would round at the 8th decimal place, for example.
You don't want to round too early (ie to the nearest whole number) because that
might be too inaccurate.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a perfect cube.
xx is only a perfect square.
xx is only a perfect cube.

Example:
Enter a number: 8
8 is only a perfect cube.
"""
import math

data = float(input("Please enter a number. "))

cube = False
square = False

if (math.sqrt(data)**2 == data):
    square = True
if (round(data ** (1 / 3)) ** 3 == data):
    cube = True
if cube == True and square == True:
    print(str(data) + " is both a perfect square and perfect cube.")
elif square == True:
    print(str(data) + " is only a perfect square")
elif cube == True:
    print(str(data) + " is only a perfect cube")
