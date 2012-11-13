#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals
from turtle import *

def zelva(level, size):
    if level == 0:
        forward(size*2)
    else:
        zelva(level-1, size/2)
        right(60)
        backward(size)
        left(60)
        zelva(level-1, size/2)
        left(60)
        backward(size)
        right(60)
        zelva(level-1, size/2)
        
speed(0)
tracer(600, 0)
hideturtle()
penup()
goto(-300, -300)
pendown()

size = 300
zelva(10, size)
for i in range(2):
    left(120)
    forward(size*2)

update()
exitonclick()