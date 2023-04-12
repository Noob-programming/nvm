# import colorgram
#
# color = colorgram.extract('image.jpg', 50)
# a = []
# for i in color:
#     a.append((i.rgb.r, i.rgb.g, i.rgb.b))

# print(a)
import random
import turtle
var = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
       (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43,
                                                       35), (145, 178, 149), (14, 98, 70), (232, 176, 165),
       (160, 142, 158), (54, 45, 50), (101, 75, 77), (183,
                                                      205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
       (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127,
                                                    153), (176, 192, 208), (168, 99, 102), (66, 64, 60),
       (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]


t = turtle.Turtle()
turtle.colormode(255)


t.speed(0)

t.penup()

t.setposition(-180, -200)

for _ in range(1, 11):
    for i in range(10):
        t.dot(20, random.choice(var))
        t.forward(50)
    t.setposition(-180, -200+(30*_))
t.hideturtle()
turtle.done()
