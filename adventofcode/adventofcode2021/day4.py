#!python
import sys


def Bingo(numbers, board):
    n = len(numbers)
    inrow = [0] * 5
    incol = [0] * 5
    value = sum([sum(board[i]) for i in range(5)])
    for i in range(n):
        for j in range(5):
            for k in range(5):
                if numbers[i] == board[j][k]:
                    inrow[j] += 1
                    incol[k] += 1
                    value -= board[j][k]
                    price = numbers[i] * value
                    if inrow[j] == 5 or incol[k] == 5:
                        return i, price
    return -1, 0



def getBingoPrice(numbers, boards, last = False):
    nb = len(boards)
    res = []
    for l in range(nb):
        b = Bingo(numbers, boards[l])
        res.append(b)

    res.sort()
    return res[-last][1] if res else 0


testnum = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
testboards = [[[22, 13, 17, 11, 0],
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
               [2, 0, 12, 3, 7]]]


print(getBingoPrice(testnum, testboards))

inp = sys.argv[1:]
numbers = inp[0].split(",") if inp else []
numbers = [int(numbers[i]) for i in range(len(numbers))]
boards = inp[1:]
boards = [boards[i:i + 5][j].split(" ") for i in range(0, len(inp[1:]), 5) for j in range(5)]
boards = [[x for x in boards[i] if not x == ""] for i in range(len(boards))]
boards = [[int(x) for x in boards[i]] for i in range(len(boards))]
boards = [boards[i:i + 5] for i in range(0, len(boards), 5)]

print(getBingoPrice(numbers, boards, True))
