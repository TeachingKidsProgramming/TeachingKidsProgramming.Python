#!/usr/bin/env python

import builtins
import turtle as t
import math

import _lib

builtins.iteration = 18
builtins.position = (-200, 100)

def dragon_curve(iteration, size, direction=1, swap=False):
    if iteration == 0:
        t.forward(size)

    else:
        t.right(45 * direction)
        dragon_curve(iteration-1, size / math.sqrt(2), int(not swap) - int(swap), swap)
        t.left(90 * direction)
        dragon_curve(iteration-1, size / math.sqrt(2), int(swap) - int(not swap), swap)
        t.right(45 * direction)

if __name__ == "__main__":
    _lib.init()
    dragon_curve(iteration, size)
    _lib.exit()
