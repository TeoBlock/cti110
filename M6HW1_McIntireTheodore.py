# User inputs five test scores and program outputs letter grades and average
# 21 November 2017
# CTI-110 M6HW1 - Test Average and Grade
# Theodore McIntire

def main():
    print('In this program User inputs five test scores.')
    print('Afterwards the program outputs the letter grades and average of all test scores')
    print('')
    
    iteration = 0
    running_total = 0
    
    test = range(1,6)   
    for count in test:
        num_grade = float(input('Enter numerical grade from 0 to 100:     '))
        determine_grade(num_grade)

        iteration = iteration + 1  #note-count could be used instead of iteration
        running_total = running_total + num_grade

        if iteration == 5: #With this if... average is only printed after all 5 numbers entered
            print('') #Inserts an empty line between previous input/output and average
            calc_average(running_total, iteration) #note-count could be used instead of iteration
# This finishes the code for this main method      


#def cal_average()  calculates average by dividing sum of values in a set by number of values in the set
def calc_average(sum_values, num_values):
    avg = sum_values / num_values
    print('------------------------------------------------------')
    print('The current average is', '\t', '\t', '\t', avg)
    determine_grade(avg)
    print('------------------------------------------------------')
# This finishes the code for this method
    

#def determine_grade() uses the nested if-else method from M3LAB - with input removed to main method
def determine_grade(score):
    # This module takes a number grade and outputs a letter grade.
    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
        
    if score >= A_score:
        print('Your letter grade is:', '\t', '\t', '\t', 'A')
    elif score >= B_score:
        print('Your letter grade is:', '\t', '\t', '\t', 'B')
    elif score >= C_score:
        print('Your letter grade is:', '\t', '\t', '\t', 'C')
    elif score >= D_score:
        print('Your letter grade is:', '\t', '\t', '\t', 'D')   
    else:
        print('Your letter grade is:', '\t', '\t', '\t', 'F')
# This finishes the code for this method

    
# program start 
main()
