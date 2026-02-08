# Case-study #1
# Developers: Eliseeva A., Kovalenko A., Leonva A.
#
import math
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


def triangle_ravnostoron(x, y, a):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.fillcolor('green')
    turtle.begin_fill()
    for n in range(3):
        turtle.forward(a)
        turtle.left(120)
    turtle.end_fill()

def triangle_ravnobedren(x, y, a, b):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.left(150)
    turtle.forward(b)
    turtle.left(150)
    turtle.forward(b)
    turtle.end_fill()


def square(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('blue')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()

def rectangle(x, y, a, b):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.right(90)
    turtle.end_fill()

def triangle_pryamougoln(x, y, a, b, c):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('orange')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    c=math.sqrt(a**2 + b**2)
    turtle.right(120)
    turtle.forward(c)
    turtle.end_fill()

