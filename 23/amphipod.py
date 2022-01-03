import json
import heapq
import itertools
from json.encoder import py_encode_basestring

def print_map(map):
    for row in map:
        print("".join(e for e in row))

with open('data.txt', 'r') as file:
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


with open('end.txt', 'r') as file:
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


# New Part 1

# Reuse priority queue

# TODO: NOt in global
# TODO: This is almost certainly a memory leak
# From Python docs 8.4

pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count
heap_size = 0

def add_task(task, priority=0):
    global heap_size
    heap_size += 1
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heapq.heappush(pq, entry)

def remove_task(task):
    global heap_size
    heap_size -= 1
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    global heap_size
    heap_size -= 1
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heapq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')

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

    # Otherwise, it must be room to room, so calculate a U
    # row_distance = abs(start[0] - end[0])
    # col_distance = start[1] - 1
    # col_distance += end[1] - 1

    horizontal_distance = abs(start[1] - end[1])
    vertical_distance = start[0] - 1
    vertical_distance += end[0] - 1
    return (horizontal_distance + vertical_distance) * move_costs[type]

# print(calculate_cost((2, 3), (3, 5), 'B'))
# print(calculate_cost((2, 9), (1, 1), 'B'))
# breakpoint()
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
    if a_row == 3 and a_col == allowed_col[a_type]:
        return {}

    if a_row == 2 and a_col == allowed_col[a_type] and map[3][a_col] == a_type:
        return {}

    moves = get_move_list((a_row, a_col), map, a_type)

    # Inner room (can only be empty if outer is too)
    if (3, allowed_col[a_type]) in moves:
        # print("Moving home - inner")
        new_map = []
        for new_row in map:
            new_map.append(list(new_row))

        new_map[a_row][a_col] = '.' # zero out old spot
        new_map[3][allowed_col[a_type]] = a_type

        # if a_row != 1:
        #     breakpoint()
        cost = calculate_cost((a_row, a_col), (3, allowed_col[a_type]), a_type)
        # if a_row != 1:
        #     breakpoint()

        configs[json.dumps(new_map)] = cost
        return configs

    # TODO: DRY with above
    if (2, allowed_col[a_type]) in moves and map[3][allowed_col[a_type]] == a_type:
        # print("moving home - outer")
        # if we haven't continued, add this config and cost
        # make a new map first
        new_map = []
        for new_row in map:
            new_map.append(list(new_row))

        new_map[a_row][a_col] = '.' # zero out old spot
        # breakpoint()
        new_map[2][allowed_col[a_type]] = a_type

        cost = calculate_cost((a_row, a_col), (2, allowed_col[a_type]), a_type)

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

            if a_row == 3 and row == 2:
                continue

            if a_row == 2 and row == 3:
                continue

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

                # if config not in fully_costed_configs or new_cost < fully_costed_configs[config]:
                #     fully_costed_configs[config] = new_cost
                # if config in fully_costed_configs and new_cost > fully_costed_configs[config]:
                #     continue
                # else:
                #     fully_costed_configs[config] = new_cost


    return fully_costed_configs

def find_cheapest_progression(start_map, end_map):
    start_string = json.dumps(start_map)
    end_string = json.dumps(end_map)
    distances = {}

    # add_task(start_string, 0)
    qq = []
    qq.append(start_string)

    distances[start_string] = 0

    while(len(qq) > 0):

        print(len(qq))
        current = qq.pop(0)

        # if current == end_string:
        #     continue

        current_map = json.loads(current)
        # print_map(current_map)
        # breakpoint()

        # if current == end_string:
        #     print("Found path to end")
            # breakpoint()

        for next_config, cost in get_and_update_all_moves_for_config(current_map, distances[current]).items():
            # if next_config == end_string:
                # print("Evaluating path to end")
            if next_config not in distances or cost < distances[next_config]:
                qq.append(next_config)
                distances[next_config] = cost
                # if next_config == end_string:
                    # print("And it was shorter")

    return distances[end_string]

def eval_keys(keys):
    for key in keys:
        map = json.loads(key)
        count = 0
        if map[2][3] == 'A':
            count += 1
        if map[3][3] == 'A':
            count += 1

        if map[2][5] == 'B':
            count += 1
        if map[3][5] == 'B':
            count += 1

        if map[2][7] == 'C':
            count += 1
        if map[3][7] == 'C':
            count += 1

        if map[2][9] == 'D':
            count += 1
        if map[3][9] == 'D':
            count += 1

        if count == 7:
            print_map(map)




    # Test dijkstra on list from first pass
    # If the result is the same, the error is in finding configs
    # If correct, my assumption that the BFS will find a best path is wrong

    # It didnt' work, which means a new config was found, which means
    # there is still a bug in the initial crawl.


    # new_distances = {}

    # for config in distances.keys():
    #     new_distances[config] = float('inf')
    #     add_task(config, float('inf'))

    # new_distances[start_string] = 0

    # remove_task(start_string)
    # add_task(start_string, 0)

    # visited = set()

    # while len(visited) != len(new_distances):
    #     print(f'heap: {heap_size}')

    #     current = pop_task()
    #     current_map = json.loads(current)
    #     visited.add(current)

    #     for neighbor_config, cost in get_and_update_all_moves_for_config(current_map, new_distances[current]).items():
    #         if neighbor_config == end_string:
    #             breakpoint()
    #         if cost < new_distances[neighbor_config]:
    #             remove_task(neighbor_config)
    #             add_task(neighbor_config, cost)

    #             new_distances[neighbor_config] == cost









print(f'result: {find_cheapest_progression(start, end)}')
# breakpoint()
