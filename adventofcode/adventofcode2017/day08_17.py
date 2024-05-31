#!python
def sol(instructions,part=1)-> int :
    registers = set([i[0][0] for i in instructions])
    registers = {r:0 for r in registers}
    max_value = 0
    for ins in instructions:
        match ins[1][1]:
            case "<":
                if registers[ins[1][0]] < ins[1][2]:
                    registers[ins[0][0]] += ins[0][1]
            case ">" :
                if registers[ins[1][0]] > ins[1][2]:
                    registers[ins[0][0]] += ins[0][1]
            case "<=":
                if registers[ins[1][0]] <= ins[1][2]:
                    registers[ins[0][0]] += ins[0][1]
            case ">=":
                if registers[ins[1][0]] >= ins[1][2]:
                    registers[ins[0][0]] += ins[0][1]
            case "==":
                if registers[ins[1][0]] == ins[1][2]:
                    registers[ins[0][0]] += ins[0][1]
            case "!=":
                if registers[ins[1][0]] != ins[1][2]:
                    registers[ins[0][0]] += ins[0][1]
            
        max_value = max(max_value,registers[ins[0][0]])
        
    return max(registers.values()) if part == 1 else max_value                    
           
           
def main():
    with open("input08_17.txt") as inp:
        instructions = [d.strip().replace("dec -","inc ") for d in inp.readlines()]
        instructions = [i.replace("dec ","inc -") for i in instructions]
        instructions = [i.split(" if ") for i in instructions]
        instructions = [(i[0].split(" inc "),i[1]) for i in instructions]
        instructions = [([i[0][0],int(i[0][1])],[i[1].split()[0],i[1].split()[1],int(i[1].split()[2])]) for i in instructions]

    print(f"Part 1 : {sol(instructions)}\nPart 2 : {sol(instructions,2)}")

if __name__ == "__main__":
    main()    