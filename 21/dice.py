with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

# Further data processing

player_pos = []
player_pos.append(None)
player_pos.append(int(data[0][len("Player 1 starting position: "):]))
player_pos.append(int(data[1][len("Player 2 starting position: "):]))

# breakpoint()

# Part 1

# This one seems too easy.  It's scaring me just a little...

# die = 1

# scores = []
# scores.append(0) # placeholder so I don't have to remember 1's score is at 0
# scores.append(0)
# scores.append(0)

# turn = 1

# while scores[1] < 1000 and scores[2] < 1000:
#     rolls = []
#     for i in range(3):
#         roll = die + i
#         # edge case for 100
#         if roll != 100:
#             roll = roll % 100

#         rolls.append(roll)

#     total = sum(rolls)
#     die = die + 3
#     # breakpoint()
#     player_pos[turn] = (player_pos[turn] + total) % 10

#     if player_pos[turn] == 0:
#         player_pos[turn] = 10

#     scores[turn] += player_pos[turn]

#     if turn == 1:
#         turn = 2
#     else:
#         turn = 1

#     # print(f"Scores: {scores}")
#     # print(f"Position:{player_pos}")
#     # breakpoint()

# print(scores)

# # print(scores[1] * scores[2])

# rolls = die - 1
# loser_score = min(scores[1:])
# print(rolls * loser_score)
# breakpoint()


# Part 2


# die = 1

scores = []
scores.append(0) # placeholder so I don't have to remember 1's score is at 0
scores.append(0)
scores.append(0)

turn = 1

# possible_roll_sums = [3, 4, 5, 6, 7, 8, 9]

# # Number of roll combos leading to this outcome
# number_per_val = [1, 3, 6, 7, 6, 3, 1]

# Pairs in a dict work better

possible_rolls = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1
}

# Games tracks the number of games with a certain score tuple.

wins = []
wins.append(None)
wins.append(0)
wins.append(0)

games = {}
# Skip, player 1 score, player 2 score, player 1 pos, player 2 pos
# games[(None, 0, 0, player_pos[1], player_pos[2])] = 1

# Try by positions then by scores
games[(None, player_pos[1], player_pos[2])] = {}

games[(None, player_pos[1], player_pos[2])][(None, 0, 0)] = 1

# breakpoint()

WIN_SCORE = 21

while len(games) > 0:
    new_games = {}
    # breakpoint()
    for position, score_sets in games.items():
        for score_set, count in score_sets.items():
            for roll, sum in possible_rolls.items():
                # breakpoint()
                new_position = (position[turn] + roll) % 10

                if new_position == 0:
                    new_position = 10

                new_game_position = [e for e in position]
                new_game_position[turn] = new_position
                new_game_position_tuple = tuple(new_game_position)

                if new_game_position_tuple not in new_games:
                    new_games[new_game_position_tuple] = {}

                new_score = [e for e in score_set]
                new_score[turn] += new_position

                new_score_tuple = tuple(new_score)
                # breakpoint()
                if new_score_tuple not in new_games[new_game_position_tuple]:
                    new_games[new_game_position_tuple][new_score_tuple] = sum * count
                else:
                    new_games[new_game_position_tuple][new_score_tuple] += (sum * count)

                # breakpoint()
    # Remove won games
    # breakpoint()
    for new_position, new_scores in dict(new_games).items():
        for new_score, count in dict(new_scores).items():

            if new_score[1] >= WIN_SCORE:
                # breakpoint()
                wins[1] += count
                del new_games[new_position][new_score]
            if new_score[2] >= WIN_SCORE:
                # breakpoint()
                wins[2] += count
                del new_games[new_position][new_score]

        if len(new_games[new_position]) == 0:
            # breakpoint()
            del new_games[new_position]


    # Update turn and games
    if turn == 1:
        turn = 2
    else:
        turn = 1

    games = new_games

    print(wins)
    # if wins[1] >= 444356092776315:
    #     breakpoint()
print(wins)

result = max(wins[1:])
print(f"Result: {result}")

breakpoint()
