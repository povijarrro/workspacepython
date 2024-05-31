#!python
def sol(captcha:str,part=1):
    if part == 1 : 
        return sum(int(captcha[i]) for i in range(len(captcha)) if captcha[i]==captcha[(i+1)%len(captcha)])
    else : 
        return sum(int(captcha[i]) for i in range(len(captcha)) if captcha[i]==captcha[(i+len(captcha)//2)%len(captcha)]) 

def main():
    with open("input01_17.txt") as inp:
        captcha = inp.readline().strip()
    
    print(f"Part 1 : {sol(captcha)}\nPart 2 : {sol(captcha,2)}") 

if __name__ == "__main__":
    main()