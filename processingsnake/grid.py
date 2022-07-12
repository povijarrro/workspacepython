import copy
from snake import Snake

class Grid:
    def __init__(self,canvas_size, grid_array, snake):
        self.canvas_size=canvas_size
        self.snake = Snake(copy.deepcopy(snake.body), copy.deepcopy(snake.head))
        self.grid_array = copy.deepcopy(grid_array)
        self.grid_size = (len(self.grid_array),len(self.grid_array[0]))
        self.w = float(self.canvas_size[0])/self.grid_size[1]
        self.h = float(self.canvas_size[1])/self.grid_size[0]
        self.grid_array[snake.head[0]][snake.head[1]]=2
        for ele in self.snake.body:
            self.grid_array[ele[0]][ele[1]]=1 
        self.generate_food()    
        
    def draw_grid(self):
        x,y=0,0
        for row in self.grid_array:
            for ele in row: 
                if ele == 0:
                    fill(255)
                elif ele == 1:
                    fill(0)     
                elif ele == 2:
                    fill(127)
                else:
                    fill(255,0,0)                    
                rect(x, y, self.w, self.h)
                x+=self.w
            y+=self.h
            x=0   
     
    def update(self, snake):
        self.snake=Snake(copy.deepcopy(snake.body), copy.deepcopy(snake.head))
    
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                if self.grid_array[i][j]!=3:
                    self.grid_array[i][j]=0
                        
        for ele in self.snake.body:
            self.grid_array[ele[0]][ele[1]]=1
        
        self.grid_array[self.snake.head[0]][self.snake.head[1]]=2
        self.draw_grid()
        
    def generate_food(self):

        while True:
            x,y=int(random(self.grid_size[0])), int(random(self.grid_size[1]))
            if self.grid_array[x][y] != 0:
                continue
            self.grid_array[x][y]=3    
            break
    
    def snake_move(self, direction):
        
        new_head=[self.snake.head[0]+direction[0], self.snake.head[1]+direction[1]]
        
        if self.grid_array[new_head[0]][new_head[1]]==3:
            self.snake.increase(copy.deepcopy(new_head))
            self.generate_food()
        elif new_head in self.snake.body or new_head[0]<0 or new_head[1]<0 or new_head[0]==self.grid_size[0] or new_head[1]==self.grid_size[1]:
            print("GAME OVER! Score is"+str(len(self.snake.body)))
            self.snake.head=[self.grid_size[0]/2, self.grid_size[1]/2]
            self.snake.body=[]
        else:
            self.snake.move(direction)    
        self.update(self.snake)   
        
        
                            
         
            
