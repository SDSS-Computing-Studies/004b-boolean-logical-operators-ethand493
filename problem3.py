#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""

a = float(input("Please enter a number."))
b = float(input("Please enter another number."))
c = float(input("Please enter a final number."))

formed = False

if a**2 + b**2 == c**2:
    formed = True
elif b**2 + c**2 == a**2:
    formed = True
elif a**2 + c**2 == b**2:
    formed = True

if formed == True:
    print(str(int(a)) + "," + str(int(b)) + "," + str(int(c)) + " form a Pythagorean Triple")
else:
    print(str(int(a)) + "," + str(int(b)) + "," + str(int(c)) + " do not form a Pythagorean Triple")