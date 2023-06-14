#!python
import sys

def solution(data):
    intersections=[]
    for d in data:
        
        intersections.append(set(d[0]).intersection(set(d[1])).pop().swapcase())
        

    return sum(list(map(lambda x:ord(x)-ord("A")+1 if x.isupper() else ord(x)-ord("a")+27,intersections)))

data=["vJrwpWtwJgWrhcsFMMfFFhFp",
"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
"PmmdzqPrVvPwwTWBwg",
"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
"ttgJtRGJQctTZtZT",
"CrZsJsPPZsGzwwsLwLmpwMDw"]

data=sys.argv[1:]
data=[(d[:len(d)//2],d[len(d)//2:]) for d in data]

print(data)
print(solution(data))  



