"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is not frue
"""

#! python3

import math

data = float(input("Please enter a number."))

isdivisible6 = False

if data%6 == 0:
    isdivisible6 = True

isdivisible8 = False

if data%8 == 0:
    isdivisible8 = True

if isdivisible8 == False and isdivisible6 == True:
    print(str(data) + " is frue")
else:
    print(str(data) + " is not frue") 
