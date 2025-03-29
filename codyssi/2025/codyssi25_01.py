#!python


def main():
    with open("input25_01.txt") as inp:
        data = [d.strip() for d in inp.readlines()]
        first1, offsets1,signs = int(data[0]), [int(d) for d in data[1:-1]], data[-1]
        first2,offsets2 = 10*first1+offsets1[0], [10*int(data[i])+int(data[i+1]) for i in range(2,len(data)-1,2)]
    miliradians1 = first1
    miliradians2 = first1
    miliradians3 = first2
    for i in range(len(offsets1)):
        if signs[i] == '-':
            miliradians1 -= offsets1[i]
        if signs[i] == "+":
            miliradians1 += offsets1[i]
        if signs[::-1][i] == '-':
            miliradians2 -= offsets1[i]
        if signs[::-1][i] == "+":
            miliradians2 += offsets1[i]

    for i in range(len(offsets2)):
        if signs[::-1][i] == '-':
            miliradians3 -= offsets2[i]
        if signs[::-1][i] == "+":
            miliradians3 += offsets2[i]        
        
    print(f"Part 1 : {miliradians1}\nPart 2 : {miliradians2}\nPart 3 : {miliradians3}") 

if __name__ ==  "__main__":
    main()