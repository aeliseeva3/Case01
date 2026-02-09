# Case-study #1
# Developers: Eliseeva A., Kovalenko A., Leonva A.
#

import turtle

def rhombus(x, y, a, b):
    '''
    Function, drawing rhombus.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a rhombus
    :param b: the degree measure of one of the angles of a rhombus
    :return: None
    '''
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
    '''
    Function, drawing parallelogram.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: the length of one side of a parallelogram
    :param b: the length of second side of a parallelogram
    :param c: the degree measure of one of the angles of a parallelogram
    :return: None
    '''
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
    '''
    Function, drawing triangle_ravnostoron.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a triangle_ravnostoron
    :return: None
    '''
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
    '''
    Function, drawing triangle_ravnobedren.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: the length of one side of a triangle_ravnobedren
    :param b: the length of second side of a triangle_ravnobedren
    :return: None
    '''
    turtle.up()
    turtle.goto(x, y)
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.down()
    turtle.goto(x+a, y)
    turtle.goto(x+a/2, y+b)
    turtle.end_fill()
    turtle.goto(x, y)

def square(x, y, a):
    '''
    Function, drawing square.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a square
    :return: None
    '''
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
    '''
    Function, drawing rectangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: the length of one side of a rectangle
    :param b: the length of second side of a rectangle
    :return: None
    '''
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

def triangle_pryamougoln(x, y, a, b):
    '''
    Function, drawing triangle_pryamougoln.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: the length of one side of a triangle_pryamougoln
    :param b: the length of second side of a triangle_pryamougoln
    :return: None
    '''
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor('orange')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.goto(x, y)
    turtle.left(90)
    turtle.end_fill()

