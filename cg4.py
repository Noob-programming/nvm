
# red circle
import turtle
# screen = turtle.Screen()
# screen.setup(320, 320)
# screen.title("new one")
# t = turtle.Turtle()

# t.setheading(90)
# t.pencolor("red")
# t.speed(0)

# for i in range(25):
#     t.penup()
#     t.setpos(0, 0)
#     t.pendown()
#     t.circle(50)
#     t.penup()
#     t.setheading(i * 15)

# turtle.done()

# squr red

# screen = turtle.Screen()
# screen.setup(320, 320)
# t = turtle.Turtle()
# t.setheading(90)
# t.pencolor('red')
# t.speed(0)


# def square(side):
#     for i in range(4):
#         t.fd(side)
#         t.rt(90)


# for i in range(19):
#     t.penup()
#     t.setpos(0, 0)
#     t.pendown()
#     square(80)
#     t.penup()
#     t.setheading(i * 20)


# turtle.done()


# circle

import random
screen = turtle.Screen()
turtle.bgcolor('black')
screen.setup(480, 320)
screen.title("new one")
t = turtle.Turtle()
t.speed(0)
color_list = ['red', 'green', 'blue', 'black', 'purple']
for i in range(5):
    t.setpos(0, 0)
    t.hideturtle()
    t.penup()
    t.pencolor(random.choice(color_list))
    t.setheading(90)
    t.pendown()
    t.circle(20*(i+1))
    t.pencolor(random.choice(color_list))
    t.circle(-20 * (i + 1))


turtle.done()
