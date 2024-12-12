#!python
from itertools import product


def satisfied(val:int, nums:list[int],conc:bool = False)->bool:
    n:int = len(nums)
    ops:list[function] = [(lambda x,y:x+y),(lambda x,y:x*y),(lambda x,y:int(str(x)+str(y)))]
    opsprod = product(*[ops for _ in range(n-1)]) if conc else product(*[ops[:-1] for _ in range(n-1)])
    for opsorder in opsprod:
        res:int = nums[0]
        i = 0
        for op in opsorder:
            res = op(res,nums[i+1])
            i += 1
        if res == val:
            return True    
    
    return False

def part1(vals:list[int],nums:list[list[int]]):
    return(sum(vals[i] for i in range(len(vals)) if satisfied(vals[i],nums[i])))

def part2(vals:list[int],nums:list[list[int]]):
    return(sum(vals[i] for i in range(len(vals)) if satisfied(vals[i],nums[i],True)))

def main()->None:
    with open("./input07_24.txt") as inp:
        data = [d.strip().split(": ") for d in inp.readlines()]
        vals = [int(d[0])  for d in data]
        nums = [list(map(int,d[1].split(" "))) for d in data]
    
    with open("./example07_24.txt") as inp:
        data = [d.strip().split(": ") for d in inp.readlines()]
        exvals = [int(d[0])  for d in data]
        exnums = [list(map(int,d[1].split(" "))) for d in data]

    print(f"Part 1 : {part1(vals,nums)}\nPart 2 : {part2(vals,nums)}")


if __name__ == "__main__":
    main()    