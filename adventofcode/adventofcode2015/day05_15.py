#!python

def is_nice1(s:str)->bool:

    vowel_counts = [s.count(v) for v in "aeiou"]
    doubles = [2*c for c in "abcdefghijklmnopqrstuvwxyz"]
    double_counts = [s.count(d) for d in doubles]
    
    if sum(vowel_counts)<3 or sum(double_counts)==0:return False
    if "ab" in s or "cd" in s or "pq" in s or "xy" in s: return False
    
    return True

def is_nice2(s:str)->bool:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    pairs = [s1+s2 for s1 in alphabet for s2 in alphabet]
    pair_counts = [s.count(p) for p in pairs]
    cycs = [s1+s2+s1 for s1 in alphabet for s2 in alphabet]
    cyc_counts = [s.count(c) for c in cycs]
    
    if max(pair_counts)<2 : return False
    if max(cyc_counts)==0 : return False
    
    
    return True

def sol(data:list[str], part=1)->int:
    is_nice = [is_nice1,is_nice2]
    n=0
    for s in data:
        if is_nice[part-1](s):
            n+=1
    
    return n

if __name__ == "__main__":
    with open("input05_15.txt") as inp:
        data = [d.strip() for d in inp.readlines()]

    print(f"Part 1 : {sol(data)}\nPart 2 : {sol(data,2)}")   