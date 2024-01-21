#!python

import re

def numsum(data:str)->int:
    return sum(int(d) for d in re.findall(r'[-+]?[0-9]+',data))

def no_red_numsum(ev)->int:
    if type(ev) != list and type(ev) != dict  and type(ev) != int:  return 0
    if type(ev) == int : return ev
    if type(ev) == dict:
        if "red" in ev.values() : return 0
        else :
            nrs = 0
            for k,v in ev.items():
                nrs += no_red_numsum(k)+no_red_numsum(v)
                
            return nrs      
    elif type(ev) == list:
        nrs = 0
        for item in ev:
            nrs += no_red_numsum(item)
        
        return nrs
                



def sol(data:str, part = 1)->int:
    if part == 1 : return numsum(data) 
    return no_red_numsum(eval(data))


if __name__ == "__main__" :
    with open("input12_15.txt") as inp:
        data = inp.readline().strip()

    print(f"Part 1 : {sol(data)}\nPart 2 : {sol(data,2)}")
    