#!python
def get_real_len(sequence:str, start,end, part = 1)->int:
    n = end-start
    if "(" not in sequence[start:end]:
        return n
    else:
        ilpar = sequence.find("(",start,end)
        irpar = sequence.find(")",ilpar+1)
        spl = sequence[ilpar+1:irpar].split("x")
        real_len = ilpar+int(spl[1])*int(spl[0])+get_real_len(sequence[irpar+1+int(spl[0]):],0,n-irpar-1-int(spl[0]))
        if part == 1:
            return real_len
        else:
            real_len = ilpar - start + int(spl[1])*get_real_len(sequence,irpar+1,irpar+1+int(spl[0]),part)+get_real_len(sequence,irpar+1+int(spl[0]),end,part)
            return real_len 

def sol(sequence:str, part = 1)->int:
    return get_real_len(sequence,0,len(sequence),part)


        
if __name__ == "__main__":
    with open("input09_16.txt") as inp:
        sequence = inp.readline().strip()

    print(f"Part 1 : {sol(sequence)}\nPart 2 : {sol(sequence,2)}")