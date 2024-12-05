#!python
class Int:
    def __init__(self,value:int,orders:list[tuple[int,int]]|None = None):
        self.value = value
        self.orders = orders
    
    def __str__(self):
        return str(self.value)
    
    def __add__(self, other):
        return Int(self.value+other.value,self.orders)
    
    def __eq__(self,other):
        return self.value == other.value and self.orders == other.orders
    
    def __lt__(self,other):
        return ((self.value,other.value) in self.orders) if self.orders != None else self.value<other.value

    def __le__(self,other):
        return self == other or self<other
    
def part1(updates:list[list[int]],orders:list[tuple[int,int]])->int:
    return sum([upd[len(upd)//2]for upd in updates if sorted(upd,key = lambda x:Int(x,orders))==upd])

def part2(updates:list[list[int]],orders:list[tuple[int,int]])->int:
    return sum([sorted(upd, key = lambda x : Int(x,orders))[len(upd)//2]for upd in updates if sorted(upd,key = lambda x:Int(x,orders))!=upd])

def main()->None:
    with open("./input05_24.txt") as inp:
        data:list[str] = inp.read().strip().split("\n\n")
        orders:list[tuple[int,int]] = [tuple(map(int,ds.split("|"))) for ds in data[0].split("\n")]
        updates:list[list[int]] = [list(map(int,ds.split(","))) for ds in data[1].split("\n")]
    
    with open("./example05_24.txt") as inp:
        data:list[str] = inp.read().strip().split("\n\n")
        exorders:list[tuple[int,int]] = [tuple(map(int,ds.split("|"))) for ds in data[0].split("\n")]
        exupdates:list[list[int]] = [list(map(int,ds.split(","))) for ds in data[1].split("\n")]
   
    print(f"Part 1 : {part1(updates,orders)}\nPart 2 : {part2(updates,orders)}")

if __name__ == "__main__":
    main()    