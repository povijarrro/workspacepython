#!python
import regex
def muls(data:str,do:bool = False)->list[str]:
    if not do:
        return regex.findall("mul\\([0-9]*,[0-9]*\\)",data)
    else:
        return regex.findall("mul\\([0-9]*,[0-9]*\\)|do\\(\\)|don't\\(\\)",data)

def part1(data:str)->int:
    return sum(int(m[4:len(m)-1].split(",")[0])*int(m[4:len(m)-1].split(",")[1]) for m in muls(data))

def part2(data:str)->int:
    ms1:list[str] = muls(data,True)
    ms:list[str] = []
    rem=False
    for m in ms1:
        if m.startswith("mul"):
            if not rem:
                ms.append(m)
        else:
            if m == "don't()":
                rem = True
            else:
                rem = False    

    return sum(int(m[4:len(m)-1].split(",")[0])*int(m[4:len(m)-1].split(",")[1]) for m in ms)               

def main()->None:
    with open("./input03_24.txt") as inp:
        data:str = inp.read().strip()
    
    print(f"Part 1 : {part1(data)}\nPart 2 : {part2(data)}")    

    
if __name__ == "__main__":
    main()    