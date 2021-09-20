import pygame as pg

def draw_grid(window, tile_size, grid_size,margin_size):
    for line in range(1, grid_size[0]+1):
        width=1
        if((line-margin_size[0])%5==0):
            width=3
        pg.draw.line(window, (255, 255, 255), (0, line * tile_size), (grid_size[1]*tile_size, line * tile_size),width)
    
    for line in range(1, grid_size[1]+1):
        width=1  
        if((line-margin_size[1])%5==0):
            width=3
        pg.draw.line(window, (255, 255, 255), (line * tile_size, 0), (line * tile_size, grid_size[0]*tile_size),width)

class Nonogram:
    
    def __init__(self,row_legend,col_legend, tile_size):
        self.row_legend=row_legend
        self.col_legend=col_legend
        self.tile_size=tile_size
        self.matrix=[]
        nrow=len(self.row_legend)
        ncol=len(self.col_legend)

        maxrowlen=len(self.row_legend[0])
        maxcollen=len(self.col_legend[0])
        self.matrix_size=(nrow+ncol,maxrowlen+maxcollen)              
        for i in range(self.matrix_size[0]):
            matrixrow=[]
            for j in range(self.matrix_size[1]):
                if((i<ncol and j<maxrowlen) or (i>=ncol and j>=maxrowlen)):
                    matrixrow.append("")
                else:
                    if(i<ncol):
                        matrixrow.append(f'{self.col_legend[i][j-maxrowlen]}') 
                    else:
                        matrixrow.append(f'{self.row_legend[i-ncol][j]}')       
            self.matrix.append(matrixrow)    

    def __str__(self):
        translation = {39: None, 44:None, 91:'[ ', 93:' ]'}  
        return("\n".join(map(str,self.matrix)).translate(translation))
 
    def draw(self,display,font,color):
        window=display.get_surface()
        draw_grid(window, self.tile_size, self.matrix_size, (len(self.col_legend), len(self.row_legend[0])))
        i = 0
        for row in self.matrix:
            j = 0
            for tile in row:
                if tile=='0':
                    tile=''
                tile_text=font.render(tile,True,color)
                text_rect = tile_text.get_rect()
                tile_rect=pg.Rect(j*self.tile_size, i*self.tile_size, self.tile_size, self.tile_size)
                j += 1
                window.blit(tile_text,(tile_rect.center[0]-text_rect.w//2, tile_rect.center[1]-text_rect.h//2))
                display.update(tile_rect)
            i += 1
    
        display.update()

        

