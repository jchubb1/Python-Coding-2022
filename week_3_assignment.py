# This is a program for week 3 assignment by Jamal Chubb
# Create a Python program that uses Turtle to draw the diagram exactly
# like it is in the pic. Note: it must be exact to recieve any points.

from turtle import *

# Do inputting here...

shape('turtle')

# Do processing here...


# Do outputting here...


# Draw outer square

pensize(5)
pencolor('red')
goto(300,0)
goto(300,300)
goto(0,300)
goto(0,0)
penup()

# Draw inner square

pensize(5)
pencolor('red')
goto(100,100)
pendown()
goto(200,100)
goto(200,200)
goto(100,200)
goto(100,100)
penup()

#Draw the dot at the center for the inner square

pensize(5)
pencolor('blue')
goto(150,150)
dot()
pendown()
hideturtle()
penup()

# Position the BLUE turtle (-100,-100) from the squares

pensize(5)
pencolor('blue')
goto(-100,-100)
showturtle()
left(90)
pendown()


done()