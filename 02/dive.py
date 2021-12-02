with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)


# Part 1

# x = 0
# y = 0 # horizontal position
# z = 0 # positive is down!!!

# for instruction in data:
#     parsed_instruction = instruction.split(" ")
#     direction = parsed_instruction[0]
#     amount = int(parsed_instruction[1])

#     if direction == "forward":
#         y += amount
#     elif direction == "down":
#         z += amount
#     elif direction == "up":
#         z -= amount

# print(y * z)

# Part 2
aim = 0
y = 0 # horizontal position
z = 0 # positive is down!!!

for instruction in data:
    parsed_instruction = instruction.split(" ")
    direction = parsed_instruction[0]
    amount = int(parsed_instruction[1])

    if direction == "forward":
        y += amount
        z += aim * amount
    elif direction == "down":
        aim += amount
    elif direction == "up":
        aim -= amount

print(y * z)
