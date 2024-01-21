#!python

def dist(reindeer:str,time:int,data:dict[str,tuple[int,int,int]])->int:
    speed,mov,rest = data[reindeer]
    if time<=mov: return speed*time

    return speed*mov*(time//(mov+rest))+speed*min(time%(mov+rest),mov)

def max_dist(time:int,data:dict[str,tuple[int,int,int]])->int:
    dists = []
    for reindeer in data.keys() :
        dists.append(dist(reindeer,time,data))
    
    return max(dists)

def winners(time:int,data:dict[str,tuple[int,int,int]])->list[str]:
    return [reindeer for reindeer in data.keys() if dist(reindeer,time,data) == max_dist(time,data)]

def points(time:int, data:dict[str,tuple[int,int,int]])->dict[str,int]:
    pts = {reindeer:0 for reindeer in data.keys()} 

    for t in range(1,time+1):
        winnrs = winners(t,data)
        for reindeer in winnrs :
            pts[reindeer] += 1
    
    return pts

def sol(time:int, data:dict[str,tuple[int,int,int]],part = 1)->int:
    if part == 1 : return max_dist(time,data)
    return max(point for point in points(time,data).values())


if __name__ == "__main__" :
    with open("input14_15.txt") as inp :
        data = [d.strip() for d in inp.readlines()]
        data = [d.split() for d in data]
        data = {spl[0]:(int(spl[3]),int(spl[6]),int(spl[-2])) for spl  in data}

    print(f"Part 1 : {sol(2503,data)}\nPart 2 : {sol(2503,data,2)}")    