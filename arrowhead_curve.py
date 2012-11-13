#!/usr/bin/env python

from turtle import *

iteration = 6
position = (-300, -240)
heading = 0
size = 600

def arrowhead_curve(iteration, size, direction=1):
    if iteration == 0:
        forward(size)

    else:
        left(60 * direction)
        arrowhead_curve(iteration-1, size/2, -direction)
        right(60 * direction)
        arrowhead_curve(iteration-1, size/2, direction)
        right(60 * direction)
        arrowhead_curve(iteration-1, size/2, -direction)
        left(60 * direction)

if __name__ == "__main__":
    speed(0)
    tracer(600, 0)
    hideturtle()
    penup()
    setpos(position)
    setheading(heading)
    pendown()

    arrowhead_curve(iteration, size)

    update()
    exitonclick()
