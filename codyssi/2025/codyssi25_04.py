#!python
def fun3(s):
    res = []
    n = 0
    for c in s:
        if len(res)>0 and c == res[-1][1]:
            res.pop()
            n += 1 
        else:
            n = 1
        res.append((n,c))       
    return "".join(str(t[0])+t[1] for t in res)
def main():
    with open("input25_04.txt") as inp:
        data  = [d.strip() for d in inp.readlines()]
    memory = {"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i]:i+1 for i in range(26)}
    memory.update({"0123456789"[i]:i for i in range(10)}) 
    fun2 = lambda s:s[:(len(s)//10)]+str(len(s)-2*(len(s)//10))+s[-1:-(len(s)//10)-1:-1][::-1]
    sol1 = sum(sum(memory[s[i]] for i in range(len(s))) for s in data)
    sol2 = sum(sum(memory[s[i]] for i in range(len(s))) for s in map(fun2,data))
    sol3 = sum(sum(memory[s[i]] for i in range(len(s))) for s in map(fun3,data))
    print(f"Part 1 : {sol1}\nPart 2 : {sol2}\nPart 3 : {sol3}")

if __name__ == "__main__" :
    main() 