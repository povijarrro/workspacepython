#!python
import sys


def numOfInc(input):
    n = len(input)
    res = 0
    for i in range(n-1):
        if int(input[i + 1]) > int(input[i]):
            res += 1
    return res

def numOfWindowInc(input):
    n = len(input)
    newInput = []
    for i in range(n-2):
        newInput.append(str(int(input[i])+int(input[i+1])+int(input[i+2])))
    return numOfInc(newInput)


print(numOfWindowInc([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]))
#print(numOfInc(sys.argv[1:]))
print(numOfWindowInc(sys.argv[1:]))

