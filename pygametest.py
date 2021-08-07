import pygame as pg

window=None

def init(bg):
    pg.init()
    bgrnd=pg.image.load(bg)
    bg_size=bgrnd.get_size()
    bgrnd = pg.transform.scale(
    bgrnd, (int(900*bg_size[0]/bg_size[1]),900))
    window=pg.display.set_mode((bgrnd.get_size()[0],900))
    window.blit(bgrnd,(0,0))
    pg.display.update()

def loop():
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

   
   



init("ball.png")
pg.display.get_surface().blit(pg.image.load("bgrnd.png"),(0,0))
pg.display.update()
loop()
