import math

with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

# Further data processing

# Make the map ints

map = []
for row, row_data in enumerate(data):
    map.append([])
    for col, value in enumerate(row_data):
        map[row].append(int(value))

# breakpoint()

# Part 1

# Now we definitely have a graph!  Find neighbor for first part

def get_neighbors(row, col, map):
    neighbors = []
    for i in range(-1, 2, 1):
        for k in range(-1, 2, 1):
            # skip self
            if i == 0 and k == 0:
                continue

            # skip diagonals (probably for now?)
            if i != 0 and k != 0:
                continue

            row_i = row + i
            col_k = col + k
            # skip off map
            if row_i < 0 or col_k < 0 or row_i >= len(map) or col_k >= len(map[0]):
                continue

            neighbors.append(map[row_i][col_k])

    return neighbors

def find_low_points(map):
    low_points = []
    for row, row_data in enumerate(data):
        for col, col_data in enumerate(row_data):
            # breakpoint()
            if min(get_neighbors(row, col, map)) > map[row][col]:
                low_points.append(map[row][col])
    # breakpoint()
    return low_points

def find_risk(low_points):
    return sum([e + 1 for e in low_points])

print(find_risk(find_low_points(map)))

# Part 2

# Yup, bfs time

# Modify neighbors because we need their coords and only want taller

def get_neighbor_coords(row, col, map):
    neighbors = []
    for i in range(-1, 2, 1):
        for k in range(-1, 2, 1):
            # skip self
            if i == 0 and k == 0:
                continue

            # skip diagonals (probably for now?)
            if i != 0 and k != 0:
                continue

            row_i = row + i
            col_k = col + k
            # skip off map
            if row_i < 0 or col_k < 0 or row_i >= len(map) or col_k >= len(map[0]):
                continue

            # only add
            neighbors.append((row_i, col_k))

    return neighbors

# modify get low points to get coords
def find_low_point_coords(map):
    low_point_coords = []
    for row, row_data in enumerate(data):
        for col, col_data in enumerate(row_data):
            # breakpoint()
            # TODO: Cleanup and use revised get neighbors
            if min(get_neighbors(row, col, map)) > map[row][col]:
                low_point_coords.append((row, col))

    return low_point_coords

# Use BFS to find basins
# External visited so we don't refind basin
# Edit much easier, we have the low points, just bfs and stop at 9s

def traverse_basin_and_return_size(row, col, map):
    visited = set()
    visited.add(str((row, col)))
    qq = []
    qq.append((row, col))

    basin_size = 0

    while len(qq) > 0:
        # breakpoint()
        current = qq.pop()
        row = current[0]
        col = current[1]

        basin_size += 1

        for neighbor in get_neighbor_coords(row, col, map):
            coord_string = str((neighbor[0], neighbor[1]))

            # Don't add visited or 9's
            height = map[neighbor[0]][neighbor[1]]
            if coord_string not in visited and height != 9:
                visited.add(coord_string)
                qq.append(neighbor)

    # breakpoint()
    return basin_size

def find_basin_sizes(map):
    # visited = set()
    # Edited:  Don't need visited here if we start from low points.  No overlap
    basin_sizes = []

    lowpoints = find_low_point_coords(map)
    # breakpoint()
    for lowpoint in lowpoints:
        row = lowpoint[0]
        col = lowpoint[1]
        basin_size = traverse_basin_and_return_size(row, col, map)
        basin_sizes.append(basin_size)

    return basin_sizes

def sum_three_largest(basin_sizes):
    sorted_basins = sorted(basin_sizes)
    # print(basin_sizes)
    return math.prod(sorted_basins[-3:])

# basin_sizes = sorted(find_basin_sizes(map))

print(sum_three_largest(find_basin_sizes(map)))
