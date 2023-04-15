from turtle import *
t = Turtle()
t.goto(-100, 0)
t.fd(300)
t.circle(30, 90)

t.fd(200)
t.lt(90)

t.fd(400)
t.lt(90)

t.fd(200)
t.circle(30, 90)
t.fd(40)

t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()
t2.penup()
t2.goto(50, 50)
t2.pendown()

t3.penup()
t3.goto(0, 50)
t3.pendown()

t4.penup()
t4.goto(50, 100)
t4.pendown()

t5.penup()
t5.goto(0, 100)
t5.pendown()


t2.fillcolor("yellow")
t2.begin_fill()
for i in range(4):
    t2.fd(40)
    t2.left(90)
t2.end_fill()

t3.fillcolor("blue")
t3.begin_fill()
for i in range(4):
    t3.fd(40)
    t3.left(90)
t3.end_fill()

t4.fillcolor("green")
t4.begin_fill()
for i in range(4):
    t4.fd(40)
    t4.left(90)
t4.end_fill()


t5.fillcolor("red")
t5.begin_fill()
for i in range(4):
    t5.fd(40)
    t5.left(90)
t5.end_fill()


done()
