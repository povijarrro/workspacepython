#!python

def numOfInc(data):
    n = len(data)
    res = 0
    for i in range(n-1):
        if int(data[i + 1]) > int(data[i]):
            res += 1
    return res

def numOfWindowInc(data):
    n = len(data)
    newInput = []
    for i in range(n-2):
        newInput.append(str(int(data[i])+int(data[i+1])+int(data[i+2])))
    return numOfInc(newInput)

def sol(data, part=1):
    return numOfInc(data) if part == 1 else numOfWindowInc(data)

def main():
    with open("input01_21.txt") as inp:
        data = [d.strip() for d in inp.readlines()]

    print(f"Part 1 : {sol(data)}\nPart 2 : {sol(data,2)}")    

if __name__ == "__main__":
    main()