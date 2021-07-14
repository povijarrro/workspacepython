def pyr(n):
     res=""
     for i in range(1,2*n):
         row=""
         for j in range(2,min(i,2*n-i)+1):
            row+=" "+str(j)
         res+="1"+row+"\n"

     return(res)

for i in range(11):
     print("i="+str(i)+":\n"+pyr(i)+"\n")