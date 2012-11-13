#!/usr/bin/env python

from turtle import *
import time

from koch_curve import koch_curve

iteration = 6
position = (-300, 250)
heading = 0
size = 600

def koch_antisnowflake(level, size):
    for i in range(3):
        koch_curve(level, size, direction=-1)
        right(120)

if __name__ == "__main__":
    speed(0)
    tracer(600, 0)
    hideturtle()
    penup()
    setpos(position)
    setheading(heading)
    pendown()

    koch_antisnowflake(iteration, size)

    update()
    exitonclick()
