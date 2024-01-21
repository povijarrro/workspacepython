#!python
from readLines import readLines
def getCounts(string:str)->dict:
    strData = string.strip().split(", ")
    strDict = {}
    for s in strData:
        spl=s.split(" ")
        strDict[spl[1]]=int(spl[0])
    return strDict

def minConditions(game:list[dict])->dict:
    mc = {}
    
    mc["red"] = max([(roll["red"] if ("red" in list(roll.keys())) else 0) for roll in game])
    mc["green"] = max([(roll["green"] if ("green" in list(roll.keys())) else 0)  for roll in game])
    mc["blue"] = max([(roll["blue"] if ("blue" in list(roll.keys())) else 0)  for roll in game])
    return mc

def solution1(data:list[list[dict]])->int:
    conditions = {"red": 12, "green" : 13, "blue" : 14}
    sol = 0
    for i, game in enumerate(data):
        mc = minConditions(game)
        if((mc["red"]<=conditions["red"] and mc["green"]<=conditions["green"]) and mc["blue"]<=conditions["blue"]):
            sol+=i+1
    return sol        

def solution2(data:list[list[dict]])->int:
    sol=0
    for game in data:
        mc=minConditions(game)
        sol+=mc["red"]*mc["green"]*mc["blue"] 
    
    return sol

if (__name__ == "__main__"):
    data = readLines("input02.txt")
    data = [s.split(":")[1:][0].split(";") for s in data]
    data = [[getCounts(t) for t in s] for s in data]
    
    print(f"Part 1 : {solution1(data)}")
    print(f"Part 2 : {solution2(data)}")
