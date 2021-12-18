from os import read

with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

# Further data processing



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


# print(find_magnitude([9, 1]))
print(find_magnitude([[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]))
