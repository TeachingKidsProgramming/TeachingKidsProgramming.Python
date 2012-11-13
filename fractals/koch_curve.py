#!/usr/bin/env python

import builtins
import turtle as t
import math

import _lib

builtins.position = (-300, 0)

def koch_curve(iteration, size, angle=60, direction=1):
    if iteration == 0:
        t.forward(size)
    else:
        size = size / (2 + 2 * math.cos(math.radians(angle)))
        koch_curve(iteration-1, size, angle, direction)
        t.left(angle * direction)
        koch_curve(iteration-1, size, angle, direction)
        t.right(2 * angle * direction)
        koch_curve(iteration-1, size, angle, direction)
        t.left(angle * direction)
        koch_curve(iteration-1, size, angle, direction)

if __name__ == "__main__":
    _lib.init()
    koch_curve(iteration, size)
    _lib.exit()
