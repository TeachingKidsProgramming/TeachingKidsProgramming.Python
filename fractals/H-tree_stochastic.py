#!/usr/bin/env python

import builtins
import turtle as t
import math
import random

import _lib

builtins.iteration = 10
builtins.position = (0, -300)
builtins.heading = 90
builtins.size = 200

def stochastic(iteration, size, angle, par, factor=0.3):
    if iteration == 0:
        return

    size2 = size * (1 + random.uniform(-factor, factor))
    angle2 = angle * (1 + random.uniform(-factor, factor))
    t.forward(size2)
    t.left(angle2)
    stochastic(iteration-1, size * par, angle, par, factor)
    t.right(angle2 * 2)
    stochastic(iteration-1, size * par, angle, par, factor)
    t.left(angle2)
    t.backward(size2)
    
_lib.init()
stochastic(iteration, size, angle=45, par=1/math.sqrt(2), factor=0.3)
_lib.exit()
