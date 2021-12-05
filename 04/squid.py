with open('test_data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

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


breakpoint()



# Part 1
