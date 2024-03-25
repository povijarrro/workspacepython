#!python

from collections import Counter
from itertools import combinations


def sol(ids:list[str],part = 1)->int|str:
    if part == 1 :
        return sum(2 in Counter(id).values() for id in ids)*sum(3 in Counter(id).values() for id in ids)
    else :
        close = [c for c in combinations(ids,2) if len([i for i in range(len(c[0])) if c[0][i] != c[1][i]]) == 1][0]
        print(close)
        i = [j for j in range(len(close[0])) if close[0][j] != close[1][j]][0]
        return close[0][:i]+close[1][i+1:]

if __name__ == "__main__":
    with open("input02_18.txt") as inp:
        ids = [d.strip() for d in inp.readlines()]

    print(f"Part 1 : {sol(ids)}\nPart 2 : {sol(ids,2)}")  