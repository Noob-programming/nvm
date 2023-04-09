from turtle import *

import random


def colors():
    return (random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255))


t = Turtle()

t.speed(0)
colormode(255)
bgcolor((0, 0, 0))
t.pensize(2)
t.right(45)
for i in range(360):
    # t.left(45)
    bgcolor(colors())
    t.color(colors())
    t.fd(i)
    t.lt(90)

done()
