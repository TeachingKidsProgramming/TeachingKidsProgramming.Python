#!/usr/bin/env python

import builtins
import turtle as t

import _lib

builtins.iteration = 10
builtins.position = (-300, -250)
builtins.size = 600

def sierpinski_triangle(iteration, size, direction=1):
    t.pendown()
    if iteration == 1:
        for i in range(3):
            t.forward(size)
            t.left(120 * direction)
    else:
        sierpinski_triangle(iteration-1, size/2, direction)
        t.forward(size/2)
        t.left(60 * direction)
        sierpinski_triangle(iteration-1, size/2, -direction)
        t.forward(size/2)
        t.left(60 * direction)
        sierpinski_triangle(iteration-1, size/2, direction)

        t.penup()
        t.right(60 * direction)
        t.backward(size/2)
        t.right(60 * direction)
        t.backward(size/2)

if __name__ == "__main__":
    _lib.init()
    sierpinski_triangle(iteration, size)
    _lib.exit()
