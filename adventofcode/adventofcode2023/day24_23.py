#!python
from itertools import combinations
from readLines import readLines
from z3 import *

def dist(A:tuple, B:tuple, vA:tuple, vB:tuple)->int:
    d = (B[0]-A[0])**2+(B[1]-A[1])**2+(B[2]-A[2])**2
    lA, lB= list(A), list(B)    
    while True:
        d2 = (lB[0]-lA[0])**2+(lB[1]-lA[1])**2+(lB[2]-lA[2])**2 
        sol=Solver()
        sol.add(d2>d)
        chck = sol.check()
        if chck == sat : return d
        d = d2
        lA,lB = [lA[0]+vA[0],lA[1]+vA[1],lA[2]+vA[2]], [lB[0]+vB[0], lB[1]+vB[1], lB[2]+vB[2]]


def hasCollisionInArea(A:tuple,B:tuple,vA:tuple,vB:tuple,limits=(200000000000000,400000000000000))->bool:
    a11 = vA[0]
    a12 = -vB[0]
    a21 = vA[1]
    a22 = -vB[1]
    b1 = B[0]-A[0]
    b2 = B[1]-A[1]
    det = a11*a22-a12*a21
    if det == 0:return False
    dett = b1*a22-a12*b2
    dets = a11*b2-b1*a21
    t, s = dett/det, dets/det
    if t<=0 or s<=0:return False
    x,y=B[:-1][0]+vB[0]*s, B[:-1][1]+vB[1]*s
    return limits[0]<=x<=limits[1] and limits[0]<=y<=limits[1]

def solution1(points:list[tuple],vels:list[tuple],limits=(200000000000000,400000000000000))->int:
    sol = 0
    for i,j in combinations(range(len(points)),2):
        sol += hasCollisionInArea(points[i],points[j],vels[i],vels[j],limits)

    return sol  

def solution2(points:list[tuple], vels:list[tuple])->int:
    s=Solver() 
    x1,x2,x3=[Int(f"x{i}") for i in range(1,4)]
    v1,v2,v3=[Int(f"v{i}") for i in range(1,4)]
    for i,p in enumerate(points):
        #s.add(dist(p,tuple(unks[:3]),vels[i],tuple(unks[3:]))==0) 
        s.add(dist(p,(x1,x2,x3),vels[i],(-3,1,2))==0)
    print(s.check()) 
    return s.model().eval(x1+x2+x3)  

if __name__ == "__main__":
    data = readLines("example24.txt")
    points = [d.split(", ") for d in [i[0] for i in [d.split(" @ ") for d in data]]]
    points = [tuple(map(int,p)) for p in points]
    vels = [d.split(", ") for d in [i[1] for i in [d.split(" @ ") for d in data]]]
    vels = [tuple(map(int,v)) for v in vels]
    
    print(f"Part 1 : {solution1(points,vels)}")
    
    print(dist(points[0],points[1],vels[0],vels[1]))
    
    for i in range(len(points)):
        print(dist(points[i],(24,13,10),vels[i],(-3,1,2)))
    
    print(solution2(points[:2],vels[:2]))

    