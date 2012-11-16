#!/usr/bin/env python

import builtins
import turtle as t
import math

import _lib
from dragon_curve import dragon_curve

builtins.iteration = 16
builtins.position = (0, 0)
builtins.size = 300

colors = ["#4bd31f", "#3eff00", "#2bb200", "#90ff45"] * 30
def changeColor():
    t.pencolor(colors.pop())
    
def dragon_curve_tiling():
    for heading in [0, 90, 180, 270]:
        t.penup()
        t.home()
        t.setheading(heading)
        changeColor()
        t.pendown()
        dragon_curve(iteration, size, swap=True)

if __name__ == "__main__":
    _lib.init()
    dragon_curve_tiling()
    _lib.exit()
