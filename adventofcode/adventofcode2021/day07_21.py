#!python
def min_fuel(crabs, increased_fuel_cost = False):

    m = sorted(crabs)[-1] if crabs else 0
    fuel = sum(crabs) if not increased_fuel_cost else sum([sum(range(crab+1)) for crab in crabs])
    for i in range(1, m+1):
        s = sum([abs(crab-i) for crab in crabs]) if not increased_fuel_cost else sum([sum(range(1, abs(crab-i)+1)) for crab in crabs])
        if s < fuel:
            fuel = s

    return fuel

def sol(data, part = 1):
    return min_fuel(data,part != 1)

def main():
    with open("input07_21.txt") as inp:
        data = [int(s) for s in inp.readline().strip().split(",")]

        print(f"Part 1 : {sol(data)}\nPart 2 : {sol(data,2)}")

if __name__ == "__main__":
    main()