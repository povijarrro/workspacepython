#!python
def largest(s, k):
    n = len(s)
    drops_allowed = n - k
    
    stack = []
    
    for i, digit in enumerate(s):
        while stack and s[stack[-1]] < digit and drops_allowed > 0:
            stack.pop()
            drops_allowed -= 1
        
        stack.append(i)
    
    indices = stack[:k]
    
    return int("".join(s[i] for i in indices))


def sol(data:list[str], part:int = 1):
    joltage = 0
    for s in data:
        joltage += largest(s,2 if part == 1 else 12)
           
    return joltage

def main()->None:
    with open("input03_25.txt") as inp:
        data = [d.strip() for d in inp.readlines()]

    print(f"Part 1 : {sol(data,1)}\nPart 2 : {sol(data,2)}")    

if __name__ == "__main__":
    main()