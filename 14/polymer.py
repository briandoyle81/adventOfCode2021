with open('test_data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

# Further data processing

template = data[0]

rules = {}

for i, line in enumerate(data):
    if i == 0 or i == 1:
        continue
    split_line = line.split(" -> ")
    rules[split_line[0]] = split_line[1]
# breakpoint()

# Part 1

# steps = 10

# polymer = template

# for i in range(steps):
#     new = ""

#     for k in range(len(polymer) - 1):
#         first = polymer[k]
#         second = polymer[k+1]

#         pair = first + second

#         if pair in rules:
#             # Add the first and the new char
#             # Second will get added when it is first
#             new += first
#             new += rules[pair]
#         else:
#             print("need to handle no inseration")
#             breakpoint()

#     # Add the last character, it was never "first"
#     new += polymer[-1]

#     polymer = new

#     # print(polymer)

# # Count the elements and find the difference between most and least

# print("Done building polymer, finding most and least")
# count = {}

# most = 0
# # least = float('inf')

# for element in polymer:
#     if element not in count:
#         count[element] = 1
#     else:
#         count[element] += 1

#     if count[element] > most:
#         most = count[element]

#     # if count[element] < least:
#     #     least = count[element]

# # breakpoint()
# # TODO: I think there must be a way to count the least as you go

# least = min(count.values())
# print(most - least)

# Part 2

# Breaks down about 20, fine for 10.  Exponential time complexity

# Need to reduce. Memoization?  Tabulation?
# Polymer doubles in size every step, but has lots of repetition

# Start building an insane dictionary?
# keep each subpattern in it

# Do it recursively?

# how to keep track of steps?
# figure that out later

def recursive_polymer(subsequences, subsequence):
    # worried about 1
    if len(subsequence) == 1:
        # print("Deal with 1")
        # breakpoint()
        return subsequence # Return what, just the letter?  I think it will get a joiner
                           # yes, new right will be the letter and get a joiner
    # base case, subsequence is in dictionary of rules
    # Don't need now, handled by pre-adding rules to subsequences
    # if len(subsequence) == 2:
    #     new = subsequence[0] + rules[subsequence] + subsequence[1]
    #     subsequences[subsequence] = new
    #     return new

    # if we've already processed this subsequence, return it
    if subsequence in subsequences:
        # print("Found subsequence")
        return subsequences[subsequence]

    # otherwise, process it recursively, and add it to sequences
    left = subsequence[:len(subsequence)//2]
    right = subsequence[len(subsequence)//2:]
    joiner = rules[left[-1] + right[0]]
    new_left = recursive_polymer(subsequences, left)
    new_right = recursive_polymer(subsequences, right)
    new = new_left + joiner + new_right
    subsequences[subsequence] = new
    # breakpoint()
    return new

steps = 7

# polymer = template
subsequences = {}

def process_sequence(polymer, steps):
    for i in range(steps):
        # print(i)
        # breakpoint()
        left = polymer[:len(polymer)//2]
        right = polymer[len(polymer)//2:]
        joiner = rules[left[-1] + right[0]]
        new_left = recursive_polymer(subsequences, left)
        new_right = recursive_polymer(subsequences, right)
        # breakpoint()
        polymer = new_left + joiner + new_right

    print(f'Length: {len(polymer)}')
    return polymer

# Maybe pre-calculating each pair out 40 steps first?
# first add rules to subsequences
for key, value in rules.items():
    subsequences[key] = key[0] + value + key[1]
# breakpoint()

# No of course not, this is the exact same calculation somewhere else

for i in range(5):
    print(f'PREPROCESSING {i}')
    to_process = list(subsequences.values())
    for item in to_process:
        # print(item)
        process_sequence(item, 4)

print("done precalculating subsequences")
# breakpoint()

# New observation, the most and least at least seem to be constant once
# established
# Length is always prior * 2 - 1
# or ... some equation that is escaping me, but I don't think it matters

# 0 = 4
# 1 = 4 * 2 - 1 = 7
# 2 = 4 * 4 - 3 = 13
# 3 = 4 * 8 - 7 = 25
# 4 = 4 * 16 - 15 = 49
# 5 = 4 * 32 - 31 = 97

# y = 4 * 2^x - (2^x - 1)

# First and Last will never change

# polymer = process_sequence(template, steps)
# Count the elements and find the difference between most and least

print("Done building polymer, finding most and least")
def find_most_least(polymer):
    count = {}

    most = 0
    # least = float('inf')

    for element in polymer:
        if element not in count:
            count[element] = 1
        else:
            count[element] += 1

        if count[element] > most:
            most = count[element]

        # if count[element] < least:
        #     least = count[element]

    # breakpoint()
    # TODO: I think there must be a way to count the least as you go

    least = min(count.values())
    print(f'Difference: {most - least}')

    smallest = ""
    largest = ""

    for element, number in count.items():
        if number == most:
            largest = element
        if number == least:
            smallest = element

    print(f'{smallest}:{least}, {largest}:{most}')
    return most-least

# print(find_most_least(polymer))

for i in range(40):
    print(f'STEPS: {i}')
    polymer = process_sequence(template, i)
    find_most_least(polymer)
    breakpoint()
