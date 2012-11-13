#!/usr/bin/env python

import builtins
import turtle as t

import _lib
from koch_curve import koch_curve

builtins.position = (-300, 250)

def koch_antisnowflake(level, size):
    for i in range(3):
        koch_curve(level, size, direction=-1)
        t.right(120)

if __name__ == "__main__":
    _lib.init()
    koch_antisnowflake(iteration, size)
    _lib.exit()
