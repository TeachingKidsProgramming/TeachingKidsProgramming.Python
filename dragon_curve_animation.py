#!/usr/bin/env python

from turtle import *
import time
from math import sqrt

start_position = (-200, 100)
size = 600

def dragon_curve(iteration, size, direction=1):
    if iteration == 0:
        forward(size)

    else:
        right(45 * direction)
        dragon_curve(iteration-1, size / sqrt(2), 1)
        left(90 * direction)
        dragon_curve(iteration-1, size / sqrt(2), -1)
        right(45 * direction)

tracer(600, 0)
speed(0)
for i in range(1, 17):
    reset()
    hideturtle()
    penup()
    setpos(start_position)
    pendown()
    dragon_curve(i, size)
    update()
    time.sleep(1)
exitonclick()
