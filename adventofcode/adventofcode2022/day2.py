#!python
import sys
import copy

LOSE_POINTS = 0
DRAW_POINTS = 3
WIN_POINTS = 6

losing_dict = {"A":"Z",
               "B":"X",
               "C":"Y", }

draw_dict = {"A":"X",
             "B":"Y",
             "C":"Z", }

winning_dict = {"A":"Y",
                "B":"Z",
                "C":"X"}

score_dict = {"X": 1,
              "Y": 2,
              "Z": 3}                

data = [x.split(" ") for x in sys.argv[1:]]

def score(data):
    total=0
    for row in data:
        if row[1] == winning_dict[row[0]]:
            total+=WIN_POINTS
        elif row[1] == draw_dict[row[0]]:
            total+=DRAW_POINTS
        else:
            total+=LOSE_POINTS    
        total+=score_dict[row[1]]        
    return total

def transform(data):
    res = copy.deepcopy(data)
    for row in res:
        match row[1]:
            case "X": 
                row[1] = losing_dict[row[0]]
            case "Y": 
                row[1] = draw_dict[row[0]]
            case "Z": 
                row[1] = winning_dict[row[0]]        

    return res


print(score(data))
print(score(transform(data)))
