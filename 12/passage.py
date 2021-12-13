import math
from statistics import median

with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

# Further data processing

# Another graph problem, make adjacency list

graph = {}

for entry in data:
    # breakpoint()
    arr = entry.split("-")
    first = arr[0]
    second = arr[1]

    if first not in graph:
        graph[first] = set()

    if second not in graph:
        graph[second] = set()

    # make a two-way connection
    graph[first].add(second)
    graph[second].add(first)



# breakpoint()

# Part 1

# This is a modified travelling salesman I think.
# Maybe a recursive DFS?
# Or just a DFT
# Don't stop at the end, can add big to visited
# Enstack paths to get paths, save them when finding start

# def find_paths(graph, start, end):
#     qq = []
#     qq.append([start])
#     visited = set()
#     visited.add(start)

#     # May need to make this a set, but I don't think it can find the
#     # same path twice because of visited
#     valid_paths = []

#     # Infinite loop does seem to be a problem, so track paths taken
#     # and don't re-enqueue them
#     explored_paths = set()
#     explored_paths.add(str([start]))

#     # Worried about infinite loops from not adding big caves

#     # Breadth first might be more thorough here, but even more worried
#     # about infinite loops

#     # Visited needs to be by path.  Maybe get rid of visited and
#     # instead use explored paths.
#     while len(qq) > 0:
#         current_path = qq.pop(0)
#         current_node = current_path[-1]

#         if current_node == end:
#             valid_paths.append(current_path)
#             # breakpoint()
#             continue

#         for neighbor in graph[current_node]:
#             # breakpoint()
#             # if neighbor not in visited:
#             #     new_path = list(current_path)
#             #     new_path.append(neighbor)
#             #     if neighbor[0].islower() and neighbor != end:
#             #         visited.add(neighbor)

#             #     qq.append(new_path)
#                 # breakpoint()
#                 # if str(new_path) not in explored_paths:
#                     # ss.append(new_path)
#                     # explored_paths.add(str(new_path))

#             # Brute force, just find all paths, find if they're valid later
#             # No actually, can check if that char is in the path already
#             if neighbor.isupper() or (neighbor.islower() and neighbor not in current_path):
#                 new_path = list(current_path)
#                 new_path.append(neighbor)
#                 # only add if it is a new path
#                 if str(new_path) not in explored_paths:
#                     explored_paths.add(str(new_path))
#                     qq.append(new_path)






#     # breakpoint()
#     return len(valid_paths)

# print(find_paths(graph, "start", "end"))


# Part 2
def can_use_neighbor(current_path, neighbor):

    if neighbor.isupper():
        return True

    if neighbor.islower() and neighbor not in current_path:
        return True
    elif neighbor.islower():
        # If the neighbor is lower and in current path, we can add
        # it if there isn't already two small_caves in there
        small_caves = set()
        for node in current_path:
            if node.islower():
                if node not in small_caves:
                    small_caves.add(node)
                else:
                    return False

    else:
        print("ERROR")
        breakpoint()
        pass

    return True


def find_paths(graph, start, end):
    qq = []
    qq.append([start])

    valid_paths = []

    explored_paths = set()
    explored_paths.add(str([start]))

    while len(qq) > 0:
        current_path = qq.pop(0)
        current_node = current_path[-1]

        if current_node == end:
            valid_paths.append(current_path)
            continue

        for neighbor in graph[current_node]:
            if neighbor == start:
                continue
            # Only add if neighbor is not in the current path
            # Except now we can once


            if can_use_neighbor(current_path, neighbor):
                new_path = list(current_path)
                new_path.append(neighbor)
                # only add if it is a new path
                if str(new_path) not in explored_paths:
                    explored_paths.add(str(new_path))
                    qq.append(new_path)

    # for path in valid_paths:
    #     print(path)

    # breakpoint()
    return len(valid_paths)

print(find_paths(graph, "start", "end"))
