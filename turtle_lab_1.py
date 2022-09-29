# This is a program for the Turtle Lab assignment #1

from turtle import *

shape('turtle')
pencolor('green')
fillcolor('green')

penup()
pensize(10)
pencolor('red')
goto(200,100)
pendown()
fillcolor('blue')
begin_fill()
circle(100)
end_fill()

pencolor('green')
fillcolor('green')

penup()
pensize(5)
pencolor('purple')
goto(-200,-200)
pendown()
fillcolor('orange')
begin_fill()
goto(0,-200)
goto(0,0)
goto(-200,0)
goto(-200,-200)
end_fill()

pencolor('green')
fillcolor('green')

penup()
pensize(15)
pencolor('brown')
goto(-200,300)
pendown()
fillcolor('grey')
begin_fill()
goto(-150,400)
goto(-50,400)
goto(0,300)
goto(-200,300)
end_fill()

pencolor('green')
fillcolor('green')

penup()
pensize(15)
goto(0,0)