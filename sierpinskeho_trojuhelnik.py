#!/usr/bin/env python

from turtle import *
import time


def sierpinskeho_trojuhelnik(iteration, size, direction=1):
    pendown()
    if iteration <= 1:
        for i in range(3):
            forward(size)
            left(120 * direction)
    else:
        sierpinskeho_trojuhelnik(iteration-1, size/2, direction)
        forward(size/2)
        left(60 * direction)
        sierpinskeho_trojuhelnik(iteration-1, size/2, -direction)
        forward(size/2)
        left(60 * direction)
        sierpinskeho_trojuhelnik(iteration-1, size/2, direction)

        penup()
        right(60 * direction)
        backward(size/2)
        right(60 * direction)
        backward(size/2)


start_position = (-250, -200)
tracer(600, 0)
speed(0)
for i in range(1, 10):
    reset()
    hideturtle()
    penup()
    setpos(start_position)
    pendown()
    sierpinskeho_trojuhelnik(i, 500)
    update()
    time.sleep(1)
exitonclick()
