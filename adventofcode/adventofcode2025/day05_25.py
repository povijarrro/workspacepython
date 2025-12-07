#!python
def range_union(ints:list[tuple[int,int]])->list[tuple[int,int]]:
    n = len(ints)
    if n == 0:
        return []
    elif n== 1:
        return [ints[0]]
    else :
        sor = sorted(ints, key=lambda x: x[0])
        merged = [sor[0]]
        
        for current_start, current_end in sor[1:]:
            last_start, last_end = merged[-1]

            if current_start <= last_end:
                merged[-1] = (last_start, max(last_end, current_end))
            else:
                merged.append((current_start, current_end))

    return merged
        

def sol(data:list[str],part:int=1)->int:
    
    ranges = [d for d in data if d.count("-") == 1]
    ranges = [r.split("-") for r in ranges]
    ranges = [(int(t[0]),int(t[1])+1) for t in ranges]
    ingredients = [int(d) for d in data if d.count("-") == 0]
    
    available_fresh = set()
    n_of_all_fresh = 0
    
    if part == 1:
        for ing in ingredients:
            for r in ranges:
                ran = range(r[0],r[1])
                if ing in ran:
                    available_fresh.add(ing)
        return len(available_fresh)
    
    elif part == 2:
        for r in range_union(ranges):
            n_of_all_fresh += r[1]-r[0]
        return n_of_all_fresh   

def main()->None:
    
    with open("input05_25.txt") as inp:
        data = [d.strip() for d in inp.readlines()]
        data.remove("")
    print(f"Part 1 : {sol(data,1)}\nPart 2 : {sol(data,2)}")

if __name__ == "__main__":
    main()