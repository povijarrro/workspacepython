#!python
from math import gcd

def duplicities(c):
    d = {}
    for i in c:
        if i in d:
            if d[i]:
                yield i
                d[i] = False
        else:
            d[i] = True


def line(A, B):
    res = [A]
    ax = A[0]
    ay = A[1]
    bx = B[0]
    by = B[1]
    dy = by - ay
    dx = bx - ax
    g = gcd(dy, dx)
    if g > 1:
        for i in range(1, g):
            res.append((ax + i * dx // g, ay + i * dy // g))
    if res[-1] != B:
        res.append(B)
    return res


def numberOfDangerousPoints(lines, diagonal = False):
    points = []
    for i in lines:

         for point in line(i[0], i[1]):
             if diagonal:
                 points.append(point)
             else:
                 if i[0][0] == i[1][0] or i[0][1] == i[1][1]:
                     points.append(point)


    return len(list(duplicities(points)))


def sol(data, part = 1):
    lines = [d.split(" -> ") for d in data]
    lines = [[eval(p) for p in d] for d in lines]
    return numberOfDangerousPoints(lines,part != 1)

def main():
    with open("input05_21.txt") as inp:
        data = [d.strip() for d in inp.readlines()]

    print(f"Part 1 : {sol(data)}\nPart 2 : {sol(data,2)}")

if __name__ == "__main__":
    main()