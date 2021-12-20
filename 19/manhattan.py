# Working here because I didn't put Part 1 in a function
# scanner 0 (0, 0, 0)
# scanner 1 (-68, 1246, 43)
# scanner 4 (20, 1133, -1061)
# scanner 2 (-1105, 1205, -1229)
# scanner 3 (92, 2380, 20)

# breakpoint()

scanners = set([(0, 0, 0), (-68, 1246, 43), (20, 1133, -1061), (92, 2380, 20)])

def find_manhattan(first, second):
    return sum([abs(first[0] - second[0]), abs(first[1] - second[1]), abs(first[2] - second[2])])


print(find_manhattan((-1105, 1205, -1229), (92, 2380, 20) ))
