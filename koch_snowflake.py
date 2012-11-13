#!/usr/bin/env python

from turtle import *

from koch_curve import koch_curve

iteration = 6
position = (-300, 180)
heading = 0
size = 600

def koch_snowflake(iteration, size):
    for i in range(3):
        koch_curve(iteration, size, direction=1)
        right(120)

if __name__ == "__main__":
    speed(0)
    tracer(600, 0)
    hideturtle()
    penup()
    setpos(position)
    setheading(heading)
    pendown()

    koch_snowflake(iteration, size)

    update()
    exitonclick()
