import turtle

t = turtle.Turtle()

t.speed(0)
for i in range(1, 4):
    t.fillcolor('cyan')
    t.begin_fill()
    for j in range(4):
        if j % 2 == 0:
            t.fd(300/i)
            t.left(90)
        else:
            t.fd(150/i)
            t.left(90)
    if i == 1:
        t.penup()
        t.goto(50, 50)
        t.pendown()
    if i == 2:
        t.penup()
        t.goto(75, 60)
        t.pendown()
    if i == 3:
        t.end_fill()


turtle.done()
