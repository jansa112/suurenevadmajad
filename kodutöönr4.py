#Suurenevad majad
#Jaanus Paasoja
#ITT20
#25.03.2021
from turtle import *
import turtle
speed(10)
shape("turtle")
pensize(4)
aken=turtle.Screen()
aken.setup(1280,720)
x=-400
y=0
a= 50
b=15
c=20
d=25
penup()
setpos(x,y)
#maja
for i in range(4):
    pencolor("black")
    pendown()
    forward(a)
    right(90)
#katus
for i in range(2):
       pencolor("green")
       right(120)
       backward(a)
#uks
pencolor("red")
penup()
left(150)
forward(a)
right(90)
forward(b)
right(90)
pendown()
forward(c)
left(90)
forward(b)
left(90)
forward(c)
for i in range (5):
    penup()
    x=x+150
    y=y+6
    setpos(x,y)
    a=a*1.12
    b=b*1.12
    c=c*1.12
    d=d*1.12
    setheading(0)
    pendown()
    for i in range(4):
        pencolor("black")
        pendown()
        forward(a)
        right(90)
    #katus
    for i in range(2):
       pencolor("green")
       right(120)
       backward(a)
    #uks
    pencolor("red")
    penup()
    left(150)
    forward(a)
    right(90)
    forward(b)
    right(90)
    pendown()
    forward(c)
    left(90)
    forward(b)
    left(90)
    forward(c)
hideturtle()
exitonclick()


