# CTI-110
# Module 5 Tutorial 1 Turtle Initials
# Theodore McIntire
# 20 October 2017
# This program uses Turtle to draw my initials

import turtle               # Load the Turtle module and allows us to use it

win = turtle.Screen()           # Creates a playground for Turtle
win.bgcolor("pink")             # Set the window background color
win.title("Initials for Theodore Blaise McIntire")      # Set the window title
turtle.speed(2)                 # Slowest speed, options from 1-10

turtle.pensize(7)
turtle.color('blue')
turtle.shape("circle")

turtle.penup()              #Make the T
turtle.forward(-250)
turtle.forward(50)
turtle.pendown()
turtle.left(90)
turtle.forward(100)
turtle.penup()  
turtle.left(90)
turtle.forward(50)
turtle.left(180)
turtle.down()
turtle.forward(100)
turtle.penup()  
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.stamp()              #Leave an impression on the canvas for the period


turtle.forward(100)         #Make the B
turtle.left(90)
turtle.pendown()
turtle.forward(100)
turtle.right(90)
turtle.forward(45)
for i in range(6):              #for loop to make a semi circle
    turtle.right(30)            #turn turtle
    turtle.forward(14)          #move turtle along
turtle.forward(31)
turtle.right(180)
turtle.forward(45)
for i in range(6):              #for loop to make a semi circle
    turtle.right(30)            #turn turtle
    turtle.forward(14)          #move turtle along
turtle.forward(31)
turtle.penup()
turtle.right(180)
turtle.forward(75)
turtle.stamp()              #Leave an impression on the canvas for the period

turtle.forward(100)         #Make the M
turtle.pendown()
turtle.left(90)
turtle.forward(100)
turtle.right(135)
turtle.forward(60)
turtle.left(90)
turtle.forward(60)
turtle.right(135)
turtle.forward(100)
turtle.left(90)
turtle.penup()
turtle.forward(15)
turtle.pendown()
turtle.stamp()              # Leave an impression on the canvas for the period

#end of program
