#!python

def sol(data:list[str],part:int=1)->int:
    
    start:int = 50
    curr_state:int = start
    num_data:list[int]=[int(d[1:]) if d[0]=="R" else -int(d[1:]) for d in data]
    password:int = 0
    
    if part == 1:
        
        for n in num_data:
        
            if curr_state == 0:
                password += 1
            
            curr_state = (curr_state + n)%100
    
    elif part == 2:

        for n in num_data:
            
            sign = n//abs(n)
            state = curr_state
            
            for _ in range(abs(n)):
                if state == 0:
                    password +=1
                state = (state + sign)%100    
            
            curr_state = (curr_state+n)%100
    
    return password




def main()->None:
    with open("input01_25.txt") as inp:
        data = [d.strip() for d in inp.readlines()]
    with open("test01_25.txt") as inp:
        test = [d.strip() for d in inp.readlines()]
    print(f"Part l : {sol(data,1)}\nPart 2 : {sol(data,2)}")
    print(f"Test part 1 : {sol(test,1)}\nTest part 2 : {sol(test,2)}")

if __name__ == "__main__":
    main()