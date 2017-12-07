# CTI-110
# Module 3 Homework 2
# Theodore McIntire
# 5 October 2017
# This program factors in discounts and calculates total cost for software package sales

# This program uses three variables
quantity = 0
discount = 0
costTotal = 0

#def main() uses the if-elif-else method
def main():    
    print ('The software package you want to buy retails for $99 and there are quantity discounts.')
    print ('Quantity 10-19:  10% discount')
    print ('Quantity 20-49:  20% discount')
    print ('Quantity 50-99:  30% discount')
    print ('Quantity 100+:   40% discount')

    quantity = int(input('Enter the number of software packages you want to purchase: '))
    if quantity >= 100:
        costTotal = quantity * 99 * 0.6
    elif quantity >= 50:
        costTotal = quantity * 99 * 0.7
    elif quantity  >= 20:
        costTotal = quantity * 99 * 0.8 
    elif quantity >= 10:
        costTotal = quantity * 99 * 0.9 
    else:
        costTotal = quantity * 99 * 1.0 

    discount = ((quantity * 99) - costTotal)     
    print ('For', format(quantity, ',.0f'), 'copies of the software your discounts is $', format(discount, ',.2f'))
    print ('Your total cost after discounts is $', format(costTotal, ',.2f'))
    print ('Thank you and come again.')
    print ('')
    # A blank line is inserted for ease of reading when multiple methods are being tested
    # This finishes the code for this method

'''
#def alt() outline if needed
def alt():    

# This finishes the code for this method 
'''
    
# program start - multiple methods are run to test the code
main()

main()

main()

main()

main()

main()

# end program
