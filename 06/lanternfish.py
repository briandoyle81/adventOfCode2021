with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

# Further data processing

# fishes = []
# fishes.append([int(e) for e in data[0].split(',')])
# fishes.append([int(e) for e in data[0].split(',')])

# part 2 data processing
fishes = [int(e) for e in data[0].split(',')]

# breakpoint()

# cycle = 7
cycle_num = 6
birth_num = 8

# breakpoint()

# Part 1

# just need a back buffer

current = 0
back = 1

days = 256

# for _ in range(days):
#     for i in range(len(fishes[current])):
#         fish = fishes[current][i] - 1
#         if fish == -1:
#             fish += cycle
#             fishes[back].append(8)
#             fishes[current].append(8)

#         # breakpoint()
#         fishes[back][i] = fish

#     # swap the buffer
#     temp = current
#     current = back
#     back = temp

# print(len(fishes[current]))

# Part 2

# create a table of how many fish in each number of days
# update that table

table = dict()

# lazy init
table[0] = 0
table[1] = 0
table[2] = 0
table[3] = 0
table[4] = 0
table[5] = 0
table[6] = 0
table[7] = 0
table[8] = 0

for fish in fishes:
    table[fish] += 1

# print(table)

for _ in range(days):
    zero = table[0]
    # print(zero)
    for i in range(1, 9):
        table[i-1] = table[i]

    table[birth_num] = zero
    table[cycle_num] += zero

    # print(table)
    # breakpoint()



count = 0

for key, value in table.items():
    count += value

print(count)
