#!python
def main():
    with open("input24_01.txt") as inp:
        data:list[str] = [d.strip() for d in inp.readlines()]
        prices = [int(d) for d in data]
    sol1 = sum(prices)
    sol2 = sum(sorted(prices,reverse = True)[20:])
    sol3 = sum(p*(-1)**i for (i,p) in enumerate(prices))

    print(f"Part 1 : {sol1}\nPart 2 : {sol2}\nPart 3 : {sol3}")
if __name__ == "__main__" :
    main() 