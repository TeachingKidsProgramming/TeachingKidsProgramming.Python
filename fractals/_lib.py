#!/usr/bin/env python

import builtins
import turtle as t

builtins.iteration = 6
builtins.position = (-300, -300)
builtins.heading = 0
builtins.size = 600
builtins.pencolor = "black"
builtins.fillcolor = "black"

def init():
    t.speed(0)
    t.tracer(600, 0)
    t.hideturtle()
    t.pencolor(pencolor)
    t.fillcolor(fillcolor)
    t.penup()
    t.setpos(position)
    t.setheading(heading)
    t.pendown()

def exit():
    t.update()
    t.exitonclick()
