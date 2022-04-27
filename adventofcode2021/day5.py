#!python
import itertools
from math import gcd
import sys


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
    res = [(str(A[0]), str(A[1]))]
    ax = int(A[0])
    ay = int(A[1])
    bx = int(B[0])
    by = int(B[1])
    dy = by - ay
    dx = bx - ax
    g = gcd(dy, dx)
    if g > 1:
        for i in range(1, g):
            res.append((str(ax + i * dx // g), str(ay + i * dy // g)))
    if not ((res[-1]) == (str(B[0]), str(B[1]))):
        res.append((str(B[0]), str(B[1])))
    return res


def numberOfDangerousPoints(lines, diagonal = False):
    points = []
    for i in lines:

         for point in line(i[0], i[1]):
             if diagonal:
                 points.append((point[0], point[1]))
             else:
                 if str(i[0][0]) == str(i[1][0]) or str(i[0][1]) == str(i[1][1]):
                     points.append((point[0], point[1]))


    return len(list(duplicities(points)))

testlines = [[("0", "9"), ("5", "9")],
             [("8", "0"), ("0", "8")],
             [("9", "4"), ("3", "4")],
             [("2", "2"), ("2", "1")],
             [("7", "0"), ("7", "4")],
             [("6", "4"), ("2", "0")],
             [("0", "9"), ("2", "9")],
             [("3", "4"), ("1", "4")],
             [("0", "0"), ("8", "8")],
             [("5", "5"), ("8", "2")]]

lines = sys.argv[1:]
lines = [[(y.split(",")[0], y.split(",")[1]) for y in x.split(" -> ")] for x in lines]
print(numberOfDangerousPoints(testlines, True))
print(numberOfDangerousPoints(lines, True))
