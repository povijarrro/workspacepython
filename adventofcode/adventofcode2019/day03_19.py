#!python

def get_path(instr:list[str],start = (0,0))->list[tuple]:
    path = [start]
    for ins in instr:
        dir, value = ins[0],int(ins[1:])
        for _ in range(value):
            match dir:
                case "R":
                    path.append((path[-1][0]+1,path[-1][1]))
                case "L":
                    path.append((path[-1][0]-1,path[-1][1])) 
                case "U":
                    path.append((path[-1][0],path[-1][1]+1))
                case "D":
                    path.append((path[-1][0],path[-1][1]-1))                   
    return path[1:]

def sol(instructions:list[list[str]],part = 1)->int:
    p1,p2 = get_path(instructions[0]),get_path(instructions[1])
    cross = sorted(list(set(p1) & set(p2)),key=lambda x:abs(x[0])+abs(x[1]))
    if part == 1:
        return abs(cross[0][0])+abs(cross[0][1])
    else:
        res = p1.index(cross[0])+1+p2.index(cross[0])+1
        for c in cross:
            steps = p1.index(c)+1+p2.index(c)+1
            if steps<res:
                res = steps
        return res


if __name__ == "__main__":
    with open("input03_19.txt") as inp:
        instructions = [d.strip().split(",") for d in inp.readlines()]

    print(f"Part 1 : {sol(instructions)}\nPart 2 : {sol(instructions,2)}")
