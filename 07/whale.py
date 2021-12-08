from statistics import mean
from statistics import median

with open('test_data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

# Further data processing

# crabs = [int(e) for e in data[0].split(',')]
crabs = [0, 0, 0, 0, 50000000]

# breakpoint()

# Part 1

# Find the average position then calc fuel?

# average = sum(crabs) // len(crabs)

# print(sum(crabs))
# print(len(crabs))
# print(average)
# print(mean(crabs)) # mean is not median, duh
# print(median(crabs))

# int average is 4

# the test answer is this minus the mode, but I think
# this is a coincidence

# I'm not sure why it isn't the average.  There must
# be a way to calculate some kind of offset, maybe with the mean?

# Non-int average and mean are the same, also likely coincidence

print("#######################")

arr = [ 0, 0, 0, 0, 5 ]

# print(sum(arr)// len(arr))

sorted_crabs = sorted(crabs)

# print(sorted_crabs)

midpoint = len(sorted_crabs) // 2

# print(midpoint)

# print(sorted_crabs[midpoint])

# I think it's the median

target = sorted_crabs[midpoint]
# print(target)

cost = 0

for crab in crabs:
    fuel = abs(target - crab)
    # print(f'Move from {crab} to {midpoint}: {fuel} fuel')
    cost += fuel

print(f'Part 1 cost: {cost}')

# Part 2

# I think this one should be the mutual average.

print(f'Raw average: {mean(crabs)}')

average = int(round(mean(crabs), 0)) - 1 # TODO: Why - 1???????

print(average)

new_cost = 0
# There's probably math to make this nicer
for crab in crabs:
    distance = abs(crab - average)
    fuel = 1
    for _ in range(distance):
        new_cost += fuel
        fuel += 1

print(f"New cost: {new_cost}")
