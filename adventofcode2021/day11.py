#!python

import numpy as np
import sys


def neighbours(i,j,m,n):
    res = []
    
    if i in range(m) and i-1 in range(m) and j in range(n):
        res.append((i-1,j))
    if i in range(m) and i+1 in range(m) and j in range(n):
        res.append((i+1,j))
    if i in range(m) and j-1 in range(n) and j in range(n):
        res.append((i, j-1))
    if i in range(m) and j+1 in range(n) and j in range(n):
        res.append((i,j+1))
    if i-1 in range(m) and j-1 in range(n) and i in range(m) and j in range(n):
        res.append((i-1,j-1)) 
    if i-1 in range(m) and j+1 in range(n) and i in range(m) and j in range(n):
        res.append((i-1,j+1))
    if i+1 in range(m) and j-1 in range(n) and i in range(m) and j in range(n):
        res.append((i+1,j-1)) 
    if i+1 in range(m) and j+1 in range(n) and i in range(m) and j in range(n):
        res.append((i+1,j+1))                    
    
    return res
 

flashes = 0 
def flash(data,i,j):
    m= len(data)
    n=len(data[0]) if m>0 else 0
    global flashes
    flashes += 1
    new_data = np.array(data)
    new_data[i,j] = -1
    
    for k,l in neighbours(i,j,m,n):
        if new_data[k,l] != -1:
            new_data[k,l]+=1 
            if new_data[k,l] > 9:
                new_data=flash(new_data,k,l)
    return new_data

def step(data):
    m = len(data)
    n = len(data[0]) if m>0 else 0
    res = np.array(data)
    global flashes
    flashes = 0

    res += 1

    for i in range(m):
        for j in range(n):
            if res[i,j]==10:
                res=flash(res, i,j)

    for i in range(m):
        for j in range(n):
            if res[i,j]==-1:
                res[i,j]=0            

    return res, flashes


def after_n_steps(data, n):
    res = np.array(data)
    flashes = 0
    for i in range(n):
        s = step(res)
        res = s[0]
        flashes += s[1]

    return res, flashes    

def all_flashes(data):
    m = len(data)
    n = len(data[0]) if m>0 else 0
    res = step(data)
    while True:
        done =True
        for i in range(m):
            for j in range(n):
                if res[0][i,j]==-1:
                    res[0][i,j]=0
                else:
                    done = False    

        if done:
            return res[1]
        res = step(res[0])   


test = [[5,4,8,3,1,4,3,2,2,3],
        [2,7,4,5,8,5,4,7,1,1],
        [5,2,6,4,5,5,6,1,7,3],
        [6,1,4,1,3,3,6,1,4,6],
        [6,3,5,7,3,8,5,4,7,8],
        [4,1,6,7,5,2,4,6,4,5],
        [2,1,7,6,8,4,1,7,2,1],
        [6,8,8,2,8,8,1,1,3,4],
        [4,8,4,6,8,4,8,5,5,4],
        [5,2,8,3,7,5,1,5,2,6]]

data = sys.argv[1:] if len(sys.argv)>1 else []
data =[[int(data[i][j]) for j in range(len(data[i]))]for i in range(len(data))]
for i in range(101):
    print(f"after {i} steps:\n{after_n_steps(data,i)}") 

print(all_flashes(data))     
         
