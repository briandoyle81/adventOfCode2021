import json
import heapq
import itertools
# from itertools import permutations
from more_itertools import distinct_permutations

with open('test_data.txt', 'r') as file:
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


# OOP is too convoluted.

# I think I need to work with the board as is, like a graph
# Use Djikstra but save costs to get to a configuration, and avoid
# repeated configurations.
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
    row_distance = abs(start[0] - end[0])
    col_distance = start[1] - 1
    col_distance += end[1] - 1
    return (row_distance + col_distance) * move_costs[type]


def get_moves_for_single(a_row, a_col, map):

    a_type = map[a_row][a_col]
    if a_type not in move_costs.keys():
        print("ERROR: Bad type")
        breakpoint()
    configs = {}

    # If it can move to it's home, do so now and skip other options

    # Inner room (can only be empty if outer is too)
    if map[3][allowed_col[a_type]] == '.':
        # if we haven't continued, add this config and cost
        # make a new map first
        new_map = []
        for new_row in map:
            new_map.append(list(new_row))

        new_map[a_row][a_col] = '.' # zero out old spot
        # breakpoint()
        new_map[3][allowed_col[a_type]] = a_type

        cost = calculate_cost((a_row, a_col), (3, allowed_col[a_type]), a_type)

        configs[json.dumps(new_map)] = cost
        return configs

    # TODO: DRY with above
    if map[2][allowed_col[a_type]] == '.' and map[3][allowed_col[a_type]] == a_type:
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
        return configs


    for row, row_data in enumerate(map):
        for col, spot in enumerate(row_data):
            # # Skip if not a hall or room
            # if spot in [' ', "#", 'X']:
            #     continue

            # # Skip of occupied
            # if spot in move_costs.keys():
            #     continue

            # Just skip if not an empty spot

            if spot != '.':
                continue

            # Don't move if in a hallway unless it can move to a room
            if a_row == 1:
                if col != allowed_col[a_type]:
                    continue

            # Rooms specific checks
            # TODO: This may be redundant now
            if row in [2, 3]:
                # Skip if invalid room
                if col != allowed_col[a_type]:
                    continue

                # Skip out if wrong in deeper, or deeper is empty
                if row == 2 and map[3][col] != a_type:
                    continue

            # if we haven't continued, add this config and cost
            # make a new map first
            new_map = []
            for new_row in map:
                new_map.append(list(new_row))

            new_map[a_row][a_col] = '.' # zero out old spot
            # breakpoint()
            new_map[row][col] = a_type

            # cost = (abs(a_row - row) + abs(a_col - col)) * move_costs[a_type]
            cost = calculate_cost((a_row, a_col), (row, col), a_type)

            configs[json.dumps(new_map)] = cost

            # breakpoint()

    return configs


# Testing
# get_moves_for_single(2, 3, den)


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

# test = get_and_update_all_moves_for_config(den, 0)
# breakpoint()


# Operating under the very big assumption that the first encounter of a
# configuration will be the cheapest



# def search_for_cheapest_reconfig(current_string, start_string, end_string):
#     configs = {}

#     visited = set()

#     ss = []






# def permute(arr,start,end, perm_string_set):
#     if start==end:
#         perm_string_set.add(tuple(arr))
#         return
#     for k in range(start,end+1):
#         arr[start],arr[k] = arr[k],arr[start]
#         permute(arr, start+1, end, perm_string_set)
#         arr[start],arr[k] = arr[k],arr[start]



# #TODO: This is pretty ineffecient because it's doing permutations of the .
# # Edit, it produces way too many.  Doing it manually
# # Nope, definitely too many to do at all
# def get_all_possible_configs(map, distances):
#     # possible_config_strings = set()

#     # Actually, just add this right to the global heap

#     # create a string of only the "permuable" parts

#     permuable_string = "......." # Legal hallway spots
#     permuable_string += map[2][3]
#     permuable_string += map[2][5]
#     permuable_string += map[2][7]
#     permuable_string += map[2][9]
#     permuable_string += map[3][3]
#     permuable_string += map[3][5]
#     permuable_string += map[3][7]
#     permuable_string += map[3][9]

#     # perms = set(permutations(permuable_string))

#     # mitigage .s by adding to set

#     # perm_set = set()

#     # for perm in perms:
#     #     perm_set.add(perm)

#     # perm_array = [e for e in permuable_string]

#     # perms = set()

#     # permute(perm_array, 0, len(perm_array)-1, perms)
#     print("Finding perms")
#     perms = set(distinct_permutations(permuable_string))
#     print("Perms found")
#     # breakpoint()
#     i = 0
#     for perm in perms:
#         # if i % 10000 == 0:
#         #     print(i)
#         # i += 1
#         new_map = []
#         perm_array = [e for e in perm]

#         new_map.append([])
#         for _ in range(13):
#             new_map[0].append('#')

#         new_map.append([])
#         new_map[1].append('#')
#         new_map[1].append(perm_array.pop(0))
#         new_map[1].append(perm_array.pop(0))
#         new_map[1].append('X')
#         new_map[1].append(perm_array.pop(0))
#         new_map[1].append('X')
#         new_map[1].append(perm_array.pop(0))
#         new_map[1].append('X')
#         new_map[1].append(perm_array.pop(0))
#         new_map[1].append('X')
#         new_map[1].append(perm_array.pop(0))
#         new_map[1].append(perm_array.pop(0))
#         new_map[1].append('#')
#         new_map.append([])
#         new_map[2].append('#')
#         new_map[2].append('#')
#         new_map[2].append('#')
#         new_map[2].append(perm_array.pop(0))
#         new_map[2].append('#')
#         new_map[2].append(perm_array.pop(0))
#         new_map[2].append('#')
#         new_map[2].append(perm_array.pop(0))
#         new_map[2].append('#')
#         new_map[2].append(perm_array.pop(0))
#         new_map[2].append('#')
#         new_map[2].append('#')
#         new_map[2].append('#')

#         new_map.append([])

#         new_map[3].append(' ')
#         new_map[3].append(' ')
#         new_map[3].append('#')
#         new_map[3].append(perm_array.pop(0))
#         new_map[3].append('#')
#         new_map[3].append(perm_array.pop(0))
#         new_map[3].append('#')
#         new_map[3].append(perm_array.pop(0))
#         new_map[3].append('#')
#         new_map[3].append(perm_array.pop(0))
#         new_map[3].append('#')

#         new_map.append([])

#         new_map[4].append(' ')
#         new_map[4].append(' ')

#         for _ in range(9):
#             new_map[4].append('#')


#         # breakpoint()

#         # possible_config_strings.add(json.dumps(new_map))
#         # instead add to heapn
#         map_string = json.dumps(new_map)

#         distances[map_string] = float('inf')
#         add_task(map_string, float('inf'))

#     # return possible_config_strings


# temp = get_all_possible_configs(start)
# breakpoint()

# def crawl_all_legal_configs(start):


def find_cheapest_progression(start_map, end_map):
    start_string = json.dumps(start_map)
    # breakpoint()
    end_string = json.dumps(end_map)

    # Calculate the cheapest cost to get to every configuration
    distances = {}
    visited = set()

    # get_all_possible_configs(start, distances)
    # print("Done setting up configs")

    add_task(start_string, 0)

    distances[start_string] = 0


    # breakpoint()
    # while(len(visited) != len(distances)):
    # TODO: Base this off heap size
    # counter = 1
    while(heap_size > 0):
        # print(f'{len(visited)} of {len(distances)}')
        print(heap_size)
        try:
            current = pop_task()
        except:
            print("Heap is empty")
            breakpoint()
        # counter -= 1

        current_map = json.loads(current)

        # visited.add(current)

        for next_config, cost in get_and_update_all_moves_for_config(current_map, distances[current]).items():
            if next_config not in distances or cost < distances[next_config]:
                add_task(next_config, cost)
                # counter += 1
                distances[next_config] = cost

            # if cost < distances[next_config]:
            #     remove_task(next_config)
            #     add_task(next_config, cost)
            #     distances[next_config] = cost

    # breakpoint()
    return distances[end_string]


print(f'result: {find_cheapest_progression(start, end)}')
breakpoint()








# Aborted first attempt for part 1 below:

# Going for an OOP graph approach to this

# class Amphipod:
#     costs = {
#         'A': 1,
#         'B': 10,
#         'C': 100,
#         'D': 1000
#     }

#     def __init__(self, type, room, rooms):
#         self.type = type
#         self.room = room
#         self.rooms = rooms
#         self.home = self.check_if_home()


#     def check_if_home(self):
#         if self.type + "_inner" == self.room.name:
#             return True

#         if (self.type + "_outer" == self.room.name and
#             self.rooms[self.type + "_inner"].occupant.type == self.type):
#             return True

#         return False

# class Room:
#     def __init__(self, name, occupant):
#         self.name = name
#         self.occupant = occupant

#         self.neighbors = set()


#     def add_neighbor(self, neighbor):
#         # Add two ways
#         self.neighbors.add(neighbor)
#         neighbor.neighbors.add(self)


# rooms = {}
# amphipods = {}

# # Create the rooms

# rooms['A_inner'] = Room("A_inner", None)
# rooms['A_outer'] = Room("A_outer", None)
# rooms['A_hall'] = Room("A_hall", None)
# rooms['B_inner'] = Room("B_inner", None)
# rooms['B_outer'] = Room("B_outer", None)
# rooms['B_hall'] = Room("B_hall", None)
# rooms['C_inner'] = Room("C_inner", None)
# rooms['C_outer'] = Room("C_outer", None)
# rooms['C_hall'] = Room("C_hall", None)
# rooms['D_inner'] = Room("D_inner", None)
# rooms['D_outer'] = Room("D_outer", None)
# rooms['D_hall'] = Room("D_hall", None)
# rooms['left_outer'] = Room("left_outer", None)
# rooms['left_inner'] = Room("left_inner", None)
# rooms['right_outer'] = Room("right_outer", None)
# rooms['right_inner'] = Room("right_inner", None)
# rooms['a_b_hall'] = Room("a_b_hall", None)
# rooms['b_c_hall'] = Room("b_c_hall", None)
# rooms['c_d_hall'] = Room("c_d_hall", None)

# # Connect the rooms

# rooms['A_inner'].add_neighbor(rooms['A_outer'])
# rooms['A_outer'].add_neighbor(rooms['A_hall'])
# rooms['A_hall'].add_neighbor(rooms['left_outer'])
# rooms['left_outer'].add_neighbor(rooms['left_inner'])
# rooms['A_hall'].add_neighbor(rooms['a_b_hall'])

# rooms['B_inner'].add_neighbor(rooms['B_outer'])
# rooms['B_outer'].add_neighbor(rooms['B_hall'])
# rooms['B_hall'].add_neighbor(rooms['a_b_hall'])
# rooms['B_hall'].add_neighbor(rooms['b_c_hall'])

# rooms['C_inner'].add_neighbor(rooms['C_outer'])
# rooms['C_outer'].add_neighbor(rooms['C_hall'])
# rooms['C_hall'].add_neighbor(rooms['b_c_hall'])
# rooms['C_hall'].add_neighbor(rooms['c_d_hall'])

# rooms['D_inner'].add_neighbor(rooms['D_outer'])
# rooms['D_outer'].add_neighbor(rooms['D_hall'])
# rooms['D_hall'].add_neighbor(rooms['right_outer'])
# rooms['right_outer'].add_neighbor(rooms['right_inner'])
# rooms['D_hall'].add_neighbor(rooms['c_d_hall'])

# # breakpoint()


# # Add the occupants
# amphipods['A1'] = Amphipod('A')
# amphipods['A2'] = Amphipod('A')

# amphipods['B1'] = Amphipod('B')
# amphipods['B2'] = Amphipod('B')

# amphipods['C1'] = Amphipod('C')
# amphipods['C2'] = Amphipod('C')

# amphipods['D1'] = Amphipod('D')
# amphipods['D2'] = Amphipod('D')

# # Place the occupants

# rooms['A_inner']

# # Move the occupants
