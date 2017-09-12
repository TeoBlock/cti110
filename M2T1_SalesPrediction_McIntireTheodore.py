# CTI-110 
# M2T1 - Sales Prediction
# Theodore McIntire
# 12 Sep 2017
#This is the exercise for reading input from keyboard to calculate profit

#An introduction is provided to explain the purpose of this program
print("Hi Mr./Mz. Hardworker and welcome to the online profit calculator!")

#Get the projected total sales (input) from the user
total_sales = float(input("Enter the sales you are projecting:  $"))

# Calculate the profit (process) which equals 23% of the total sales
profit = total_sales * 0.23

#Display the profit (output) calculated in the above line
print("The profit from your projected sales is $", format(profit, ',.2f'))

#The user is invited to run further iterations of the program
print("Run the program again to calculate a profit from projected sales.")
