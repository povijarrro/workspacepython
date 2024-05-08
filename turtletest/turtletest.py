#!python
from random import randint
from turtle import Turtle, pencolor
import turtle

def koch_curve(t, size, level):
    if level <= 1:
        t.forward(size)
    else:
        koch_curve(t, size/3.0, level-1)
        t.left(60)
        koch_curve(t, size/3.0, level-1)
        t.right(120)
        koch_curve(t, size/3.0, level-1)
        t.left(60)
        koch_curve(t, size/3.0, level-1)

def koch_snowflake(t, size, level):
    for _ in range(3):
        koch_curve(t, size, level)
        t.right(120)        

scr=turtle.Screen()
screenTk = scr.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)
scr.colormode(255)
scr.bgcolor(0,2,255)
t=Turtle()
t.hideturtle()
t.speed(0)
t.penup()
t.goto(-700, 0)
t.pendown()

n=5
#koch_curve(t, 1560, n)
koch_snowflake(t,100,n)
scr.exitonclick()
  