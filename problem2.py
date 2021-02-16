#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""
import math

data1 = float(input("Please enter a number."))
data2 = float(input("Please enter another number."))

isfactor = False

if data1%data2 == 0:
    isfactor = True

if isfactor == True:
    print(str(int(data2))) + " is a factor of " + str(int(data1)))
else:
    print(str(int(data2))) + " is not a factor of " + str(int(data1)))
