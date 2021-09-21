import pygame as pg
import sys

def draw_grid(window, pos, tile_size, grid_size,margin_size):
    for line in range(0, grid_size[0]+1):
        width=1
        if((line-margin_size[0])%5==0):
            width=3
        pg.draw.line(window, (255, 255, 255), (pos[0], line * tile_size+pos[1]), (grid_size[1]*tile_size+pos[0], line * tile_size+pos[1]),width)
    
    for line in range(0, grid_size[1]+1):
        width=1  
        if((line-margin_size[1])%5==0):
            width=3
        pg.draw.line(window, (255, 255, 255), (line * tile_size+pos[0], pos[1]), (line * tile_size+pos[0], grid_size[0]*tile_size+pos[1]),width)

class Nonogram:
    
    def __init__(self,row_legend,col_legend, tile_size):
        self.row_legend=row_legend
        self.col_legend=col_legend
        self.tile_size=tile_size
        self.matrix=[]
        self.nrow=len(self.row_legend)
        self.ncol=len(self.col_legend)
        self.maxrowlen=len(self.row_legend[0])
        self.maxcollen=len(self.col_legend[0])
        self.matrix_size=(self.nrow+self.ncol, self.maxrowlen+self.maxcollen)              
        for i in range(self.matrix_size[0]):
            matrixrow=[]
            for j in range(self.matrix_size[1]):
                if((i<self.ncol and j<self.maxrowlen) or (i>=self.ncol and j>=self.maxrowlen)):
                    matrixrow.append("")
                else:
                    if(i<self.ncol):
                        matrixrow.append(f'{self.col_legend[i][j-self.maxrowlen]}') 
                    else:
                        matrixrow.append(f'{self.row_legend[i-self.ncol][j]}')       
            self.matrix.append(matrixrow) 
        self.nono_matrix=[[self.matrix[i][j] for j in range(self.maxrowlen,self.matrix_size[1])] for i in range(self.ncol, self.matrix_size[0])]       

    def __str__(self):
        translation = {39: None, 44:None, 91:'[ ', 93:' ]'}  
        return("\n".join(map(str,self.matrix)).translate(translation))
    
    def check(self,matrix):
        return matrix==self.nono_matrix
        


    def draw(self,display, pos, font, color):
        window=display.get_surface()
        draw_grid(window, pos, self.tile_size, self.matrix_size, (self.ncol, self.maxrowlen)) 
        while(True):
            i = 0
            for row in self.matrix:
                j = 0
                for tile in row:
                    if tile=='0':
                        tile=''
                    tile_text=font.render(tile,True,color)
                    text_rect = tile_text.get_rect()
                    tile_rect=pg.Rect(j*self.tile_size+pos[0], i*self.tile_size+pos[1], self.tile_size, self.tile_size)
                    if(i>=self.ncol and j>=self.maxrowlen):
                        if(pg.mouse.get_pressed()[0] and tile_rect.collidepoint(pg.mouse.get_pos())):
                            window.fill((255,0,0,0), tile_rect)
                        elif(pg.mouse.get_pressed()[2] and tile_rect.collidepoint(pg.mouse.get_pos())):
                            window.fill((255,255,255),tile_rect)
                    j += 1
                    window.blit(tile_text,(tile_rect.center[0]-text_rect.w//2, tile_rect.center[1]-text_rect.h//2))
                     
                    display.update(tile_rect)
                i += 1
            
            display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

        

