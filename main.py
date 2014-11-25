
from turtle import *
from time import clock

class Vec3(tuple):

    def __new__(cls, x, y, z):
        return tuple.__new__(cls, (x, y, z))
    def __add__(self, other):
        return Vec3(self[0]+other[0], self[1]+other[1], self[2]+other[2])
    def __rmul__(self, other):
        return Vec3(self[0]*other, self[1]*other, self[2]*other)
  
def triangle(laenge, stufe, f1, f2, f3):  # f1, f2, f3 colors of the vertices
    if stufe == 0:
        color((1./3)*(f1+f2+f3))
        begin_fill()
        for i in range(3):
            fd(laenge)
            lt(120)
        end_fill()
    else:
        c12 = 0.5*(f1+f2)
        c13 = 0.5*(f1+f3)
        c23 = 0.5*(f2+f3)
        triangle(0.5*laenge, stufe - 1, f1, c12, c13)
        fd(laenge)
        lt(120)
        triangle(0.5*laenge, stufe - 1, f2, c23, c12)
        fd(laenge)
        lt(120)
        triangle(0.5*laenge, stufe - 1, f3, c13, c23)
        fd(laenge)
        lt(120)

def main():
    setup(720, 720)
    reset()
    setundobuffer(1)
    sierp_size = 600
    colormode(255)
    speed(0)
    ht()
    pu()
    bk(sierp_size*0.5)
    lt(90)
    bk(sierp_size*0.4)
    rt(90)
    tracer(1,0)
    ta = clock()
    triangle(sierp_size, 6,
            Vec3(255.0,0,0), Vec3(0,255.0,0), Vec3(0,0,255.0))
    tb = clock()
    return "%.2f sec." % (tb-ta)

if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()
