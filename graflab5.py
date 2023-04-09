from graphics import *

win = GraphWin("noob king", 600, 600)

circle = Circle(Point(300, 300), 200)
# circle.draw(win)  # .setFill("black")
# rectangle = Rectangle(Point(100, 100), Point(150, 200))

# rectangle.setFill("green")

# rectangle.draw(win)
Circle(Point(100, 250), 50).draw(win)  .setFill("gray")
Circle(Point(150, 250), 50).draw(win)   .setFill("cyan")
Circle(Point(200, 250), 50).draw(win)   .setFill("blue")
Circle(Point(250, 250), 50).draw(win)   .setFill("red")
Circle(Point(130, 310), 50).draw(win)   .setFill("pink")
Circle(Point(180, 310), 50).draw(win)   .setFill("yellow")
Circle(Point(230, 310), 50).draw(win)   .setFill("gray")

Line(Point(100, 100), Point(200, 300)).draw(win)
win.getMouse()
win.close()
