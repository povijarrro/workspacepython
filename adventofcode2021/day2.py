#!python
import sys


def getPosition(input, aimed=False):
    pos = [0, 0]
    n = len(input)
    aim = 0
    for i in range(n):
        splitted = input[i].split(" ")
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


pos1 = getPosition(sys.argv[1:], False)
pos2 = getPosition(sys.argv[1:], True)
print(pos1[0] * pos1[1])
print(pos2[0] * pos2[1])
