#!python
from collections import Counter
from readLines import readLines

cards = ("2","3","4","5","6","7","8","9","T","J","Q","K","A")
types =("HIGH","ONE_P", "TWO_P","THREE","FULL","FOUR","FIVE")
d=dict()
for i,s in enumerate("23456789TJQKA"):
    d[s]="23456789ABCDE"[i]

d2 = dict() 
for i,s in enumerate("J23456789TQKA"):
    d2[s]="123456789ABCD"[i]


def trn(card:str)->str:
    return card.translate("23456789TJQKA".maketrans(d))

def trn2(card:str)->str:
    return card.translate("23456789TJQKA".maketrans(d2))

def jokerValue(hand:str)->str:
    c =Counter(hand.replace("J",""))
    if c.most_common()==[] or not "J" in hand : return "A" 
    m="2"
    most=c.most_common()[0][1]
    for s,count in c.most_common():
        if (count<most):break
        if(trn(s)>m):
            m=s
    return m


def tOfHand(hand:str)->str:
    counts=[hand.count(card) for card in hand]
    
    if 5 in counts:return "FIVE"
    if 4 in counts: return "FOUR"
    if 3 in counts:
        if 2 in counts:
            return "FULL"
        return "THREE"
    if counts.count(2)==4:return "TWO_P"
    if 2 in counts:return "ONE_P"   
    return "HIGH" 


def solution1(data:list[tuple])->int:
    sdata=sorted(data,key=lambda a:(types.index(tOfHand(a[0])),trn(a[0])))
    total=0
    for i,pair in enumerate(sdata):
        total+=(i+1)*pair[1]
    
    return total

def solution2(data:list[tuple])->int:
    sdata=sorted(data,key=lambda a:(types.index(tOfHand(a[0].replace("J",jokerValue(a[0])))),trn2(a[0])))
    total=0
    for i,pair in enumerate(sdata):
        total+=(i+1)*pair[1]
    
    return total


if __name__ == "__main__":
    data = readLines("input07.txt")
    data = [(i.split()[0], int(i.split()[1])) for i in data]

    print(f"Part 1 : {solution1(data)}")
    print(f"Part 2 : {solution2(data)}")




    
    