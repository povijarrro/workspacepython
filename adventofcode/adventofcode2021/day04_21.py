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


def sol(data,part = 1):
    numbers = data[0].split(",") if data else []
    numbers = [int(n) for n in numbers]
    boards = [b for b in data[2:] if b != ""]
    boards = [boards[i:i + 5][j].split() for i in range(0, len(boards), 5) for j in range(5)]
    boards = [[int(x) for x in boards[i]] for i in range(len(boards))]
    boards = [boards[i:i + 5] for i in range(0, len(boards), 5)]
    
    return getBingoPrice(numbers, boards, part != 1)

def main():
    with open("input04_21.txt") as inp:
        data = [d.strip() for d in inp.readlines()]
    
    print(f"Part 1 : {sol(data)}\nPart 2 : {sol(data,2)}")

if __name__ == "__main__":
    main()        