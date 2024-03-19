#!python
import sys
sys.setrecursionlimit(100000)
def get_real_seq(sequence:str, part = 1)->str:
    if "(" not in sequence:
        return sequence
    else:
        ilpar = sequence.index("(")
        irpar = sequence.index(")")
        spl = sequence[ilpar+1:irpar].split("x")
        real_seq = sequence[:ilpar]+int(spl[1])*sequence[irpar+1:irpar+1+int(spl[0])]+get_real_seq(sequence[irpar+1+int(spl[0]):])
        if part == 1:
            return real_seq
        else:
            real_seq = sequence
            while "(" in real_seq:
                real_seq = get_real_seq(real_seq)
            return real_seq    

def sol(sequence:str, part = 1)->int:
    return len(get_real_seq(sequence,part))


        
if __name__ == "__main__":
    with open("input09_16.txt") as inp:
        sequence = inp.readline().strip()

    print(sol(sequence,2))     

    