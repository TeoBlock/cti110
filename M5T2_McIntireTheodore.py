# CTI-110
# Module 5 Tutorial 2
# Theodore McIntire
# 12 October 2017
# This program totals the number of bugs collected in a week

#def main() uses a for loop
def main():

    # This program uses these variables
    # ? ? ? I DO NOT UNDERSTAND WHY THIS PROGRAM DOES NOT RUN
    # IF THESE VARIABLES ARE DEFINED OUTSIDE OF/ABOVE MAIN ? ? ?
    quantityPerDay = 0
    runningTotal = 0


    week = range(1, 8)
    for count in week:
        print('Day', count)
        quantityPerDay = int(input('Enter the number of bugs collected: '))
        runningTotal = runningTotal + quantityPerDay
        print ('On day', count, 'the number of bugs collected is', quantityPerDay, 'and subtotal is', runningTotal)
        print(' ')
    
    print("At the end of the week the total number of bugs collected is:", runningTotal)
# This finishes the code for this method

'''
#def alt() outline if needed
def alt():    

# This finishes the code for this method 
'''
    
# program start - multiple methods are run to test the code

main()

#end of program
