import turtle as tl
import math

t=tl.Turtle()
t.shape('classic')
t.turtlesize(0.5)
#t.hideturtle()

def main():
    screen = tl.Screen()
    screen.title("A Turtle Graphics Screen")
    screen.setup(1850, 610)
    screen.bgcolor("cyan")

def draw_poly(turtle,n,len):
    for i in range(n):
        turtle.forward(len)
        turtle.left(360.0/n)

def koch(t,len, n):
    t=t
    if(n==1):
        t.forward(len)
    else:
        koch(t,len/3.0,n-1)
        t.left(60.0)
        koch(t,len/3.0,n-1)
        t.right(120.0)
        koch(t,len/3.0,n-1)
        t.left(60.0)
        koch(t,len/3.0,n-1)

def polygon(t,d,n):
    t=t
    for i in range(n):
        t.forward(d*math.sin(math.pi/n))
        t.left(360.0/n)  


main()
t.penup()
t.goto(0,0)
t.pendown()
t.speed(0)
#koch(t,1800,5)
for i in range(3,101):
    polygon(t,100,i)
    t.penup()
    t.goto(0,0)
    t.pendown()
tl.done()