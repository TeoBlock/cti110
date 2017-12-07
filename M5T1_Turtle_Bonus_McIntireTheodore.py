# CTI-110
# Module 5 Tutorial 1 Turtle Bonus
# Theodore McIntire
# 20 October 2017
# This program uses the Turtle Pologyon module to draw a snowflake


import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# add some display options
t.pensize(4)            # increase pensize (takes integer)
t.pencolor("red")     # set pencolor (takes string)
t.shape("turtle")

#commands from here to the last line can be replaced

# draw a N sided polygon
numSides = int(input("Enter a number between 4 and 9 for sides of the snowflake: "))
               
angle = 360 / numSides
sides = range(numSides)
# distance = 300 / numSides # try different values 
distance = 60
t.speed(10)

t.penup()       #This section moves the snowflake more towards the center
t.right(180)
t.forward(distance)
t.left(90)
t.forward(distance)
t.left(90)
t.pendown()

               
for i in sides:
    t.forward(distance)
    t.left(angle)

for i in sides:
    t.penup()
    t.forward(distance/2)
    t.right(90)
    t.pendown()
    t.forward(distance + numSides*10)
    t.left(90)
    t.penup()
    t.forward(-distance/2)
    t.pendown()
    for i in sides:
        t.forward(distance)
        t.left(angle)
    t.penup()
    t.forward(distance/2)
    t.left(90)
    t.forward(distance + numSides*10)
    t.right(90)
    t.forward(distance/2)
    t.left(angle)
    

# end commands
win.mainloop()             # Wait for user to close window
