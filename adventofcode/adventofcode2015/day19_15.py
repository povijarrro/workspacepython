#!python
from random import shuffle


def get_molecules(data:list[tuple],molecule:str, reverse = False):
    for pair in data:
        for i in range(len(molecule)-len(pair[reverse])+1):
            if molecule[i:i+len(pair[reverse])] == pair[reverse] :
                yield molecule[:i]+pair[1-reverse]+molecule[i+len(pair[reverse]):]

def random_replace(data:list[tuple],start:str,goal:str):
    # thanks to mjpieters
    molecule = start
    reversed = [(v, k) for k,v in data]
    steps = 0
    target = molecule
    while target != goal:
        changed = False
        for repl, source in reversed:
            if repl in target:
                target = target.replace(repl, source, 1)
                steps += 1
                changed = True
        if not changed:
            target = molecule
            shuffle(reversed)
            steps = 0
    return steps

def sol(data:list[tuple],molecule:str,part=1)->int:
    if part == 1 : 
        return len(set(get_molecules(data,molecule)))
    else:
        return random_replace(data,molecule,"e")
        
def main():
    with open("input19_15.txt") as inp:
        data = [d.strip() for d in inp.readlines()]
        molecule = data[-1]
        data = [tuple(d.split(" => ")) for d in data[:-2]]
        
    print(f"Part 1 : {sol(data,molecule)}\nPart 2 : {sol(data,molecule,2)}")

if __name__ == "__main__":
    main()