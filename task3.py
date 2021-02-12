#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer
"""
import math

data = float(input("Please enter a number. "))

if data >= 0:
    print(str(data) + " is a positive integer.")
else:
    print(str(data) + " is not a positive integer")