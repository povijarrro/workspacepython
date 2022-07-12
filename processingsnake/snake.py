import copy

class Snake:
    def __init__(self, body, head):
        self.head=copy.deepcopy(head)
        self.body=copy.deepcopy(body)
        
    def move(self, direction):
        self.head=copy.deepcopy(self.head)
        new_head=[self.head[0]+direction[0], self.head[1]+direction[1]]
        if self.body != []:
            
            self.body=copy.deepcopy(self.body[1:])
            self.body.append(copy.deepcopy(self.head))
                
        self.head=new_head        
            
    def increase(self, tile):
        self.body.append(copy.deepcopy(self.head))
        self.head=copy.deepcopy(tile)
                    
