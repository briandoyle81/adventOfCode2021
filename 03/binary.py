with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)


# Part 1

# zeroes = [0] * len(data[1])
# ones = [0] * len(data[1])

# for entry in data:
#     for i in range(len(zeroes)):
#         if entry[i] == "0":
#             zeroes[i] += 1
#         if entry[i] == "1":
#             ones[i] += 1

# gamma = [None] * len(data[1])
# epsilon = [None] * len(data[1])

# for i in range(len(zeroes)):
#     if zeroes[i] > ones[i]:
#         gamma[i] = 0
#         epsilon[i] = 1
#     elif ones[i] > zeroes[i]:
#         gamma[i] = 1
#         epsilon[i] = 0
#     else:
#         print("ERROR: EQUAL VALUES")



# # This is probably roundabout
# gamma_int = int("".join(str(e) for e in gamma), 2)
# epsilon_int = int("".join(str(e) for e in epsilon), 2)

# print(gamma_int * epsilon_int)

# Part 2

def find_gamma_epsilon_at_index(data, i):
    zeroes = 0
    ones = 0

    for entry in data:
        if entry[i] == "0":
            zeroes += 1
        if entry[i] == "1":
            ones += 1

    if zeroes > ones:
        return 0
    if zeroes < ones:
        return 1
    if zeroes == ones:
        return "even" # blegh


def reduce_by_position(pos, data, comp, match):
    # breakpoint()
    result = []
    for entry in data:
        # breakpoint()
        if comp == "even":
            #TODO handle co2
            # breakpoint()
            if int(entry[pos]) == match:
                result.append(entry)
        elif int(entry[pos]) == comp:
            result.append(entry)

    # breakpoint()
    return result

def reduce_lists(data):
    oxygen = None
    co2 = None
    # find oxygen
    # breakpoint()
    reduced = data
    for i in range(len(data[0])):
        more = find_gamma_epsilon_at_index(reduced, i)
        reduced = reduce_by_position(i, reduced, more, 1)
        if len(reduced) == 1:
            oxygen = reduced[0]
            break

    # find co2
    reduced = data
    for i in range(len(data[0])):
        more = find_gamma_epsilon_at_index(reduced, i)
        # invert to work with the same logic
        if more == 1:
            less = 0
        if more == 0:
            less = 1
        if more == "even":
            # breakpoint()
            less = "even"
        reduced = reduce_by_position(i, reduced, less, 0)
        # breakpoint()
        if len(reduced) == 1:
            co2 = reduced[0]
            break


    # breakpoint()
    return oxygen, co2

# this can probably be done together by wrapping the above, but first pass here
# maybe I will.
# find oxygen and co2

oxygen, co2 = reduce_lists(data)
# breakpoint()
# breakpoint()

oxygen_rating = int("".join(str(e) for e in oxygen), 2)
co2_rating = int("".join(str(e) for e in co2), 2)

print(oxygen_rating * co2_rating)
