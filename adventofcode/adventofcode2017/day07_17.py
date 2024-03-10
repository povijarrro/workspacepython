#!python
def sol(lines:list[str],part = 1)->str:
    if part == 1:
        structure = {l.split()[0]}  
    

if __name__ == "__main__":
    with open("example07_17.txt") as inp:
        lines = [d.strip() for d in inp.readlines()]

    print(sol(lines))
    #print([line for line in lines if line.split()[0] in ["ebii","havc","ugml"]])