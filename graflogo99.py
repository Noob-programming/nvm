from graphics import *

win = GraphWin("noob king", 600, 600)

# Circle large
Circle(Point(300, 300), 200).draw(win).setWidth(5)
Circle(Point(300, 300), 200).draw(win).setFill("gray")

Circle(Point(200, 200), 50).draw(win).setWidth(5)
Circle(Point(400, 200), 50).draw(win).setWidth(5)
Circle(Point(200, 400), 50).draw(win).setWidth(5)
Circle(Point(400, 400), 50).draw(win).setWidth(5)
Circle(Point(150, 300), 50).draw(win).setWidth(5)
Circle(Point(450, 300), 50).draw(win).setWidth(5)
Circle(Point(300, 150), 50).draw(win).setWidth(5)
Circle(Point(300, 450), 50).draw(win).setWidth(5)

Line(Point(200, 250), Point(300, 300)).draw(win).setArrow("first")
Line(Point(400, 250), Point(300, 300)).draw(win).setArrow("first")
Line(Point(200, 350), Point(300, 300)).draw(win).setArrow("first")
Line(Point(400, 350), Point(300, 300)).draw(win).setArrow("first")


Line(Point(200, 300), Point(400, 300)).draw(win).setArrow("both")
Line(Point(300, 200), Point(300, 400)).draw(win).setArrow("both")


# width
Line(Point(200, 250), Point(300, 300)).draw(win).setWidth(5)
Line(Point(400, 250), Point(300, 300)).draw(win).setWidth(5)
Line(Point(200, 350), Point(300, 300)).draw(win).setWidth(5)
Line(Point(400, 350), Point(300, 300)).draw(win).setWidth(5)
Line(Point(200, 300), Point(400, 300)).draw(win).setWidth(5)
Line(Point(300, 200), Point(300, 400)).draw(win).setWidth(5)


# Circle min
Circle(Point(200, 200), 25).draw(win).setWidth(5)
Circle(Point(200, 200), 25).draw(win).setWidth(5)
Circle(Point(400, 200), 25).draw(win).setWidth(5)
Circle(Point(200, 400), 25).draw(win).setWidth(5)
Circle(Point(400, 400), 25).draw(win).setWidth(5)
Circle(Point(150, 300), 25).draw(win).setWidth(5)
Circle(Point(450, 300), 25).draw(win).setWidth(5)
Circle(Point(300, 150), 25).draw(win).setWidth(5)
Circle(Point(300, 450), 25).draw(win).setWidth(5)
# circle color

Circle(Point(200, 200), 25).draw(win).setFill("gold")
Circle(Point(200, 200), 25).draw(win).setFill("gold")
Circle(Point(400, 200), 25).draw(win).setFill("gold")
Circle(Point(200, 400), 25).draw(win).setFill("gold")
Circle(Point(400, 400), 25).draw(win).setFill("gold")
Circle(Point(150, 300), 25).draw(win).setFill("gold")
Circle(Point(450, 300), 25).draw(win).setFill("gold")
Circle(Point(300, 150), 25).draw(win).setFill("gold")
Circle(Point(300, 450), 25).draw(win).setFill("gold")

win.getMouse()
win.close()
