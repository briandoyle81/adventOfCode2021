with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)


# Part 1
# last = int(data[0])

# i = 1

# increases = 0

# while i < len(data):
#     if int(data[i]) > last:
#         increases += 1

#     last = int(data[i])
#     i += 1

# print(increases)

# Part 2

last = int(data[0]) + int(data[1]) + int(data[2])

i = 1

increases = 0

while i < len(data) - 2:
    if int(data[i]) + int(data[i+1]) + int(data[i+2]) > last:
        increases += 1

    last = int(data[i]) + int(data[i+1]) + int(data[i+2])
    i += 1

print(increases)
