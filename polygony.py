#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals
from turtle import *
import time
import math

def polygon(n, o=1000):
    a = o/n
    uhel = 360/n
    for i in range(n):
        forward(a)
        left(uhel)
        
def kruh(r):
    polygon(360, o=2*math.pi*r)

#for i in range(3, 10):
#    hideturtle()
#    speed(0)
#    polygon(i)
#    time.sleep(1)
#    bye()
    
hideturtle()
tracer(600, 0)
speed(0)
kruh(50)
update()
exitonclick()
