#!python

def sol(triangles:list[list],part=1)->int:
    if part == 1 : return sum([t[0]+t[1]>t[2] for t in [sorted(t) for t in triangles]])
    else :
        res = 0
        for i in range(0,len(triangles)-2,3):
            for j in range(len(triangles[i])):
                t = sorted([triangles[i][j],triangles[i+1][j],triangles[i+2][j]])
                if t[0]+t[1]>t[2]:res+=1
        
        return res


if __name__ == "__main__":
    with open("input03_16.txt") as inp:
        triangles = [[int(i) for i in d.strip().split()] for d in inp.readlines()]

    print(f"Part 1 : {sol(triangles)}\nPart 2 : {sol(triangles,2)}")   