#!python

def decrypt(s:str, shift:int)->str:
    return s.translate({i:(i+shift%26) if 97<=i+shift%26<=122 else i+shift%26-26   for i in range(97,123)})

def sol(encrs:list[str],checksums:list[str],ids:list[int],part = 1)->int:
    if part == 1: 
        res = 0
        for i in range(len(encrs)):
            s = "".join(sorted(list(set("".join(encrs[i]))), key = lambda c:("".join(encrs[i]).count(c),-ord(c)),reverse=True)[:5])
            if s==checksums[i]:
                res += ids[i]

        return res
    else:
        for i in range(len(encrs)):
            names = []
            for s in encrs[i]:
                names.append(decrypt(s,ids[i]))
            
            real_name = " ".join(names)
            if  "north" in real_name:
                return ids[i]


     
def main():
    with open("input04_16.txt") as inp:
        rooms = [r.strip() for r in inp.readlines()]
        spl = [r.split("-") for r in rooms]
        encrs = [s[:-1] for s  in spl]
        ids = [int(s[-1].split("[")[0]) for s in spl]
        checksums = [s[-1].split("[")[-1][:-1] for s in spl]

    print(f"Part 1 : {sol(encrs,checksums,ids)}\nPart 2 : {sol(encrs,checksums,ids,2)}")

if __name__ == "__main__":
    main()    