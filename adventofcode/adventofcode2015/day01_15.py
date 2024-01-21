#!python

def get_floor(data:str)->int:
    floor = 0
    base = 0
    d = {"(":1,
         ")":-1}
    for i,c in enumerate(data):
        floor += d[c]
        if base == 0:
            if floor == -1:
                base = i+1
    return floor, base

def sol(data:str,part=1)->int:
    return get_floor(data)[part-1]

if __name__ == "__main__":
    with open("input01_15.txt") as inp:
        data = inp.readlines()[0]

    print(f"Part 1 : {sol(data,1)}\nPart 2 : {sol(data,2)}") 