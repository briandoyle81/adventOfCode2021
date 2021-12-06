with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

# Further data processing

class Line():
    def __init__(self, str):
        # breakpoint()
        spl = str.split()
        self.start = [int(e) for e in spl[0].split(',')]
        self.end = [int(e) for e in spl[2].split(',')]


lines = [Line(e) for e in data]

# breakpoint()

# Part 1

# Again, naive option is appealing.  Just make the thing
# only a million wide by a million long
# actually that is a lot.  let's see what happens

# brute force doesn't work, use dict instead
map = [] # row, col
size = 10
for i in range(size):
    map.append([0] * size)

log = dict()

# breakpoint()

for line in lines:
    if line.start[0] == line.end[0]:
        # continue
        direction = "vertical"
    elif line.start[1] == line.end[1]:
        # continue
        direction = "horizontal"
    else:
        # continue
        direction = "diagonal"
    # print(direction)
    # if direction == "vertical":
    #     differenceY = line.end[1] - line.start[1]
    # if direction == "horizontal":
    #     difference = line.end[0] - line.start[0]
    # if direction == "diagonal":
    #     # a bit hacky for now
    differenceX = line.end[0] - line.start[0]
    differenceY = line.end[1] - line.start[1]


    # print(difference)
    length = max(abs(differenceX), abs(differenceY))
    # print(length)

    for i in range(length + 1):
        # print(i)
        # if direction == "vertical":
        #     if difference > 0:
        #         map[line.start[0]][line.start[1] + i] += 1

        #     if difference < 0:
        #         map[line.start[0]][line.end[1] - i] += 1

        # if direction == "horizontal":
        #     if difference > 0:
        #         map[line.start[0]+i][line.start[1]] += 1

        #     if difference < 0:
        #         map[line.end[0]-i][line.end[1]] += 1
        row = line.start[1]
        col = line.start[0]

        if direction == "vertical" or direction == "diagonal": # x,y to row,col
            if differenceY > 0: # down
                # map[line.start[1] + i][line.start[0]] += 1
                # key = f'{line.start[1] + i},{line.start[0]}'
                # if key not in log:
                #     log[key] = 0
                # else:
                #     log[key] += 1

                row = line.start[1] + i

            elif differenceY < 0:
                # map[][] += 1
                # key = f'{line.end[1]+i},{line.start[0]}'
                # if key not in log:
                #     log[key] = 0
                # else:
                #     log[key] += 1

                row = line.start[1] - i


        if direction == "horizontal" or direction == "diagonal":
            if differenceX > 0:
                # map[][] += 1
                # key = f'{line.start[1]},{line.start[0]+i}'
                # if key not in log:
                #     log[key] = 0
                # else:
                #     log[key] += 1

                col = line.start[0]+i

            if differenceX < 0:
                # print(i)
                # map[][] += 1
                # key = f'{line.start[1]},{line.end[0]+i}'
                # if key not in log:
                #     log[key] = 0
                # else:
                #     log[key] += 1

                col = line.start[0]-i

        key = f'{row},{col}'
        # if row == 0 and col == 0:
        #     breakpoint()
        if key not in log:
            log[key] = 1
        else:
            log[key] += 1


    # for row in map:
    #     print(row)
    # breakpoint()


# for key, value in log.items():
#     # breakpoint()
#     split = key.split(',')
#     map[int(split[0])][int(split[1])] = value


# for row in map:
#     print(row)

count = 0

# for row in map:
#     for item in row:
#         if item > 1:
#             count += 1

for key, value in log.items():
    if value > 1:
        count += 1

print(count)
