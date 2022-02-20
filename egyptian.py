from math import gcd

def egyptian(x,y):
    g=gcd(x,y)
    neg=False
    if((x<0)^(y<0)):neg=True
    x=abs(x//g)
    y=abs(y//g)
    if(x==1): return("1/"+str(y))
    if(x==0): return("0")
    if(y==0): return("UNDEFINED")
    c=y//x+1
    composition="1/"+str(c)+"+"+egyptian((-y)%x,y*c)
    if(neg):
        composition="-"+composition.replace("+","-")
    return(composition)

print(egyptian(41,43))