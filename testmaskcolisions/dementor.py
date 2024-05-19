#!python
import sys
import pygame as pg

SIZE = 800,800

pg.init()

dis = pg.display.set_mode(SIZE)
dis.fill((255,255,255))
clock=pg.time.Clock()

dementor_img=pg.image.load("dementor.png").convert_alpha()
dementor_rect=dementor_img.get_rect()
dementor_rect.center=SIZE[0]/2, SIZE[1]/2
dementor_mask=pg.mask.from_surface(dementor_img)



point=pg.Surface((1,1)).convert_alpha()
point.fill((0,0,0))
m=pg.mask.from_surface(point)

dis.blit(dementor_img, dementor_rect)
pg.display.update()

run = True
i=0
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run=False
            pg.quit()
            sys.exit()

            
        if event.type == pg.MOUSEBUTTONDOWN:
            pos=pg.mouse.get_pos()
            i+=1
            print(f"{dementor_mask.overlap(m,(pos[0]-dementor_rect.left, pos[1]-dementor_rect.top)) != None} {i}")
    
    pg.display.update()
    clock.tick(60)            


pg.quit()