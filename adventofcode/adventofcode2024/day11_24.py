#!python

def blink(stone:int,times:int,seen:dict[tuple[int,int],int] = {})->int: #thanks to jonathanpaulsson https://github.com/jonathanpaulson/AdventOfCode/blob/master/2024/11.py 
    if (stone,times) in seen:
       return seen[(stone,times)]
    
    if times == 0:
        res = 1
    elif stone == 0:
        res = blink(1,times-1)
    elif len(str(stone))%2 == 0:
        strstone:str = str(stone)
        lstone = len(strstone)
        res = blink(int(strstone[:lstone//2]),times-1)+blink(int(strstone[lstone//2:]),times-1)
    else:
        res = blink(2024*stone,times-1)
    
    seen[(stone,times)] = res
    return res

def sol(arr:list[int],times:int)->int:
    return sum(blink(stone,times) for stone in arr)        

def part1(arr:list[int]):
    return sol(arr,25)

def part2(arr:list[int])->int:
    return sol(arr,75)

def main()->None:
    with open("./input11_24.txt") as inp:
        arr:list[int] = list(map(int,inp.read().strip().split()))
    
    print(f"Part 1 : {part1(arr)}\nPart 2 : {part2(arr)}")

if __name__ == "__main__":
    main()    