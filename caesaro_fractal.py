#!/usr/bin/env python

from turtle import *

from koch_curve import koch_curve

iteration = 6
position = (-300, -300)
heading = 0
size = 600

def caesaro(iteration, size):
    for i in range(4):
        koch_curve(iteration, size, 85)
        left(90)

if __name__ == "__main__":
    speed(0)
    tracer(600, 0)
    hideturtle()
    penup()
    setpos(position)
    setheading(heading)
    pendown()

    caesaro(iteration, size)

    update()
    exitonclick()
