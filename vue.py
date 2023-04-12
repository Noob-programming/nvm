from turtle import *

t = Turtle()

t.speed(0)


def line():
    t.fd(30)
    t.rt(120)


def newline():
    t.rt(120)
    t.fd(150)


# v small make
t.color("black")
t.begin_fill()
for i in range(6):
    if i % 2 == 1 and i < 4:
        t.fd(60)
    else:
        line()

for i in [300, 60]:
    t.setheading(i)
    t.fd(30)

t.setheading(0)
t.end_fill()

# v large
# -----------
t.fd(30)
t.fd(30)
t.color("green")
t.begin_fill()
newline()

newline()
for i, j in [(0, 30), (300, 90), (60, 90)]:
    t.setheading(i)
    t.fd(j)

t.end_fill()
t.hideturtle()
# --------------
done()
