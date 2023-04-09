import turtle

# Creating turtle
# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor("black")
# t.pencolor("red")
# a = 0
# b = 0
# t.speed(0)
# t.penup()
# t.goto(0, 200)
# t.pendown()
# while (True):
#     t.forward(a)
#     t.right(b)
#     a += 3
#     b += 1
#     if b == 360:
#         break
#     t.hideturtle()

# 3d box
# t = turtle.Turtle()
# t2, t3, t4 = turtle.Turtle(), turtle.Turtle(), turtle.Turtle()
# t.speed(0), t2.speed(0), t3.speed(0), t4.speed(0)
# a = 10
# for i in range(20):
#     for j in range(4):
#         t.fd(a)
#         t.left(90)
#         t2.fd(a)
#         t2.right(90)
#         t3.left(270)
#         t3.fd(a)
#         t4.right(270)
#         t4.fd(a)
#
#     a += 10

color = ['red', 'blue', 'green', 'cyan', 'gray']
t = turtle
t.speed(0)
t.pensize(4)
a = 0

# star*


def DrawShape():
    global a
    for j in range(5):
        t.color(color[j % 5])
        t.fd(a)
        t.left(145)

        a += 2
    return None


# * 9 star

# def DrawShape():
#     global a
#     for j in range(8):
#         t.color(color[j % 5])
#         t.fd(a)
#         t.left(160)

#         a += 2
#     return None


for i in range(50):
    DrawShape()

turtle.done()
