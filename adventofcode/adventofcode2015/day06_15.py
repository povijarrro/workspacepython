#!python

def new_lights(instruction:str, lights:list[list[bool]], bright:list[list[int]])->list[list[bool]]:
    nl=[]
    op=""
    br = []
    for i in range(len(lights)):
        rownl = []
        rowbr = []
        for j in range(len(lights[i])):
            rownl.append(lights[i][j])
            rowbr.append(bright[i][j])
        nl.append(rownl)
        br.append(rowbr)
    
    if "on" in instruction:
        spl = "".join(instruction.split(" on ")[1:]).split(" through ")
        start = [int(s) for s in spl[0].split(",")] 
        end = [int(s) for s in spl[1].split(",")]
        op = "on"
        
    elif "off" in instruction:
        spl = "".join(instruction.split(" off ")[1:]).split(" through ")
        start = [int(s) for s in spl[0].split(",")] 
        end = [int(s) for s in spl[1].split(",")]
        op = "off"
        
    else:
        spl = "".join(instruction[7:]).split(" through ")
        start = [int(s) for s in spl[0].split(",")] 
        end = [int(s) for s in spl[1].split(",")]
        op = "toggle"
        
    for i in range(start[0], end[0]+1):
        for j in range(start[1],end[1]+1):
            if op=="on":
                nl[i][j] = True
                br[i][j] += 1
            elif op =="off":
                nl[i][j] = False
                if br[i][j]>0:br[i][j]-= 1
            else: 
                nl[i][j] = not nl[i][j]
                br[i][j] += 2 
 
    return nl,br

def sol(data:list[str], part=1)->int:
    lights = []
    brights = []
    for _ in range(1000):
        rowl = []
        rowb = []
        for _ in range(1000):
            rowl.append(False)
            rowb.append(0)
        lights.append(rowl)
        brights.append(rowb)

    for d in data:
        lights,brights=new_lights(d,lights,brights)

    return (sum([sum(l) for l in lights]), sum([sum(b) for b in brights]))[part-1]   

def main():
    with open("input06_15.txt") as inp:
        data = [d.strip() for d in inp] 
    
    
    print(f"Part 1 : {sol(data)}\nPart 2 : {sol(data,2)}")

if __name__ == "__main__":
    main()