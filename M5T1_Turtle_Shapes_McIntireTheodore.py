# CTI-110
# Module 5 Tutorial 1 Turtle Shapes
# Theodore McIntire
# 20 October 2017
# This program uses Turtle to draw a square and a triangle

import turtle  # Load the Turtle module

win = turtle.Screen()         # Creates a playground for Turtle
win.bgcolor("lightgreen")      # Set the window background color
win.title("Draw a Square (slowly) and a Triangle (fast)")      # Set the window title

s = turtle.Turtle()           # Create a Turtle, assign to s (square)
s.pensize(10)
s.color('purple')
s.shape("square")
s.speed(1)     # Slowest speed, options from 1-10
s.penup()
s.forward(100)
s.pendown()
for i in range (4):      #use for loop to draw square
    s.forward(100)
    s.left(90)
    
t = turtle.Turtle()           # Create a Turtle, assign to t (triangel)
t.pensize(10)
t.color('red')
t.shape("circle")
t.speed(10)     # Fastest speed, options from 1-10
t.penup()
t.forward(-200)
t.pendown()
for j in range (3):      #use for loop to draw triangle
    t.forward(100)
    t.left(120)




#end of program
