#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function
from turtle import *

def zelva(level, size):
    if level < 1:
        return
    else:
        forward(size)
        for i in range(3):
            zelva(level-1, size/2)
            left(60)
            forward(size)
            left(60)
        backward(size)
        
speed(1)
tracer(600, 0)
hideturtle()
penup()
goto(-300, -300)
pendown()

size = 300
zelva(10, size)
for i in range(3):
    forward(size*2)
    left(120)

update()
exitonclick()


# export
#size = 1600
#border = 10
#color = "black"
#for i in range(1,8):
#    screensize(size, size)
#    hideturtle()
#    pensize(3)
#    pencolor(color)
#    fillcolor(color)
#    penup()
#    goto(-window_width()/2+border*1.5, window_height()/2+border-size)
#    pendown()
#    
#    for ii in range(3):
#        forward(size)
#        left(120)
#    zelva(i, size/2)
#    update()
#    
#    cv = getcanvas()
#    cv.postscript(file="/media/data/Bordýlek/Sierpinského trojúhelník 2/sierpinski-"+color+"-"+str(i)+".ps", width=size+2*border, height=size+2*border)
#    
#    reset()