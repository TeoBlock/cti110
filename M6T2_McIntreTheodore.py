# This program takes user input of feet and converts to inches
# 16 November 2017
# CIT-110 M6HW2 - Random Number Guessing Game
# Theodore McIntire
#


# Constant is defined outside of functions - feet to inches
F2I_CONV_FACTOR = 12

def main():
    
# The main function calls the show_inches function and prints the result

# ideally variables defined at the outset of def main():

    feet = 0
    ft = 0
    inches = 0

    feet = float(input('Please enter a distance in feet: '))

    inches = feet_2_inches(feet)
    
    print(format(feet, ',.2f'), 'feet =', format(inches, ',.2f'), 'inches.')

#Note - Alternate print function per tutorial obviates need for "inches = ..."
    print(format(feet, ',.2f'), 'feet =', format(feet_2_inches(feet), ',.2f'), 'inches.')
    
# This is the end of def main():

def feet_2_inches(ft):

# The feet_2_inches function gets user input of feet and RETURNS a value in inches 

    return ft * F2I_CONV_FACTOR
          
# This is the end of def feet_2_inches():

main() 

#end of program
