with open('test_data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

# Further data processing


def find_coord_rotations(coords):
    # I think the order of these matters
    rotations = []
    found = set()

    new_coords = coords
    # rotations.add(new_coords)
    # coords x y z

    # Clockwise -> New x, y = old y, -x
    # -3, 1 becomes 1, 3
    #

    # rotate existing about z clockwise
    new_x = new_coords[0]
    new_y = new_coords[1]
    for _ in range(4):
        old_x = new_x
        old_y = new_y
        new_x = old_y
        new_y = -old_x
        new = (new_x, new_y, coords[2])
        if new not in found:
            rotations.append(new)
            found.add(new)

    # Take each of these and rotate around y clockwise

    for coord in list(rotations):
        new_x = coord[0]
        new_y = coord[1] # Doesn't change here
        new_z = coord[2]
        for _ in range(4):
            old_x = new_x
            old_y = new_y
            old_z = new_z
            new_x = old_z
            new_z = -old_x
            new = (new_x, new_y, new_z)
            if new not in found:
                rotations.append(new)
                found.add(new)

    # Take each of these and rotate y, z around x clockwise
    for coord in list(rotations):
        new_x = coord[0] # Doesn't change here
        new_y = coord[1]
        new_z = coord[2]
        for _ in range(4):
            old_x = new_x
            old_y = new_y
            old_z = new_z
            new_y = old_z
            new_z = -old_y
            new = (new_x, new_y, new_z)
            if new not in found:
                rotations.append(new)
                found.add(new)

    # breakpoint()
    if len(rotations) != 24:
        print("Missing rotations")
        breakpoint()

    # TODO: Avoid Duplications in a better way

    return rotations

scanners = {}
found_scanners = set()
missing_scanners = set()
current_scanner = data[0].strip("- ")
found_scanners.add(current_scanner)

for i in range(1, len(data), 1):
    line = data[i]
    if line == "":
        continue
    elif line[0:2] == "--":
        current_scanner = line.strip("- ")
        # print(current_scanner)
        missing_scanners.add(current_scanner)
    else:
        if current_scanner not in scanners:
            # scanners[current_scanner] = set()
            scanners[current_scanner] = []

        # # Add a tuple for that coord to set
        # scanners[current_scanner].add(tuple([int(e) for e in line.split(',')]))

        # instead add all permutations
        coords = tuple([int(e) for e in line.split(',')])
        permutations = find_coord_rotations(coords)
        # breakpoint()
        scanners[current_scanner].append(permutations)

        # print(f"Added permutations for {coords} to {current_scanner}")



# TODO:
# Pre-calculate all possible coords for all beacons


# Add the beacons in zero to found
found_beacons = set()
for beacon in scanners['scanner 0']:
    # breakpoint()
    found_beacons.add(beacon[0])

# breakpoint()

# Dicts of sets of tuples gives me fast lookup.  Brute force from here?

# Part 1

# This is basically a 3d matrix rotation problem combined with a collision problem
# That makes for horrible time complexity.

# 24 orientations for each scanner
#

# 12 overlapping beacons makes a pair

# Possible approach, start with 1, compare to all others in all orientations
# looking for a pair?  Continue building on that same set?

# I think each coordinate could therefor be in any order with any + or -

# 6 possible arrangements of 3 values

# 7 possible arrangements of + or -


# scanner 0 is at 0, 0, 0 by declaration



# find_coord_rotations((404,-588,-901))

while len(missing_scanners) > 0:
    for scanner_name in missing_scanners:
        print(scanner_name)
        matches = 0
        current_scanner = scanners[scanner_name]
        # current_scanner[0] is the list of all for coord 0 len 24
        # current_scanner[1] is the list of all for coord 1 len 24

        # current_scanner[0][1]
        for i in range(24): # this should always be 24
            for k in range(len(current_scanner)): # how many beacons we have
                # print(f"Scanning down row i: {i}")
                coords = current_scanner[k][i]
                # breakpoint()
                print(f"Coords: {coords}")
                # breakpoint()
                # NOPE, this won't work.  Missing the offset
                # Maybe I do need to do it with numpy and matrices
                # if coords in found_beacons:
                #     print("Found one!")
                #     matches += 1

                # if matches >= 12:
                #     breakpoint()


    breakpoint()
