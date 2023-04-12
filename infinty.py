from turtle import *

f = Turtle()
# f.speed(0)
# first angle
f.pensize(20)
f.pencolor("blue")
f.lt(30)
f.fd(50)
f.backward(80)
f.lt(120)
f.fd(50)
# -----------
# second angel + رجعه
f.rt(60)
f.fd(50)
f.rt(45)
f.fd(50)
f.rt(70)
f.fd(50)
f.lt(60)
f.backward(50)
f.fd(100)
# ---------
# therd angel بدون كسرة
f.rt(40)
f.rt(40)
f.fd(50)
f.rt(45)
# ------------
# final angel + كسرة
f.fd(50)
f.rt(55)
f.fd(50)
f.rt(45)
f.fd(40)

done()