import math
from statistics import median

with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

# Further data processing


# breakpoint()

# Part 1
# balanced brackets

closer_map = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}

opener_map = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

def find_if_corrupted(line):
    ss = []

    for char in line:
        if char not in closer_map:
            ss.append(char)

        else:
            last = ss.pop()
            if closer_map[char] != last:
                return char

    return None

def find_score(data):
    score = 0

    for line in data:
        result = find_if_corrupted(line)
        if result is not None:
            score += points[result]

    return score


print(find_score(data))

# Part 2

# discard corrupted lines

good_lines = [line for line in data if not find_if_corrupted(line)]

for line in good_lines:
    print(line)

completion_scores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

def find_completion(line):
    line_score = 0
    ss = []

    for char in line:
        if char not in closer_map:
            ss.append(char)

        else:
            last = ss.pop()

    # breakpoint()
    reversed = ss[::-1]
    for opener in reversed:
        # breakpoint()
        closer = opener_map[opener]
        line_score *= 5
        line_score += completion_scores[closer]

    # breakpoint()
    return line_score

def do_autocompleted(good_lines):
    scores = []
    for line in good_lines:
        scores.append(find_completion(line))

    print(scores)
    return scores

print(median(do_autocompleted(good_lines)))
