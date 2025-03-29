#!python
def main():
    with open("input25_02.txt") as inp:
        data = [d.strip() for d in inp.readlines()]
        add, mul, power = int(data[0].split()[-1]), int(data[1].split()[-1]),int(data[2].split()[-1]) 
        qualities = sorted(int(d) for d in data[4:])
        fun = lambda x:add+mul*(x**power)
        median = qualities[len(qualities)//2]
        sol1 = fun(median)
        sol2 = fun(sum(q for q in qualities if q%2 == 0))
        CAN_PAY = 15000000000000
        sol3 = max(q for q in qualities if fun(q)<=CAN_PAY)
    print(f"Part 1 : {sol1}\nPart 2 : {sol2}\nPart 3 : {sol3}")      

if __name__ == "__main__":
    main()

