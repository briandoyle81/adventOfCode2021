from statistics import mean
from statistics import median

with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

# Further data processing

# TODO: Can this be combined into one step elegantly or do you have to use a loop?

patterns = [e.split('|')[0].split() for e in data]
outputs  = [e.split('|')[1].split() for e in data]

# breakpoint()

# Part 1

# length to digit reference

lookup = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}

unique = 0

for pattern in patterns:
    for digit in pattern:
        if len(digit) in lookup:
            unique += 1

print(unique)

# Part 2

# Reference

#  aaaa
# b    c
# b    c
#  dddd
# e    f
# e    f
#  gggg

numbers = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg"
}

lengths = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

contained_in = {
    "a": {0, 2, 3, 5, 6, 7, 8, 9},
    "b": {0, 4, 5, 6, 8, 9},
    "c": {0, 1, 2, 3, 4, 7, 9, 9},
    "d": {2, 3, 4, 5, 6, 8, 9},
    "e": {0, 2, 6, 8},
    "f": {0, 1, 3, 4, 5, 6, 7, 8, 9},
    "g": {0, 2, 3, 5, 6, 8, 9}
}

total = 0
for i, pattern in enumerate(patterns):
    # sort by length, get the easy ones
    pattern.sort(key=len)
    print(pattern)
    output = outputs[i]
    # breakpoint()

    # progress through the pattern to determine mapping
    # start with the numbers known by length
    mixed_numbers = {
        1: set(pattern[0]),
        7: set(pattern[1]),
        4: set(pattern[2]),
        8: set(pattern[9])
    }

    # create a map from mixed up letter to standard letter
    # this might be better with a graph.
    # solve like word ladder
    # but trying the dumb way first

    # or maybe an not and mapping?

    # a == 7 - 1
    # b ==

    # binary_rep = {
    #     0:
    # }

    conversion_map = dict()

    # a is the letter that is in 1 but not 7

    for letter in mixed_numbers[7]:
        if letter not in mixed_numbers[1]:
            conversion_map["a"] = letter
            break

    # known letters: a
    # known numbers: 1, 4, 7, 8

    # 0 is the length 6 number that has all letters from 4

    length_6 = {e for e in pattern if len(e) == 6}

    for entry in length_6:
        # breakpoint()
        if mixed_numbers[4].issubset(set(entry)):
            mixed_numbers[9] = set(entry)
            length_6.remove(entry)
            # breakpoint()
            # print("found 9")
            break

    if 9 not in mixed_numbers:
        print("ERROR")
        breakpoint()

    # e is the letter in 8 but not 9
    conversion_map["e"] = list(mixed_numbers[8].difference(mixed_numbers[9]))[0]

    # known letters: a, e
    # known numbers: 1, 4, 7, 8, 9
    # length_6 has: 6, 0

    # 0 is the remaining 6 length that has all the letters from 1
    for entry in length_6:
        # breakpoint()
        if mixed_numbers[1].issubset(set(entry)):
            mixed_numbers[0] = set(entry)
            length_6.remove(entry)
            # breakpoint()
            # print("found 0")
            break

    if 0 not in mixed_numbers:
        print("ERROR")
        breakpoint()

    # 6 is the reamaining 6 length
    mixed_numbers[6] = set(list(length_6)[0])

    # c is the letter in 6 but not 8
    conversion_map["c"] = list(mixed_numbers[8].difference(mixed_numbers[6]))[0]

    # f is the letter in 1 that is not c
    conversion_map["f"] = list(mixed_numbers[1].difference({conversion_map["c"]}))[0]

    # d is the letter in 8 but not 0
    conversion_map["d"] = list(mixed_numbers[8].difference(mixed_numbers[0]))[0]

    # b is the letter in 4 that is not known
    conversion_map["b"] = list(mixed_numbers[4] - set(conversion_map.values()))[0]

    # g is the last letter
    conversion_map["g"] = list({"a", "b", "c", "d", "e", "f", "g"} - set(conversion_map.values()))[0]
    print(conversion_map)

    # known letters: a, e, c, f, d, b, g
    # known numbers: 1, 4, 7, 8, 9, 0, 6

    # probably don't need all the letters matched
    # length 5 contains: 2, 3, and 5
    length_5 = {e for e in pattern if len(e) == 5}

    # 3 is the number containing the letters from 1

    for entry in length_5:
        # breakpoint()
        if mixed_numbers[1].issubset(set(entry)):
            mixed_numbers[3] = set(entry)
            length_5.remove(entry)
            # breakpoint()
            # print("found 3")
            break

    if 3 not in mixed_numbers:
        print("ERROR")
        breakpoint()

    # known letters: a, e, c, f, d, b, g
    # known numbers: 1, 4, 7, 8, 9, 0, 6, 3
    # length 5 contains: 2, 5

    # 5 is the entry that all of it's numbers are in 6

    for entry in length_5:
        # breakpoint()
        if set(entry).issubset(mixed_numbers[6]):
            mixed_numbers[5] = set(entry)
            length_5.remove(entry)
            # breakpoint()
            # print("found 5")
            break

    if 5 not in mixed_numbers:
        print("ERROR")
        breakpoint()

    # the last number in length_5 and overall is 2

    mixed_numbers[2] = set(list(length_5)[0])

    print(mixed_numbers)
    # breakpoint()

    output = outputs[i]
    # breakpoint()

    digits = []

    for digit in output:
        for key, code in mixed_numbers.items():
            if set(digit) == code:
                digits.append(key)

    print(digits)
    # breakpoint()
    # TODO: Cleaner way to do this
    number = int("".join(str(e) for e in digits))
    total += number

print(f"The total is {total}")
