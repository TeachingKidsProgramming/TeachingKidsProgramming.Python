#!/usr/bin/env python

from turtle import *
import math

iteration = 6
position = (-300, 0)
heading = 0
size = 600

def koch_curve(iteration, size, angle=60, direction=1):
    if iteration == 0:
        forward(size)
    else:
        size = size / (2 + 2 * math.cos(math.radians(angle)))
        koch_curve(iteration-1, size, angle, direction)
        left(angle * direction)
        koch_curve(iteration-1, size, angle, direction)
        right(2 * angle * direction)
        koch_curve(iteration-1, size, angle, direction)
        left(angle * direction)
        koch_curve(iteration-1, size, angle, direction)

if __name__ == "__main__":
    speed(0)
    tracer(600, 0)
    hideturtle()
    penup()
    setpos(position)
    setheading(heading)
    pendown()

    koch_curve(iteration, size)

    update()
    exitonclick()
