#!/usr/bin/env python

from turtle import *

def zelva(level, size):
    if level == 0:
        return
    else:
        left(60)
        forward(size)
        right(60)
        begin_fill()
        for i in range(3):
            forward(size)
            right(120)
        end_fill()
        zelva(level-1, size/2)
        left(60)
        backward(size)
        right(60)
        zelva(level-1, size/2)
        forward(size)
        zelva(level-1, size/2)
        backward(size)
        
speed(0)
tracer(600, 0)
hideturtle()
penup()
goto(-300, -300)
pendown()

fillcolor = "blue"
pencolor = "blue"
size = 600
for i in range(3):
    forward(size)
    left(120)
zelva(5, size/2)

update()
exitonclick()



# export
#size = 1600
#border = 10
#color = "blue"
#for i in range(1,7):
#    screensize(size, size)
#    hideturtle()
#    pensize(3)
#    pencolor(color)
#    fillcolor(color)
#    penup()
#    goto(-window_width()/2+border*1.5, window_height()/2+border-size)
#    pendown()
#    
#    for ii in range(3):
#        forward(size)
#        left(120)
#    zelva(i, size/2)
#    update()
#    
#    cv = getcanvas()
#    cv.postscript(file="/media/data/Bordýlek/Sierpinského trojúhelník 1/sierpinski-"+color+"-"+str(i)+".ps", width=size+2*border, height=size+2*border)
#    
#    reset()
