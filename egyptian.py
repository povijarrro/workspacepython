#!python
from math import gcd

def egyptian(x:int, y:int)->str:
    
    if(y==0): return("UNDEFINED")
    if(x==0): return("0")
   
    g=gcd(x,y)
    neg=((x<0)^(y<0))
    x=abs(x//g)
    y=abs(y//g)
    
    if(x==1): return("1/"+str(y))

    if(x>y):
        div=x//y
        first=str(div)
        x=x-y*div
        return(first+"+"+egyptian(x,y))
    
    c=y//x+1
    composition='1/'+str(c)+' + '+egyptian((-y)%x, y*c)
    
    if(neg):
        composition="-"+composition.replace('+', '-')
    
    return(composition)

def main()->None:

    for n in range(1,10):
        for i in range(1,n+1):
            print(f"{i}/{n} = {egyptian(i, n)}")


if __name__ == "__main__":
    main()           