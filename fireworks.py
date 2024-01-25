import turtle as t
import random as rd
import time
pens=[]
pen=[]
n=90
t.tracer(0)
for i in range(n):
    t0=t.Turtle()
    t0.pu()
    t0.left(360/n*i)
    pens.append(t0)
for i in range(n):
    t0=t.Turtle()
    t0.pu()
    t0.left(360/n*i)
    pen.append(t0)
t.update()
t.colormode(255)
x=3
for i in range(18000):
    for j in range(n):
        pens[j].circle(160,6)
    t.update()
    time.sleep(0.0002)
    if i%60==59:
        x=rd.randrange(50,100)
        y=rd.randrange(50,100)
        z=rd.randrange(1,3)
        c=rd.randrange(0,255)
        a=rd.randrange(0,255)
        b=rd.randrange(0,255)
        for j in range(n):
            pens[j].left(z*180)
            pens[j].fd(x)
            if z == 1:
                pens[j].left(90)
            else:
                pens[j].left(-90)
            pens[j].fd(y)
            pens[j].color(a,b,c)
    for j in range(n):
        pen[j].circle(160,6)
    t.update()
    time.sleep(0.0002)
    if i%60==59:
        x=rd.randrange(50,100)
        y=rd.randrange(50,100)
        z=rd.randrange(1,3)
        a=rd.randrange(0,255)
        b=rd.randrange(0,255)
        c=rd.randrange(0,255)
        for j in range(n):
            pen[j].left(z*180)
            pen[j].fd(x)
            if z == 1:
                pen[j].left(90)
            else:
                pen[j].left(-90)
            pen[j].fd(y)
            pen[j].color(a,b,c)
t.done()
