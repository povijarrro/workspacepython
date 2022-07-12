import config
import copy
from grid import Grid
from snake import Snake

direction=(0,1)
snake1 = Snake([],[10,10])
grid1 = Grid(config.SIZE, [config.GRID_SIZE[1]*[0] for i in range(config.GRID_SIZE[0])], snake1)

def setup():
    size(config.SIZE[0], config.SIZE[1])
    frameRate(5)

def draw():

    grid1.snake_move(direction)
    
def keyPressed():
    global direction
    if key == CODED:
        if keyCode == UP:
            direction = (-1,0) if direction != (1, 0) else (1, 0)
        elif keyCode == DOWN:
            direction = (1,0) if direction != (-1, 0) else (-1, 0) 
        elif keyCode == LEFT:
            direction = (0,-1) if direction != (0, 1) else (0, 1)
        elif keyCode == RIGHT:
            direction = (0,1) if direction != (0, -1) else (0, -1)
           
