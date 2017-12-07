# CIT-110
# Theodore McIntire
# 15 November 2017
# This program takes user input distance in kilometers and converts to miles

# Constant is defined outside of functions
K2M_CONV_FACTOR = 0.621

def main():
    
# The main function gets the user input of kilometers

# ideally variables defined at the outset of def main():

    kilometers = 0
    km = 0
    miles = 0

    kilometers = float(input('Please enter a distance in kilometers: '))

    show_miles(kilometers)

# This is the end of def main():


def show_miles(km):

# The show_miles function converts kilometers to miles and shows/prints result

    miles = km * K2M_CONV_FACTOR
    
    print(format(km, ',.2f'), 'kilometers =', format(miles, ',.2f'), 'miles.')
                       
# This is the end of def show_miles():


main() 

#end of program
