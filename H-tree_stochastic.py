#!/usr/bin/env python

from turtle import *
import math
import random

start_position = (0, -300)
start_heading = 90
size = 200

def stochastic(level, size, angle, par, factor=0.3):
    if level <= 0:
        return

    size2 = size * (1 + random.uniform(-factor, factor))
    angle2 = angle * (1 + random.uniform(-factor, factor))
    forward(size2)
    left(angle2)
    stochastic(level-1, size * par, angle, par, factor)
    right(angle2 * 2)
    stochastic(level-1, size * par, angle, par, factor)
    left(angle2)
    backward(size2)
    
tracer(600, 0)
speed(0)
hideturtle()
penup()
setpos(start_position)
setheading(start_heading)
pendown()

stochastic(10, size=200, angle=45, par=1/math.sqrt(2), factor=0.3)

update()
exitonclick()
