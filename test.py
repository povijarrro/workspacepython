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
print(draw_stars_pyramid(10,False),factorial(100000))
