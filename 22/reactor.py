with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

# Further data processing

instructions = []

for line in data:
    first_split = line.split()

    command = first_split[0]

    coords = first_split[1].split(',')

    x = [ int(e) for e in coords[0].split('=')[1].split('..') ]
    y = [ int(e) for e in coords[1].split('=')[1].split('..') ]
    z = [ int(e) for e in coords[2].split('=')[1].split('..') ]

    instructions.append({
        'command': command,
        'x': x,
        'y': y,
        'z': z
    })

# breakpoint()

# Part 1

# I still thing virtual is probably the best

# But maybe nested sets

# For now just run it as is

# on_cubes = set()

# reactor_range = 50

# length = len(instructions)

# for i, instruction in enumerate(instructions):
#     print(f'Starting {i} of {length}')
#     for x in range(instruction['x'][0], instruction['x'][1]+1, 1):
#         if x < -reactor_range or x > reactor_range:
#             continue
#         for y in range(instruction['y'][0], instruction['y'][1]+1, 1):
#             if y < -reactor_range or y > reactor_range:
#                 continue
#             for z in range(instruction['z'][0], instruction['z'][1]+1, 1):
#                 if z < -reactor_range or z > reactor_range:
#                     continue

#                 if instruction['command'] == 'on':
#                     on_cubes.add((x, y, z))
#                 else:
#                     if (x, y, z) in on_cubes:
#                         on_cubes.remove((x, y, z))

# print(len(on_cubes))

# Part 2



# on_cubes = set()

# reactor_range = 50

# length = len(instructions)

# for i, instruction in enumerate(instructions):
#     print(f'Starting {i} of {length}')

#     # breakpoint()

#     for x in range(instruction['x'][0], instruction['x'][1]+1, 1):
#         # if x < -reactor_range or x > reactor_range:
#         #     continue
#         for y in range(instruction['y'][0], instruction['y'][1]+1, 1):
#             # if y < -reactor_range or y > reactor_range:
#             #     continue
#             for z in range(instruction['z'][0], instruction['z'][1]+1, 1):
#                 # if z < -reactor_range or z > reactor_range:
#                 #     continue

#                 if instruction['command'] == 'on':
#                     on_cubes.add((x, y, z))
#                 else:
#                     if (x, y, z) in on_cubes:
#                         on_cubes.remove((x, y, z))

# print("Old:", len(on_cubes))


# Ideas

# Build cube as an object.  Keep track of total lit, subtract overlap.

# But overlap lit is a problem, and it's still one by one

# Grid is still one by one

# I keep thinking of frequency filters, but can't figure out how to do that in 3d
# unbound to the outside

# Maybe do the object approach and do oct-trees for collision, then loop
# for pixel perfect collision?

# Object-based approach should only be n^2
# If this doesn't work, I think I need to learn how to do an octree

class Cube:
    def __init__(self, x, y, z, command):
        self.x = x
        self.y = y
        self.z = z
        self.command = command

        self.volume = ((abs(self.x[1] - self.x[0]) + 1) *
                       (abs(self.y[1] - self.y[0]) + 1) *
                       (abs(self.z[1] - self.z[0]) + 1))

        # breakpoint()

        self.minus_cubes = []

    def compare_cube(self, c_cube):
        if not self.detect_collision(c_cube):
            return

        # Compare and modify the existing cube based on the new cube
        shared_x = (max(self.x[0], c_cube.x[0]), min(self.x[1], c_cube.x[1]))
        shared_y = (max(self.y[0], c_cube.y[0]), min(self.y[1], c_cube.y[1]))
        shared_z = (max(self.z[0], c_cube.z[0]), min(self.z[1], c_cube.z[1]))
        # I missed changing the the last coord in the line above to z after
        # copy/pasting.   Facepalm...


        # Always subtract the new cube from the existing cube
        # if it's a subtraction cube, it will be gone anyway
        # if it's an addition cube, these cubes will be traced in the new one

        # also subtract this cube from the cubes in minus cubes
        new_minus = Cube(shared_x, shared_y, shared_z, 'off')
        # breakpoint()
        for existing_minus in self.minus_cubes:
            # breakpoint()
            new_minus.compare_cube(existing_minus)
        self.minus_cubes.append(new_minus)


    def detect_collision(self, c_cube):
        if not self.detect_overlap(self.x, c_cube.x):
            return False
        if not self.detect_overlap(self.y, c_cube.y):
            return False
        if not self.detect_overlap(self.z, c_cube.z):
            return False

        return True

    def detect_overlap(self, first_pair, second_pair):
        overlap = (max(first_pair[0], second_pair[0]), min(first_pair[1], second_pair[1]))
        return True if overlap[0] <= overlap[1] else False

    def return_volume(self):
        # breakpoint()
        actual_volume = self.volume

        if len(self.minus_cubes) == 0:
            return actual_volume

        else:
            for current in self.minus_cubes:
                # breakpoint()
                # print("Before", actual_volume)
                actual_volume -= current.return_volume()


        # print("After", actual_volume)
        # breakpoint()

        return actual_volume

# temp = Cube(instructions[0]['x'], instructions[0]['y'], instructions[0]['z'])

# print(temp.volume)

processed_cubes = []

for instruction in instructions:
    # breakpoint()
    new_cube = Cube(instruction['x'], instruction['y'], instruction['z'], instruction['command'])

    for cube in processed_cubes:
        cube.compare_cube(new_cube)

    if new_cube.command == "on":
        processed_cubes.append(new_cube)


# breakpoint()

total_volume = 0

for cube in processed_cubes:
    # print("Current Cube", cube.volume, cube.return_volume())

    total_volume += cube.return_volume()
    # print("Running total: ", total_volume)

print("New: ", total_volume)

# breakpoint()
