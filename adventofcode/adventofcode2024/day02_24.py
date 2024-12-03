#!python
def safe(report:list[int],rem:bool=False)->bool:
    n:int = len(report)
    if not rem:
        return (report == sorted(report) or report == sorted(report,reverse=True)) and sum(abs(report[i+1]-report[i]) in {1,2,3}  for  i in range(n-1)) == n-1
    else:
        return sum(safe(report[0:i]+report[i+1:]) for i in range(n+1)) > 0
    
def part1(data:list[list[int]])->int:
    return sum(safe(d) for d in data)

def part2(data:list[list[int]])->int:
    return sum(safe(d,True) for d in data)  
            
def main()->None:
    with open("./input02_24.txt") as inp:
        data:list[int] = [list(map(int,d.strip().split())) for d in inp.readlines()]
    
    print(f"Part 1 : {part1(data)}\nPart 2 : {part2(data)}")

if __name__ == "__main__":
    main()    