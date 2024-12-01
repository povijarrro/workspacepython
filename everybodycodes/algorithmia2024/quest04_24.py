#!python

def sol(nails,part3=False)->int:
    return sum([nail-min(nails) for nail in nails]) if not part3 else sum([abs(nail-sorted(nails)[len(nails)//2])for nail in nails])

def main()->None:
    nails1 = [11,18,16,7,14,15,17,10,10,19,17]
    with open("./in04_24_2.txt") as inp:
        nails2 = [int(n.strip()) for n in inp.readlines()]

    with open("./in04_24_3.txt") as inp:
        nails3 = [int(n.strip()) for n in inp.readlines()]  
        nails3.sort() 
    
    print(f"Part 1 : {sol(nails1,False)}\nPart 2 : {sol(nails2,False)}\nPart 3 : {sol(nails3,True)}")
    
if __name__ == "__main__":
    main()