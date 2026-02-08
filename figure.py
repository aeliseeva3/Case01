# Case-study #1
# Developers: Eliseeva A., Kovalenko A., Leonva A.
#

import turtle

def rhombus(x, y, a, b):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('pink')
    turtle.begin_fill()
    b1 = 180 - b
    turtle.forward(a)
    turtle.left(b)
    turtle.forward(a)
    turtle.left(b1)
    turtle.forward(a)
    turtle.left(b)
    turtle.forward(a)
    turtle.left(b1)
    turtle.down()
    turtle.end_fill()

def parallelogram(x, y, a, b, c):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('purple')
    turtle.begin_fill()
    c1 = 180 - c
    turtle.forward(a)
    turtle.left(c)
    turtle.forward(b)
    turtle.left(c1)
    turtle.forward(a)
    turtle.left(c)
    turtle.forward(b)
    turtle.left(c1)
    turtle.down()
    turtle.end_fill()