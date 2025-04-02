#!python
from itertools import permutations
def transfer(balances,transactions, part = 1):
    res = balances.copy()
    amount = 0
    debts = {c:0 for c in permutations(balances,2)}
    for t in transactions:
        if part == 1:
            amount = t["amount"]
            res[t["from"]] -= amount
            res[t["to"]] += amount
        elif part == 2:
            amount = min(t["amount"],res[t["from"]]) 
            res[t["from"]] -= amount
            res[t["to"]] += amount
        elif part == 3:
            if res[t["from"]]< t["amount"]-debts[(t["from"],t["to"])]:
                res[t["from"]] = 0
                res[t["to"]] += res[t["from"]]- sum(debts[(t["to"],codename)] for codename in balances if codename != t["to"])
                debts[(t["from"],t["to"])] -= t["amount"]
            else :
                res[t["from"]] -= t["amount"] + debts[(t["from"],t["to"])] 
                debts[(t["from"],t["to"])] = 0  
            

    return res    

def main():
    with open("example25_09.txt") as inp:
        data:list[str] = [d.strip() for d in inp.readlines()]
        balances={d.split(" HAS ")[0]:int(d.split(" HAS ")[1]) for d in data if " HAS " in d}
        transactions = [{"from":d.split()[1],
                         "to":d.split()[3],
                         "amount":int(d.split()[-1])} for d in data if "FROM" in d]
        
        print(transfer(balances,transactions,3))
    print(len(balances))
    print(len(list(permutations(balances,2))))
    sol1 = sum(amount for amount in sorted(transfer(balances,transactions,1).values(),reverse=True)[:3])
    sol2 = sum(amount for amount in sorted(transfer(balances,transactions,2).values(),reverse=True)[:3])
    sol3 = sum(amount for amount in sorted(transfer(balances,transactions,3).values(),reverse=True)[:3])

    print(f"Part 1 : {sol1}\nPart 2 : {sol2}\nPart 3 : {sol3}")
if __name__ == "__main__" :
    main() 