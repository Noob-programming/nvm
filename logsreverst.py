from turtle import *

t= Turtle()
t.pensize(5)
t.speed(0)


def i2():
    t.fd(50)
    t.lt(90)
    t.fd(50)


# angel 1
i2()

t.penup()
t.fd(30)
t.pendown()
# angel 2
i2()
t.penup()
t.fd(30)
t.pendown()
# angel 3
i2()
t.penup()
t.fd(30)
t.pendown()
# angel 4
i2()

t.pencolor("blue")
def xline():
    t.fd(40)
    t.penup()
    t.fd(30)
    t.pendown()
    t.fd(40)


t.penup()
t.setposition(-70, 55)
t.pendown()

xline()
t.penup()
t.setposition(-70, 65)
t.pendown()
xline()



def yline():
    t.fd(30)
    t.penup()
    t.fd(40)
    t.pendown()
    t.fd(30)


t.penup()
t.setposition(-20, 120)
t.pendown()
t.rt(90)
yline()
t.penup()
t.setposition(-10, 120)
t.pendown()
yline()

t.penup()
t.setposition(-105, 130)
t.pendown()

done()