#!python

import sys

def min_fuel(crabs, increased_fuel_cost = False):

    m = sorted(crabs)[-1] if crabs else 0
    fuel = sum(crabs) if not increased_fuel_cost else sum([sum(range(crab+1)) for crab in crabs])
    for i in range(1, m+1):
        s = sum([abs(crab-i) for crab in crabs]) if not increased_fuel_cost else sum([sum(range(1, abs(crab-i)+1)) for crab in crabs])
        if s < fuel:
            fuel = s

    return fuel

test = [16,1,2,0,4,2,7,1,2,14]

crabs = sys.argv[1:]
crabs = crabs[0].split(",") if crabs else []
crabs = [int(crab) for crab in crabs]
print(min_fuel(test, True))
print(min_fuel(crabs, True))