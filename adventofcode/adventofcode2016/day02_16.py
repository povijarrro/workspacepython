#!python

def get_path(start:tuple,instructions:str,layout:dict[tuple,str])->list[tuple]:
    directions = {"U":(-1,0), "D":(1,0), "L":(0,-1), "R":(0,1)}
    x,y = start
    path = []
    for instr in instructions:
        if (x+directions[instr][0],y+directions[instr][1]) in layout:
            x,y = x+directions[instr][0],y+directions[instr][1]
        path.append((x,y))

    return path    

def sol(data:list[str],part=1) :
    start = (1,1) if part == 1 else (2,0)
    layout = dict()
    if part == 1:
        layout = {(0,0):"1", (0,1):"2", (0,2):"3",
                  (1,0):"4", (1,1):"5", (1,2):"6",
                  (2,0):"7", (2,1):"8", (2,2):"9",}
    else:
        layout = {(0,2):"1", (1,1):"2", (1,2):"3",
                   (1,3):"4", (2,0):"5", (2,1):"6",
                   (2,2):"7", (2,3):"8", (2,4):"9",
                   (3,1):"A", (3,2):"B", (3,3):"C",
                   (4,2):"D"}   
    
    password = ""
    for line in data:
        start = get_path(start,line,layout)[-1]
        password=password+layout[start]

    return password   

if __name__ == "__main__":
    with open("input02_16.txt") as inp:
        data = [d.strip() for d in inp.readlines()]

    print(f"Part 1 : {sol(data)}\nPart 2 : {sol(data,2)}")   