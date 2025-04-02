#!python
def base_65(n):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#"
    m = n
    res = ""
    while m > 0:
        s = m%65
        m = m//65
        res = digits[s]+res
    return res    

def main():
    with open("input24_03.txt") as inp:
        data:list[str] = [d.strip() for d in inp.readlines()]
        bases = [int(d.split()[1]) for d in data]
        values = [int(d.split()[0],int(d.split()[1])) for d in data]
    
    

    sol1 = sum(bases)
    sol2 = sum(values)
    sol3 = base_65(sol2)

    print(f"Part 1 : {sol1}\nPart 2 : {sol2}\nPart 3 : {sol3}")
if __name__ == "__main__" :
    main() 