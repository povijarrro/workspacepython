#!python
def sol(data,part:int=1):
    
    splits = [d.split("-") for d in data]
    ranges = [range(int(a),int(b)+1) for a,b in splits]

    invalids = []

    for r in ranges:
        for n in r:
            l = len(str(n))
            if part == 1:
                if str(n)[:l//2] == str(n)[l//2:]:
                    invalids.append(n)
            elif part == 2:
                for p in range(2, l+1):
                    if str(n) == p*str(n)[:l//p]:
                        invalids.append(n)

    return sum(set(invalids))         

def main()->None:
    
    with open("input02_25.txt") as inp:
        data = [d.strip() for d in inp.readlines()]
        data = data[0].split(",")
    print(f"Part 1 : {sol(data,1)}\nPart 2 : {sol(data,2)}")    

if __name__ == "__main__":
    main()