from statistics import mean
from statistics import median

with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

# Further data processing

# TODO: Can this be combined into one step elegantly or do you have to use a loop?

patterns = [e.split('|')[0].split() for e in data]
outputs = patterns = [e.split('|')[1].split() for e in data]

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
