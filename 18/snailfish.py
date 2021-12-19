import json

with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

# Further data processing

homework = []
for line in data:
    homework.append(json.loads(line))


# breakpoint()

# Part 1

def find_magnitude(snailfish_number):
    # Always in pairs, base is if ints
    if type(snailfish_number[0]) == int:
        left = snailfish_number[0]

    else:
        left = find_magnitude(snailfish_number[0])

    if type(snailfish_number[1]) == int:
        right = snailfish_number[1]
    else:
        right = find_magnitude(snailfish_number[1])

    return left * 3 + right * 2

def add(first, second):
    new = [first, second]

    return reduce(new)

def test_for_explode(snailfish_number):
    ss = []

    # Not recursive for explode because it applies to only leftmost
    # Because of reduction, there will never be more than 4 deep

    snail_str = str(snailfish_number)

    for char in snail_str:
        if char == '[':
            ss.append(char)

        elif char == ']':
            ss.pop()

        else:
            pass

        if len(ss) == 5:
            return True


    return False

def test_for_split(snailfish_number):
    left = False
    right = False
    if type(snailfish_number[0]) == int:
        if snailfish_number[0] >= 10:
            left = True
    else:
        left = test_for_split(snailfish_number[0])

    if type(snailfish_number[1]) == int:
        if snailfish_number[1] >= 10:
            right = True
    else:
        right = test_for_split(snailfish_number[1])

    return left or right


def reduce(snailfish_number):
    done = False

    while not done:
        print(f"Reducing...")

        # If any pair nested inside four pairs: explode
        if test_for_explode(snailfish_number):
            print(f'Exploding: {snailfish_number}')
            snailfish_number = explode(snailfish_number)
        # else if any regular number is 10 or greater, split
        elif test_for_split(snailfish_number):
            print(f'Splitting: {snailfish_number}')
            # breakpoint()
            snailfish_number, _ = process_split(snailfish_number, False)
        # else done
        else:
            done = True
            print(f'Done: {snailfish_number}')

        # breakpoint()

    return snailfish_number

# def add_to_left(snailfish_number, cursor, left):
#     i = cursor[0]
#     k = cursor[1]
#     m = cursor[2]
#     o = cursor[3]
#     # breakpoint()
#     if o == 1:
#         # left would have popped first
#         # This should probably be in the loops below
#         # print("Added to left of deep pair")
#         snailfish_number[i][k][m][0] += left
#         return snailfish_number

#     # breakpoint()
#     # add to left if present
#     # Iterate backwards from stating point
#     for i_r in range(i, -1, -1):
#         if type(snailfish_number[i_r]) == int:
#                     snailfish_number[i_r] += left
#                     return snailfish_number
#         else:
#             for k_r in range(k, -1, -1):
#                 if type(snailfish_number[i_r][k_r]) == int:
#                         snailfish_number[i_r][k_r] += left
#                         return snailfish_number
#                 else:
#                     for m_r in range(m, -1, -1):
#                         if type(snailfish_number[i_r][k_r][m_r]) == int:
#                             snailfish_number[i_r][k_r][m_r] += left
#                             return snailfish_number

#     return snailfish_number

# def add_to_right(snailfish_number, cursor, right):
#     i = cursor[0]
#     k = cursor[1]
#     m = cursor[2]
#     o = cursor[3]
#     # I think this will skip some.  We should start in the right place
#     if o == 0:
#         if type(snailfish_number[i][k][m][1]) == int:
#             snailfish_number[i][k][m][1] += right
#             return snailfish_number
#         elif type(snailfish_number[i][k][m][1][0]) == int:
#             snailfish_number[i][k][m][1][0] += right
#         else:
#             print("ERROR: Must handle deeper nesting")

#     for i_r in range(i, 2, 1):
#         if type(snailfish_number[i_r]) == int:
#                     snailfish_number[i_r] += right
#                     return snailfish_number
#         else:
#             for k_r in range(k, 2, 1):
#                 if type(snailfish_number[i_r][k_r]) == int:
#                         snailfish_number[i_r][k_r] += right
#                         return snailfish_number
#                 else:
#                     for m_r in range(m, 2, 1):
#                         if type(snailfish_number[i_r][k_r][m_r]) == int:
#                             snailfish_number[i_r][k_r][m_r] += right
#                             return snailfish_number




# def add_left_and_right(snailfish_number, cursor, left, right):
#     # breakpoint()
#     # print(snailfish_number)
#     snailfish_number = add_to_left(snailfish_number, cursor, left)
#     # print("Updated to left")
#     # print(snailfish_number)
#     # breakpoint()
#     snailfish_number = add_to_right(snailfish_number, cursor, right)
#     # print("Updated to right")
#     # print(snailfish_number)
#     # breakpoint()


#     # add to right if present
#     return snailfish_number

def explode(snailfish_number):
    # This could probably be combined with the test since we still need
    # to find what to split
    # But I think I've got a dirty way to get in there
    # This is hideous :D
    # ss = []
    # leftmost_regular_parent = None
    # for i, first in enumerate(snailfish_number):
    #     ss.append(first)
    #     if type(first) is not int:
    #         for k, second in enumerate(first):
    #             ss.append(second)
    #             if type(second) is not int:
    #                 for m, third in enumerate(second):
    #                     ss.append(third)
    #                     if type(third) is not int:
    #                         for o, fourth in enumerate(third):
    #                             # ss.append(fourth) # Don't want this one
    #                             if type(fourth) is not int:
    #                                 left = fourth[0]
    #                                 right = fourth[1]

    #                                 # print(snailfish_number)
    #                                 # breakpoint()
    #                                 snailfish_number[i][k][m][o] = 0
    #                                 cursor_point = [i, k, m, o]


    #                                 # breakpoint()
    #                                 # this is hateful, but just do it here
    #                                 return add_left_and_right(snailfish_number, cursor_point, left, right)

    #                                 # while len(ss) > 0:
    #                                 #     current = ss.pop()
    #                                 #     if type(current) == int:
    #                                 #         current +=
    #     #                 else:
    #     #                     leftmost_regular_parent = second
    #     #         ss.pop()
    #     #     ss.pop()
    #     # ss.pop()



    # return snailfish_number
    # Enough is enough
    # Again, could probably combine this with finding it, but
    # maybe knowing it is here is useful.

    snail_string = str(snailfish_number)
    # print(snail_string)

    left_brackets = 0
    left_cursor = 0
    right_cursor = None
    left_number = None
    right_number = None

    # cont = True

    # Find and remove the explosion point, and get the numbers
    while True:
        current = snail_string[left_cursor]
        if current == "[":
            left_brackets += 1
        elif current == "]":
            left_brackets -= 1
        elif left_brackets == 5:
            # find the left number
            print(f'Pair area:{snail_string[left_cursor:left_cursor+5]}')
            offset = 0
            left_chars = ''
            num_cursor = left_cursor
            while snail_string[num_cursor] != ',':
                left_chars += snail_string[num_cursor]
                num_cursor += 1

            left_number = int(left_chars)
            left_part = snail_string[:left_cursor-1]
            # find the right number and part
            # skip the space
            num_cursor += 1
            right_chars = ''
            while snail_string[num_cursor] != ']':
                right_chars += snail_string[num_cursor]
                num_cursor += 1

            right_number = int(right_chars)
            right_part = snail_string[num_cursor+1:]

            # breakpoint()

            # pair = snail_string[left_cursor: left_cursor+4]
            # # TODO: THIS CAN"T HANDLE 2 digit NUMBERS
            # split_pair = pair.split(', ')
            # left_number = int(split_pair[0])
            # # so handle it
            # # Except it can be up to any digit because we explode before split
            # try:
            #     right_number = int(split_pair[1])
            # except:
            #     pair = snail_string[left_cursor: left_cursor+5]
            #     split_pair = pair.split(', ')
            #     right_number = int(split_pair[1])
            # left_part = snail_string[:left_cursor-1]
            # if len(pair) == 4:
            #     right_part = snail_string[left_cursor+5:]
            # elif len(pair) == 5:
            #     right_part = snail_string[left_cursor+6:]
            # elif len(pair) == 6:
            #     right_part = snail_string[left_cursor+7:]
            # else:
            #     print("Something else went wrong")
            #     breakpoint()

            # breakpoint()
            new_snail_string = left_part + '0' + right_part
            left = 0
            right = 0
            for char in new_snail_string:
                if char == '[':
                    left += 1
                if char == ']':
                    right += 1
            if left != right:
                print('foobar')
                breakpoint()
            # breakpoint()
            # put the cursors on the zero for now
            left_cursor -= 1
            right_cursor = left_cursor

            # print("Change to zero")
            # print(new_snail_string)
            # breakpoint()
            break

        left_cursor += 1

    # left = 0
    # right = 0
    # for char in new_snail_string:
    #     if char == '[':
    #         left += 1
    #     if char == ']':
    #         right += 1
    # if left != right:
    #     print('bar')
    #     breakpoint()
    # This is so horrible
    right_cursor += 1
    while right_cursor < len(new_snail_string):
        if new_snail_string[right_cursor] not in [',', '[', ']', ' ']:
            # print("right number")
            # breakpoint()
            # Handle 2 digit numbers
            char = ''
            offset = 0
            while new_snail_string[right_cursor+offset] not in [',', '[', ']', ' ']:
                char += new_snail_string[right_cursor+offset]
                offset += 1

            new_number = int(char) + right_number
            left_part = new_snail_string[:right_cursor] # confirmed correct
            right_part = new_snail_string[right_cursor+offset:]
            new_snail_string = left_part + str(new_number) + right_part

            break

        right_cursor += 1

    # left = 0
    # right = 0
    # for char in new_snail_string:
    #     if char == '[':
    #         left += 1
    #     if char == ']':
    #         right += 1
    # if left != right:
    #     print('foo')
    #     breakpoint()

    # Update the left side
    # Don't start on the zero
    left_cursor -= 1


    while left_cursor > 0:
        if new_snail_string[left_cursor] not in [',', '[', ']', ' ']:
            # print("left number")
            # breakpoint()
            # Handle multi digit numbers
            char = ""
            offset = -0
            while new_snail_string[left_cursor+offset] not in [',', '[', ']', ' ']:
                char = new_snail_string[left_cursor+offset] + char
                offset -= 1
            new_number = int(char) + left_number
            left_part = new_snail_string[:left_cursor+offset+1] # + offset because negative +1 because exclusive
            right_part = new_snail_string[left_cursor+1:] # this should be right
            # above, we're counting leftward, so the right side will always start
            # at the starting point + 1
            new_snail_string = left_part + str(new_number) + right_part

            break

        left_cursor -= 1

    # print("Add to left if found")
    # print(new_snail_string)
    # breakpoint()


    try:
        new_list = json.loads(new_snail_string)
    except:
        print("Bad string brackets")
        left = 0
        right = 0
        for char in new_snail_string:
            if char == '[':
                left += 1
            if char == ']':
                right += 1
        breakpoint()
    return new_list

def process_split(snailfish_number, have_split_already):
    # This is ineffecient but will make my current solution work
    # TODO: Refactor
    if have_split_already:
        return snailfish_number, have_split_already
    if type(snailfish_number) == int:
        if snailfish_number >= 10:
            have_split_already = True
            return split(snailfish_number), have_split_already
        else:
            return snailfish_number, have_split_already
    else:
        left, have_split_already = process_split(snailfish_number[0], have_split_already)
        right, have_split_already = process_split(snailfish_number[1], have_split_already)


    return [left, right], have_split_already

def split(snailfish_number):
    left = snailfish_number // 2
    remainder = snailfish_number % 2
    if remainder == 0:
        right = left
    else:
        right = left + 1

    return [left, right]

def do_homework(homework):
    total = homework[0]
    for i in range(1, len(homework), 1):
        total = add(total, homework[i])

    print(f"Total: {total}")
    return find_magnitude(total)


# print(find_magnitude([9, 1]))
# print(find_magnitude([[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]))
# print(add([1,2], [[3, 4], 5]))
# print(test_for_split([[[[0,7],4],[15,[0,13]]],[1,1]]))
# print(test_for_explode([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]))
# print(test_for_explode([[[[0,7],4],[[7,8],[0,13]]],[1,1]]))
# print(explode([7,[6,[5,[4,[3,2]]]]]))

# print(explode([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]))

# print(explode([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]))

# print(explode([[[[[9,8],1],2],3],4]))

# print(explode([[[[0,7],4],[7,[[8,4],9]]],[1,1]]))

# add([[[[4,3],4],4],[7,[[8,4],9]]], [1,1])



#   [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
# + [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
# = [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[8, [7, 7]], [[7, 9], [5, 0]]]]
#bad[[[[4, 0], [5, 4]], [[7, 7], [6, 5]]], [[[5, 5], [0, 6]], [[6, 5], [5, 5]]]]


# add([[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]], [7,[[[3,7],[4,3]],[[6,3],[8,8]]]])



print(do_homework(homework))
