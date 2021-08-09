import pygame as pg
from pygame.constants import K_ESCAPE

def init(bg):
    pg.init()
    bgrnd=pg.image.load("pygametest/"+bg)
    bg_size=bgrnd.get_size()
    bgrnd=pg.transform.scale(bgrnd,(int(900*bg_size[0]/bg_size[1]), 900))
    bg_size = bgrnd.get_size()
    window = pg.display.set_mode(bg_size)
    window.blit(bgrnd,(0,0))
    pg.display.update()

init("bgrnd.jpg")
car = pg.image.load("pygametest/car-5.png")
window = pg.display.get_surface()
size=window.get_size()
car_size=car.get_size()
window.blit(car,(int(size[0]/2-car_size[0]/2),size[1]-250))
pg.display.update()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
