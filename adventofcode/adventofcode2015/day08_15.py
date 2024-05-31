#!python

def reallen(s:str)->int:
    real=s[1:-1]
    real=real.replace("\\\\","\\")
    real=real.replace('\\"','"')
    for i in range(256):
        real=real.replace("\\x{:02x}".format(i),"a")
    
    return len(real)

def codelen(s:str)->int:
    res = 0
    for c in s :
        res+=1+(c in '"\\') 

    
    return res+2


def sol(data:list[str],part = 1)->int:
    res=0
    for s in data:
        res+=len(s)-reallen(s) if part == 1 else codelen(s)-len(s)

    return res   

def main():
    with open("input08_15.txt") as inp:
        data = [d.strip() for d in inp.readlines()]

    print(f"Part 1 : {sol(data)}\nPart 2 : {sol(data,2)}")
    codelen('""')

if __name__ == "__main__":
    main()