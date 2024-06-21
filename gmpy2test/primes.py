#!python
import gmpy2

def main():
    print(gmpy2.next_prime(1_000_000))
    p = 1
    with open("primes.txt","w") as primes:

        for i in range(1,1_000_001):
            p = gmpy2.next_prime(p)
            primes.write(f"{i} : {p}\n")
    

if __name__ == "__main__":
    main()