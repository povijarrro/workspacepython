#!python
import regex
def intervals(runes:list[str], text:str , cyc:bool = False)->list[tuple[int,int]]:
    ints:list[tuple[int,int]] = []
    n = len(text)
    for r in runes:
        rfi = regex.finditer(r,(1+cyc)*text, overlapped = True)
        rfi2 = regex.finditer(r[::-1],(1+cyc)*text, overlapped = True)
        ints += [(rf.span()[0]%n,rf.span()[1]%n) if rf.span()[1]>n else rf.span() for rf in rfi if rf.span()[0]<n]
        ints += [(rf.span()[0]%n,rf.span()[1]%n) if rf.span()[1]>n else rf.span() for rf in rfi2 if rf.span()[0]<n] 
    return ints

def interval_union(intervals:list[tuple[int,int]],max_length:int)->set[int]:
    as_set:list[set[int]] = [set(range(max_length)).difference(set(range(interval[1],interval[0]))) if interval[0]>interval[1] else set(range(interval[0],interval[1])) for interval in intervals]
    u:set[int] = set()
    for v in as_set:
        u = u.union(v)
    return u
 
def ind_of_sym(runes:list[str],text:str)->int:
    return interval_union(intervals(runes,text),len(text))

def column(texts:list[str],c:int)->str:
    return "".join([t[c] for t in texts])

def transpose(texts:list[str]):
    m = len(texts[0])
    return [column(texts,j) for j in range(m)]

def cycled_highlighted(runes:list[str],text:str,cyc:bool=True)->set[int]:
    n = len(text)
    return(interval_union(intervals(runes,text,cyc),n))

def highlighted(runes:list[str],texts:list[str], trans:bool = False,cyc:bool = True)->set[tuple[int,int]]:
    if not trans:
        hl:set[tuple[int,int]] = set()
        n:int = len(texts)
        for i in range(n):
            hl = hl.union({(i,j) for j in cycled_highlighted(runes,texts[i],cyc)})
        return hl                   
    else:
        thl = highlighted(runes,transpose(texts),False,False)
        thl = {(t[1],t[0]) for t in thl}
        return thl
   
   
def part1(runes:list[str],text:str)->int:
    return sum([len(regex.findall(r,text,overlapped=True)) for r in runes])

def part2(runes:list[str],texts:list[str])->int:
    return sum([len(ind_of_sym(runes,t)) for t in texts])


def part3(runes:list[str],texts:list[str])->int:
    return len(highlighted(runes,texts).union(highlighted(runes,texts,True,False)))
    
def main()->None:
    with open("./in02_24_1.txt") as inp:
        lines:list[str] = inp.readlines()
        runes1:str = lines[0].strip()[6:]
        runes1 = runes1.split(",")
        text1:str = lines[-1].strip()


    with open("./in02_24_2.txt") as inp:
        lines:list[str] = inp.readlines()
        runes2:str = lines[0].strip()[6:]
        runes2 = runes2.split(",")
        texts2:list[str] = [l.strip() for l in lines[2:]]


    with open("./in02_24_3.txt") as inp:
        lines:list[str] = inp.readlines()
        runes3:str = lines[0].strip()[6:]
        runes3 = runes3.split(",")
        texts3:str = [l.strip() for l in lines[2:]]


    print(f"Part 1 : {part1(runes1,text1)}\nPart 2 : {part2(runes2,texts2)}\nPart 3 : {part3(runes3,texts3)}")
    

if __name__ == "__main__":
    main()