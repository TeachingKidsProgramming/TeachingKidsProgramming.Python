#!/usr/bin/env python

import builtins
import turtle as t
import time
import math

import fractals._lib as _lib
from fractals import *

builtins.position = (-300, -250)

_lib.init()

for i in range(7):
    t.clear()
    t.penup()
    t.setpos(position)
    t.setheading(heading)
    t.pendown()

    arrowhead_curve(i, size)
#    caesaro(i, size)
#    dragon_curve(i, size)
#    h_tree(i, size, angle=90, par=1/math.sqrt(2))
#    h_tree(i, size, angle=85, par=0.69)
#    h_tree(i, size, angle=45, par=1/math.sqrt(2))
#    stochastic(i, size, angle=45, par=1/math.sqrt(2), factor=0.3)
#    koch_antisnowflake(i, size)
#    koch_curve(i, size)
#    koch_snowflake(i, size)
#    sierpinski_triangle(i, size)

    t.update()
    time.sleep(1)

_lib.exit()
