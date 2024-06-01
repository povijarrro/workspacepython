#!python
import re
from readLines import readLines

englishDigits={"1":"1", "2":"2", "3":"3",
               "4":"4", "5":"5", "6":"6",
               "7":"7", "8":"8", "9":"9",
               "one":"1", "two":"2", "three":"3", 
               "four":"4", "five":"5", "six":"6", 
               "seven":"7", "eight":"8", "nine":"9"}
    
basicInput=["two1nine", "eightwothree", "abcone2threexyz",
            "xtwone3four", "4nineeightseven2" , "zoneight234",
            "7pqrstsixteen"]

def firstDigit(string):
    for i in range(len(string)):
        for k,v in englishDigits.items():
            if(string[i:].startswith(k)):
                return v,i
   
    return None 

def lastDigit(string):
    for i in range(len(string)):
        for k,v in englishDigits.items():
            if(string[::-1][i:].startswith(k[::-1])):
                return v,len(string)-len(k)-i
    return None  

def solution1(lst):
    nums=[]
    for string in lst:
        s=re.sub(r"[a-z]","",string)
        nums.append(int(s[0]+s[-1]))
    return sum(nums) 

def solution2(lst):
    sum = 0
    for string in lst: 
        f,l=firstDigit(string)[0], lastDigit(string)[0]
        sum+=int(f+l)
    return sum 


               
def main():
    data = readLines("input01_23.txt")

    print(f"Part 1 : {solution1(data)}")
    print(f"Part 2 : {solution2(data)}")

if __name__ == "__main__":
    main()    