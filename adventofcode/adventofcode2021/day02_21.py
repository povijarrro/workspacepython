#!python

def getPosition(data, aimed=False):
    pos = [0, 0]
    n = len(data)
    aim = 0
    for i in range(n):
        splitted = data[i].split(" ")
        match splitted[0]:
            case "forward":
                pos[0] += int(splitted[1])
                if aimed:
                    pos[1] += int(splitted[1])*aim
            case "up":
                if not aimed:
                    pos[1] -= int(splitted[1])
                else:
                    aim -= int(splitted[1])
            case "down":
                if not aimed:
                    pos[1] += int(splitted[1])
                else:
                    aim += int(splitted[1])

    return pos

def sol(data, part = 1):
    pos = getPosition(data,part != 1)
    return pos[0]*pos[1]

def main():
    with open("input02_21.txt") as inp:
        data = [d.strip() for d in inp.readlines()]
    print(f"Part 1 : {sol(data)}\nPart 2 : {sol(data,2)}")


if __name__ == "__main__":
    main()