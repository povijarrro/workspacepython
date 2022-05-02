#!python

import sys
from collections import Counter

# def next_day(fishes):
#     res = [fish - 1 if fish > 0 else 6 for fish in fishes]
#     temp = fishes
#     for fish in temp:
#         if fish == 0:
#             res.append(8)
#     return res

# def next_day(fishes):
#
#     for fish in fishes:
#         if fish > 0:
#             yield fish-1
#         else:
#             yield 6
#             yield 8



def after_n_days(fishes, n):
    c = Counter(fishes)
    c = [c[t] for t in range(9)]
    for day in range(n):
        nc = c[1:]
        nc.append(c[0])
        nc[6] = c[0] + c[7]
        c = nc
    return sum(c)


fishes = sys.argv[1:]
fishes = fishes[0].split(",") if fishes else []
fishes = [int(fish) for fish in fishes]


print(after_n_days(fishes, 80))
print(after_n_days(fishes, 256))
