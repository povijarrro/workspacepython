#!python
def set_chips(instructions:list[str])->dict:
    res = {}
    for ins in instructions:
        if ins.startswith("value"):
            spl= ins.split()
            if spl[-1] not in res : 
                res[spl[-1]] = int(spl[1])
            else:
                res[spl[-1]] = {"low":min(res[spl[-1]],int(spl[1])),
                                "high":max(res[spl[-1]],int(spl[1]))}
        
    return res

def changed(bots:dict, instructions:list[str])->dict:
    cbots = bots.copy()
    two_valued = [bot for bot in bots if isinstance(bots[bot],dict)][0]
    for ins in instructions:
        spl=ins.split()
        if ins.startswith("bot") and spl[1] == two_valued:
            
            if "output" not in ins:
                cbots[spl[6]] = bots[two_valued]["low"] if spl[6] not in bots else {"low":min(bots[two_valued]["low"],bots[spl[6]]),
                                                                                    "high":max(bots[two_valued]["low"],bots[spl[6]])}
                cbots[spl[-1]] = bots[two_valued]["high"] if spl[-1] not in bots else {"low":min(bots[two_valued]["high"],bots[spl[-1]]),
                                                                                       "high":max(bots[two_valued]["high"],bots[spl[-1]])} 
            else:
                if spl[5] == "bot" :
                    cbots[spl[6]] = bots[two_valued]["low"] if spl[6] not in bots else {"low":min(bots[two_valued]["low"],bots[spl[6]]),
                                                                                        "high":max(bots[two_valued]["low"],bots[spl[6]])}
                    cbots[two_valued] = bots[two_valued]["high"]   
                else:
                    cbots[spl[-1]] = bots[two_valued]["high"] if spl[-1] not in bots else {"low":min(bots[two_valued]["high"],bots[spl[-1]]),
                                                                                           "high":max(bots[two_valued]["high"],bots[spl[-1]])}
                    cbots[two_valued] = bots[two_valued]["low"]
            cbots.pop(two_valued,None)
    return cbots 

def sol(instructions:list[str],d,part=1)->str:
    bots = set_chips(instructions)
    if d in bots.values():
        return [bot for bot in bots if bots[bot]==d][0]
    while d not in bots.values():
        bots=changed(bots,instructions)
        if d in bots.values():
            return [bot for bot in bots if bots[bot]==d][0]


if __name__ == "__main__":
    with open("input10_16.txt") as inp:
        instructions = [d.strip() for d in inp.readlines()]
    
    print(sol(instructions,{"low":17,"high":61}))