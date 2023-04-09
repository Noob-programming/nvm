from turtle import *


t = Turtle()

bgcolor('black')

t.pensize(2)


def cav():
    for i in range(200):
        t.right(1)
        t.forward(1)


t.speed(0)

t.color('pink', 'red')

t.begin_fill()
t.left(140)
t.forward(111.65)
cav()
t.left(120)

cav()
t.fd(111.65)
t.end_fill()

done()
