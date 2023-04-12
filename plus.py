from turtle import *

t = Turtle()

t.penup()
t.setpos((0, -70))
t.pendown()


t.speed(0)
t.fillcolor("green")
t.begin_fill()
t.circle(150)
t.end_fill()
t.penup()
t.setpos(-30, 0)
t.pendown()
t.lt(30)
t.fd(130)
t.lt(120)
t.fd(130)
t.lt(120)
t.fd(130)

t.penup()
t.setpos(-40, 26)
t.pendown()
t.setheading(0)
t.lt(30)
t.fd(80)
t.lt(120)
t.fd(80)
t.lt(120)
t.fd(80)


t.penup()
t.setpos(0, -100)
t.pendown()
t.hideturtle()
t.write(arg="pluralsight")

done()
