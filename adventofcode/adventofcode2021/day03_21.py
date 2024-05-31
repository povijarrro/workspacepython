#!python
from statistics import multimode, mode

def columns(l):
    n = len(l)
    ll = [len(l[i]) for i in range(n)]
    if ll:
        m = min(ll)
    else:
        m = 0
    res = [[l[i][j] for i in range(n)] for j in range(m)]

    return res


def getPowerConsumption(data):
    cols = columns(data)
    nc = len(cols)
    gamma = 0
    eps = 0
    for i in range(nc):
        m = int(mode(cols[i]))
        gamma = 2 * gamma + m
        eps = 2 * eps + 1 - m

    return gamma * eps


def getRating(inp, t):
    newinp = inp
    j = 0
    if t == "ox" or t == "co2":
        while len(newinp) > 1:
            cols = columns(newinp)
            m = int(max(multimode(cols[j])))
            ninp = []
            n = len(newinp)
            for i in range(n):
                if int(newinp[i][j]) == (m if t == "ox" else (1-m)):
                    ninp.append(newinp[i])
            newinp = ninp
            j += 1
        return newinp[0]
    else:
        return int(getRating(inp, "ox"), 2)*int(getRating(inp, "co2"), 2)

def sol(data,part = 1):
    return getPowerConsumption(data) if part == 1 else getRating(data,"life")

def main():
    with open("input03_21.txt") as inp:
        data = [d.strip() for d in inp.readlines()]
    print(f"Part 1 : {sol(data)}\nPart 2 : {sol(data,2)}")    

if __name__ == "__main__":
    main()