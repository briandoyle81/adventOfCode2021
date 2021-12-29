import json
import heapq
import itertools

with open('test_data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

# Further data processing

den = []

for row in data:
    new_row = []
    den.append(new_row)
    for char in row:
        new_row.append(char)

# breakpoint()


# New Part 1

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

def get_moves_for_single(a_row, a_col, map):

    a_type = map[a_row][a_col]
    if a_type not in move_costs.keys():
        print("ERROR: Bad type")
        breakpoint()
    configs = {}

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

            # Rooms specific checks
            if row in [2, 3]:
                # Skip if invalid room
                if col != allowed_col[a_type]:
                    continue

                # Skip out if wrong in deeper, or deeper is empty
                if row == 2 and spot != a_type:
                    continue

            # if we haven't continued, add this config and cost
            # make a new map first
            new_map = []
            for new_row in map:
                new_map.append(list(new_row))

            new_map[a_row][a_col] = '.' # zero out old spot
            # breakpoint()
            new_map[row][col] = a_type

            cost = abs(a_row - row) + abs(a_col - col)

            configs[json.dumps(new_map)] = cost

            breakpoint()


# Testing
get_moves_for_single(2, 3, den)



def get_configs_and_additional_costs(map):
    configs = {}


    for row, row_data in enumerate(map):
        for col, col_data in enumerate(row_data):
            pass



# def calculate_legal_configurations(map):
#     configurations = set()



# def find_cheapest_progression(start_map, end_map):
#     start_string = json.dumps(start_map)
#     end_string = json.dumps(end_map)

#     # Calculate the cheapest cost to get to every configuration
#     config_costs = {}
#     calculated_configs = set()



#     ss =










# TODO: NOt in global
# From Python docs 8.4

pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heapq.heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heapq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')

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
