#!python
from collections import Counter

def part1(left:list[int],right:list[int])->int:
    return sum([abs(sorted(left)[i]-sorted(right)[i]) for i in range(len(left))])

def part2(left:list[int], right:list[int])->int:
    c=Counter(right)
    return sum([left[i]*c[left[i]] for i in range(len(left))])

def main()->None:
    with open("./input01_24.txt") as inp:
        data = [d.strip().split() for d in inp.readlines()]
        left = [int(d[0]) for d in data]
        right = [int(d[1]) for d in data]
    
    print(f"Part 1 : {part1(left,right)}\nPart 2 : {part2(left,right)}")

if __name__ == "__main__":
    main()