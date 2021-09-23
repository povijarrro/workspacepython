from pygame.constants import MOUSEBUTTONDOWN
from nonogram import Nonogram, draw_empty_grid
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
[4,1,1,6,5,3,1,1,2,3]],20)

nono2=Nonogram([
[0,0,0,2],
[0,1,1,2],
[1,1,1,1],
[1,1,1,1],
[0,1,2,1]],
[
[0,0,0,0,0,0,0,3,1,0],
[0,0,0,0,0,11,4,3,4,0],
[0,1,1,11,1,2,6,2,2,5],
[4,1,1,6,5,3,1,1,2,3]],20)


#print([[nono.matrix[i][j] for j in range(nono.maxrowlen,nono.matrix_size[1])] for i in range(nono.ncol,nono.matrix_size[0])])
window.fill((255,255,255))
nono_surf=nono.get_surface(pg.font.SysFont("comicsans",20),(255,255,255),(0,0,0))
window.blit(nono_surf, (0,0))
draw_empty_grid(window,(0,0), (0,0,0), nono.tile_size, nono.matrix_size, nono.margin_size)
print(nono)
pg.display.update()
print(nono.matrix_size)
running=True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running=False                   
pg.quit()            
