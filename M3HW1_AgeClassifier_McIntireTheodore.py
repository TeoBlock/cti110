# CTI-110
# Module 3 Homework 1
# Theodore McIntire
# 03 October 2017
# This program gets user input as person's age and outputs infant, child, teen or adult

# system identifies the lower limit for each age range
A_age = 20
T_age = 13
C_age = 1
# The lower range of ages have been defined and below one year old is I (Infant)

#def main() used the nested if-else method
def main():    
    age = float(input('Enter the age of the person in years: '))
    if age >= A_age:
        print('This person is an adult')
    elif age >= T_age:
        print('This person is a teen')
    elif age > C_age:
        print('This person is a child')
    else:
        print('This person is an infant')
    # This finishes the code for this method

'''
#def alt() outline for using the nested if-else method
def alt():    
    age = float(input('Enter the age of the person in years: '))
    if age >= A_age:
        print('This person is an adult')
    else:
        if age >= T_age:
            print('This person is a teen')
        else:
            if age > C_age:
                print('This person is a child')
            else:
                print('This person is an infant')
# This finishes the code for this method 
'''
    
# program start - multiple methods are alternated to test/compare code
main()

main()

main()

main()

main()

# end program
