#!/usr/bin/env python
# -*- coding: utf-8 -*-

# autor: Michal Plch

from __future__ import division, print_function
from turtle import *

def koberec(n, s, p=False):
    if p == True:
        for i in range(4):
            forward(s)
            right(90)

    penup()
    right(90)
    forward(s / 3)
    left(90)
    forward(s / 3)
    pendown()
    begin_fill()
    for i in range(4):
        forward(s / 3)
        right(90)
    end_fill()
    penup()
    backward(s / 3)
    left(90)
    forward(s / 3)
    right(90)

    if n > 1:
        for i in range(1, 9):
            koberec(n - 1, s / 3)
            penup()
            forward(s / 3)
            if i in (3, 5, 7):
                right(90)
                forward(s / 3)
        forward(s / 3)
        right(90)
    
    

hideturtle()
tracer(3600)
speed(0)

#penup()
#goto(-400, 400)
#pendown()
#
#koberec(5, 800, True)
#
#update()
#exitonclick()



# export
# autor: Jakub Klinkovský
size = 1600
border = 10
color = "black"
for i in range(6,7):
    screensize(size, size)
    hideturtle()
    pencolor(color)
    fillcolor(color)
    penup()
    goto(-window_width()/2+border, window_height()/2-border)
    pendown()
    
    koberec(i, size, True)
    update()
    
    cv = getcanvas()
    cv.postscript(file="/media/data/Bordýlek/Sierpinského koberec/sierpinski-"+color+"-"+str(i)+".ps", width=size+2*border, height=size+2*border)
    
    reset()
