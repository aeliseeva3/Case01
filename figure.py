# Case-study #1
# Developers: Eliseeva A., Kovalenko A., Leonva A.
#

import turtle
import math
turtle.setup(500,500)

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
    Dog function.
    :return: None
    '''
    triangle_pryamougoln(-150,-400,75, 75)
    turtle.setheading(0)
    triangle_pryamougoln(-75,-325,150,150)
    turtle.right(45)
    triangle_pryamougoln(0,-250,150,150)
    turtle.left(90)
    triangle_ravnobedren(-150,-250,100,65)
    turtle.setheading(0)
    square(0,-325,75)
    triangle_ravnobedren(75,-250,100,75)
    turtle.setheading(48)
    parallelogram(75,-250,75,75,42)
    turtle.setheading(0)

def bird():
    '''
    Bird function.
    :return: None
    '''
    square(-550, 50, 50)
    triangle_pryamougoln(-550,50,100,200)
    turtle.setheading(0)
    triangle_ravnobedren(-450, 250, 100, 75)
    turtle.setheading(180)
    parallelogram(-450, 250, 100, 50, 63)

def candle():
    '''
    Candle function.
    :return: None
    '''
    turtle.setheading(270)
    triangle_ravnobedren(300, -100, 200, 260)
    turtle.setheading(0)
    triangle_pryamougoln(300, -300, 240,100 )
    turtle.setheading(90)
    triangle_pryamougoln(540, -200, 100,240 )
    turtle.setheading(60)
    rhombus(420,-100, 60, 60)

def fish():
    '''
    Fish function.
    :return: None
    '''
    turtle.setheading(160)
    triangle_ravnostoron(300,150, 100)
    turtle.setheading(0)
    triangle_pryamougoln(300, 150, 120, 100)
    turtle.setheading(90)
    rectangle(420, 150, 100, 170)
    turtle.setheading(90)
    triangle_pryamougoln(590, 90, 60,50 )
    turtle.setheading(235)
    triangle_ravnobedren(520, 150, 100, 70)
    turtle.setheading(0)
    square(590, 170, 80)
    turtle.setheading(270)
    triangle_pryamougoln(590, 250, 80, 80)
    turtle.setheading(105)
    rhombus(570, 250, 60, 60)

def swan():
    '''
    Swan function.
    :return: None
    '''
    triangle_pryamougoln(-550, -120, 60, 60)
    turtle.setheading(270)
    parallelogram(-490, -60, 90, 50, 63)
    turtle.right(27)
    square(-445, -173, 50)
    turtle.left(45)
    triangle_ravnobedren(-513, -195, 70, 50)
    turtle.right(178)
    triangle_ravnobedren(-422, -290, 100, 75)
    turtle.left(37)
    triangle_ravnobedren(-321, -284, 160, 100)
    turtle.left(60)
    triangle_ravnostoron(-340, -136, 130)

def airplane():
    '''
    Airplane function.
    :return: None
    '''
    turtle.setheading(0)
    triangle_pryamougoln(-200, 250, 100, 150)
    turtle.left(123)
    turtle.right(270)
    triangle_pryamougoln(-140, 150, 100, 60)
    turtle.left(60)
    square(-140 ,250, 100)
    turtle.right(90)
    triangle_pryamougoln(-40, 290, 100, 100)
    turtle.left(45)
    triangle_pryamougoln(60, 190, 100, 100)
    turtle.right(45)
    triangle_ravnobedren(21, 149, 80, 57)
    parallelogram(101, 149, 80, 57, 134)





#if __name__ == '__main__':
swan()
airplane()     
bird()
dog()
candle()
fish()

