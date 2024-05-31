#!python

def look_and_say(s:str)->str:

    if(s == "") : return ""
    
    substr = s[0]
    substrs = []
    
    for i in range(len(s)-1) :
        if s[i]==s[i+1]:
            substr += s[i+1]
        else :
            substrs.append(substr)
            substr = s[i+1]  
    
    substrs.append(substr)

    res = ""

    for sub in substrs : res += str(len(sub))+sub[0]

    return res

def sol(s:str, part=1)->int:
    las=s
    
    for _ in range(40+10*(part-1)):
        las=look_and_say(las)
    
    return len(las)

def main() :
    s = "1321131112"
    print(f"Part 1 : {sol(s)}\nPart 2 : {sol(s,2)}")

if __name__ == "__main__":
    main()    