def gcd(a,b):
    if(abs(b)>abs(a)):
        a,b=abs(b),abs(a)
    if(b==0):
        return a
    else:
        return gcd(a-b,b)
    
def lcm(a,b):
    return int(a*b/gcd(a,b))

print(gcd(60,-90),lcm(90,60))