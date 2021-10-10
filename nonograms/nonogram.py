import pygame as pg

def draw_empty_grid(window, pos, color, tile_size, grid_size, margin_size):
    for line in range(0, grid_size[0]+1):
        width=1
        if((line-margin_size[0])%5==0):
            width=3
        pg.draw.line(window, color, (pos[0], line * tile_size+pos[1]), (grid_size[1]*tile_size+pos[0], line * tile_size+pos[1]),width)
    
    for line in range(0, grid_size[1]+1):
        width=1  
        if((line-margin_size[1])%5==0):
            width=3
        pg.draw.line(window, color, (line * tile_size+pos[0], pos[1]), (line * tile_size+pos[0], grid_size[0]*tile_size+pos[1]),width)

def draw_general_grid(window, grid, pos):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            tile_size=grid[i][j].get_rect().w
            window.blit(grid[i][j], (j*tile_size+pos[0], i*tile_size+pos[1]))


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
        self.margin_size=(self.ncol, self.maxrowlen)              
        for i in range(self.matrix_size[0]):
            matrixrow=[]
            for j in range(self.matrix_size[1]):
                if((i<self.ncol and j<self.maxrowlen) or (i>=self.ncol and j>=self.maxrowlen)):
                    matrixrow.append(0)
                else:
                    if(i<self.ncol):
                        matrixrow.append(self.col_legend[i][j-self.maxrowlen]) 
                    else:
                        matrixrow.append(self.row_legend[i-self.ncol][j])       
            self.matrix.append(matrixrow) 
        self.nono_matrix=[[self.matrix[i][j] for j in range(self.maxrowlen,self.matrix_size[1])] for i in range(self.ncol, self.matrix_size[0])]       

    def __str__(self):
        translation = {39: None, 44:None, 91:'[ ', 93:' ]'}  
        return("\n".join(map(str, self.matrix)).translate(translation))
    
    def check(self,matrix):
        pass
        


    def get_surface(self, font, bg_color, text_color): 
        surf=pg.Surface((self.matrix_size[1]*self.tile_size, self.matrix_size[0]*self.tile_size))
        surf.fill(bg_color)
        i = 0
        for i in range(self.matrix_size[0]):
            for j in range(self.matrix_size[1]):
                tile=str(self.matrix[i][j])
                if tile=='0':
                    tile=' '
                tile_text=font.render(str(tile),True,text_color)
                text_rect = tile_text.get_rect()
                pos=(j*self.tile_size, i*self.tile_size)
                tile_size=(self.tile_size, self.tile_size)
                tile_surf=pg.Surface(tile_size)
                tile_surf.fill(bg_color)
                tile_rect=tile_surf.get_rect()
                tile_surf.blit(tile_text,(tile_rect.w//2-text_rect.w//2, tile_rect.h//2-text_rect.h//2))
                surf.blit(tile_surf, pos)
        return surf
        

