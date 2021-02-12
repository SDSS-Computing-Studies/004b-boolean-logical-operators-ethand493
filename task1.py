
#! python3
"""
The Earth maintains an orbit where it's closest distance to  
the sun is 0.9759 AU and it's furthest distance to the sun is 
1.016 AU. 
Ask the user to enter a number. 
Tell them if the number is between 0.9759 and 1.016.
(2 points)

Inputs:
a number (float)

Outputs:
That is within normal Earth orbit.
That is not within normal Earth orbit.
"""

data = float(input("Please enter a number. "))

if data >= 0.9759 and data <= 1.016:
    print("That is within normal Earth orbit.")
else:
    print("That is not within normal Earth orbit.") 
    
     