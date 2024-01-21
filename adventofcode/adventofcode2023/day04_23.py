#!python
from readLines import readLines

def nOfMatches(win:set,play:set)->int:
    return len(win.intersection(play))

def score(win:set,play:set)->int:
    nom=nOfMatches(win,play)
    return 2**(nom-1) if nom>=1 else 0

def solution1(data:list[list[set]])->int:
    return sum([score(i[0],i[1]) for i in data])

def solution2(data:list[list[set]])->int:
    copies = len(data)*[1]
    for i,row in enumerate(data):
        n=nOfMatches(row[0],row[1])
        for j in range(i+1,min(len(data),i+1+n)):
            copies[j]+=copies[i]
        
    return sum(copies)


if __name__=="__main__":
    data = readLines("input04.txt")
    data = [i.split("|") for i in data]
    for row in data:
        row[0]=set(row[0][row[0].index(":")+2:].strip().split(" "))
        row[1]=set(row[1].strip().split(" ")).difference(set([""]))

    print(f"Part 1 : {solution1(data)}")
    print(f"Part 2 : {solution2(data)}")
