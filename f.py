import random
import turtle


def rgb():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


t = turtle.Turtle()
# t2 = turtle.Turtle()
# t3, t4 = turtle.Turtle(), turtle.Turtle()
t.speed(0)
# , t2.speed(0), t3.speed(0), t4.speed(0)
#
# turtle.color('#000000')
# re = [0, 90, 180, 270]
turtle.colormode(255)
#
# # t.pensize(5) for _ in range(50): t.color(rgb()), t2.color(rgb()), t3.color(rgb()), t4.color(rgb()) t.forward(30),
# t2.forward(30), t3.forward(30), t4.forward(30) t.setheading(random.choice(re)), t2.setheading(random.choice(re)),
# t3.setheading(random.choice(re)), t4.setheading( random.choice(re))


def draw_circle(size):
    for i in range(int(360/size)):
        t.color(rgb())
        t.circle(100)
        t.setheading(t.heading()+size)


draw_circle(50)

turtle.done()
