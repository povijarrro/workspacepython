#!python
from readLines import readLines

def getDict(data)->dict:
    d={}
    for row in data:
        d[row[1]]=(row[0],row[2])
    
    return d

def getValues(olds,rules):
    news=[]
    for num in olds:
        value=None
        for k,v in rules.items():
            if num in range(k,k+v[1]):
                value = num+v[0]-k
                break
            else: 
                value = num
                continue
        news.append(value)
    
    return news

def getMappedIntervals(olds,rules):
    news=[]
    for interval in olds:
        news.append((getValues([interval[0]],rules)[0],getValues([interval[1]],rules)[0]))

    return news

def getIntervals(olds):
    ints=[]
    for i in range(0,len(olds)-1,2):
        ints.append((olds[i],olds[i]+olds[i+1]-1))
    return ints

        
def solution1(data):
    seeds = [int(i) for i in data[0][0].split()[1:]]
    soil = [list(map(lambda a:int(a),i.split())) for i in data[1][1:]]
    fertilizer = [list(map(lambda a:int(a),i.split())) for i in data[2][1:]]
    water = [list(map(lambda a:int(a),i.split())) for i in data[3][1:]]
    light = [list(map(lambda a:int(a),i.split())) for i in data[4][1:]]
    temperature = [list(map(lambda a:int(a),i.split())) for i in data[5][1:]]
    humidity = [list(map(lambda a:int(a),i.split())) for i in data[6][1:]]
    location = [list(map(lambda a:int(a),i.split())) for i in data[7][1:]]

    soils=getValues(seeds, getDict(soil))
    ferts=getValues(soils,getDict(fertilizer))
    waters=getValues(ferts,getDict(water))
    lights=getValues(waters,getDict(light))
    temps=getValues(lights,getDict(temperature))
    humids=getValues(temps,getDict(humidity))
    locs=getValues(humids,getDict(location))

    return min(locs)

def solution2(data):
    seeds = getIntervals([int(i) for i in data[0][0].split()[1:]])
    soil = [list(map(lambda a:int(a),i.split())) for i in data[1][1:]]
    fertilizer = [list(map(lambda a:int(a),i.split())) for i in data[2][1:]]
    water = [list(map(lambda a:int(a),i.split())) for i in data[3][1:]]
    light = [list(map(lambda a:int(a),i.split())) for i in data[4][1:]]
    temperature = [list(map(lambda a:int(a),i.split())) for i in data[5][1:]]
    humidity = [list(map(lambda a:int(a),i.split())) for i in data[6][1:]]
    location = [list(map(lambda a:int(a),i.split())) for i in data[7][1:]]
    
    soils=getMappedIntervals(seeds, getDict(soil))
    print(soils)
    ferts=getValues(soils,getDict(fertilizer))
    waters=getValues(ferts,getDict(water))
    lights=getValues(waters,getDict(light))
    temps=getValues(lights,getDict(temperature))
    humids=getValues(temps,getDict(humidity))
    locs=getValues(humids,getDict(location))



if __name__ == "__main__":
    data = readLines("input05.txt","\n\n")
    data = [i.splitlines() for i in data]
    seeds = [int(i) for i in data[0][0].split()[1:]]

    print(f"Part 1 : {solution1(data)}")
    #print(f"Part 2 : {solution2(data)}")