#!python

def detect_sue(data:dict[int,dict[str,int]], conditions:dict[str,int],retro =  True)->int:
    poss=data.copy()
    while len(poss) > 1:
        for entity,condition in conditions.items():
            for sue,v in data.items(): 
                if retro:
                    if entity in v and v[entity]!=condition:
                        poss = {kp:kv for kp,kv in poss.items() if kp!=sue}
                else:
                    if entity in v:
                        if entity == "cats" or entity == "trees":
                            if v[entity]<=condition:
                                poss = {kp:kv for kp,kv in poss.items() if kp!=sue}
                        elif entity == "pomeranians" or entity == "goldfish":
                            if v[entity]>=condition:
                                poss = {kp:kv for kp,kv in poss.items() if kp!=sue}    
                        else :
                           if v[entity]!=condition:
                               poss = {kp:kv for kp,kv in poss.items() if kp!=sue}
                               

    return list(poss.keys())[0]
    
def sol(data:dict[int,dict[str,int]],conditions:dict[str,int],part=1)->int:
    return detect_sue(data,conditions,part==1)


def main() :
    with open("input16_15.txt") as inp:
        data = [(d.strip()+",").split() for d in inp.readlines()]
        data = {int(spl[1][:-1]):{spl[i][:-1]:int(spl[i+1][:-1]) for i in range(2,7,2)} for spl in data}
    
    conditions={"children": 3,
         "cats": 7,
         "samoyeds": 2,
         "pomeranians": 3,
         "akitas": 0,
         "vizslas": 0,
         "goldfish": 5,
         "trees": 3,
         "cars": 2,
         "perfumes": 1}
    
    print(f"Part 1 : {sol(data,conditions)}\nPart 2 : {sol(data,conditions,2)}") 

if __name__ == "__main__":
    main()