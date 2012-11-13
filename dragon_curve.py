#!/usr/bin/env python

from turtle import *
import time
import math


def dragon(iteration, step, direction=1):
    if iteration <= 0:
        forward(step)
        return
    
    right(45 * direction)
    dragon(iteration-1, step / math.sqrt(2), 1)
    left(90 * direction)
    dragon(iteration-1, step / math.sqrt(2), -1)
    right(45 * direction)

# "backwards" (swapped direction)
def dragon2(iteration, step, direction=1):
    if iteration <= 0:
        forward(step)
        return
    
    right(45 * direction)
    dragon2(iteration-1, step / math.sqrt(2), -1)
    left(90 * direction)
    dragon2(iteration-1, step / math.sqrt(2), 1)
    right(45 * direction)

colors = ["#4bd31f", "#3eff00", "#2bb200", "#90ff45"] * 30
def changeColor():
    pencolor(colors.pop())
def doprava(drak=dragon):
    changeColor()
    setheading(0)
    drak(17, 300)
def nahoru(drak=dragon):
    changeColor()
    setheading(90)
    drak(17, 300)
def doleva(drak=dragon):
    changeColor()
    setheading(180)
    drak(17, 300)
def dolu(drak=dragon):
    changeColor()
    setheading(270)
    drak(17, 300)
    
tracer(600, 0)
speed(0)

def run1():
    for i in xrange(15):
        reset()
        hideturtle()
        penup()
        setpos(-200, 100)
        pendown()
        dragon(i, 470)
        update()
        time.sleep(1)
    exitonclick()
    
def run2():
    tracer(600, 0)
    speed(0)
    hideturtle()

    for drak in [doprava, nahoru, doleva, dolu]:
        penup()
        home()
        pendown()
        drak(dragon2)
    update()
    exitonclick()
    
#run1()
#run2()

# export
size = 1600
border = 10
color = "blue"
for i in range(0,17):
    screensize(size, size)
    hideturtle()
    pensize(3)
    pencolor(color)
    fillcolor(color)
    penup()
    goto(-window_width()/2+size/4.1, window_height()/2-size*0.4)
    pendown()
    
    dragon(i, size/1.55)
    update()
    
    cv = getcanvas()
    cv.postscript(file="/media/data/Bordýlek/Dračí křivka/dragon-"+color+"-"+str(i+1)+".ps", width=size+2*border, height=size+2*border)
    
    reset()
