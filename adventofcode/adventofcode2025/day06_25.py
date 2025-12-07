#!python
from functools import reduce


def get_cols(mat:list[list])->list:
    res = []
    for c in range(len(mat[0])):
        res.append([mat[r][c] for r in range(len(mat))])
    return res    

def sol(data,part:int = 1)->int:
    res = 0
    op = ""
    cols = get_cols(data)
    op = cols[0][-1]
    n = int(op == "*")
    for j,c in enumerate(cols):
        if part == 1:    
            res += reduce(lambda x,y:eval(f"{x}{c[-1]}{y}"),c[:-1])
            
        elif part == 2:
            jo = "".join(c[:-1]).strip()
            if j<len(cols)-1:
                if jo:
                    num = int(jo)
                    n=eval(f"{n}{op}{num}")  
                else:
                    res += n
                    op = cols[j+1][-1]
                    n = int(op == "*")
            else:
                num = int(jo)
                n = eval(f"{n}{op}{num}")
                res += n
                 
    return res                 

def main()->None:
    with open("input06_25.txt") as inp:
        data = [s for s in inp.readlines()]
        data = [data[i][:-1] if i < len(data)-1 else data[i] for i in range(len(data))]
        numdata = [[int(s) if s.isdigit() else s for s in d.strip().split()] for d  in data]

    print(f"Part 1 : {sol(numdata,1)}\nPart 2 : {sol(data,2)}")
if __name__ == "__main__":
    main()