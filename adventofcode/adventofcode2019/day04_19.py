#!python
def get_counts(s:str)->list[int]:
    counts=[1]
    for i in range(len(s)-1):
        if s[i]!=s[i+1]:
            counts.append(1)
        else:
            counts[-1]+=1    
    return counts

def has_double(s:str,part = 1)->bool:
    gc = get_counts(s)
    return any(c>=2 for c in gc) if part == 1 else any(c==2 for c in gc)
        
def is_nondecreasing(s:str)->bool:
    for i in range(len(s)-1):
            if ord(s[i+1])<ord(s[i]):
                return False
    return True

def get_passwords(low:int,high:int, part = 1)->set[str]:
    passwords = set()
    for i in range(max(low,100000),min(high,1000000)):
        if has_double(str(i),part) and is_nondecreasing(str(i)):
            passwords.add(str(i))
    return passwords 

def sol(low:int,high:int,part = 1):
    return len(get_passwords(low,high,part)) 



if __name__ == "__main__":
    low,high = 172851,675869
    
    print(f"Part 1 : {sol(low,high)}\nPart 2 : {sol(low,high,2)}")
