#!python
def value(c:str):
    if c.islower():
        return ord(c)-ord("a")+1
    elif not c.isalpha():
        return 0
    else:
        return ord(c)-ord("A")+27

def corvalue(i,s):
    if s[i].isalnum():
        return value(s[i])
    else:
        return (2*corvalue(i-1,s)-5)%52


def main():
    with open("input25_06.txt") as inp:
        data  = [d.strip() for d in inp.readlines()]
        data = data[0]
    print(data)
    sol1 = len("".join(c for c in data if c.isalnum()))
    sol2 = sum(map(value,data))
    sol3 = sum(map(lambda i:corvalue(i,data),range(len(data))))
    print(f"Part 1 : {sol1}\nPart 2 : {sol2}\nPart 3 : {sol3}")

if __name__ == "__main__" :
    main() 