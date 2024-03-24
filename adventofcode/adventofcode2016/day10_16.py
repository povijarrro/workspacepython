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

def changed(bots:dict, instructions:list[str],output:dict)->dict:
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
                    output.update({spl[-1]:bots[two_valued]["high"]})
                       
                else:
                    cbots[spl[-1]] = bots[two_valued]["high"] if spl[-1] not in bots else {"low":min(bots[two_valued]["high"],bots[spl[-1]]),
                                                                                           "high":max(bots[two_valued]["high"],bots[spl[-1]])}
                    cbots[two_valued] = bots[two_valued]["low"]
                    output.update({spl[6]:bots[two_valued]["low"]})
                    if spl[-2] == "output":
                        output.update({spl[-1]:bots[two_valued]["high"]})

            cbots.pop(two_valued,None)
    return cbots,output

def sol(instructions:list[str],d,part=1)->str:
    bots = set_chips(instructions)
    output = {}
    if part == 1:
        if d in bots.values():
            return [bot for bot in bots if bots[bot]==d][0]
        while d not in bots.values():
            bots,_ = changed(bots,instructions,output)
            if d in bots.values():
                return [bot for bot in bots if bots[bot]==d][0]
    else:
        while "0" not in output or "1" not in output or "2" not in output:
            bots,output = changed(bots,instructions,output)
            if "0" in output and "1" in output and "2" in output:
                return output["0"]*output["1"]*output["2"]       


if __name__ == "__main__":
    with open("input10_16.txt") as inp:
        instructions = [d.strip() for d in inp.readlines()]
    
    print(f"Part 1 : {sol(instructions,{"low":17,"high":61})}\nPart 2 : {sol(instructions,None,2)}")