#!python

def  swap(freqs,swaps,part=1):
    res = freqs[:]
    for i,(x,y) in enumerate(swaps):
        if part == 1:
            res[y-1],res[x-1] = res[x-1],res[y-1]
        elif part == 2:
            z = swaps[(i+1)%len(swaps)][0]
            res[y-1],res[z-1],res[x-1] = res[x-1],res[y-1],res[z-1]
        elif part == 3:
            less, greater = min(x,y)-1, max(x,y)-1
            length = min(greater-less,len(res)-greater)
            res[greater:greater+length], res[less:less+length] = res[less:less+length], res[greater:greater+length]        
    return res

def main():
    with open("input25_07.txt") as inp:
        data  = [d.strip() for d in inp.readlines()]
        swaps = [tuple(map(int,d.split("-"))) for d in data if "-" in d]
        freqs = [d for d in data[:-1] if d and "-" not in d]
        index = int(data[-1])
    sol1 = swap(freqs,swaps,1)[index-1]
    sol2 = swap(freqs,swaps,2)[index-1]
    sol3 = swap(freqs,swaps,3)[index-1]
    print(f"Part 1 : {sol1}\nPart 2 : {sol2}\nPart 3 : {sol3}")

if __name__ == "__main__" :
    main() 