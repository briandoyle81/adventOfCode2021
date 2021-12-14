with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

# Further data processing

dots = set()
instructions = []

for line in data:
    if line == "":
        continue
    elif line[0] != 'f':
        dots.add(line)
    else:
        inst = line.split()[2].split('=')
        instructions.append(inst)

# breakpoint()

# Part 1

for instruction in instructions:
    if instruction[0] == "x":
        fold_axis_index = 0
    else: # "y"
        fold_axis_index = 1

    fold_line = int(instruction[1])

    new_dots = set()
    for dot in dots:
        dot_split = dot.split(',')
        dot_coords = (int(dot_split[0]), int(dot_split[1]))

        # on unfolded side, it doesn't move, add the same one
        if dot_coords[fold_axis_index] <= fold_line:
            new_dots.add(dot)
        else:
            distance = dot_coords[fold_axis_index] - fold_line
            new_pos = fold_line - distance


            if fold_axis_index == 0:
                new_coords = f'{new_pos},{dot_coords[1]}'
            else:
                new_coords = f'{dot_coords[0]},{new_pos}'

            new_dots.add(new_coords)

    dots = new_dots

    # print(len(dots))
    # breakpoint()

# breakpoint()

# Print to get letters maybe?

grid = []

# 40,40 should be enough
for _ in range(40):
    new_row = []
    grid.append(new_row)
    for _ in range(40):
        new_row.append('.')

for dot in dots:

    split_dot = dot.split(',')
    # reverse for row column
    row = int(split_dot[1])
    col = int(split_dot[0])

    grid[row][col] = '#'


for row in grid:
    print("".join(e for e in row))
