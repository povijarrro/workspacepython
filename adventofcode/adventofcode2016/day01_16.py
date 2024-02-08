#!python

def get_path(start:tuple, instructions:list[str])->list[tuple]:
    directions = {"L":90, "R":-90}
    changes = {0:(1,0), 90:(0,1), 180:(-1,0), 270:(0,-1)}
    x,y,d = start
    path = []
    path.append((x,y))
    for instr in instructions:

        d = (d + directions[instr[0]])%360
        for _ in range(int(instr[1:])):
            x,y = x+changes[d][0],y+changes[d][1]
            path.append((x,y))
    
    return path
        
def sol(start:tuple,instructions:list[str],part=1):
    path = get_path((0,0,90),instructions)
    x,y = path[-1]
    if part != 1 :
        counts=[(path.count(coords),coords[0],coords[1]) for coords in path]
        _,x,y = [t for t in counts if t[0]>=2][0]
         
    return abs(x-start[0])+abs(y-start[1])

if __name__ == "__main__":
    with open("input01_16.txt") as inp:
        instructions = inp.readline().strip().split(", ")

    print(f"Part 1 : {sol((0,0,90),instructions)}\nPart 2 : {sol((0,0,90),instructions,2)}")   


