#!python
from collections import Counter

def pair(p:str)->int:
        c:Counter = Counter(p)
        if "x" in p:
            return c["B"]+3*c["C"]+5*c["D"]
        else :
            return c["A"]+2*c["B"]+4*c["C"]+6*c["D"]
        
def tripple(p:str)->int:
        c:Counter = Counter(p)
        bonus:int = 2 - c["x"]
        return bonus*c["A"]+(1+bonus)*c["B"]+(3+bonus)*c["C"]+(5+bonus)*c["D"]

def part1(data:str)->int:
    c:Counter = Counter(data)
    return c["B"]+3*c["C"]

def part2(data:str)->int:
    pairs = [data[i]+data[i+1] for i in range(0,len(data)-1,2)]   
    return sum([pair(p) for p in pairs])

def part3(data:str)->int:
    tripples = [data[i]+data[i+1]+data[i+2] for i in range(0,len(data)-2,3)]   
    return sum([tripple(t) for t in tripples])
     
def main()->None:
    with open("./in01_24_1.txt") as inp:
        data1:str = inp.readline().strip()

    with open("./in01_24_2.txt") as inp:
        data2:str = inp.readline().strip()

    with open("./in01_24_3.txt") as inp:
        data3:str = inp.readline().strip()
    

    print(f"Part 1 : {part1(data1)}\nPart 2 : {part2(data2)}\nPart 3 : {part3(data3)}")

if __name__ == "__main__":
    main()