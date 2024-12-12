#!python
from copy import deepcopy


# class Id:
#     def __init__(self,id:int):
#         self.id = id
    
#     def __repr__(self):
#         return f"Id({self.id})" 
    
#     def __iadd__(self,val):
#         return Id(self.id+val)

#     def __int__(self):
#         return self.id       

def checksum(data:str)->int:
    n:int = len(data)
    disk:list = []
    id:int = 0

    for i in range(0,n,2):
        disk.extend([id for _ in range(int(data[i]))])
        id += 1
        if i+1<n:
            disk.extend(["." for _ in range(int(data[i+1]))]) 
    
    cdisk = deepcopy(disk)
    i = 0
    for d in cdisk[::-1]:
        if "." in disk[i:]: 
            i += disk[i:].index(".")
            disk[i]= d
            disk = disk[:-1]
        else:
            break

    
    return sum(i*d for i,d in enumerate(disk)) 

    # disk:list[tuple[Id,int,int]] = []
    # n:int = len(data)
    # id:int = 0 
    # for i in range(0,n,2):
    #     disk.append((i))

def main()->None:
    with open("./input09_24.txt") as inp:
        data = inp.read().strip()
    
    exdata = "2333133121414131402"
    print(checksum(data))

if __name__ == "__main__":
    main()