with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

# Further data processing

algorithm_line = data.pop(0)

# discard the blank line

data.pop(0)

lit_pixels = set()

for row, row_data in enumerate(data):
    for col, col_data in enumerate(row_data):
        if col_data == '#':
            lit_pixels.add((row, col))


# breakpoint()

# Part 1

def enhance(lit_pixels, algorithm_line, steps):
    inverted = False
    tracked_pixels = lit_pixels
    for _ in range(steps):
        new_tracked_pixels = set()
        neighbor_pixels = set()

        # add unlit pixels neighboring neighbor pixels to set to evaluate
        # this might be a problem for the real algorithm, looks like 0 = lit
        # can solve by flipping it every other time

        for tracked_pixel in tracked_pixels:
            for i in range (-1, 2, 1):
                for k in range(-1, 2, 1):
                    # breakpoint()
                    row_i = tracked_pixel[0] + i
                    col_k = tracked_pixel[1] + k

                    if (row_i, col_k) not in tracked_pixels:
                        neighbor_pixels.add((row_i, col_k))

        tracked_symbol = "." if not inverted else "#"

        # If inverted, we are tracking dark pixels because of algo[0] = On
        for tracked_pixel in tracked_pixels:
            # Find the correct number, regardless of inversion
            number = get_pixel_number(tracked_pixel, tracked_pixels, inverted)

            enhanced_pixel = algorithm_line[number]

            if enhanced_pixel == tracked_symbol:
                new_tracked_pixels.add(tracked_pixel)

        for neighbor_pixel in neighbor_pixels:
            number = get_pixel_number(neighbor_pixel, tracked_pixels, inverted)

            enhanced_pixel = algorithm_line[number]
            if enhanced_pixel == tracked_symbol:
                new_tracked_pixels.add(neighbor_pixel)


        tracked_pixels = new_tracked_pixels
        print(len(tracked_pixels))
        inverted = not inverted

    # print(tracked_pixels)
    return len(tracked_pixels)





def get_pixel_number(pixel, tracked_pixels, inverted):
    neighbors = []
    for i in range (-1, 2, 1):
        for k in range(-1, 2, 1):
            # breakpoint()
            row_i = pixel[0] + i
            col_k = pixel[1] + k

            # TODO: DRY
            if not inverted:
                if (row_i, col_k) in tracked_pixels:
                    neighbors.append('1')
                else:
                    neighbors.append('0')
            else:
                if (row_i, col_k) in tracked_pixels:
                    neighbors.append('0')
                else:
                    neighbors.append('1')
    # breakpoint()
    return int("".join(neighbors), 2)

normal_test = set([(1, 0), (2, 1)])

inverted_test = set([(0, 0),
                     (0, 1),
                     (0, 2),
                     (1, 1),
                     (1, 2),
                     (2, 0),
                     (2, 2)]
)

# print(get_pixel_number((1, 1), normal_test, False))

# print(get_pixel_number((1, 1), inverted_test, True))


# print(get_pixel_number((2, 2), lit_pixels))

print(f"Result: {enhance(lit_pixels, algorithm_line, 50)}")

# incorrect = {(3, -1), (3, 1), (5, 4), (5, 1), (0, 5), (2, 2), (1, 6), (1, 3), (6, 2), (-1, -2), (-1, 4), (-2, 4), (-2, -1), (-2, 1), (4, 2), (4, 5), (3, 3), (3, 6), (5, 3), (0, -2), (2, -1), (2, -2), (1, 2), (2, 4), (-2, 5), (6, 4), (-2, 2), (5, 2), (4, 4), (0, 0), (0, 3), (0, 6), (6, 3), (-1, 5)}

# correct = {(4, 0), (3, -1), (3, 4), (4, 3), (3, 1), (5, 4), (4, 6), (5, 1), (0, 5), (1, 3), (6, 2), (-1, -1), (-1, 4), (4, 2), (4, 5), (3, 3), (0, -2), (2, -2), (2, 4), (1, 2), (0, 4), (1, 5), (6, 4), (3, 2), (-1, 2), (3, 5), (5, 2), (4, 4), (5, 5), (0, 0), (1, -2), (0, 6), (2, 6), (6, 3), (-2, 5)}

# for pair in correct:
#     if pair not in incorrect:
#         print(pair)
