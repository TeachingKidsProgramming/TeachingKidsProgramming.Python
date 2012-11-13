#!/usr/bin/env python

import builtins
import turtle as t

import _lib
from koch_curve import koch_curve

builtins.position = (-300, 180)

def koch_snowflake(iteration, size):
    for i in range(3):
        koch_curve(iteration, size, direction=1)
        t.right(120)

if __name__ == "__main__":
    _lib.init()
    koch_snowflake(iteration, size)
    _lib.exit()
