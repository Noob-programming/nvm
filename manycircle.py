import turtle


t = turtle.Turtle()
t.speed(0)
color_list = ['red', 'green', 'blue', 'black', 'purple']
for i in range(5):
    t.setpos(0, 0)
    t.hideturtle()
    t.penup()
    t.pencolor(color_list[i % 5])
    t.setheading(90)
    t.pendown()
    t.circle(20*(i+1))
    t.pencolor(color_list[i % 5])
    t.circle(-20 * (i + 1))
    t.setheading(180)
    t.pencolor(color_list[i % 5])
    t.circle(-20 * (i + 1))
    t.pencolor(color_list[i % 5])
    t.circle(20 * (i + 1))


turtle.done()
