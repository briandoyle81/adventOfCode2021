with open('test_data.txt', 'r') as file:
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
def score(board_number, last_number):
    board = boards[board_number]
    marks = marked_spots[board_number]

    sum = 0

    for row in range(len(board)):
        for col in range(len(board[0])):
            if marks[row][col] == 'x':
                sum += board[row][col]

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

    # check diagonals
    left = ""
    right = ""
    for i in range(len(marks)):
        left += marks[i][i]
        right += marks[i][len(marks)-1-i]
    if left == "xxxxx" or right == "xxxxx":
        return True

    return False

# set up tracking form marked spots
marked_spots = len(boards) * [5 * [5 * ["."]]]


test_marks_1 = [
    ['x', 'x', 'x', 'x', 'x'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.']
]

test_marks_2 = [
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['x', 'x', 'x', 'x', 'x']
]

test_marks_3 = [
    ['.', '.', '.', '.', 'x'],
    ['.', '.', '.', '.', 'x'],
    ['.', '.', '.', '.', 'x'],
    ['.', '.', '.', '.', 'x'],
    ['.', '.', '.', '.', 'x']
]

test_marks_4 = [
    ['.', '.', '.', '.', 'x'],
    ['.', '.', '.', 'x', '.'],
    ['.', '.', 'x', '.', '.'],
    ['.', 'x', '.', '.', '.'],
    ['.', '.', '.', '.', 'x']
]

test_marks_5 = [
    ['.', '.', '.', '.', 'x'],
    ['.', '.', '.', 'x', '.'],
    ['.', '.', 'x', '.', '.'],
    ['.', 'x', '.', '.', '.'],
    ['x', '.', '.', '.', '.']
]

test_marks_6 = [
    ['x', '.', '.', '.', '.'],
    ['.', 'x', '.', '.', '.'],
    ['.', '.', 'x', '.', '.'],
    ['.', '.', '.', 'x', '.'],
    ['.', '.', '.', '.', 'x']
]

print(check_for_winner(test_marks_1))
print(check_for_winner(test_marks_2))
print(check_for_winner(test_marks_3))
print(check_for_winner(test_marks_4))
print(check_for_winner(test_marks_5))
print(check_for_winner(test_marks_6))
