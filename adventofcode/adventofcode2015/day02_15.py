#!python

def get_paper_area(dim:str)->int:
    dims=sorted([int(s) for s in dim.split("x")])
    return(dims[0]*dims[1]+2*(dims[0]*dims[1]+dims[0]*dims[2]+dims[1]*dims[2]))

def get_ribbon_length(dim:str)->int:
    dims=sorted([int(s) for s in dim.split("x")])
    return(dims[0]*dims[1]*dims[2]+2*(dims[0]+dims[1]))



def sol(data:list[str], part=1)->int:
    paper = 0
    ribbon = 0
    for s in data:
        paper += get_paper_area(s)
        ribbon += get_ribbon_length(s)

    return paper if part == 1 else ribbon   

def main():

    with open("input02_15.txt") as inp:
        data = [s.strip() for s in inp.readlines()]

    print(f"Part 1 : {sol(data,1)}\nPart 2 : {sol(data,2)}")   

if __name__ == "__main__":
    main()    