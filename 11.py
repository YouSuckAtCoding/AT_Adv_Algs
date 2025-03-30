import time

import numpy as np

def print_board(board):
    for row in board:
        print(" ".join(f"{cell:2}" for cell in row))
    print()

def safeMove(x, y, board):
    if 0 <= x < board_size and 0 <= y < board_size and board[x][y] == -1:
        return True
    return False

def knightBruteForce(board_size, board, curr_x, curr_y, moves, pos=1):

    if pos == (board_size ** 2):
        return True

    for move_x, move_y in moves:
        x = curr_x + move_x
        y = curr_y + move_y

        if safeMove(x, y, board):

            board[x][y] = pos

            if knightBruteForce(board_size, board, x, y, moves, pos + 1):
                return True

            board[x][y] = -1

    return False

def knightWarnsdorff(board_size, board, start_x, start_y, moves):

    board[start_x][start_y] = 0

    for curr_move in range(1, (board_size ** 2)):
        next_moves = []
        for move_x, move_y in moves:

            x = start_x + move_x
            y = start_y + move_y

            if safeMove(x,y,board):
                curr_pos_valid_moves = sum(1 for curr_x, curr_y in moves if safeMove(curr_x + x, curr_y + y, board))
                next_moves.append((curr_pos_valid_moves, x, y))

        if not next_moves:
            return False

        next_moves.sort()
        best_move = next_moves[0]
        start_x, start_y = best_move[1],best_move[2]

        board[start_x][start_y] = curr_move

    return board


moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

sizes = [5,8,10,12]

for board_size in sizes:

    board = np.full((board_size,board_size), -1, dtype=int)
    board[0][0] = 0

    start_time = time.time()

    print(f"Brute force with size {board_size}")
    if board_size >= 10 or not knightBruteForce(board_size, board, 0, 0, moves):
        print("No solution")
    else:
        print_board(board)
    print(f"Brute force with size {board_size} in {time.time() - start_time}")

    board = np.full((board_size,board_size), -1, dtype=int)
    board[0][0] = 0

    print(f"Warnsdorff with size {board_size}")

    start_time = time.time()

    res = knightWarnsdorff(board_size, board, 0, 0, moves)

    if isinstance(res, np.ndarray) : print_board(res)
    else: print("No Solution")

    print(f"Warnsdorff with size {board_size} in {time.time() - start_time}")

