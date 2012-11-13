#!/usr/bin/env python

from turtle import *
import random

def zelva(level, size, angle=90, par=1/sqrt(2)):
    if level <= 0:
        return

    forward(size)
    left(angle)
    zelva(level-1, size * par, angle, par)
    right(angle * 2)
    zelva(level-1, size * par, angle, par)
    left(angle)
    backward(size)
    
def stochastic(level, size, angle, par, factor=0.3):
    if level <= 0:
        return

    size2 = size * (1 + random.randrange(-factor, factor, int=float))
    angle2 = angle * (1 + random.randrange(-factor, factor, int=float))
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

# go to start
left(90)
penup()
backward(300)
pendown()

## klasický H-strom
#zelva(10, 300, angle=90, par=1/sqrt(2))

## pootočený H-strom
#zelva(10, 300, angle=85, par=0.69)

## Pythagorův strom
zelva(10, 200, angle=45, par=1/sqrt(2))

## stochastický H-strom (factor - max. odchylka)
#stochastic(10, size=200, angle=45, par=1/sqrt(2), factor=0.3)

update()
exitonclick()
