#!python

def get_children(s:str,start=0,step=1)->set:
    d={"^":(0,1),"v":(0,-1),"<":(-1,0),">":(1,0)}
    children = []
    children.append((0,0))
    for i in range(start,len(s),step):
        children.append((children[-1][0]+d[s[i]][0],children[-1][1]+d[s[i]][1]))

    return set(children)

def sol(data:str,part=1)->int:
    if part==1:
        return len(get_children(data))
    else : return len(get_children(data,step=2).union(get_children(data,start=1,step=2)))    

if __name__ == "__main__":
    with open("input03_15.txt") as inp:
        data=inp.readline() 
    
    print(f"Part 1 : {sol(data)}\nPart 2 : {sol(data,2)}")
        