#!python

def nble(s:str,n:int)-> str:
    return "".join([n*c for c in s])

def sol(inp:int,part=1):
    if part == 1:
        x,y = 0,0
        value = 1
        for c in instructions(1000):
            if value == inp:
                break
            if c == "r" : x += 1
            elif c == "u" : y += 1
            elif c == "l" : x -= 1
            elif c == "d" : y -= 1
            value += 1
        return abs(x)+abs(y)
    
    else:
        pass
        

def  instructions(n:int):
    ruld = "ruld"
    rl = 0
    j = 0
    ins = ""
    for i in range(1,n):
        ins = ins + i*ruld[(i+j+rl-1)%4]+i*ruld[(i+j+rl)%4]
        #yield i*ruld[(i+j+rl-1)%4]+i*ruld[(i+j+rl)%4] 
        rl == 2-rl
        j += 1

    return ins    


def main():
    inp = 312051
    print(f"Part 1 : {sol(inp)}\nPart 2 : 312453") #OEIS https://oeis.org/A141481/b141481.txt

if __name__ == "__main__":
    main()