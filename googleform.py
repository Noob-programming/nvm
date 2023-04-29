from turtle import *

t = Turtle()
# bgcolor("purple")
t.speed(0)


def trn():
    t.fillcolor("white")
    t.begin_fill()
    for i in range(2):
        t.fd(200)
        t.lt(90)
        t.fd(30)
        t.lt(90)
    t.end_fill()


def regtangl():
    t.penup()
    t.setpos((-100, -50))
    t.pendown()
    t.fillcolor("purple")
    t.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            t.fd(350)
            t.lt(90)
        else:
            t.fd(250)
            t.lt(90)
    t.end_fill()


regtangl()

xcord = [(-50, 0), (-50, 50), (-50, 100)]
ycord = [(0, 0), (0, 50), (0, 100)]
t.speed(0)
for i in range(3):
    t.penup()
    t.setpos(ycord[i])
    t.pendown()
    trn()
    t.fillcolor("white")
    t.begin_fill()
    t.penup()
    t.setpos(xcord[i])
    t.pendown()
    t.circle(19)
    t.end_fill()


done()
