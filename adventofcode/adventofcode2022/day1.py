#!python

def load_input(file_name):
    elfs=[]
    elf=[]
    with open(file_name,"r") as inp:
        for line in inp.readlines():
            if line=="\n":
                elfs.append(elf)
                elf=[]
                continue
            else:
                elf.append(int(line))
        elfs.append(elf)        
    return elfs

elfs=load_input("input1.txt")
print(sum(sorted([sum(elf) for elf in elfs],reverse=True)[:3]))
