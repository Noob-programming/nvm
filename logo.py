# import graphics as g
#
# win = g.GraphWin("logo", 800, 480)
# g.Rectangle(g.Point(0, 0), g.Point(800, 480)).draw(win).setFill("#a45bc2")
# mbox = g.Text(g.Point(170, 100), "Pycharm")
# mbox.draw(win).setSize(36)
# mbox1 = g.Text(g.Point(120, 150), "Professional")
# mbox1.draw(win)
# date = g.Text(g.Point(200, 150), "2022.1")
# date.draw(win).setStyle("bold")
# # mbox.setWidth(30)
# # mbox = mbox
# # mbox = mbox.setSize(30)
#
# win.getMouse()
# win.close()


import turtle
import random

# تعريف الألوان التي ستستخدمها في رسم الأشكال
colors = ["red", "blue", "green", "purple", "orange", "yellow"]


# تعريف دالة لرسم الأشكال
def draw_shape():
    # توليد عدد عشوائي لتحديد عدد الأضلاع في الشكل
    sides = random.randint(3, 8)
    # تحديد لون الشكل بشكل عشوائي
    color = random.choice(colors)
    # رسم الشكل
    turtle.color(color)
    turtle.begin_fill()
    for i in range(sides):
        turtle.forward(50)
        turtle.right(360 / sides)
        turtle.end_fill()


# تعريف دالة الرسم الرئيسية
def main():
    turtle.setup(600, 600)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.setpos(-200, 200)
    turtle.pendown()
    # رسم 20 شكلاً غير متصل
    for i in range(20):
        draw_shape()
        turtle.penup()
        turtle.forward(100)
        turtle.pendown()


# تشغيل البرنامج

if __name__ == "__main__":
    main()
    turtle.done()

#     حتى تعرفين شنو اسم ملف اذا تردين تستخدمين __name__
print(__name__)