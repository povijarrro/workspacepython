#!python

wires = {}

def eval_gate(s:str,data:dict[str,str])->int:
    if s.isdigit() : return int(s)
    
    if s in wires : return wires[s]
    
    if s in data and data[s].isdigit() :
        wires[s]=int(data[s]) 
    
        return wires[s]
     
    if "NOT" in data[s] : 
        wires[s] = ~eval_gate(data[s][4:],data)&65535
        
        return wires[s]
    
    elif "LSHIFT" in data[s] : 
        l,r = data[s].split(" LSHIFT ")
        wires[s] = eval_gate(l,data)<<int(r)

        return wires[s]
    
    elif "RSHIFT" in data[s] : 
        l,r = data[s].split(" RSHIFT ")
        wires[s] = eval_gate(l,data)>>int(r)

        return wires[s]
    
    elif "AND" in data[s] : 
        l,r=data[s].split(" AND ")
        wires[s] = eval_gate(l,data) & eval_gate(r,data)
        return wires[s]
    
    elif "OR" in data[s] : 
        l,r = data[s].split(" OR ")
        wires[s] = eval_gate(l,data) | eval_gate(r,data)
        return wires[s]
    
    return eval_gate(data[s],data)
    
def sol(data:dict[str,str],part=1)->int:
    global wires
    wires = {}
    if part == 1 :
        return eval_gate("a",data)
    else :
        wires = {"b":eval_gate("a",data)}
        return eval_gate("a",data)


def main():
    with open("input07_15.txt") as inp:
        data = [d.strip() for d in inp.readlines()]
        data = [d.split(" -> ") for d in data]
        data = {d[1]:d[0] for d in data}
    
    #ew = eval_wires(data)
    #print(eval_wire("123 AND 456"))
    #for k,v in data.items():
    #    if v.isdigit():
    #        print(k,v)       

    d={"x":"123",
       "y":"456",
       "d":"x AND y",
       "e":"x OR y",
       "f":"x LSHIFT 2",
       "g":"y RSHIFT 2",
       "h":"NOT x",
       "i":"NOT y"}
    
    print(f"Part 1 : {sol(data)}\nPart 2 : {sol(data,2)}")

if __name__ == "__main__":
    main()   