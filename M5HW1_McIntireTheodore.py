# CTI-110
# Module 5 Homework 1
# Theodore McIntire
# 12 October 2017
# This program gets inputs of speed and hours from the user,
# then this program calculates and displays distance traveled

#def main() uses a for loop

def main():

    #This program uses these variables
    count = 0
    hourInteger = 0
    hours = 0
    speed = 0
    distance = 0
    
    #print ('This program calculates distance traveled.')
    speed = float(input('What the speed of the vehicle in mph: '))
    hours = float(input('How many hours has it traveled: '))
    print ('Hour     Distance Traveled')
    print ('--------------------------')
    hourInteger = hours//1
    while count < hourInteger:
        count = count + 1
        distance = speed * count
        print (format(count, ',.1f'), '\t', format(distance, ',.1f'))

    # This if statement is included if hours does not equal a whole number 
    if count != hours:
        distance = speed * hours
        print (hours, '\t', format(distance, ',.2f'))
    print(' ')
    
# end of def main()
main()
main()
# end of program
        
