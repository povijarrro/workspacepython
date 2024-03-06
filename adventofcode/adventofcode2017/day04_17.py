#!python

def sol(passwords, part = 1):
    if part == 1 :
        return sum(1 for words in passwords if all(c == 1 for c in [words.count(w) for w in words]))
    
    else:
        std = [["".join(sorted(list(s))) for s in words] for words in passwords]
        return sol(std)


if __name__ == "__main__":
    with open("input04_17.txt") as inp:
        passwords = [d.strip().split() for d in inp.readlines()]

    print(f"Part 1 : {sol(passwords)}\nPart 2 : {sol(passwords,2)}")   