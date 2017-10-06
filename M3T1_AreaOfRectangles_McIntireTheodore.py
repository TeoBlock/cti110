# CTI-110
# Module 3 Tutorial 1
# Theodore McIntire
# 05 October 2017
# This program gets user input and then outputs which rectangle has the greater area

# variables for rectangle 1 and 2 length and width 
length1 = 0
width1 = 0
area1 = 0
length2 = 0
width2 = 0
area2 = 0
# initial variable values are set to zero

#def main() to get user inputs, calculate areas and compare areas using the nested if-else method
def main():    
    print ('This program gets user input and then outputs which rectangle has the greater area.') 
    length1 = float(input('Enter the length of the 1st rectangle: '))
    width1 = float(input('Enter the width of the 1st rectangle: '))
    area1 = length1 * width1
    print ('The area of the first rectangle is ', format(area1, ',.2f'))
    print ()
    length2 = float(input('Enter the length of the 2nd rectangle: '))
    width2 = float(input('Enter the width of the 2nd rectangle: '))
    area2 = length2 * width2
    print ('The area of the second rectangle is ', format(area2, ',.2f'))
    print ()
 
    if area1 > area2:
        print('The first rectangle has the greater area')
    elif area1 < area2:
        print('The second rectangle has the greater area')
    elif area1 == area2:
        print('The two rectangles have the same area')
    else:
        print('This program is messed up - complain to person who coded it...')
    print ()
    print ()
    # This finishes the code for this method

'''
#def alt() outline for using the nested if-else method
def alt():    

'''
    
# program start - multiple methods are alternated to test/compare code

main()

main()

main()

main()

# end program
