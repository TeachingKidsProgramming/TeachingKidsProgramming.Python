#!/usr/bin/env python

import builtins
import turtle as t

import _lib

builtins.position = (-300, -240)

def arrowhead_curve(iteration, size, direction=1):
    if iteration == 0:
        t.forward(size)

    else:
        t.left(60 * direction)
        arrowhead_curve(iteration-1, size/2, -direction)
        t.right(60 * direction)
        arrowhead_curve(iteration-1, size/2, direction)
        t.right(60 * direction)
        arrowhead_curve(iteration-1, size/2, -direction)
        t.left(60 * direction)

if __name__ == "__main__":
    _lib.init()
    arrowhead_curve(iteration, size)
    _lib.exit()
