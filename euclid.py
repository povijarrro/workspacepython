
def gcd(a,b):
    a,b=abs(a),abs(b)
    while(b):
        a,b=b,a%b
    return a    
    
def lcm(a,b):
    return int(a*b/gcd(a,b))

print(gcd(2*3*3*5*5*5*7*11,-5*7*11*13))