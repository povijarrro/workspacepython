#!python
from readLines import readLines

def diffs(lst:list[int])->list[int]:
    return [lst[i+1]-lst[i] for i in range(len(lst)-1)]


def next(lst:list[int])->int:
    if lst.count(0)==len(lst):return 0
    return lst[-1]+next(diffs(lst))

def prev(lst:list[int])->int:
    if lst.count(0)==len(lst):return 0
    return lst[0]-prev(diffs(lst))

def solution1(data:list[list[int]])->int:
    return(sum([next(d) for d in data]))

def solution2(data:list[list[int]])->int:
    return sum([prev(d) for d in data])

def main():
    data = readLines("input09_23.txt")
    data = [list(map(int,d.split())) for d in data]

    print(f"Part 1 : {solution1(data)}")
    print(f"Part 2 : {solution2(data)}")

if __name__ == "__main__":
    main()