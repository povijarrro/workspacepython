#!python
import hashlib

def password(s:str,start="00000", length=8,part=1)->int:
    if part == 1:
        pw = ""
        i = 0
        while len(pw)<8:
            while not hashlib.md5((s+str(i)).encode()).hexdigest().startswith(start):
                i+=1
        
            pw += hashlib.md5((s+str(i)).encode()).hexdigest()[len(start)]
            i+=1
    else:
        pw = dict()

        i = 0
        while len(pw.keys())<8:
            while not hashlib.md5((s+str(i)).encode()).hexdigest().startswith(start):
                i+=1
            
            hash = hashlib.md5((s+str(i)).encode()).hexdigest()
            
            if hash[len(start)] not in pw.keys():
                if hash[len(start)].isdigit():
                    if "0"<=hash[len(start)]<str(length):
                        pw[hash[len(start)]] = hash[len(start)+1]
            
            i+=1


    return pw if part == 1 else "".join([pw[i] for i in sorted(pw.keys())])

def sol(id,part=1)->str:
    return password(id,"00000",8,part)

def main():
    id = "ffykfhsq"
    
    print(f"Part 1 : {sol(id)}\nPart 2 : {sol(id,2)}")

if __name__ == "__main__":
    main()