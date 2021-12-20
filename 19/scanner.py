with open('data.txt', 'r') as file:
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
            # scanners[current_scanner] = []
            scanners[current_scanner] = {}
            for i in range(24):
                scanners[current_scanner][i] = set()

        # # Add a tuple for that coord to set
        # scanners[current_scanner].add(tuple([int(e) for e in line.split(',')]))

        # instead add all permutations
        coords = tuple([int(e) for e in line.split(',')])
        permutations = find_coord_rotations(coords)
        # breakpoint()
        # scanners[current_scanner].append(permutations)

        # Instead, create sets of permutation groups
        for i in range(24):
            scanners[current_scanner][i].add(permutations[i])

        # print(f"Added permutations for {coords} to {current_scanner}")



# TODO:
# Pre-calculate all possible coords for all beacons


# Add the beacons in zero to found
# found_beacons = set()
# for beacon in scanners['scanner 0']:
#     breakpoint()
#     found_beacons.add(beacon[0])

# With the new system, because of how rotation is done, [3] has the original data
found_beacons = set()
for coords in scanners['scanner 0'][3]:
    found_beacons.add(coords)

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
    print(len(missing_scanners))
    for scanner_name in missing_scanners:
        # print(scanner_name)
        matches = 0
        current_scanner = scanners[scanner_name]
        # current_scanner[0] is the list of all for coord 0 len 24
        # current_scanner[1] is the list of all for coord 1 len 24

        # # current_scanner[0][1]
        # for i in range(24): # this should always be 24
        #     for k in range(len(current_scanner)): # how many beacons we have
        #         # print(f"Scanning down row i: {i}")
        #         coords = current_scanner[k][i]
        #         # breakpoint()
        #         print(f"Coords: {coords}")
        #         # breakpoint()
        #         # NOPE, this won't work.  Missing the offset
        #         # Maybe I do need to do it with numpy and matrices
        #         # if coords in found_beacons:
        #         #     print("Found one!")
        #         #     matches += 1

        #         # if matches >= 12:
        #         #     breakpoint()

        # Now that scanners have sets for each permutation
        for key, beacon_coords in current_scanner.items():
            # breakpoint()
            # Here, go through each found_beacon, and assume each beacon
            # is each found one, and look for other matches.
            # beacon_coords is a list of matching orientation beacon coords
            matches = 0
            for found_beacon in found_beacons:
                # Don't add to matches yet, because otherwise we'll get
                # double-entry in the next step
                # Holy time-complexity, Batman!  But at least O(1) lookups
                matches = 0
                for beacon_coord in beacon_coords:
                    # assume each beacon is the found_beacon
                    # # then test the rest
                    matches = 0
                    # print("Resetting matches and trying again")
                    offset = (beacon_coord[0] - found_beacon[0],
                              beacon_coord[1] - found_beacon[1],
                              beacon_coord[2] - found_beacon[2])

                    for test_coord in beacon_coords:
                        # we should always have at least 1 match here
                        # the original being testes
                        offset_coord = (test_coord[0] - offset[0],
                                        test_coord[1] - offset[1],
                                        test_coord[2] - offset[2])

                        if offset_coord in found_beacons:
                            matches += 1
                            # print(matches)

                        if matches == 12:
                            # print("Found 12!!!")
                            # breakpoint()
                            # add all the offset testcoords to found
                            for match_coord in beacon_coords:
                                new_coord = (match_coord[0] - offset[0],
                                             match_coord[1] - offset[1],
                                             match_coord[2] - offset[2])

                                found_beacons.add(new_coord)

                            # remove this scanner from missing and add to found
                            found_scanners.add(scanner_name)
                            missing_scanners.remove(scanner_name)
                            # breakpoint()
                            break

                    if matches == 12:
                        # print("Breaking out of: for beacon_coord in beacon_coords:")
                        break

                if matches == 12:
                    # print("Breaking out of for found_beacon in found_beacons:")
                    break

            if matches == 12:
                # print("Breaking out of: for key, beacon_coords in current_scanner.items():")
                break

        if matches == 12:
            # print("Breaking out of: for scanner_name in missing_scanners:")
            break





print(len(found_beacons))
