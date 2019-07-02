#!/usr/bin/env python3


def draw_board(board):
    # Print the board was passed
    print("  a b c d e f g h")
    for y in range(8):
        string = ""
        for x in range(8):
            string += " " + board[x][y]
        print(str(y + 1) + string)


def get_new_board():
    # Create new blank board
    board = []
    for i in range(8):
        board.append([" "] * 8)
    return board


def reset_board(board):
    # Blanks out the board except the original starting position
    for x in range(8):
        for y in range(8):
            board[x][y] = "."
    # Given pieces
    board[3][3] = "W"
    board[3][4] = "B"
    board[4][3] = "B"
    board[4][4] = "W"


def is_valid_move(board, chess, x, y):
    if board[x][y] != "." or not is_on_board(x, y):
        return False
    # Temporarily set the chess on the board
    board[x][y] = chess
    if chess == black_icon_chess:
        other_chess = white_icon_chess
    else:
        other_chess = black_icon_chess
    chess_flip = []

    for x_direction, y_direction in direction:
        new_x, new_y = x, y
        new_x += x_direction   # first step in the direction
        new_y += y_direction   # first step in the direction
        if is_on_board(new_x, new_y) and board[new_x][new_y] == other_chess:
            # A piece belonging to the other next to previous piece
            new_x += x_direction
            new_y += y_direction
            if not is_on_board(new_x, new_y):
                continue
            while board[new_x][new_y] == other_chess:
                new_x += x_direction
                new_y += y_direction
                if not is_on_board(new_x, new_y):
                    break
            if not is_on_board(new_x, new_y):
                continue
            if board[new_x][new_y] == chess:
                while True:
                    new_x -= x_direction
                    new_y -= y_direction
                    if new_x == x and new_y == y:
                        break
                    chess_flip.append([new_x, new_y])

    board[x][y] = "."
    # If no chess were flipped, it's not valid move
    if len(chess_flip) == 0:
        return False
    return chess_flip


def is_on_board(x, y):
    return x >= 0 and x <= 7 and y >= 0 and y <= 7


def get_valid_moves(board, chess):
    # Return list of valid moves
    valid_moves = []
    for x in range(8):
        for y in range(8):
            if is_valid_move(board, chess, x, y) is not False:
                valid_moves.append([x, y])
    return valid_moves


def get_score_of_board(board):
    # Determine the score by couting the chesses
    black_score = 0
    white_score = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == black_icon_chess:
                black_score += 1
            if board[x][y] == white_icon_chess:
                white_score += 1
    return {black_icon_chess: black_score, white_icon_chess: white_score}


def enter_chess():
    chess = ""
    while not (chess == "W" or chess == "B"):
        chess = "B"
    if chess == "W":
        return ["W", "B"]
    else:
        return ["B", "W"]


def move_chess(board, chess, x, y):
    # Place the chess on the board at x, y and flip any of the opponent's piece
    # Return false if this is an valid move, True if it is valid moves
    chess_flip = is_valid_move(board, chess, x, y)
    if chess_flip is False:
        return False
    board[x][y] = chess
    for new_x, new_y in chess_flip:
        board[new_x][new_y] = chess
    return True


def is_on_corner(x, y):
    # Return true if the position is in one of the 4 corners.
    return x == 0 and y == 0 or x == 7 and y == 7 or x == 7 and y == 7


def get_black_moves(board, chess):
    x_chars = "a b c d e f g h".split()
    y_nums = "1 2 3 4 5 6 7 8".split()
    try:
        while True:
            move = input("Player B: ")
            move_item = list(move)
            if len(move_item) == 2 and move_item[0] in x_chars and\
                    move_item[1] in y_nums:
                move_item[0] = x_chars.index(move_item[0]) + 1
                x = int(move_item[0]) - 1
                y = int(move_item[1]) - 1
                if is_valid_move(board, chess, x, y) is False:
                    print(move + ": Invalid choice")
                    check_valid_choices(get_valid_moves(main_board, chess))
                    continue
                else:
                    break
            else:
                print(move + ": Invalid choice")
                check_valid_choices(get_valid_moves(main_board, chess))
        return [x, y]
    except EOFError:
        pass


def get_white_moves(board, chess):
    x_chars = "a b c d e f g h".split()
    y_nums = "1 2 3 4 5 6 7 8".split()
    try:
        while True:
            move = input("Player W: ")
            move_item = list(move)
            if len(move_item) == 2 and move_item[0] in x_chars and\
                    move_item[1] in y_nums:
                move_item[0] = x_chars.index(move_item[0]) + 1
                x = int(move_item[0]) - 1
                y = int(move_item[1]) - 1
                if is_valid_move(board, chess, x, y) is False:
                    print(move + ": Invalid choice")
                    check_valid_choices(get_valid_moves(main_board, chess))
                    continue
                else:
                    break
            else:
                print(move + ": Invalid choice")
                check_valid_choices(get_valid_moves(main_board, chess))
        return [x, y]
    except EOFError:
        pass


def show_point(black_chess, white_chess):
    score = get_score_of_board(main_board)
    print(
        "End of the game. W: %s, B: %s"
        % (score[white_chess], score[black_chess])
    )


def check_valid_choices(color):
    line = ""
    print("Valid choices: ", end="")
    for i in range(len(color)):
        left = char[color[i][0]]
        right = num[color[i][1]]
        line += left + right + " "
    line.rstrip()
    print(line, end="\n")


if __name__ == "__main__":
    char = "a b c d e f g h".split()
    num = "1 2 3 4 5 6 7 8".split()
    eight_direction = [
                       [0, 1], [1, 1], [1, 0], [1, -1],
                       [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    try:
        while True:
            main_board = get_new_board()
            reset_board(main_board)
            black_icon_chess, white_icon_chess = enter_chess()
            while True:
                turn = black_icon_chess
                while turn == black_icon_chess:
                    draw_board(main_board)
                    valid_black_chess = get_valid_moves(main_board, black_icon_chess)
                    if len(valid_black_chess) == 0:
                        print("Player B cannot play.")
                        break
                    check_valid_choices(valid_black_chess)
                    move_black_chess = get_black_moves(main_board, black_icon_chess)
                    move_chess(main_board, black_icon_chess, move_black_chess[0], move_black_chess[1])
                    break
                turn = white_icon_chess
                while turn == white_icon_chess:
                    draw_board(main_board)
                    valid_white_chess = get_valid_moves(main_board, white_icon_chess)
                    if len(valid_white_chess) == 0:
                        print("Player W cannot play.")
                        break
                    check_valid_choices(valid_white_chess)
                    move_white_chess = get_white_moves(main_board, white_icon_chess)
                    move_chess(main_board, white_icon_chess, move_white_chess[0], move_white_chess[1])
                    break
                if len(valid_black_chess) == 0 and len(valid_white_chess) == 0:
                    break
            score = get_score_of_board(main_board)
            show_point(black_icon_chess, white_icon_chess)
            if score[black_icon_chess] > score[white_icon_chess]:
                print("B wins.")
            elif score[white_icon_chess] > score[black_icon_chess]:
                print("W wins.")
            else:
                print("Draw.")
            break
    except TypeError:
        pass
