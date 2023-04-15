from turtle import *

t = Turtle()
t.speed(0)
t.rt(45)

for i in range(62):
    if 7 < i < 62:
        t.left(5)
    # if 80 < i < 133:
    #     t.rt(5)

    if i < 62:
        t.fd(5)
    # else:
    #     t.fd(5)
t.fd(50)
t2 = Turtle()
t.speed(0)
t2.lt(135)
for i in range(62):
    if 7 < i < 62:
        t2.left(5)
    # if 80 < i < 133:
    #     t.rt(5)

    if i < 62:
        t2.fd(5)
    else:
        t2.fd(5)

t2.left(20)
t2.fd(50)
done()

'''
# Importing turtle
import turtle

# Forming a Screen
wd = turtle.Screen()
wd.bgcolor("White")
wd.title("Logo - Coding Ninjas")


#Initialising the turtle object
tt = turtle.Turtle()

# Setting pen for drawing the circle
tt.color("Orange")
tt.width(32)

# Drawing the C shape of the logo
tt.backward(60)
for x in range(180):
    tt.backward(1)
    tt.right(1)
tt.backward(60)

# Setting pen for drawing the eyes
tt.color("Black")
tt.width(5)

# Positioning the pen to draw left eye
tt.up()
tt.left(90)
tt.forward(45)
tt.right(90)
tt.forward(80)

#Drawing the left Eye
tt.down()
tt.left(75)
tt.begin_fill()
tt.circle(15,180)
tt.end_fill()
tt.hideturtle()

#Repositioning for the right eye
tt.up()
tt.right(75)
tt.forward(20)

# Drawing the right eye
tt.down()
tt.right(75)
tt.begin_fill()
tt.circle(15,180)
tt.end_fill()

# Finish by turtle.done() command
turtle.done()
'''