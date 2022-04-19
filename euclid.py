import math

def gcd(a,b):
    a,b=abs(a),abs(b)
    while(b):
        a,b=b,a%b
    return a    
    
def lcm(a,b):
    return int(a*b/gcd(a,b))

print(gcd(789,678))
print(math.gcd(789,678))