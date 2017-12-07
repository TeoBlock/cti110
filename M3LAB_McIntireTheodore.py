# CTI-110
# Module 3 Lab
# Theodore McIntire
# 26 September 2017
# This LAB completes and debuggs a program provided by the instructor
    # This program takes a number grade and outputs a letter grade.
    # system uses 10-point grading scale
A_score = 90
B_score = 80
C_score = 70
D_score = 60
    # The scores have been defined and below 60 is an F

#def main() used the nested if-else method
def main():    
    score = float(input('Enter numerical grade from 0 to 100: '))
    if score >= A_score:
        print('Your letter grade is: A')
    else:
        if score >= B_score:
            print('Your letter grade is: B')
        else:
            if score >= C_score:
                print('Your letter grade is: C')
            else:
                if score >= D_score:
                    print('Your letter grade is: D')   
                else:
                    print('Your letter grade is: F')
    # This finishes the code for this method 

#def alt() used the nested if-else method
def alt():    
    score = float(input('Enter numerical grade from 0 to 100: '))
    if score >= A_score:
        print('Your letter grade is: A')
    elif score >= B_score:
        print('Your letter grade is: B')
    elif score >= C_score:
        print('Your letter grade is: C')
    elif score >= D_score:
        print('Your letter grade is: D')   
    else:
        print('Your letter grade is: F')
    # This finishes the code for this method 
# program start - the methods are alternated to test/compare code
main()
alt()
main()
alt()
main()
alt()
main()
alt()
main()
alt()
# end program
