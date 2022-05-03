#!python
from ast import If
import sys
from collections import Counter

def number_of_matching_lengths(array_of_signals, lengths):
    res = 0
    for signals in array_of_signals:
        for signal in signals:
            l = len(signal)
            if l in lengths:
                res += 1
                
    return res


def get_output(train, test):
    length_two = ''
    length_three = ''
    length_four = ''
    length_five = []
    length_six = []
    length_seven =''
    order = ["z", "z", "z", "z", "z", "z", "z"]
    
    for signal in train:
        match len(signal):
            case 2:
                length_two = signal
            case 3:
                length_three = signal
            case 4:
                length_four = signal
            case 5:
                length_five.append(signal)
            case 6:
                length_six.append(signal)   
            case 7:
                length_seven = signal     

    
    four_minus_two = length_four.translate({ord(i):None for i in length_two})                   

    for char in length_three:
        if  char not in length_two:
            order[0] = char

    for signal in length_five:
        if Counter(signal) > Counter(length_two):
            for char in signal:
                if char not in length_three and char not in length_four:
                    order[6] = char
   
    for signal in length_six:
        if not (Counter(signal) > Counter(length_two)):
                if length_two[0] not in signal:
                    order[2] = length_two[0]
                    order[5] = length_two[1]

                else:
                    order[5] = length_two[0]
                    order[2] = length_two[1]
        elif Counter(signal) > Counter(four_minus_two):
            order[4] = "abcdefg".translate({ord(i):None for i in signal})
        else:
            order[3] = "abcdefg".translate({ord(i):None for i in signal})
    
    order[1] = "abcdefg".translate({ord(i):None for i in order})

    digits = [[0,1,2,4,5,6], [2,5], [0,2,3,4,6],
              [0,2,3,5,6], [1,2,3,5], [0,1,3,5,6],
              [0,1,3,4,5,6], [0,2,5], [0,1,2,3,4,5,6],
              [0,1,2,3,5,6]]


    res=0
    for i in range(len(test)):
        segments = []
        for char in test[i]:
            segments.append(order.index(char))
        
        segments.sort()
        
        
        for j in range(len(digits)):
            if digits[j] == segments:
                res = 10*res+j  
                break  

    return res
            

def get_total_output(trains, tests):
    res = 0
    for i in range(len(trains)):
        res += get_output(trains[i], tests[i]) 
    
    return res            
    


test = [["fdgacbe", "cefdb", "cefbgd", "gcbe"],
        ["fcgedb", "cgb", "dgebacf", "gc"],
        ["cg", "cg", "fdcagb", "cbg"],
        ["efabcd", "cedba", "gadfec", "cb"],
        ["gecf", "egdcabf", "bgf", "bfgea"],
        ["gebdcfa", "ecba",  "ca", "fadegcb"],
        ["cefg", "dcbef", "fcge", "gbcadfe"],
        ["ed", "bcgafe" "cdgba", "cbgef"],
        ["gbdfcae", "bgc", "cg", "cgb"],
        ["fgae", "cfgab", "fg", "bagce"]]


data = sys.argv[1:]
traindata = [x.split("|")[0].split() for x in data]
testdata = [x.split("|")[1].split() for x in data]


print(number_of_matching_lengths(testdata, [2, 4, 3, 7]))
print(Counter("abcdefg") > Counter("k"))
print(get_total_output(traindata, testdata))