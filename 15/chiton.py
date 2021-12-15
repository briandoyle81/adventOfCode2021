import heapq
import itertools


with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

# Further data processing

# Data for part 1
# map = []
# for row, row_data in enumerate(data):
#     map.append([])
#     for col, value in enumerate(row_data):
#         map[row].append(int(value))

# Data for part 2
map = []

for row in range(len(data) * 5):
    map.append([])
    for col in range(len(data[0]) * 5):
        new_value = int(data[row % len(data)][col % len(data[0])])
        new_value += row // len(data) + col // len(data[0])
        if new_value > 9:
            new_value -= 9
        # breakpoint()
        map[row].append(new_value)


# breakpoint()

# Part 1

# Djikstra for part 1

# Borrow get neighbor again

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

# class Node:
#     def __init__(self, coords, distance):
#         self.coords = coords
#         self.distance = distance

def find_smallest_unvisited(visited, distances, priority):
    # # TODO: Heap would be faster
    # smallest_distance = float('inf')
    # smallest_node = None
    # for node in distances:
    #     if node not in visited and distances[node] < smallest_distance:
    #         smallest_distance = distances[node]
    #         smallest_node = node

    # if smallest_node is None:
    #     breakpoint()
    # if len(priority) == 1:
    #     breakpoint()
    # top = heapq.heappop(priority)
    # coord = top[1]
    # while coord in visited:
    #     top = heapq.heappop(priority)
    #     coord = top[1]

    # print(coord)
    # if coord == (49, 49):
    #     breakpoint()
    coord = pop_task()
    # breakpoint()
    return coord

def djikstra(start, end, map):
    # Trying to do from memory first
    # Weighted BFS, just track cost with path IIRC
    # No it's more complicated, looking it up
    # I think djikstra is brute force, final dataset may be too big
    # might need a*
    # might want a heap for distances found???

    distances = {}
    # priority = [] # (priority, key)

    visited = set()

    # qq = set()

    for row, row_data in enumerate(map):
        for col, col_data in enumerate(row_data):
            distances[(row,col)] = float('inf')
            add_task((row, col), float('inf'))
            # heapq.heappush(pq, (float('inf'), (row,col)))
            # qq.add(str((row, col)))
            # breakpoint()

    # breakpoint()
    distances[start] = 0
    # heapq.heapreplace(priority, (0, start))
    remove_task(start)
    add_task(start, 0)
    # breakpoint()


    # qq.append(start)
    last = None

    # TODO: WHy are some getting skipped now???
    # Because I'm not correctly updating the heap
    while len(visited) != len(distances):
        print(len(visited))
        # breakpoint()
        # this isn't a queue
        # don't pop the next item
        # pop the one with the smallest distance
        # that's why I thought I needed a heap
        # current = qq.pop(0)

        current = find_smallest_unvisited(visited, distances, pq)
        # breakpoint()

        # add all above and left to visited
        # can refine later, for now, just add all in one row/col back
        # if current[0] is not 0:
        #     # add all columns in row above
        #     for i in range(len(map[0])):
        #         visited.add((current[0]-1, i))

        # if current[1] is not 0:
        #     # add all rows in col left
        #     for i in range(len(map)):
        #         visited.add((i, current[1]-1))

        # if end in visited:
        #     breakpoint()
        # # breakpoint()
        # if current == (end):
        #     breakpoint()
        #     return distances[current]


        visited.add(current)
        # breakpoint()
        for neighbor_coords in get_neighbor_coords(current[0], current[1], map):
            # breakpoint()
            weight = map[neighbor_coords[0]][neighbor_coords[1]]
            new_total = weight + distances[current]
            if new_total < distances[neighbor_coords]:
                # breakpoint()
                # This does NOT replace the one listed
                # heapq.heapreplace(priority, (distances[neighbor_coords], neighbor_coords))

                # Using implementation in python docs
                remove_task(neighbor_coords)
                add_task(neighbor_coords, new_total)
                # breakpoint()
                distances[neighbor_coords] = new_total


    return distances[end]




# Part 2

# And of course it's vastly bigger and a time complexity problem again
# could try a* and hope to get lucky
# but there is probably an exact solution

# Linear time with Djikstra is doable, but long.  On a hunch, if it's always down or right
# easy enough to hack a* like rule into get neighbors

# But that's not significantly faster.  Need to cull all no longer possible probably

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

print(djikstra((0,0), (len(map)-1, len(map[0])-1), map))
