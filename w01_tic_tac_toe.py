##############################################################################
# W01 Prove: Developer
# Student: Marcos Guimarães
# Professor: Brad Lythgoe
# Tic-Tac-Toe Game
##############################################################################

# The board
game_board = """ Positions
   |   |         7 | 8 | 9
---+---+---     ---+---+---
   |   |         4 | 5 | 6
---+---+---     ---+---+---
   |   |         1 | 2 | 3
"""
positions = [
    None,    # Added element to facilitate indexes
    (5, 1),  # 1
    (5, 5),  # 2
    (5, 9),  # 3
    (3, 1),  # 4
    (3, 5),  # 5
    (3, 9),  # 6
    (1, 1),  # 7
    (1, 5),  # 8
    (1, 9)   # 9
    ]
# positions that lead to winning the game
# Plays making a row, a column or diagonals win
# Numbers represent winning positions
win = [
          [1, 2, 3],  # lines
          [4, 5, 6],
          [7, 8, 9],
          [7, 4, 1],  # Columns
          [8, 5, 2],
          [9, 6, 3],
          [7, 5, 3],  # Diagonals
          [1, 5, 9]
        ]

# Build the board from strings, generating a list of lists that can be modified.
board = []
for line in game_board.splitlines():
    board.append(list(line))

player = "X"  # Start playing with X
playing = True
plays = 0  # Play counter
while True:
    for t in board:  # print the board
        print("".join(t))
    if not playing:  # Ends after printing the last board
        break
    if plays == 9:  # If 9 plays have been made, all positions have already been filled
        print("Nobody won!.")
        break
    play = int(input(f"Enter position to play 1-9 (player {player}):"))
    if play < 1 or play > 9:
        print("Invalid position")
        continue
    # Checks if the position is free
    if board[positions[play][0]][positions[play][1]] != " ":
        print("Position occupied. Choose another.")
        continue
    # Mark play for the player
    board[positions[play][0]][positions[play][1]] = player
    # Check if you won
    for p in win:
        for x in p:
            if board[positions[x][0]][positions[x][1]] != player:
                break
        else:  # If o ends without a break, all p positions belong to the same player.
            print(f"The player {player} won ({p}): ")
            playing = False
            break
    player = "X" if player == "O" else "O"  # Toggle player
    plays += 1  # Play counter