from turtle import*

speed(5)
pensize(8)
colormode(255)
def ci(a,b,c,d,e):
    penup()
    goto(a,b)
    pd()
    color(c,d,e)
    circle(75)
    pass

ci(-140,50,0,0,255)
ci(0,50,0,0,0)
ci(140,50,255,0,0)
ci(-50,-30,255,255,0)
ci(50,-30,0,255,0)
pu()
goto(-250,-200)
pd()
color(0,0,0)
write("happy olympics",font=("Segoe Print",50,"normal"))
ht()
done()
