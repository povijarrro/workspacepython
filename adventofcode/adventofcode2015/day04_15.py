#!python
import hashlib

def ending(s:str,start="00000")->int:
    i=0
    while not hashlib.md5((s+str(i)).encode()).hexdigest().startswith(start):
        i+=1
    
    return i  

def sol(data,part=1):
    return ending(data,"00000"+(part-1)*"0")

if __name__ == "__main__":
    data = "ckczppom"
    
    print(f"Part 1 : {sol(data)}\nPart 2 : {sol(data,2)}")