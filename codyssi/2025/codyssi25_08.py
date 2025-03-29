#!python
def reduced(s:str, part = 2):
    for i, c in enumerate(s):
        condition = False
        if part == 2:
            condition = ((c.isdigit() and (s[i-1].isalpha() or s[i-1] == "-")) or ((c.isalpha()  or c == "-") and s[i-1].isdigit()))
        elif part == 3:
            condition = (c.isdigit() and s[i-1].isalpha()) or (c.isalpha() and s[i-1].isdigit())    
        if condition:
            if 0<=i-1:
                return reduced(s[:i-1]+s[i+1:],part)   
    return s

def main():
    with open("example25_08.txt") as inp:
        data:list[str] = [d.strip() for d in inp.readlines()]
        print(data)
    sol1 = sum(sum(c.isalpha() for c in s) for s in data)
    sol2 = sum(len(reduced(d,2)) for d in data)
    sol3 = sum(len(reduced(d,3)) for d in data)

    print(f"Part 1 : {sol1}\nPart 2 : {sol2}\nPart 3 : {sol3}")
if __name__ == "__main__" :
    main() 