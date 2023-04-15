from turtle import *

t = Turtle()
# t.speed(0)
# t.penup()
# t.goto(-100, -100)
# t.pendown()
for i in [300, 200]*2:
    t.fd(i)
    t.circle(30, 90)

t.penup()
t.goto(150, 100)
t.pendown()
t.circle(30, 180)

done()