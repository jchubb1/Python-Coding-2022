# This is a demonstration of Turtle Graphics Library
import turtle  # Normal turtle
from turtle import * # Import so that you dont have to use "turtle." everytime

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.right(45)
turtle.forward(100)


turtle.forward(50)
turtle.setheading(90)
turtle.forward(100)
turtle.setheading(180)
turtle.forward(50)
turtle.setheading(270)
turtle.forward(100)

# spaces and lines

LINE= 150
SPACE= 15

turtle.forward(LINE)
turtle.penup()
turtle.forward(SPACE)
turtle.pendown()
turtle.forward(LINE)
turtle.penup()
turtle.forward(SPACE)
turtle.penup()
turtle.forward(LINE)

circle

turtle.circle(100)

# Working with turtle color and window size

turtle.setup(1024,1024)
turtle.bgcolor('green')
turtle.pensize(5)
turtle.pencolor('DarkGrey')
turtle.circle(100)


turtle.color('red','yellow')
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(pos()) < 1:
        break
turtle.end_fill()

# Working with coordinates.

turtle.shape('turtle')
turtle.hideturtle()
turtle.speed(1)
turtle.goto(0,100)
turtle.showturtle()
turtle.goto(100,0)
turtle.goto(0,0)

# Display text on the GUI

turtle.write('Hello world from my turtle program')

bgcolor('purple')
turtle.pensize(5)
turtle.pencolor('green')
turtle.circle(100)
turtle.hideturtle()
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

# Keep program window open after it runs




done()

