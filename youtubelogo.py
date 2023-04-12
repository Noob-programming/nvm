from turtle import *

t = Turtle()

t.speed(0)


# def co():
#     for i in range(180):
#         t.fd(1)
#         t.rt(1)


# t.fd(30)
# t.rt(90)
# t.fd(100)
# co()
# t.fd(100)
# t.rt(90)
# t.fd(30)

# t.rt(90)
# t.fd(100)
# for i in range(180):
#     t.fd(0.5)
#     t.lt(1)

# t.fd(100)


# head ^
# t.penup()
# t.setpos(30, 50)
# t.pendown()
# t.fd(30)
# t.lt(120)
# t.fd(100)
# t.lt(120)
# t.fd(100)
# t.lt(30)
# t.fd(30)
a = Screen()
a.setup(800, 600, 0, 0)
t.color("red")

t.setpos(-100, -100)
t.begin_fill()
for i in [300, 200]*2:
    t.fd(i)
    t.circle(30, 90)
t.end_fill()
t.penup()
t.goto(20, -20)
t.pendown()
t.color("white")
t.begin_fill()
for i in [30, 120, 120]:
    t.lt(i)
    t.fd(100)
t.end_fill()
t.hideturtle()

done()
