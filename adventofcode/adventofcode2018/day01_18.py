#!python

from itertools import accumulate, cycle


def sol(changes:list[int], part = 1)->int:
    if part == 1:
        return sum(changes)
    else:
        # frequency = 0
        # seen = []
        # i = 0
        # while frequency not in seen:
            # seen.append(frequency)
            # frequency += changes[i%len(changes)]
            # i += 1
        # return frequency
        seen = set()
        return next(f for f in accumulate(cycle(changes)) if f in seen or seen.add(f))
 
def main():
    with open("input01_18.txt") as inp:
        changes = [int(d.strip()) for d in inp.readlines()]

    print(f"Part 1 : {sol(changes)}\nPart 2 : {sol(changes,2)}") 

if __name__ == "__main__":
    main()