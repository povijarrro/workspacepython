import pygame as pg

def init(bg):
    pg.init()
    bgrnd=pg.image.load(bg)
    bg_size=bgrnd.get_size()
    window=pg.display.set_mode((900*bg_size[0]/bg_size[1],900))
    pg.display.update()

init("bgrnd.jpg")

running = True
while running:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False
