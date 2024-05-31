#!python

import itertools


def is_in(item:list[int],lst:list[list[int]])-> bool:
    for l in lst:
        if l == item : return True

    return False    


def sol(banks:list[int],part = 1)->int:
    bnks = banks.copy()
    n = len(bnks)
    states = [bnks.copy()]
    steps = 0
    while True:
        i = bnks.index(max(bnks))
            
        bnks2=bnks.copy()
        bnksi = bnks[i]
        bnks2[i] = 0

        for k in range(i+1,i+1+bnksi):
            bnks2[k%n] += 1
        bnks = bnks2
        if is_in(bnks,states) :
            return (steps+1) if part == 1 else sol(bnks)

        states.append(bnks2)
        steps += 1

         
def main():
    with open("input06_17.txt") as inp:
        banks = list(map(int,inp.readline().strip().split()))

    print(f"Part 1 : {sol(banks)}\nPart 2 : {sol(banks,2)}")

if __name__ == "__main__":
    main()