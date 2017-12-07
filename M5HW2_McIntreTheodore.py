# CIT-110
# Theodore McIntire
# 12 October 2017
# This program takes user input positive numbers and outputs a total



def main():
    
# variable defined
# program does not run if variables defined outside/above def main():
    number = 0
    total = 0
    
    while number >= 0:
        number = float(input('Enter a number ? '))
        total = total + number

# below if statement required
# to ensure the negative number is not added to the total
        if number < 0:
            total = total - number
            
    print ('Total: ', format(total, ',.2f'))

# This is the end of def main():

main()

#end of program
