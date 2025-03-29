#!python
def boxes(pile1,pile2=None):
    if pile2 == None:
        return set(range(int(pile1[0].split("-")[0]),int(pile1[0].split("-")[1])+1)).union(set(range(int(pile1[1].split("-")[0]),int(pile1[1].split("-")[1])+1)))
    else:
        return boxes(pile1).union(boxes(pile2))
def main():
    with open("input25_03.txt") as inp:
        data  = [d.strip().split() for d in inp.readlines()]
        inventory = []
        for d in data:
            inventory.extend(d)
        sol1 = sum(1-eval(i) for i in inventory)
        sol2 = sum(len(boxes(d)) for d in data)
        sol3 = max(len(boxes(data[i],data[i+1])) for i in range(len(data)-1))
        print(f"Part 1 : {sol1}\nPart 2 : {sol2}\nPart 3 : {sol3}")

if __name__ == "__main__" :
    main() 

  