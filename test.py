import pygame

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
    testfile.writelines(draw_stars_pyramid(4,filled=False))
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
pygame.font.init()
print(type(pygame.font.SysFont("comicsans",20).render("NIECO",1,(255,0,0))))
print(__name__)