from os import read

with open('test_data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

# Further data processing

data[0] = data[0][13:]

x_y = data[0].split(", ")
x_y[0] = x_y[0][2:]
x_y[1] = x_y[1][2:]

x_range = [int(e) for e in x_y[0].split('..')]
y_range = [int(e) for e in x_y[1].split('..')]

# breakpoint()

# Part 1

# Y down is negative!

def move_probe(position, velocity, x_range, y_range):
    new_position = (position[0] + velocity[0], position[1] + velocity[1])
    # print(new_position)
    # breakpoint()

    if (new_position[0] >= x_range[0] and new_position[0] <= x_range[1] and
        new_position[1] >= y_range[0] and new_position[1] <= y_range[1]):
        result = 'hit'
    elif new_position[0] > x_range[1] or new_position[1] < y_range[1]:
        result = 'miss'
    else:
        result = 'continue'

    return new_position, result

def fire_shot(velocity, x_range, y_range):
    position = (0, 0)
    max_y = 0
    result = 'continue'

    while result == 'continue':
        position, result = move_probe(position, velocity, x_range, y_range)
        if position[1] > max_y:
            max_y = position[1]

        new_x = velocity[0]
        new_y = velocity[1]

        if velocity[0] > 0:
            new_x -= 1

        new_y -= 1

        velocity = (new_x, new_y)
        # print(velocity)

    return result, max_y, velocity

# print(fire_shot([7, 9], x_range, y_range))

# n^2 Solution

def find_peak(max, x_range, y_range):
    max_y = 0
    max_y_velocity = None
    max_y_final_velocity = None

    # For part 2, count all valid
    valid_count = 0

    # And go negative for y
    for i in range(max):
        # for k in range(max): # Part 1 version
        for k in range(-max, max, 1):
            print([i, k])
            result, shot_max_y, shot_velocity = fire_shot([i, k], x_range, y_range)

            if result == 'hit':
                valid_count += 1
                if shot_max_y > max_y:
                    max_y = shot_max_y
                    max_y_velocity = (i, k)
                    max_y_final_velocity = shot_velocity
    # Add valid count for part 2
    return valid_count, max_y, max_y_velocity, max_y_final_velocity

# N Solution
# X velocity is independent and can be calculated separately
# There is probably a better mathy way to do this
# Find X where X + X - 1 + X - 2 ... = Y

def move_probe_x(x_position, x_velocity, x_range):
    new_x_position = x_position + x_velocity
    # print(new_x_position)
    # breakpoint()

    if new_x_position >= x_range[0] and new_x_position <= x_range[1]:
        result = 'hit'
    elif new_x_position > x_range[1] or (new_x_position < x_range[0] and x_velocity == 0):
        result = 'miss'
    else:
        result = 'continue'

    return new_x_position, result

def process_x_only(x_velocity, x_range):
    x_position = 0
    result = 'continue'

    while result == 'continue':
        x_position, result = move_probe_x(x_position, x_velocity, x_range)
        x_velocity -= 1

    return result

def find_peak_better(max, x_range, y_range):
    max_y = 0
    max_y_velocity = None
    max_y_final_velocity = None

    # Calculate i first, assuming an X velocity of 0 at the end
    i = 0
    result = 'continue'
    while result != 'hit':
        i += 1
        # breakpoint()
        result = process_x_only(i, x_range)

    # breakpoint()
    print(f"X Velocity is : {i}")

    for k in range(max):
        # print([i, k])
        result, shot_max_y, shot_velocity = fire_shot([i, k], x_range, y_range)

        if result == 'hit' and shot_max_y > max_y:
            max_y = shot_max_y
            max_y_velocity = (i, k)
            max_y_final_velocity = shot_velocity

    return max_y, max_y_velocity, max_y_final_velocity


print(find_peak(250, x_range, y_range))
# print(find_peak_better(10000, x_range, y_range))

# The max height really should be infinite.
# How would I prove at which height the velocity is guaranteed to always miss?
# Assuming part 2 is whoops, it's 10x bigger, can't n^2 it?
#
