#!/usr/bin/env python

import builtins
import turtle as t

import _lib
from koch_curve import koch_curve


def caesaro(iteration, size):
    for i in range(4):
        koch_curve(iteration, size, 85)
        t.left(90)

if __name__ == "__main__":
    _lib.init()
    caesaro(iteration, size)
    _lib.exit()
