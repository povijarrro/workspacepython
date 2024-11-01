#!python

def factorial(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return(res)

def draw_stars_pyramid(n,filled=True):
    res=""
    if filled:
         ch="*"
    else:
        ch=" "     
    for i in range(n):
        if i<n-1:
            res+=(n-1-i)*" "+"*"+(2*(i-1)+1)*ch
            if i!=0: res+="*"  
            res+="\n"
        else :
            res+=(2*n-1)*"*"

    return(res)    

with open("testfile.txt","w") as testfile:
    testfile.writelines(draw_stars_pyramid(4,filled=True))
#print(draw_stars_pyramid(10,False),factorial(100000))
p=[[1,2,3],
[4,5,6],
[7,8,9]]
print(str(p[1][1]))

a=[[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]
b=[]
for i in range(5):
    row=[]
    for j in range(5):
        row.append(5*i+j)
    b.append(row)    
print([[a[i][j] for j in range(2,4)] for i in range(1,4)])

def timestamp():
    n = 1
    for h in range(24):
        h1,h2 = h//10,h%10
        if h1<h2:
            for m in range(10*(h2+1),60):
               m1,m2  = m//10,m%10
               if m1<=m2:
                   for s in range(10*m2,60):
                       s1,s2 = s//10,s%10
                       if s1<s2:
                           print(f"{n}. {h1}{h2}:{m1}{m2}:{s1}{s2}")
                           n+=1

timestamp() 
n = 1
print("hours")
for h in range(24):
    h1,h2 = h//10,h%10
    if h2<=4 and h1<h2:
        print(f"{n}. {h}")
        n+=1

print("minutes")        
n=1
for m in range(33,60):
    m1,m2 = m//10,m%10
    if m2<=5 and m1<=m2:
        print(f"{n}. {m}")
        n+=1

print("seconds")        
n=1
for s in range(56,60):
    s1,s2 = s//10,s%10
    if s1<s2:
        print(f"{n}. {s}")
        n+=1