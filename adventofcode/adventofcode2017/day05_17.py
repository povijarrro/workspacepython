#!python

def sol(instructions:list[int],part=1)->int:
    ins = instructions.copy()
    if part == 1 :
        i = 0
        steps = 0
        while i<len(ins):
            ins[i] += 1
            i += ins[i]-1
            steps += 1

    else:
        i = 0
        steps = 0
        while i<len(ins):
            if ins[i]<3 :
                ins[i] += 1
                i += ins[i]-1
            else:
                ins[i] -= 1
                i += ins[i]+1    
            steps += 1

    return steps


def main():
    with open("input05_17.txt") as inp:
        instructions = [int(d.strip()) for d in inp.readlines()]

    print(f"Part 1 : {sol(instructions)}\nPart 2 : {sol(instructions,2)}")

if __name__ == "__main__":
    main()