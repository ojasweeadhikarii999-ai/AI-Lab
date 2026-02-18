def tic_tac_toe_heuristic(board, player):
    opponent = 'O' if player == 'X' else 'X'
    lines = []

    # Rows
    for row in board:
        lines.append(row)

    # Columns
    for col in range(3):
        lines.append([board[row][col] for row in range(3)])

    # Diagonals
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2-i] for i in range(3)])

    player_open = 0
    opponent_open = 0

    for line in lines:
        # Check open for player
        if all(cell == player or cell == '-' for cell in line):
            player_open += 1

        # Check open for opponent
        if all(cell == opponent or cell == '-' for cell in line):
            opponent_open += 1

    return player_open - opponent_open


# -------- USER INPUT --------

print("Enter board row by row (use X, O, or - for empty)")

board = []
for i in range(3):
    row = input(f"Row {i+1}: ").split()
    board.append(row)

player = input("Enter player (X or O): ")

h = tic_tac_toe_heuristic(board, player)

print("Heuristic value:", h)
