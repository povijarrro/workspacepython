import turtle as tl

t=tl.Turtle()
t.shape('classic')
t.turtlesize(0.5)
t.hideturtle()

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


main()
t.penup()
t.goto(-900,-300)
t.pendown()
t.speed(-100)
koch(t,1800,7)

tl.done()