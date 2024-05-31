#!python
from collections import Counter

def after_n_days(states:list[int], n:int)->int:
    c = Counter(states)
    c = [c[t] for t in range(9)]
    for _ in range(n):
        nc = c[1:]
        nc.append(c[0])
        nc[6] = c[0] + c[7]
        c = nc
    return sum(c) 

def sol(data, part = 1):
    n = 80 if part == 1 else 256
    return after_n_days(data,n)

def main():
    with open("input06_21.txt") as inp:
        data = [int(s) for s in inp.readline().strip().split(",")]
    print(f"Part 1 : {sol(data)}\nPart 2 : {sol(data,2)}")    

if __name__ == "__main__":
    main()