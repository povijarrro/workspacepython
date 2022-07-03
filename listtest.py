#!python
import copy
import numpy as np

l=5*[3*[1]]
print(l)
l[2][1]=3
print(l)

a=np.ones((5,3), dtype=int)
print(a)
a[2,1]=3
print(a)
print(a.prod())

print(np.concatenate((np.array([[1,2,3],[4,5,6]]),np.array([[7,8,9],[10,11,12],[13,14,15]])))) 

test_list=[]
tl=[1,2,3]
tlc=copy.deepcopy(tl)
test_list.append(tlc)
print(tl in test_list)
print(id(tl), id(tlc), id([1,2,3]))