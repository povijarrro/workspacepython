#!python
def fuel(n:int,part = 1)->int:
    if part == 1:
        return max(0,n//3 - 2)
    else:
        m = n//3 -2
        if m<=0:
            return 0
        else:
            return m +fuel(m,part)

def sol(data:list[int],part = 1)->int:
    return sum([fuel(d,part) for d in data])

def main():
    with open("input01_19.txt") as inp:
        data = [int(d.strip()) for d in inp.readlines()]
    
    print(f"Part 1 : {sol(data)}\nPart 2 : {sol(data,2)}")  

if __name__ == "__main__":
    main()      