import pygame as pg

def draw_grid(window, tile_size, grid_size):
    for line in range(1, grid_size[0]+1):
        pg.draw.line(window, (255, 255, 255), (0, line * tile_size), (grid_size[1]*tile_size, line * tile_size))
    
    for line in range(1, grid_size[1]+1):  
        pg.draw.line(window, (255, 255, 255), (line * tile_size, 0), (line * tile_size, grid_size[0]*tile_size))

class Nonogram:
    
    def __init__(self,row_legend,col_legend):
        self.row_legend=row_legend
        self.col_legend=col_legend
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
        dim=max(self.matrix_size[0],self.matrix_size[1])
        tile_size=(20,20)
        i = 0
        for row in self.matrix:
            j = 0
            for tile in row:
                tile_text=font.render(tile,True,color)
                rect = tile_text.get_rect()
                rect.x=j*tile_size[0]
                rect.y=i*tile_size[1]
                j += 1
                window.blit(tile_text,(rect.x,rect.y))
                display.update(rect)
            i += 1
                
        draw_grid(window, 20, self.matrix_size)
        display.update()

        

