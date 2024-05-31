#!python
import sys

def check_brackets_line(line):
    bracket_pairs = {"(":")", "[":"]", "{":"}", "<":">", ")":"(", "]":"[", "}":"{", ">":"<"}
    open_brackets = "([{<"
    brackets = "()[]{}<>"
    actual_brackets = []
    for bracket in line:
        if bracket not in brackets:
            return False, bracket, actual_brackets
        elif bracket in open_brackets:
            actual_brackets.append(bracket)
        elif actual_brackets[-1] != bracket_pairs[bracket]:
            return False, bracket, actual_brackets
        else:
            actual_brackets.pop()    

    return True, None, actual_brackets

def get_total_error_score(data):
    score = 0
    score_table = {")":3, "]":57, "}":1197, ">":25137}
    for line in data:
        check=check_brackets_line(line)
        if not check[0]:
            score += score_table[check[1]] 
    return score


def get_completion(line):
    check = check_brackets_line(line)
    if check[0]:
        return "".join(reversed(check[2])).translate({ord("("):")", ord("["):"]", ord("{"):"}", ord("<"):">"})


def get_completion_score(line):
    compl = get_completion(line)
    if compl is None:
        return None
    score = 0
    score_table = {")":1, "]":2, "}":3, ">":4}
    for bracket in compl:
        score *=5
        score += score_table[bracket]
    return score

def get_middle_completion_score(data):
    score_list = []
    for line in data:
        cs = get_completion_score(line)
        if cs is None:
            continue
        else:
            score_list.append(cs)
    
    return sorted(score_list)[(len(score_list)-1)//2]


test = ["[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]"]


for line in test:
    print(get_completion(line), get_completion_score(line))

print(get_middle_completion_score(test))
# print(get_total_error_score(test))

data = sys.argv[1:]

#print(get_total_error_score(data))

print(get_middle_completion_score(data))