#!python

import re

def is_abba(s:str)->bool:
    if len(s) != 4 : return False
    return s[0] != s[1] and s[1] == s[2] and s[3] == s[0]

def is_aba(s:str)->bool:
    if len(s) != 3 : return False
    return s[0] != s[1] and s[2] == s[0]

def contains_abba(lst:list[str])->bool:

    for s in lst:
        for i in range(len(s)-3):
            if is_abba(s[i:i+4]) : return True

    return False


def get_abas(lst:list[str])->list[str]:
    abas = []
    for s in lst:
        for i in range(len(s)-2):
            if is_aba(s[i:i+3]):
                abas.append(s[i:i+3])

    return abas

def bab(aba:str)->str:
    return aba[1]+aba[0]+aba[1]

def sol(outsides:list[list[str]],hypernets:list[list[str]],part = 1)->int:
    res = 0
    if part == 1:
        for i in range (len(outsides)):
            res += contains_abba(outsides[i]) and not contains_abba(hypernets[i])
    
    else:
        for i in range(len(outsides)):
            for aba in get_abas(outsides[i]):
                if bab(aba) in get_abas(hypernets[i]):
                    res+=1
                    break

    return res

def main():
    with open("input07_16.txt") as inp:
        ips = [d.strip() for d in inp.readlines()]
        hypernets = [[s[1:-1] for s in re.findall(r"\[.*?\]",ip)] for ip in ips]
        outsides = [re.split(r"\[.*?\]",ip) for ip in ips]

    print(f"Part 1 : {sol(outsides,hypernets)}\nPart 2 : {sol(outsides,hypernets,2)}")

if __name__ == "__main__":
    main()    