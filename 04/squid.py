with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
# not for this one, use it to find the last board
# data.pop(-1)

# Further data processing

numbers = [int(e) for e in data[0].split(',')]
        #board, row, column
boards = []
board = []
row_counter = 0

for i in range(2, len(data)):
    if row_counter == 5:
        boards.append(board)
        row_counter = 0
        board = []
        continue

    board.append([int(e) for e in data[i].split()])
    row_counter += 1


# breakpoint()

# Part 1

# First one I need to break out step 2

# naive option:  just do the drawings and look for a winner each time

# brute force:  calculate all boards to winning point, look for first to win

# to calculate winner

# simply checking each of the 12 winning states has constant complexity
# o(n) for number of boards, and there aren't a lot

# calculate score of winning board
def score(board, marks, last_number):
    # board = boards[board_number]
    # marks = marked_spots[board_number]

    sum = 0

    for row in range(len(board)):
        for col in range(len(board[0])):
            if marks[row][col] == '.':
                sum += board[row][col]
    # breakpoint()
    return sum * last_number

def check_for_winner(marks):
    # check rows
    for row in marks:
        # breakpoint()
                            #TODO: magic strings
        if ''.join(row) == 'xxxxx':
            return True

    # check columns
    for i in range(len(marks)):
        # breakpoint()
        # arr = [row[i] for row in marks]
        # breakpoint()
        if ''.join([row[i] for row in marks]) == 'xxxxx':
            return True

    # Failed step 1 of polya - diagonals don't count
    # check diagonals
    # left = ""
    # right = ""
    # for i in range(len(marks)):
    #     left += marks[i][i]
    #     right += marks[i][len(marks)-1-i]
    # if left == "xxxxx" or right == "xxxxx":
    #     breakpoint()
    #     return True

    return False

# set up tracking form marked spots
# marked_spots = len(boards) * [5 * [5 * ["."]]]
# stupid is better than fancy #TODO: learn this better

marked_spots = []

for i in range(len(boards)):
    marked_spots.append([])
    for _ in range(len(boards[0][0])):
        marked_spots[i].append(['.', '.', '.', '.', '.'])

# breakpoint()

# test_marks_1 = [
#     ['x', 'x', 'x', 'x', 'x'],
#     ['.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.']
# ]

# test_marks_2 = [
#     ['.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.'],
#     ['x', 'x', 'x', 'x', 'x']
# ]

# test_marks_3 = [
#     ['.', '.', '.', '.', 'x'],
#     ['.', '.', '.', '.', 'x'],
#     ['.', '.', '.', '.', 'x'],
#     ['.', '.', '.', '.', 'x'],
#     ['.', '.', '.', '.', 'x']
# ]

# test_marks_4 = [
#     ['.', '.', '.', '.', 'x'],
#     ['.', '.', '.', 'x', '.'],
#     ['.', '.', 'x', '.', '.'],
#     ['.', 'x', '.', '.', '.'],
#     ['.', '.', '.', '.', 'x']
# ]

# test_marks_5 = [
#     ['.', '.', '.', '.', 'x'],
#     ['.', '.', '.', 'x', '.'],
#     ['.', '.', 'x', '.', '.'],
#     ['.', 'x', '.', '.', '.'],
#     ['x', '.', '.', '.', '.']
# ]

# test_marks_6 = [
#     ['x', '.', '.', '.', '.'],
#     ['.', 'x', '.', '.', '.'],
#     ['.', '.', 'x', '.', '.'],
#     ['.', '.', '.', 'x', '.'],
#     ['.', '.', '.', '.', 'x']
# ]

# print(check_for_winner(test_marks_1))
# print(check_for_winner(test_marks_2))
# print(check_for_winner(test_marks_3))
# print(check_for_winner(test_marks_4))
# print(check_for_winner(test_marks_5))
# print(check_for_winner(test_marks_6))

# Play the boards

winners = set()
# win_order = []

def play(numbers, boards, marked_spots):
    for number in numbers:
        # print(number)
        for i in range(len(boards)):
            if i in winners:
                # print(f'Skipping {i}')
                continue
            # look for and mark the numbers
            for row in range(len(boards[i])):
                for col in range(len(boards[i][row])):
                    if boards[i][row][col] == number:
                        # breakpoint()
                        marked_spots[i][row][col] = 'x'

            # breakpoint()
            if check_for_winner(marked_spots[i]):
                # breakpoint()
                if len(winners) + 1 == len(boards):
                    # last winner found
                    return(score(boards[i], marked_spots[i], number))
                else:
                    # breakpoint()
                    winners.add(i)

print(play(numbers, boards, marked_spots))
