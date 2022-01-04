import json
import heapq
import itertools
from json.encoder import py_encode_basestring

def print_map(map):
    for row in map:
        print("".join(e for e in row))

with open('pt2_data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

# Further data processing

start = []

for row in data:
    new_row = []
    start.append(new_row)
    for char in row:
        new_row.append(char)


with open('pt2_end.txt', 'r') as file:
    end_data = file.read().split('\n')

start_string = json.dumps(start)


# cut trailing newline
end_data.pop(-1)

# Further data processing

end = []

for row in end_data:
    new_row = []
    end.append(new_row)
    for char in row:
        new_row.append(char)

end_string = json.dumps(end)

move_costs = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}

allowed_col = {
    'A': 3,
    'B': 5,
    'C': 7,
    'D': 9,
}

def calculate_cost(start, end, type):
    # Simple L if starting in the hall
    # or ending in the hall
    if start[0] == 1 or end[0] == 1:
        return (abs(start[0] - end[0]) + abs(start[1] - end[1])) * move_costs[type]

    horizontal_distance = abs(start[1] - end[1])
    vertical_distance = start[0] - 1
    vertical_distance += end[0] - 1
    return (horizontal_distance + vertical_distance) * move_costs[type]

# Borrow get neighbor yet again
def get_neighbor_coords(row, col, map, a_type):
    # breakpoint()
    neighbors = []
    for i in range(-1, 2, 1):
        for k in range(-1, 2, 1):
            # skip self
            if i == 0 and k == 0:
                continue

            # skip diagonals
            if i != 0 and k != 0:
                continue

            row_i = row + i
            col_k = col + k
            # skip off map
            if row_i < 0 or col_k < 0 or row_i >= len(map) or col_k >= len(map[0]):
                continue

            # skip if not move-to-able
            if map[row_i][col_k] != '.':
                continue

            # only add
            neighbors.append((row_i, col_k))

    return neighbors

def get_move_list(start, map, a_type):
    visited = set()
    qq = []

    qq.append(start)
    visited.add(start)

    while len(qq) > 0:
        current = qq.pop(0)

        for neighbor in get_neighbor_coords(current[0], current[1], map, a_type):
            if neighbor not in visited:
                visited.add(neighbor)
                qq.append(neighbor)

    # Remove the start from visited, we don't need it
    visited.remove(start)

    # breakpoint()

    return visited


def get_moves_for_single(a_row, a_col, map):

    a_type = map[a_row][a_col]
    if a_type not in move_costs.keys():
        print("ERROR: Bad type")
        breakpoint()
    configs = {}

    # No need to move if already home
    # ASSUMPTION: They will stack in from the bottom
    if a_row in range(2, 6) and a_col == allowed_col[a_type]:
        home = True
        for i in range(2, 6):
            if map[i][allowed_col[a_type]] not in ['.', a_type]:
                home = False
        if home:
            return {}


    moves = get_move_list((a_row, a_col), map, a_type)

    # Inner room (can only be empty if outer is too)
    # Loop backwards to attempt to fill from the bottom
    for move_row in range(5, 1, -1):
        row = move_row
        col = allowed_col[a_type]

        # can't move to a room if that room isn't full of correct type
        if map[row][col] not in [a_type, '.']:
            break

        if (row, col) in moves:
            new_map = []
            for new_row in map:
                new_map.append(list(new_row))

            new_map[a_row][a_col] = '.' # zero out old spot

            new_map[move_row][allowed_col[a_type]] = a_type

            cost = calculate_cost((a_row, a_col), (move_row, allowed_col[a_type]), a_type)

            configs[json.dumps(new_map)] = cost
            # breakpoint()
            return configs

    # Can't move from a hallway to hallway
    if a_row != 1:
        for move in moves:
            # Because rooms are handled above, only handle the hallway here
            row = move[0]
            col = move[1]

            # Don't move to the forbidden hallway spots
            if col in allowed_col.values():
                continue

            # if a_row in range(2, 6) and row in range(2, 6):
            #     continue

            new_map = []
            for new_row in map:
                new_map.append(list(new_row))

            new_map[a_row][a_col] = '.' # zero out old spot

            new_map[row][col] = a_type

            cost = calculate_cost((a_row, a_col), (row, col), a_type)

            configs[json.dumps(new_map)] = cost


    return configs

def get_and_update_all_moves_for_config(map, cost_for_config):
    fully_costed_configs = {}

    for row, row_data in enumerate(map):
        for col, spot in enumerate(row_data):
            # Skip if not an amphipod
            if spot not in move_costs.keys():
                continue

            new_configs = get_moves_for_single(row, col, map)

            for config, cost in new_configs.items():
                new_cost = cost + cost_for_config

                fully_costed_configs[config] = new_cost

    return fully_costed_configs

def find_cheapest_progression(start_map, end_map):
    start_string = json.dumps(start_map)
    end_string = json.dumps(end_map)
    distances = {}

    qq = []
    qq.append(start_string)

    distances[start_string] = 0

    while(len(qq) > 0):

        print(len(qq))
        current = qq.pop(0)

        current_map = json.loads(current)

        for next_config, cost in get_and_update_all_moves_for_config(current_map, distances[current]).items():
            if next_config not in distances or cost < distances[next_config]:
                qq.append(next_config)
                distances[next_config] = cost


    # breakpoint()
    return distances[end_string]


print(f'result: {find_cheapest_progression(start, end)}')
