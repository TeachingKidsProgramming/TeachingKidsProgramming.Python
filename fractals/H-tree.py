#!/usr/bin/env python

import builtins
import turtle as t
import math

import _lib

builtins.iteration = 10
builtins.position = (0, -300)
builtins.heading = 90
builtins.size = 300

def h_tree(iteration, size, angle=90, par=1/math.sqrt(2)):
    if iteration == 0:
        return

    t.forward(size)
    t.left(angle)
    h_tree(iteration-1, size * par, angle, par)
    t.right(angle * 2)
    h_tree(iteration-1, size * par, angle, par)
    t.left(angle)
    t.backward(size)
    
_lib.init()    

## classic H-tree
h_tree(iteration, size, angle=90, par=1/math.sqrt(2))

## different angle
#h_tree(iteration, size, angle=85, par=0.69)

## Pythagoras tree
#builtins.size = 200
#h_tree(iteration, size, angle=45, par=1/math.sqrt(2))

_lib.exit()
