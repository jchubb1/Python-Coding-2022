# This is a program for the second week assignment by Jamal Chubb
# Create a Python program that uses Turtle to draw the diagram
# exactly like it is in the pic. Note: it must be exact to 
# receive any points

from turtle import *

# Do inputting here...


# Do processing here...


# Do outputting here...


# Draw rectangle of traffic light

setup(480,840)
pensize(5)
pencolor('black')
goto(100,0)
goto(100,300)
goto(0,300)
goto(0,0)
penup()

#Draw traffic circles

pensize(5)
pencolor('black')
goto(50,30)
pendown()
fillcolor('green')
begin_fill()
circle(30)
end_fill()
penup()



pensize(5)
pencolor('black')
goto(50,120)
pendown()
fillcolor('yellow')
begin_fill()
circle(30)
end_fill()
penup()



pensize(5)
pencolor('black')
goto(50,210)
pendown()
fillcolor('red')
begin_fill()
circle(30)
end_fill()
penup()






done()