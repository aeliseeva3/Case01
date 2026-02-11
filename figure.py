# Case-study #1
# Developers: Eliseeva A., Kovalenko A., Leonva A.
#

import turtle
import math

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
    turtle.down()
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.forward(a)
    h=math.sqrt(b**2-(a/2)**2)
    angle=math.degrees(math.atan2(h, a/2))
    turtle.left(180-angle)
    turtle.forward(b)
    turtle.left(2*angle)
    turtle.forward(b)
    turtle.end_fill()
    turtle.left(180-angle)

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
    turtle.setposition(x,y)
    turtle.down()
    turtle.fillcolor('orange')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    h=math.sqrt(a**2+b**2)
    angle=math.degrees(math.atan2(b,a))
    turtle.left(90+angle)
    turtle.forward(h)
    turtle.end_fill()

def dog():
    '''
    dog function.
    :return: None
    '''
    square(-150,-300,50)
    square(100,-300,50)
    rectangle(-150,-190,300,110)
    rectangle(-200,-140,100,50)
    triangle_ravnostoron(-150,-140,50)
    triangle_ravnobedren(100,-190,100,75)


def bird():
    '''
    Bird function.
    :return: None
    '''
    square(200,0, 25)
    turtle.right(90)
    triangle_pryamougoln(250,100,100,50)
    triangle_ravnobedren(250,100,50, 25)
    turtle.right(90)
    parallelogram(250, 100, 50, 25, 65)
    turtle.done

def candle():
    turtle.setheading(270)
    triangle_ravnobedren(300, -100, 200, 260)
    turtle.setheading(0)
    triangle_pryamougoln(300, -300, 240,100 )
    turtle.setheading(90)
    triangle_pryamougoln(540, -200, 100,240 )
    turtle.setheading(60)
    rhombus(420,-100, 50, 60)

#if __name__ == '__main__':
#dog()
#bird()

dog()
candle()