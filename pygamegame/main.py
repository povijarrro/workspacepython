#!python
import config as cfg
import pygame as pg
from random import randint

pg.init()

screen=pg.display.set_mode(cfg.SIZE)
font=pg.font.SysFont("Arial",30)
text=font.render("click",True, cfg.RED, cfg.GREEN)
text_rect=text.get_rect()
running=True
score=0
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
        elif event.type==pg.MOUSEBUTTONDOWN:
            x,y=pg.mouse.get_pos()
            if text_rect.collidepoint(x,y):
                score+=1
                print(score)

    screen.fill(cfg.BLACK)
    text_rect.center = randint(0,cfg.SIZE[0]-1), randint(0, cfg.SIZE[1]-1)
    #text_rect.center=cfg.SIZE[0]/2, cfg.SIZE[1]/2
    screen.blit(text,text_rect)
    pg.time.Clock().tick(2)
    pg.display.update() 

pg.quit()