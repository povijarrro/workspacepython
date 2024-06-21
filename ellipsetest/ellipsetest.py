#!python
from cmath import sqrt
import pygame as pg
from random import randint
import sys

def norm(vec):
    res=0
    n=len(vec)
    for i in range(n):
        res+=vec[i]**2
        
    res=sqrt(res).real
   
    return res



def scaled_midpoints(xvec,yvec):
    xres=[]
    yres=[]
    n=len(xvec)
    for i in range(n):
        if i<n-1:
            x=(xvec[i]+xvec[i+1])/2
            y=(yvec[i]+yvec[i+1])/2
    
        else:
            x=(xvec[i]+xvec[0])/2
            y=(yvec[i]+yvec[0])/2
        xres.append(x)
        yres.append(y)   

        
    xresnorm=norm(xres)
    yresnorm=norm(yres)
    
    xres=[200*x/xresnorm for x in xres]
    yres=[200*y/yresnorm for y in yres]


    return xres, yres

def randpoints(n):
    xres=[]
    yres=[]  
    for __ in range(n-1):
        xres.append(randint(-screen.get_width()//2,screen.get_width()//2))
        yres.append(randint(-screen.get_height()//2,screen.get_height()//2)) 
       
    xres.append(-sum(xres))
    yres.append(-sum(yres)) 

    xresnorm=norm(xres)
    yresnorm=norm(yres)
    
    for i in range(n):
        xres[i]/=xresnorm
        yres[i]/=yresnorm 

    return xres,yres

def draw_polygon(xvec,yvec):
    pg.draw.aalines(screen,(255,255,255),True, [[screen.get_width()/2+xvec[i],screen.get_height()/2-yvec[i]] for i in range(len(xvec))])

if __name__== "__main__":
    pg.init()
    screen=pg.display.set_mode((400,400))

    clock=pg.time.Clock()
    
    points=randpoints(100)
    
    draw_polygon(points[0],points[1])
    points=scaled_midpoints(points[0],points[1])
    draw_polygon(points[0],points[1])
    
    while True:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                sys.exit()
        
        screen.fill((0,0,0))
        points=scaled_midpoints(points[0],points[1])
        draw_polygon(points[0],points[1])
        
         
        clock.tick(100)
        pg.display.update()



