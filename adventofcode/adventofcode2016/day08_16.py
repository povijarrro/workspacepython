#!python
from copy import deepcopy

def to_string(display:list[list[str]])->str:
    return "".join(["".join(d)+"\n" for d  in display])[:-1]


def rect(display:list[list[str]],dim:tuple[int,int])->list[list[str]]:
    dis = deepcopy(display)
    for i in range(dim[0]):
        for j in range(dim[1]):
            dis[i][j]="#"
    
    return dis

def rotate(display:list[list[str]],index:int,by:int,col=False)->list[list[str]]:
    dis = deepcopy(display)
    if not col :
        for j in range(len(display[index])):
            dis[index][(j + by) % len(display[index])] = display[index][j]

    else:
        for i in range(len(display)):
            dis[(i + by) % len(display)][index] = display[i][index]
    
    return dis

def change(display:list[list[str]],instructions:list[str])->list[list[str]]:
    dis = deepcopy(display)
    for instr in instructions:
        if "rect" in instr:
            d2,d1=[int(s) for s in instr[5:].split("x")] 
            dis = rect(dis,(d1,d2))
        else :
            spl = instr.split("=")[1].split(" by ")
            index,by = map(int,spl)
            dis = rotate(dis,index,by,"column" in instr)
      
    return dis

def sol(instructions:list[str],part=1)->int|str:
    display = []
    for _ in range(6):
        row = []
        for _ in range(50):
            row.append(" ")
        display.append(row)

    display = change(display,instructions)
    if part == 1:
        res = 0
        for pixels in display:
            for pixel in pixels:
                res += pixel == "#"   
        
        return res
    else :
        return to_string(display)
    
if __name__ == "__main__":
    with open("input08_16.txt") as inp:
        instructions = [d.strip() for d in inp.readlines()]
    
    display = []
    for _ in range(6):
        row = []
        for _ in range(50):
            row.append(" ")
        display.append(row)    

    print(f"Part 1 : {sol(instructions)}\nPart 2 : \n{sol(instructions,2)}")