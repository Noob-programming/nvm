from turtle import *
import random


def colors():

    return (random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255))


t = Turtle()
colormode(255)
t.speed(0)
for i in range(36):
    t.fillcolor(colors())
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.left(10)


done()
