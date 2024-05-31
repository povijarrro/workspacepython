#!python

def is_valid(s:str)->bool:
    if  not (set("iol").isdisjoint(set(s))) : return False
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    abc = [alphabet[i]+alphabet[i+1]+alphabet[i+2] for i in range(len(alphabet)-2)]
    aa = [2*c for c in alphabet]
    if not any(c in s for c in abc) : return False
    if not sum(s.count(c) for c in aa)>=2 : return False
    return True

def inc(s:str)->str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if s == "" : return "a" 
    if len(s) == 1 :
        if s == "z" : return "aa"
        return alphabet[(alphabet.index(s)+1)%26]
    if s[-1] != "z" : return s[:-1]+alphabet[alphabet.index(s[-1])+1]
    else : return inc(s[:-1])+"a"

def next(s:str)->str:

    psw = inc(s)

    if is_valid(psw) : return psw
    
    while not is_valid(psw):
        psw = inc(psw)
    
    return psw

def sol(s:str,part=1)->str:
    ns = next(s)
    if part == 1 : return ns
    else : return next(ns)



def main() :
    s = "hepxcrrq"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    abc = [alphabet[i]+alphabet[i+1]+alphabet[i+2] for i in range(len(alphabet)-2)]

    print(f"Part 1 : {sol(s)}\nPart 2 : {sol(s,2)}")

if __name__ == "__main__":
    main() 