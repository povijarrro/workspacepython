#!python

def output(program:list[int],intcodes:tuple)->int:
    p = program.copy()
    p[1],p[2] = intcodes
    for i in range(len(program)//4+1):
        if p[4*i] == 99:
            return p[0]
        elif p[4*i] == 1:
            p[p[4*i+3]] = p[p[4*i+1]]+p[p[4*i+2]]
        elif p[4*i] == 2:
            p[p[4*i+3]] = p[p[4*i+1]]*p[p[4*i+2]]
    return p[0]


def sol(program:list[int],part = 1)->int:
    if part == 1:
        return output(program,(12,2))
    else:
        for noun in range(100):
            for verb in range(100):
                if output(program,(noun,verb)) == 19690720:
                    return 100*noun+verb


def main():
    with open("input02_19.txt") as inp:
        program = list(map(int,inp.readline().strip().split(",")))
    
    print(f"Part 1 : {sol(program)}\nPart 2 : {sol(program,2)}")

if __name__ == "__main__":
    main()    