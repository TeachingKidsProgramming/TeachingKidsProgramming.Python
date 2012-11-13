#!/usr/bin/env python

from turtle import *
import time
import math

def polygram(n, variant=1, a=300):
    pendown()
    if variant == 1:
        right(360/n)
        for i in range(n):
            forward(a)
            right(2*360/n)
        left(360/n)

    elif variant == 2:
        right(90-90/n)
        for i in range(n):
            forward(a)
            right(180-180/n)
        left(90-90/n)
    penup()

def star(n, a=200, zaklad=100):
    uhel1 = 180 - 2*math.asin(zaklad/2/a)/math.pi*180       # doplněk do 180 vnitřního úhlu hvězdy
    uhel2 = -360/n+2*math.acos(zaklad/2/a)/math.pi*180      # doplněk do 180 vnějšího úhlu hvězdy
    print(uhel1, uhel2)
    left(math.acos(zaklad/2/a)/math.pi*180)
    for i in range(n):
        forward(a)
        right(uhel1)
        forward(a)
        left(uhel2)

#for i in range(3, 10):
#    hideturtle()
#    speed(0)
#    polygon(i)
#    time.sleep(1)
#    bye()

#hideturtle()
#tracer(600, 0)
speed(0)
penup()
for i in range(5,19,2):
    goto(-550+150*(i-5), 400)
    polygram(i, variant=1, a=1500/i)

    goto(-550+150*(i-5), 0)
    polygram(i, variant=2, a=300)
#star(20, 100, 50)
update()
exitonclick()
