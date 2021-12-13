import math
from statistics import median

with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

# Further data processing

octopuses = []
octopuses.append([])
octopuses.append([])

for line in data:
    new_front = []
    new_back = []
    octopuses[0].append(new_front)
    octopuses[1].append(new_back)
    for char in line:
        new_front.append(int(char))
        new_back.append(None)



# breakpoint()

# Part 1

# Borrow get neighbor coords from day 09

def get_neighbor_coords(row, col, map):
    neighbors = []
    for i in range(-1, 2, 1):
        for k in range(-1, 2, 1):
            # skip self
            if i == 0 and k == 0:
                continue

            # # skip diagonals (probably for now?)
            # if i != 0 and k != 0:
            #     continue

            row_i = row + i
            col_k = col + k
            # skip off map
            if row_i < 0 or col_k < 0 or row_i >= len(map) or col_k >= len(map[0]):
                continue

            # only add
            neighbors.append((row_i, col_k))

    return neighbors


def count_flashes(octopuses):
    front = 0
    back = 1

    flashes = 0

    step = 0


    # for step in range(100):
    while(True):
        step += 1
        # print(f"Start of loop {_}, front is:")
        # for row in octopuses[front]:
        #     print(row)

        # # for row in octopuses[back]:
        # #     print(row)

        # breakpoint()

        # coords flashed
        flashed = []
        # Step 1: Increase energy of all by 1 and save in back buffer

        for row, row_val in enumerate(octopuses[front]):
            for col, col_val in enumerate(row_val):
                octopuses[back][row][col] = octopuses[front][row][col] + 1

        # print("After First Part, back is: ")
        # for row in octopuses[back]:
        #     print(row)

        # # for row in octopuses[back]:
        # #     print(row)

        # breakpoint()
        # Step 2: Use buffers back and forth to process secondaries

        # Swap the buffers and continue writing to the back
        temp = front
        front = back
        back = temp

        process_secondaries = True
        while(process_secondaries):

            process_secondaries = False

            # Start the back in the same state as the front
            # NOTE: this seems very ineffecient

            for row, row_val in enumerate(octopuses[front]):
                for col, col_value in enumerate(row_val):
                    octopuses[back][row][col] = octopuses[front][row][col]

            for row, row_val in enumerate(octopuses[front]):
                for col, col_val in enumerate(row_val):
                    # Write to the back no matter what
                    # print(f'Processing {row}, {col}')

                    if octopuses[front][row][col] is None:
                        continue
                    if octopuses[front][row][col] > 9:
                        # breakpoint()
                        process_secondaries = True
                        flashes += 1
                        flashed.append((row, col))
                        octopuses[back][row][col] = None
                        neighbors = get_neighbor_coords(row, col, octopuses[front])
                        # breakpoint()
                        for neighbor in neighbors:

                            # Look at back and write to back here, no need to
                            # write ones that have already flashed
                            if octopuses[back][neighbor[0]][neighbor[1]] != None:
                                octopuses[back][neighbor[0]][neighbor[1]] += 1

            # Swap the buffer again if we still need to process secondaries
            if process_secondaries:
                temp = front
                front = back
                back = temp

        # print("Processed Secondaries, back is: ")
        # for row in octopuses[back]:
        #     print(row)

        # breakpoint()


        # TODO: Track which to use for step 3?
        # Step 3
        # Look at the back and change zeros to ones
        for row, row_val in enumerate(octopuses[back]):
            for col, col_val in enumerate(row_val):
                if octopuses[back][row][col] == None:
                    octopuses[back][row][col] = 0

        # One final swap to bring the current to the front

        temp = front
        front = back
        back = temp

        # for row in octopuses[front]:
        #     print(row)

        # breakpoint()

        if len(flashed) == 100:
            print (f"Synchronized at {step}")
            break

    # for row in octopuses[front]:
    #     print(row)

    # return flashes

# print(count_flashes(octopuses))

count_flashes(octopuses)
