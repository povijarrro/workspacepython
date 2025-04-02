#!python
def true_gates(sensors):
    if len(sensors) == 1:
        return sensors[0]
    else:
        gates = [((sensors[i] and sensors[i+1]) if i%4 == 0 else (sensors[i] or sensors[i+1])) for i in range(0, len(sensors), 2)]
        return sum(sensors)+true_gates(gates)

def main():
    with open("input24_02.txt") as inp:
        data:list[str] = [d.strip() for d in inp.readlines()]
        sensors = [d == "TRUE" for d in data]
        
    sol1 = sum((i+1)*s for (i,s) in enumerate(sensors))
    sol2 = sum(((sensors[i] and sensors[i+1]) if i%4 == 0 else (sensors[i] or sensors[i+1])) for i in range(0, len(sensors), 2))
    sol3 = true_gates(sensors)

    print(f"Part 1 : {sol1}\nPart 2 : {sol2}\nPart 3 : {sol3}")
if __name__ == "__main__" :
    main() 