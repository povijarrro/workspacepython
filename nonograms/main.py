from nonogram import Nonogram
import pygame as pg
import sys

pg.init()
window=pg.display.set_mode((1000,1000))

nono=Nonogram([
[0,0,0,2],
[0,1,1,2],
[1,1,1,1],
[1,1,1,1],
[0,1,2,1],
[0,1,2,1],
[0,1,2,2],
[0,1,2,1],
[0,1,1,1],
[0,1,1,2],
[0,0,0,5],
[0,0,2,2],
[0,0,0,3],
[0,0,0,4],
[0,0,4,2],
[0,1,1,3],
[1,1,1,2],
[1,1,1,1],
[1,1,1,2],
[0,0,2,3]],
[
[0,0,0,0,0,0,0,3,1,0],
[0,0,0,0,0,11,4,3,4,0],
[0,1,1,11,1,2,6,2,2,5],
[4,1,1,6,5,3,1,1,2,3]])
print(nono)
nono.draw(pg.display,pg.font.SysFont("comicsans",20),pg.Color('yellow'))

#blit_text(window,str(nono),(0,0),pg.font.SysFont("comicsans",50))
#pg.display.update()

while True:
    for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()