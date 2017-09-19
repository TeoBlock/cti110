# CTI-110
# M2HW2 - Tip Tax Total 
# Theodore McIntire
# 19 September 2017
#This program takes the cost of the meal and Cupon Discount and calculates the tip, tax and total cost

#Declare variables and set their values to zero
#This updated version of the program allows for use of a discount coupon
mealCost = 0
tipValue = 0
salesTax = 0
totalBill = 0
cuponDiscount = 0
discountPercentage = 0

#Declare CONSTANTS and identify their values
TIP_RATE = 0.18
TAX_RATE = 0.07


#An introduction is provided to explain the purpose of this program
print ("Now that your belly is full this program will help calculate your total bill")

#Get the charge for the food (input) from the user
mealCost = float(input("Enter your Meal Cost:  $", ))

#Get the cuopon discount (input) from the user
cuponDiscount = float(input("Enter any Cupon Discount percentage:  %", ))

#Enter a response to confirm receipt of user input and to separate user input from results 
print ("Thank You")

#variables are calculated based on entered mealCost, cuponDiscount and known CONSTANTS
#for ease of calculation and to use exisitng program structure discountPercentage is calculated
discountPercentage = 1 - cuponDiscount/100

tipValue = mealCost * discountPercentage * TIP_RATE

salesTax = mealCost * discountPercentage * TAX_RATE

totalBill = mealCost * discountPercentage + tipValue + salesTax

#The results are provided to the user

print ("You entered that your Meal Cost is $", format(mealCost, ',.2f'))

print ("You entered that your Cupon Discount percentage is %", format(cuponDiscount, ',.0f'))

print ("Your Discounted Food Cost is $", format(mealCost * discountPercentage, ',.2f'))

print ("Your Tip of 18% should be $", format(tipValue, ',.2f'))

print ("Your Tax of 7% is $", format(salesTax, ',.2f'))

print ("Your Total Bill is $", format(totalBill, ',.2f'))

#end of program
