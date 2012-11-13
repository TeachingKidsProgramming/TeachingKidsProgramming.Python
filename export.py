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
#~ #~
    dragon(i, size/1.55)
    update()
#~ #~
    cv = getcanvas()
    cv.postscript(file="/media/data/Bordýlek/Dračí křivka/dragon-"+color+"-"+str(i+1)+".ps", width=size+2*border, height=size+2*border)
#~ #~
    reset()
