#!python
import sys


def getBingoPrice(numbers, boards):
    n = len(numbers)
    nb = len(boards)
    value = [sum([sum(boards[j][i]) for i in range(5)]) for j in range(len(boards))]
    inrow = [([0] * 5) for i in range(nb)]
    incol = [([0] * 5) for i in range(nb)]
    for i in range(n):
        for l in range(nb):
            for j in range(5):
                for k in range(5):
                    if numbers[i] == boards[l][j][k]:
                        inrow[l][j] += 1
                        incol[l][k] += 1
                        final = int(numbers[i])
                        value[l] -= int(boards[l][j][k])
                        price = final * value[l]
                        if inrow[l][j] == 5 or incol[l][k] == 5:
                            return price, l
    return 0, -1


print(getBingoPrice([7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1],
                    [[[22, 13, 17, 11, 0],
                      [8, 2, 23, 4, 24],
                      [21, 9, 14, 16, 7],
                      [6, 10, 3, 18, 5],
                      [1, 12, 20, 15, 19]],

                     [[3, 15, 0, 2, 22],
                      [9, 18, 13, 17, 5],
                      [19, 8, 7, 25, 23],
                      [20, 11, 10, 24, 4],
                      [14, 21, 16, 12, 6]],

                     [[14, 21, 17, 24, 4],
                      [10, 16, 15, 9, 19],
                      [18, 8, 23, 26, 20],
                      [22, 11, 13, 6, 5],
                      [2, 0, 12, 3, 7]]]))

print(getBingoPrice([7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21],
                    [[[14, 21, 17, 24, 4],
                      [10, 16, 15, 9, 19],
                      [18, 8, 23, 26, 20],
                      [22, 11, 13, 6, 5],
                      [2, 0, 12, 3, 7]]]))
inp = sys.argv[1:]
numbers = inp[0].split(",") if inp else []
boards = [inp[1:][i:i+5][j].split(" ") for i in range(0, len(inp[1:]), 5) for j in range(5)]
boards = [[x for x in boards[i] if not x == ""] for i in range(len(boards))]
#print(getBingoPrice(numbers, boards))
print(boards)
