#!python

from collections import Counter

def getCol(data:list[str],j:int)-> str:
    if j in range(len(data[0])):
        col = []
        for d in data:
            col.append(d[j])
        return "".join(col)
    return None


def sol(words:list[str],part=1)->str:
    cols = []
    for j in range(len(words[0])):
        cols.append(getCol(words,j))
    

    message = ""
    for w in cols:
        c= Counter(w)
        if part == 1:
            message += c.most_common(1)[0][0]
        else:
            message += c.most_common(len(w))[-1][0]    

    return message    
            
if __name__ == "__main__":
    with open("input06_16.txt") as inp:
        words = [w.strip() for w in inp.readlines()]


    print(f"Part 1 : {sol(words)}\nPart 2 : {sol(words,2)}")
 
    