from turtle import *


t = Turtle()
t.speed(0)
t.pensize(5)
t.color('gray')
# t.fillcolor('blue')
# t.begin_fill()
for j in range(5):
    t.fd(100)
    t.penup()
    t.fd(60)
    t.pendown()
    t.fd(100)
    t.left(144)

# t.end_fill()
done()
