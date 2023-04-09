import turtle
import math

# t = turtle.Turtle()

# for _ in range(4):
#     t.fd(100)
#     t.left(90)

# c = int(math.sqrt(math.pow(100, 2)+math.pow(100, 2))/2)

c = int(((100) ** 2+(100) ** 2) ** 0.5)

print(c)
# t1 = turtle.Turtle()

# # print(c)

# for _ in range(3):
#     t1.fd(100)
#     t1.left(90)
#     if _ == 1:
#         t1.left(45)
#         t1.fd(45)


t2 = turtle.Turtle()


# t2.backward(100)
# t2.right(90)

# t2.fd(100)
# t2.left(135)
# t2.fd(c)
# t2.right(135)

turtle.bgcolor('black')

t2.pencolor('cyan')
t2.speed(0)
for j in range(8):
    for i in range(4):
        t2.left(45)
        t2.fd(100)

        t2.right(135)
    t2.left(135)


# def draw(a):
#     return int(360/a)


# for i in range(3):
#     t2.fd(100)
#     t2.left(draw(3))

turtle.done()
